#!/usr/bin/env python3
"""Build the complete binary source / three actual Schur signs collector.

The root collector is copied, never modified.  Every one of its complete
C relations is evaluated in the same three signed SL2(F5) epikernels.
"""
from pathlib import Path
from hashlib import sha256
import json

HERE = Path(__file__).resolve().parent


def main():
    names = ['e_a6_double_central_root.cpp', 'de_a6_gl_central_model.bin',
             'de_a6_gl_central_prepare.npz', 'e_a6_double_central_model_root.bin',
             'e_a6_double_model_root.bin', 'de_a6_schreier_residual_derived.bin']
    hashes = {n: sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    source = (HERE/names[0]).read_text()

    def replace(old, new):
        nonlocal source
        assert source.count(old) == 1, (old[:100], source.count(old))
        source = source.replace(old, new)

    replace('constexpr unsigned NG=10,NC=30,RC=NG+NC;',
            'constexpr unsigned NG=10,NC=30,NS=3,RC=NG+NC+NS;')
    insert = r'''
using Signs=std::array<uint8_t,NS>;
struct SignedData {
  unsigned sid,z;uint8_t sm[120][120],si[120];
  Signs one;std::array<Signs,NG>original;
  SignedData(const std::string&name,const CentralData&c){
    std::ifstream f(name,std::ios::binary);
    if(Model::integer<uint32_t>(f)!=0xA6C6CE13||Model::integer<uint32_t>(f)!=1)
      throw std::runtime_error("signed header");
    sid=Model::integer<uint32_t>(f);z=Model::integer<uint32_t>(f);
    if(sid>=120||z>=120||Model::integer<uint32_t>(f)!=NG)
      throw std::runtime_error("signed dimensions");
    unsigned n=Model::integer<uint32_t>(f);if(n!=c.base_original[0].size())
      throw std::runtime_error("signed base degree");
    f.read((char*)sm,sizeof(sm));f.read((char*)si,sizeof(si));
    f.read((char*)original.data(),sizeof(original));
    std::vector<P>bp(NG,P(n));for(auto&p:bp)f.read((char*)p.data(),2*n);
    if(!f||f.peek()!=EOF||bp!=c.base_original)
      throw std::runtime_error("signed literal C source mismatch");
    for(auto&row:sm)for(auto a:row)if(a>=120)throw std::runtime_error("signed product range");
    for(auto a:si)if(a>=120)throw std::runtime_error("signed inverse range");
    for(auto&row:original)for(auto a:row)if(a>=120)throw std::runtime_error("signed original range");
    one.fill(sid);
  }
  Signs mul(const Signs&a,const Signs&b)const{Signs v;for(unsigned j=0;j<NS;++j)v[j]=sm[a[j]][b[j]];return v;}
  Signs inv(const Signs&a)const{Signs v;for(unsigned j=0;j<NS;++j)v[j]=si[a[j]];return v;}
};

'''
    replace('struct CentralProbe {', insert+'struct CentralProbe {')
    replace('Engine&e;Model&m;CentralData&c;std::vector<Node>nodes;',
            'Engine&e;Model&m;CentralData&c;SignedData&s;std::vector<Node>nodes;\n  std::vector<Signs>signed_values,signed_inverses;')
    replace('CentralProbe(Engine&engine,Model&model,CentralData&central):e(engine),m(model),c(central){',
            'CentralProbe(Engine&engine,Model&model,CentralData&central,SignedData&signs):e(engine),m(model),c(central),s(signs){')
    replace('values.push_back(v);inverses.push_back(m.inv(v));exponents.push_back(a);',
            r'''Signs sv;
      if(n.op==0)sv=s.one;
      else if(n.op==1)sv=s.original.at(n.a);
      else if(n.op==2)sv=s.mul(signed_values.at(n.a),signed_values.at(n.b));
      else if(n.op==3)sv=signed_inverses.at(n.a);
      else if(n.op==4)sv=s.mul(s.mul(s.mul(signed_values.at(n.a),signed_values.at(n.b)),signed_inverses.at(n.a)),signed_inverses.at(n.b));
      else if(n.op==5)sv=s.mul(s.mul(signed_values.at(n.a),signed_values.at(n.b)),signed_inverses.at(n.a));
      else throw std::runtime_error("signed word operation");
      values.push_back(v);inverses.push_back(m.inv(v));exponents.push_back(a);
      signed_values.push_back(sv);signed_inverses.push_back(s.inv(sv));''')
    replace('nodes.push_back({2,a,b});values.push_back(v);inverses.push_back(m.inv(v));exponents.push_back(plus(exponents[a],exponents[b]));return nodes.size()-1;',
            'nodes.push_back({2,a,b});values.push_back(v);inverses.push_back(m.inv(v));exponents.push_back(plus(exponents[a],exponents[b]));\n    Signs sv=s.mul(signed_values[a],signed_values[b]);signed_values.push_back(sv);signed_inverses.push_back(s.inv(sv));return nodes.size()-1;')
    replace('nodes.push_back({3,a,0});values.push_back(v);inverses.push_back(values[a]);exponents.push_back(plus(z,exponents[a],-1));return nodes.size()-1;',
            'nodes.push_back({3,a,0});values.push_back(v);inverses.push_back(values[a]);exponents.push_back(plus(z,exponents[a],-1));\n    Signs sv=signed_inverses[a];signed_values.push_back(sv);signed_inverses.push_back(signed_values[a]);return nodes.size()-1;')
    replace('for(unsigned j=0;j<NC;++j)row[NG+j]=(2-cv[j])%2;',
            r'''for(unsigned j=0;j<NC;++j)row[NG+j]=(2-cv[j])%2;
    Signs sign=s.one;
    for(auto[a,invert]:history)sign=s.mul(sign,invert?signed_inverses[a]:signed_values[a]);
    for(unsigned j=0;j<NS;++j){
      if(sign[j]!=s.sid&&sign[j]!=s.z)throw std::runtime_error("noncentral actual SL2 relation");
      row[NG+NC+j]=(sign[j]==s.z);
    }''')
    replace('if(values[w]!=v||exponents[w]!=ab)throw std::runtime_error("central relation word replay");',
            'if(values[w]!=v||exponents[w]!=ab||signed_values[w]!=sign)throw std::runtime_error("coupled relation word replay");')
    replace('if(basis.size()==RC)return false;',
            'if(basis.size()>RC-3)throw std::runtime_error("contradiction with actual onto E2 abelianization map");')
    replace('if(!complete&&basis.size()!=RC)throw std::runtime_error("incomplete rank bound");',
            'if(!complete)throw std::runtime_error("all coupled relations required");')
    replace('PASS_EXACT_CENTRAL_COINVARIANT_PRESENTATION',
            'PASS_EXACT_BINARY_THREE_SIGN_PULLBACK_PRESENTATION')
    replace('<<",\\n\\\"all_original_central_shift_parameters\\\":"<<NG*NC',
            '<<",\\n\\\"independent_Schur_sign_dimension\\\":"<<NS\n     <<",\\n\\\"all_original_central_shift_parameters\\\":"<<NG*(NC+NS)')
    replace('<<(basis.size()==RC?"true":"false")',
            '<<(basis.size()==RC-3?"true":"false")')
    replace('if(argc!=5)throw std::runtime_error("usage: executable source_model.bin central_model.bin C_certificate.bin output.json");',
            'if(argc!=6)throw std::runtime_error("usage: executable source_model.bin central_model.bin signed_model.bin C_certificate.bin output.json");')
    replace('auto e=Engine::replay(argv[3]);std::cout<<"complete perfect C base replay passed"<<std::endl;',
            'SignedData s(argv[3],c);auto e=Engine::replay(argv[4]);std::cout<<"complete perfect C base replay passed"<<std::endl;')
    replace('CentralProbe probe(*e,m,c);bool complete=probe.run();',
            'CentralProbe probe(*e,m,c,s);bool complete=probe.run();')
    replace('probe.save(argv[4],complete,seconds);', 'probe.save(argv[5],complete,seconds);')
    destination = HERE/'de_a6_double_bridge.cpp'
    destination.write_text(source)
    out = {'status':'PASS_COMPLETE_BINARY_SIGNED_COLLECTOR_BUILT',
           'input_sha256':hashes,'output_sha256':sha256(destination.read_bytes()).hexdigest(),
           'original_exponent_columns':10,'binary_coinvariant_columns':30,
           'independent_signed_columns':3,'all_original_shift_parameters':330,
           'all_complete_C_relations_required':True,
           'actual_C_lift_base_permutations_compared':True}
    (HERE/'de_a6_double_bridge_build.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps(out,indent=2))


if __name__ == '__main__':
    main()
