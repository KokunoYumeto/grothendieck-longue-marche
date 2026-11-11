// Finite 2-group certificate for the degree-two cover in Part C.
// Compile: g++ -std=c++17 -O3 ceh_pro2_cover.cpp -o ceh_pro2_cover
// No external algebra package is used.  All arithmetic is in
// F_2<X,Y,Z>/(all words of length >=5).
#include <array>
#include <cassert>
#include <cstdint>
#include <iomanip>
#include <fstream>
#include <iostream>
#include <sstream>
#include <unordered_set>
#include <vector>
using U=__uint128_t;
using A=std::array<U,3>;
int len[121], cod[121], pw[5]={1,3,9,27,81};
int off[5]={0,1,4,13,40};
int cat[121][121];
U X[3];
int low(U a) {
  auto lo=(uint64_t)a;
  return lo?__builtin_ctzll(lo):64+__builtin_ctzll((uint64_t)(a>>64));
}
U bit(int i) { return U(1)<<i; }
U mul(U a,U b) {
  U c=0;
  while(a) {
    int i=low(a); a&=a-1;
    U t=b;
    while(t) {
      int j=low(t); t&=t-1;
      if(cat[i][j]>=0)c^=bit(cat[i][j]);
    }
  }
  return c;
}
U inv(U a) {
  assert(a&1); U h=a^1,p=1,r=1;
  for(int i=1;i<=4;i++) { p=mul(p,h);r^=p; }
  assert(mul(a,r)==1&&mul(r,a)==1);return r;
}
U br(U a,U b) { return mul(a,b)^mul(b,a); }
U conj(U c,U a) {return mul(mul(c,a),inv(c));}
// An automorphism stores images of augmentation generators X_i=x_i-1.
A compose(const A &a,const A &b) {
  U subs[121];subs[0]=1;
  for(int j=1;j<121;j++)subs[j]=mul(subs[(j-1)/3],a[(j-1)%3]);
  A r={0,0,0};
  for(int i=0;i<3;i++) {
    U p=b[i];while(p){int j=low(p);p&=p-1;r[i]^=subs[j];}
  }
  return r;
}
U eval(const A &a,U p) {
  U subs[121];subs[0]=1;
  for(int j=1;j<121;j++)subs[j]=mul(subs[(j-1)/3],a[(j-1)%3]);
  U r=0;while(p){int j=low(p);p&=p-1;r^=subs[j];}return r;
}
struct AH {
  size_t operator()(const A&a)const {
    size_t h=0x9e3779b97f4a7c15ULL;
    for(U x:a)for(int j=0;j<2;j++) {
      uint64_t y=(uint64_t)(x>>(64*j));
      y^=y>>30;y*=0xbf58476d1ce4e5b9ULL;y^=y>>27;
      y*=0x94d049bb133111ebULL;y^=y>>31;
      h^=y+0x9e3779b97f4a7c15ULL+(h<<6)+(h>>2);
    }
    return h;
  }
};
std::string hx(U x) {
  std::ostringstream o;
  o<<std::hex<<std::setfill('0')<<std::setw(16)<<(uint64_t)(x>>64)
   <<std::setw(16)<<(uint64_t)x;return o.str();
}
// Necessity of inner equivalence: solve c*b(x_i)=a(x_i)*c,
// c=1+sum_{1<=|w|<=3}c_w w.  Degree-four terms of c commute modulo I^5.
// Any group conjugator is a unit of this form modulo degree four.
// Return -1 if impossible; otherwise the dimension of the solution space.
int unit_intertwiner(const A&a,const A&b,std::vector<int>*certificate=nullptr) {
  uint64_t rows[363]={};
  constexpr uint64_t rhs=uint64_t(1)<<39;
  for(int k=0;k<3;k++) {
    U q=a[k]^b[k];
    while(q){int j=low(q);q&=q-1;rows[121*k+j]^=rhs;}
    for(int w=1;w<40;w++) {
      U p=b[k];
      while(p){int j=low(p);p&=p-1;
        if(cat[w][j]>=0)rows[121*k+cat[w][j]]^=uint64_t(1)<<(w-1);}
      p=a[k];
      while(p){int j=low(p);p&=p-1;
        if(cat[j][w]>=0)rows[121*k+cat[j][w]]^=uint64_t(1)<<(w-1);}
    }
  }
  uint64_t basis[39]={};int rank=0;
  std::array<uint64_t,6> proofs[39]={};
  for(int ri=0;ri<363;ri++) {
    uint64_t r=rows[ri];std::array<uint64_t,6> proof={};
    if(certificate)proof[ri/64]=uint64_t(1)<<(ri%64);
    while(r) {
      int j=__builtin_ctzll(r);
      if(j==39){
        if(certificate){certificate->clear();for(int k=0;k<363;k++)
          if((proof[k/64]>>(k%64))&1)certificate->push_back(k);}
        return -1;
      }
      if(!basis[j]){basis[j]=r;proofs[j]=proof;rank++;break;}
      r^=basis[j];
      if(certificate)for(int k=0;k<6;k++)proof[k]^=proofs[j][k];
    }
  }
  return 39-rank;
}
int main(int argc,char**argv) {
  for(int n=0;n<=4;n++)for(int j=0;j<pw[n];j++){len[off[n]+j]=n;cod[off[n]+j]=j;}
  for(int i=0;i<121;i++)for(int j=0;j<121;j++)cat[i][j]=
    len[i]+len[j]<=4?off[len[i]+len[j]]+cod[i]*pw[len[j]]+cod[j]:-1;
  for(int i=0;i<3;i++)X[i]=bit(i+1);
  A id={X[0],X[1],X[2]};
  U x=1^X[0],y=1^X[1],z=1^X[2],P=mul(mul(x,y),z);
  A delta={conj(y,z)^1,X[1],X[0]};
  A dinv={X[2],X[1],conj(inv(y),x)^1};
  assert(compose(delta,dinv)==id&&compose(dinv,delta)==id);
  A iny={conj(y,x)^1,X[1],conj(y,z)^1};
  assert(compose(delta,delta)==iny);
  assert(eval(delta,P)==conj(inv(x),P));
  A twists[2],tinvs[2];
  U xy=mul(x,y),yz=mul(y,z);
  twists[0]={conj(xy,x)^1,conj(xy,y)^1,X[2]};
  twists[1]={X[0],conj(yz,y)^1,conj(yz,z)^1};
  tinvs[0]={conj(inv(xy),x)^1,conj(inv(xy),y)^1,X[2]};
  tinvs[1]={X[0],conj(inv(yz),y)^1,conj(inv(yz),z)^1};
  for(int j=0;j<2;j++){
    assert(compose(twists[j],tinvs[j])==id);
    assert(eval(twists[j],P)==P);
  }
  std::vector<A> geom={id},ginv={id};std::vector<std::vector<int>> words(1);
  std::unordered_set<A,AH> seen;
  seen.insert(id);
  for(size_t i=0;i<geom.size();i++)for(int j=0;j<2;j++) {
    A h=compose(twists[j],geom[i]);
    if(seen.insert(h).second){
      geom.push_back(h);ginv.push_back(compose(ginv[i],tinvs[j]));
      words.push_back(words[i]);words.back().push_back(j);
      assert(geom.size()<1000000);
    }
  }
  std::vector<A> orbit;std::vector<std::vector<int>> orbitwords;
  std::unordered_set<A,AH> oseen;
  for(size_t i=0;i<geom.size();i++) {
    assert(compose(geom[i],ginv[i])==id);
    A h=compose(compose(geom[i],delta),ginv[i]);
    if(oseen.insert(h).second){orbit.push_back(h);orbitwords.push_back(words[i]);}
  }
  U X0=X[0],X1=X[1],X2=X[2];
  std::array<A,6> aa={
    A{br(br(X0,X1),X1),br(X0,br(X0,X1)),0},
    A{br(X0,br(X1,X2)),br(X0,br(X0,X2)),br(X0,br(X0,X1))},
    A{br(br(X0,X2),X2),0,br(X0,br(X0,X2))},
    A{br(X1,br(X1,X2)),br(br(X0,X2),X1),br(br(X0,X1),X1)},
    A{br(br(X1,X2),X2),br(br(X0,X2),X2),br(X0,br(X1,X2))^br(br(X0,X2),X1)},
    A{0,br(br(X1,X2),X2),br(X1,br(X1,X2))}
  };
  std::array<A,6> ds;
  for(int b=0;b<6;b++) {
    for(int j=0;j<3;j++)ds[b][j]=br(aa[b][j],X[j]);
    assert((ds[b][0]^ds[b][1]^ds[b][2])==0);
  }
  std::cout<<"geometric_aut_image_order="<<geom.size()<<"\n";
  std::cout<<"geometric_deck_conjugates_in_Aut="<<orbit.size()<<"\n";
  int failures=0,first=-1;
  for(int mask=0;mask<64;mask++) {
    A alpha=id;
    for(int b=0;b<6;b++)if(mask&(1<<b))for(int j=0;j<3;j++)alpha[j]^=ds[b][j];
    assert(compose(alpha,alpha)==id&&eval(alpha,P)==P);
    A target=compose(compose(alpha,delta),alpha);
    int matches=0;
    for(const A&beta:orbit)if(unit_intertwiner(target,beta)>=0)matches++;
    if(!matches){failures++;if(first<0)first=mask;}
    std::cout<<"mask="<<mask<<" unrestricted_unit_matches="<<matches<<"\n";
  }
  std::cout<<"certified_misses="<<failures<<"\nfirst_miss="<<first<<"\n";
  if(first>=0) {
    A alpha=id;
    for(int b=0;b<6;b++)if(first&(1<<b))for(int j=0;j<3;j++)alpha[j]^=ds[b][j];
    A target=compose(compose(alpha,delta),alpha);
    for(int j=0;j<3;j++)std::cout<<"witness_alpha_X"<<j<<"="<<hx(alpha[j])<<"\n";
    for(int j=0;j<3;j++)std::cout<<"witness_target_X"<<j<<"="<<hx(target[j])<<"\n";
    const char*path=argc>1?argv[1]:"ceh_pro2_certificates.json";
    std::ofstream f(path);assert(f);
    f<<"{\n  \"witness_mask\": "<<first<<",\n  \"geometric_group_order\": "
     <<geom.size()<<",\n  \"certificates\": [\n";
    for(size_t i=0;i<orbit.size();i++){
      std::vector<int> cert;assert(unit_intertwiner(target,orbit[i],&cert)==-1);
      f<<"    {\"twist_word\": [";
      for(size_t j=0;j<orbitwords[i].size();j++)f<<(j?",":"")<<orbitwords[i][j];
      f<<"], \"equation_rows\": [";
      for(size_t j=0;j<cert.size();j++)f<<(j?",":"")<<cert[j];
      f<<"]}"<<(i+1==orbit.size()?"":",")<<"\n";
    }
    f<<"  ]\n}\n";f.close();assert(f);
    std::cout<<"dual_certificates_written="<<path<<"\n";
  }
  return 0;
}
