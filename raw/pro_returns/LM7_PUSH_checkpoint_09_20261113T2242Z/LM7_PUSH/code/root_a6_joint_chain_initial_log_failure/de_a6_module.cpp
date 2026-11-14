// Exact coordinates of E/E', with its actual full-source conjugation.
#define main schreier_engine_main
#include "de_a6_schreier.cpp"
#undef main

std::string multiply_decimal(std::string digits,unsigned factor) {
  unsigned carry=0;
  for(int i=(int)digits.size()-1;i>=0;--i){unsigned v=(digits[i]-'0')*factor+carry;digits[i]='0'+v%10;carry=v/10;}
  while(carry){digits.insert(digits.begin(),'0'+carry%10);carry/=10;}return digits;
}
int main(int argc,char**argv){try {
  if(argc!=6)throw std::runtime_error("usage: module E.bin Eprime.bin source.input selected_indices.input output.json");
  auto C=Engine::replay(argv[2]);
  if(!C->derived_mode)throw std::runtime_error("missing derived certificate");
  auto E=Engine::replay(argv[1]);
  std::ifstream index_file(argv[4]);unsigned dim;index_file>>dim;
  std::vector<unsigned> selected(dim);for(auto &i:selected)index_file>>i;
  if(!index_file||dim!=9||C->original.size()!=dim)throw std::runtime_error("basis metadata");
  if(E->order()!=multiply_decimal(C->order(),19683))throw std::runtime_error("actual quotient index");
  for(unsigned j=0;j<dim;++j) {
    if(E->original.at(selected[j])!=C->original[j])throw std::runtime_error("nested original-word comparison");
    P cube=E->mul(E->mul(C->original[j],C->original[j]),C->original[j]);
    if(!C->contains(cube))throw std::runtime_error("quotient has a nontrivial basis cube");
  }
  // The nine displayed generators generate E, by their literal words
  // in the complete greedy certificate.  The exact derived index3^9
  // and the nine cube checks identify the quotient with F3^9.
  std::vector<int> base;for(auto &l:E->chain)base.push_back(l.base);
  E->chain.clear();for(int b:base)E->new_level(b);
  for(unsigned j=0;j<E->gens.size();++j)
    for(int k=0;k<=E->gens[j].depth;++k)E->extend(k,j,true);
  using V=std::vector<int>;
  std::vector<V> value(E->nodes.size(),V(dim,0));std::vector<bool> known(E->nodes.size(),false);
  for(unsigned i=0;i<E->nodes.size();++i){auto v=E->nodes[i];
    if(v.op==0)known[i]=true;
    else if(v.op==1){for(unsigned j=0;j<dim;++j)if(v.a==selected[j]){known[i]=true;value[i][j]=1;}}
    else if(v.op==2){known[i]=known[v.a]&&known[v.b];for(unsigned j=0;j<dim;++j)value[i][j]=(value[v.a][j]+value[v.b][j])%3;}
    else if(v.op==3){known[i]=known[v.a];for(unsigned j=0;j<dim;++j)value[i][j]=(3-value[v.a][j])%3;}
    else if(v.op==4)known[i]=true;
    else if(v.op==5){known[i]=known[v.b];value[i]=value[v.b];}
    else throw std::runtime_error("word operation");
  }
  for(auto &g:E->gens)if(!known[g.node])throw std::runtime_error("strong generator lacks selected-basis word");
  for(auto &l:E->chain)for(auto w:l.word)if(!known[w])throw std::runtime_error("transversal lacks selected-basis word");
  auto coordinates=[&](P h){V ans(dim,0);
    for(auto &l:E->chain){int b=h[l.base];if(b==l.base)continue;int pos=l.pos[b];if(pos<0)throw std::runtime_error("probe outside E");
      h=E->mul(h,l.inv[pos]);for(unsigned j=0;j<dim;++j)ans[j]=(ans[j]+value[l.word[pos]][j])%3;
    }
    if(!E->identity(h))throw std::runtime_error("nontrivial coordinate sift residue");return ans;
  };
  for(unsigned j=0;j<dim;++j){V unit(dim,0);unit[j]=1;if(coordinates(C->original[j])!=unit)throw std::runtime_error("basis coordinate");}
  std::ifstream in(argv[3]);int n,m;in>>n>>m;if(n!=E->n||m!=2)throw std::runtime_error("source header");
  std::vector<P> source(m,P(n));for(auto &p:source)for(auto &v:p){unsigned x;in>>x;if(!in||x>=(unsigned)n)throw std::runtime_error("source entry");v=x;}
  for(auto &p:source){P sorted=p;std::sort(sorted.begin(),sorted.end());if(sorted!=E->id)throw std::runtime_error("source generator");}
  P s=source[0],r=source[1],ri=E->inverse(r);
  P x=E->mul(E->mul(E->mul(ri,s),ri),s),y=E->mul(E->mul(E->mul(s,ri),s),ri);
  std::vector<P> conjugators{s,r,x,y};std::vector<std::vector<V>> matrices;
  for(auto &g:conjugators){std::vector<V> M(dim,V(dim,0));
    for(unsigned j=0;j<dim;++j){auto v=coordinates(E->conjugate(g,C->original[j]));for(unsigned i=0;i<dim;++i)M[i][j]=v[i];}
    matrices.push_back(M);
  }
  V comm=coordinates(E->commutator(x,y));
  std::vector<V> original_coords;for(auto &g:E->original)original_coords.push_back(coordinates(g));
  std::ofstream out(argv[5]);if(!out)throw std::runtime_error("output");
  auto vector=[&](const auto &v){out<<'[';for(unsigned i=0;i<v.size();++i){if(i)out<<',';out<<v[i];}out<<']';};
  auto matrix=[&](const auto &M){out<<'[';for(unsigned i=0;i<M.size();++i){if(i)out<<',';vector(M[i]);}out<<']';};
  out<<"{\"status\":\"PASS\",\"module_dimension\":9,\"module_exponent\":3,\"actual_derived_index\":19683,\"selected_original_indices\":";
  vector(selected);out<<",\"nine_basis_cubes_killed_in_actual_derived_subgroup\":true,\"conjugation_matrices\":[";
  for(unsigned i=0;i<matrices.size();++i){if(i)out<<',';matrix(matrices[i]);}
  out<<"],\"conjugator_labels\":[\"s\",\"r\",\"x\",\"y\"],\"commutator_x_y\":";vector(comm);
  out<<",\"all_original_E_generator_coordinates\":";matrix(original_coords);out<<"}\n";
  std::cout<<"PASS actual F3^9 quotient, nine basis cubes, four conjugation matrices, and "
           <<original_coords.size()<<" original-generator coordinates."<<std::endl;return 0;
}catch(const std::exception&e){std::cerr<<"ERROR: "<<e.what()<<std::endl;return 1;}}
