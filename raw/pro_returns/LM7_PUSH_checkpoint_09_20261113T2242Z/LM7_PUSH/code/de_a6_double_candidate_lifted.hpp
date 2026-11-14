#pragma once
struct CandidateLift {
  CandidateModel&m;Engine&e;std::vector<Node>nodes;std::vector<CandidateElement>values,inverses;
  CandidateSpan span;uint64_t relations=0,normal_additions=0;
  CandidateLift(CandidateModel&model,Engine&engine):m(model),e(engine){
    if(e.derived_mode||e.original.size()!=2)throw std::runtime_error("ordinary base required");
    for(unsigned j=0;j<2;++j){bool found=false;for(auto&g:e.gens)if(g.node==j+1&&g.p==e.original[j])found=true;
      if(!found)throw std::runtime_error("original strong generator missing");}
    std::vector<int>bases;for(auto&c:e.chain)bases.push_back(c.base);e.chain.clear();
    for(int b:bases)e.new_level(b);
    for(unsigned j=0;j<e.gens.size();++j)for(int k=0;k<=e.gens[j].depth;++k)e.extend(k,j,true);
    nodes=e.nodes;values.reserve(nodes.size()+5000);inverses.reserve(nodes.size()+5000);
    for(auto n:nodes){CandidateElement v;
      if(n.op==0)v=m.one;else if(n.op==1)v=m.original.at(n.a);
      else if(n.op==2)v=m.mul(values.at(n.a),values.at(n.b));
      else if(n.op==3)v=inverses.at(n.a);
      else if(n.op==4)v=m.mul(m.mul(m.mul(values.at(n.a),values.at(n.b)),inverses.at(n.a)),inverses.at(n.b));
      else if(n.op==5)v=m.mul(m.mul(values.at(n.a),values.at(n.b)),inverses.at(n.a));
      else throw std::runtime_error("word operation");values.push_back(v);inverses.push_back(m.inv(v));
    }
  }
  uint32_t product(uint32_t a,uint32_t b){if(!a)return b;if(!b)return a;
    CandidateElement v=m.mul(values.at(a),values.at(b));nodes.push_back({2,a,b});values.push_back(v);inverses.push_back(m.inv(v));return nodes.size()-1;}
  uint32_t inverse(uint32_t a){if(!a)return 0;CandidateElement v=inverses.at(a);nodes.push_back({3,a,0});values.push_back(v);inverses.push_back(values[a]);return nodes.size()-1;}
  void normal_close(){
    for(unsigned at=0;at<span.basis.size();++at)for(unsigned j=0;j<2;++j){
      CandidateElement v=m.conj(m.original[j],m.kernel(span.basis[at]));CandidateBits b=m.vector(v);
      if(!span.contains(b)){uint32_t g=j+1;
        if(nodes.at(g).op!=1||nodes[g].a!=j)throw std::runtime_error("original word node");
        uint32_t w=product(product(g,span.words[at]),inverse(g));
        if(values[w]!=v)throw std::runtime_error("normal literal word");span.add(b,w);++normal_additions;}
    }
  }
  void solve(){
    for(int lev=(int)e.chain.size()-1;lev>=0;--lev){auto&l=e.chain[lev];unsigned old=span.basis.size();
      for(unsigned at=0;at<l.orbit.size();++at)for(unsigned gi=0;gi<e.gens.size();++gi){
        const auto&g=e.gens[gi];if(g.depth<lev)continue;
        int to=l.pos[g.p[l.orbit[at]]];if(to<0)throw std::runtime_error("base orbit edge");
        P h=e.mul(e.mul(l.trans[at],g.p),l.inv[to]);
        CandidateElement v=m.mul(m.mul(values[l.word[at]],values[g.node]),inverses[l.word[to]]);
        std::vector<std::pair<uint32_t,bool>>history{{l.word[at],false},{g.node,false},{l.word[to],true}};
        for(int k=lev+1;k<(int)e.chain.size();++k){auto&c=e.chain[k];int b=h[c.base];if(b==c.base)continue;
          int pos=c.pos[b];if(pos<0)throw std::runtime_error("incomplete base relation");
          h=e.mul(h,c.inv[pos]);v=m.mul(v,inverses[c.word[pos]]);history.push_back({c.word[pos],true});}
        if(!e.identity(h))throw std::runtime_error("nonidentity base relation");++relations;CandidateBits b=m.vector(v);
        if(!span.contains(b)){uint32_t w=0;for(auto[a,invert]:history)w=product(w,invert?inverse(a):a);
          if(values[w]!=v)throw std::runtime_error("relator literal word");span.add(b,w);normal_close();
          std::cout<<"kernel rank "<<span.basis.size()<<" relators "<<relations<<" level "<<lev<<std::endl;}
      }
      if(lev%5==0||span.basis.size()!=old)std::cout<<"level "<<lev<<" orbit "<<l.orbit.size()<<" relators "<<relations<<" kernel rank "<<span.basis.size()<<std::endl;
    }
    if(relations!=e.final_relations)throw std::runtime_error("complete relator count");
    normal_close();for(const auto&b:span.basis)for(const auto&g:m.original)
      if(!span.contains(m.vector(m.conj(g,m.kernel(b)))))throw std::runtime_error("final normal closure");
  }
  void save(const std::string&name,double seconds){std::ofstream f(name);if(!f)throw std::runtime_error("output");
    f<<"{\n\"status\":\"PASS_COMPLETE_ACTUAL_DOUBLE_SIGNED_CANDIDATE_KERNEL\",\n\"base_order\":\""<<e.order()<<"\",\n\"base_degree\":"<<e.n
     <<",\n\"kernel_ambient_dimension\":"<<CBW<<",\n\"kernel_dimension\":"<<span.basis.size()
     <<",\n\"all_Schreier_relators_evaluated\":true,\n\"relators_evaluated\":"<<relations
     <<",\n\"complete_base_relator_count\":"<<e.final_relations<<",\n\"normal_closure_additions\":"<<normal_additions
     <<",\n\"independent_Python_operation_controls\":"<<m.controls<<",\n\"kernel_coordinate_controls\":"<<m.kernel_controls
     <<",\n\"literal_word_DAG\":[";
    for(unsigned i=0;i<nodes.size();++i){if(i)f<<",";auto n=nodes[i];f<<"["<<n.op<<","<<n.a<<","<<n.b<<"]";}
    f<<"],\n\"kernel_basis_word_nodes\":[";for(unsigned i=0;i<span.words.size();++i){if(i)f<<",";f<<span.words[i];}
    f<<"],\n\"kernel_basis_coordinates\":[";
    for(unsigned i=0;i<span.basis.size();++i){if(i)f<<",";f<<"[";bool first=true;
      for(int p=0;p<CBW;++p){unsigned a=CandidateSpan::coefficient(span.basis[i],p);if(a){if(!first)f<<",";first=false;f<<"["<<p<<","<<a<<"]";}}f<<"]";}
    f<<"],\n\"seconds\":"<<seconds<<"\n}\n";
  }
};

