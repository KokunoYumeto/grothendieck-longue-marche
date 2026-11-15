// Exhaust the joint six-evaluation cycle system modulo four.
// This is a necessary finite system, not an assertion of full liftability.
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <algorithm>
using namespace std;
using U=uint64_t;
int mt[48][48], iv[48], ei;
vector<array<int,4>> mat;
U mul(U a,U b){U c=0;for(int k=0;k<6;k++)c|=U(mt[(a>>(6*k))&63][(b>>(6*k))&63])<<(6*k);return c;}
U inv(U a){U c=0;for(int k=0;k<6;k++)c|=U(iv[(a>>(6*k))&63])<<(6*k);return c;}
U conj(U a,U b){return mul(mul(a,b),inv(a));}
int main(){
 for(int a=0;a<4;a++)for(int b=0;b<4;b++)for(int c=0;c<4;c++)for(int d=0;d<4;d++)
  if((a*d-b*c+16)%4==1)mat.push_back({a,b,c,d});
 assert(mat.size()==48);
 auto idx=[&](array<int,4>a){return int(find(mat.begin(),mat.end(),a)-mat.begin());};
 for(int i=0;i<48;i++)for(int j=0;j<48;j++){
  auto a=mat[i],b=mat[j];mt[i][j]=idx({(a[0]*b[0]+a[1]*b[2])%4,(a[0]*b[1]+a[1]*b[3])%4,(a[2]*b[0]+a[3]*b[2])%4,(a[2]*b[1]+a[3]*b[3])%4});
 }
 ei=idx({1,0,0,1});for(int i=0;i<48;i++)for(int j=0;j<48;j++)if(mt[i][j]==ei)iv[i]=j;
 int ss=idx({0,1,3,0}),tt=idx({1,3,0,1}),zz=iv[mt[ss][tt]];
 int triple[3]={ss,tt,zz};U X=0,Y=0,ID=0;int k=0;
 for(int a=0;a<3;a++)for(int b=0;b<3;b++)if(a!=b){X|=U(triple[a])<<(6*k);Y|=U(triple[b])<<(6*k);ID|=U(ei)<<(6*k);k++;}
 U Z=inv(mul(X,Y));
 vector<U> G{ID};vector<uint32_t> parent{0};vector<unsigned char> letter{0},ex{0},ey{0};
 unordered_map<U,uint32_t> index;index.reserve(2200000);index[ID]=0;
 vector<array<uint32_t,2>> edges;
 bool loops[144]={};
 for(uint32_t i=0;i<G.size();i++){
  array<uint32_t,2> ed;
  for(int j=0;j<2;j++){
   U v=mul(G[i],j?Y:X);auto it=index.find(v);uint32_t ni;
   if(it==index.end()){ni=G.size();index.emplace(v,ni);G.push_back(v);parent.push_back(i);letter.push_back(j);ex.push_back((ex[i]+!j)%12);ey.push_back((ey[i]+j)%12);}
   else ni=it->second;
   ed[j]=ni;loops[((ex[i]+!j-ex[ni]+12)%12)*12+(ey[i]+j-ey[ni]+12)%12]=true;
  }
  edges.push_back(ed);
 }
 cerr<<"group "<<G.size()<<endl;
 vector<int> ag{0};bool aset[144]={};aset[0]=true;
 for(size_t i=0;i<ag.size();i++)for(int b=0;b<144;b++)if(loops[b]){
  int c=((ag[i]/12+b/12)%12)*12+(ag[i]%12+b%12)%12;
  if(!aset[c]){aset[c]=true;ag.push_back(c);}
 }
 cerr<<"abelianization "<<144/ag.size()<<endl;
 auto subst=[&](U a,U b,bool check,vector<U>&vals){
  vals.resize(G.size());vals[0]=ID;
  for(size_t i=1;i<G.size();i++)vals[i]=mul(vals[parent[i]],letter[i]?b:a);
  if(check)for(size_t i=0;i<G.size();i++)if(vals[edges[i][0]]!=mul(vals[i],a)||vals[edges[i][1]]!=mul(vals[i],b))return false;
  return true;
 };
 vector<U> th,ro,tmp;assert(subst(Y,X,true,th));assert(subst(Y,Z,true,ro));
 vector<uint32_t> roidx(G.size());for(size_t i=0;i<G.size();i++)roidx[i]=index.at(ro[i]);
 size_t derived=0,cycles=0,autos=0;vector<U> fs;
 for(size_t i=0;i<G.size();i++)if(aset[ex[i]*12+ey[i]]){
  derived++;U f=G[i];if(mul(f,th[i])!=ID)continue;
  if(mul(mul(ro[roidx[i]],ro[i]),f)!=ID)continue;
  cycles++;fs.push_back(f);
 }
 cerr<<"derived "<<derived<<" cycles "<<cycles<<endl;
 unordered_map<U,size_t> sframes,rframes;
 for(U f:fs){sframes[f]=0;rframes[f]=0;}
 for(size_t i=0;i<G.size();i++){
  U sf=mul(G[i],inv(th[i]));
  auto si=sframes.find(sf);if(si!=sframes.end())si->second++;
  U rf=mul(G[i],inv(ro[roidx[i]]));
  auto ri=rframes.find(rf);if(ri!=rframes.end())ri->second++;
 }
 ofstream out("LM8_PUSH/code/pbc_descent_cycle4.json");
 out<<"{\n\"scope\":\"Necessary six-evaluation finite cycle-automorphism system only; no full lift asserted\",\n\"modulus\":4,\n\"group_order\":"<<G.size()<<",\n\"derived_order\":"<<derived<<",\n\"cycle_count\":"<<cycles<<",\n\"rows\":[\n";
 for(U f:fs){
  U ay=conj(inv(f),Y);if(!subst(X,ay,true,tmp))continue;
  unordered_set<U> image(tmp.begin(),tmp.end());if(image.size()!=G.size())continue;
  auto fi=index.at(f);U h=mul(ro[fi],f);
  if(autos++)out<<",\n";
  out<<"{\"f\":"<<f<<",\"h\":"<<h<<",\"s_frames\":"<<sframes[f]<<",\"r_frames\":"<<rframes[f]<<",\"six_f\":[";
  for(int j=0;j<6;j++){if(j)out<<",";auto m=mat[(f>>(6*j))&63];out<<"["<<m[0]<<","<<m[1]<<","<<m[2]<<","<<m[3]<<"]";}
  out<<"],\"six_h\":[";
  for(int j=0;j<6;j++){if(j)out<<",";auto m=mat[(h>>(6*j))&63];out<<"["<<m[0]<<","<<m[1]<<","<<m[2]<<","<<m[3]<<"]";}
  out<<"]}";
 }
 out<<"\n],\n\"automorphism_count\":"<<autos<<"\n}\n";
 cout<<"group_order "<<G.size()<<"\nderived_order "<<derived<<"\ncycle_count "<<cycles<<"\nautomorphism_count "<<autos<<"\n";
}
