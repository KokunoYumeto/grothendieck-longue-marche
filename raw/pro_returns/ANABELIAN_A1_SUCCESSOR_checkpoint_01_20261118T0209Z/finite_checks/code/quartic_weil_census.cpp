// Exact Weil data for every recovered pointed quartic, using precomputed
// cubic-root tables on the projection from the distinguished point.
#include <array>
#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <chrono>
using namespace std;
struct Field {
 int p,n,q;vector<int> modp,add,mul,neg;vector<unsigned char>roots;array<int,125>quad{};
 Field(int pp,vector<int>m):p(pp),n(m.size()-1),modp(m){
  q=1;for(int i=0;i<n;i++)q*=p;add.resize(q*q);mul.resize(q*q);neg.resize(q);
  for(int a=0;a<q;a++)for(int b=0;b<q;b++){
   vector<int>A(n),B(n),C(2*n-1);int aa=a,bb=b,z=0,pow=1;
   for(int i=0;i<n;i++){A[i]=aa%p;B[i]=bb%p;aa/=p;bb/=p;z+=((A[i]+B[i])%p)*pow;pow*=p;}
   add[a*q+b]=z;
   for(int i=0;i<n;i++)for(int j=0;j<n;j++)C[i+j]=(C[i+j]+A[i]*B[j])%p;
   for(int i=2*n-2;i>=n;i--)for(int j=0;j<n;j++)C[i-n+j]=(C[i-n+j]-C[i]*modp[j]%p+p)%p;
   z=0;pow=1;for(int i=0;i<n;i++){z+=C[i]*pow;pow*=p;}mul[a*q+b]=z;
  }
  for(int a=0;a<q;a++){bool inverse=a==0;for(int b=0;b<q;b++){if(add[a*q+b]==0)neg[a]=b;if(mul[a*q+b]==1)inverse=true;}if(!inverse)throw 1;}
  roots.resize(q*q*q);
  for(int a=0;a<q;a++)for(int b=0;b<q;b++)for(int z=0;z<q;z++){
   int z2=M(z,z),v=A(A(M(z2,z),M(a,z2)),M(b,z));roots[(a*q+b)*q+neg[v]]++;
  }
  for(int a=0;a<p;a++)for(int d=0;d<p;d++)for(int u=0;u<p;u++)for(int z=0;z<q;z++)if(A(A(M(a,M(z,z)),M(d,z)),u)==0)quad[(a*p+d)*p+u]++;
 }
 int A(int a,int b)const{return add[a*q+b];}int M(int a,int b)const{return mul[a*q+b];}
 int eval(const vector<int>&co,int x)const{int a=0;for(int i=co.size()-1;i>=0;i--)a=A(M(a,x),co[i]);return a;}
 int count(const vector<int>&f)const{
  int total=1+quad[(f[9]*p+f[12])*p+f[14]];
  for(int x=0;x<q;x++){
   int a=eval({f[2],f[6],f[9]},x),b=eval({f[3],f[7],f[10],f[12]},x),c=eval({f[4],f[8],f[11],f[13],f[14]},x);
   total+=roots[(a*q+b)*q+c];
  }
  return total;
 }
};
int main(int argc,char**argv){string dir=argc>1?argv[1]:".";auto start=chrono::steady_clock::now();
 for(int p:{3,5}){
  vector<Field>ks;
  ks.emplace_back(p,vector<int>{0,1});
  ks.emplace_back(p,p==3?vector<int>{1,0,1}:vector<int>{2,0,1});
  ks.emplace_back(p,p==3?vector<int>{1,2,0,1}:vector<int>{1,1,0,1});
  ifstream in(dir+"/pointed_quartic_F"+to_string(p)+"_census.csv");string line;getline(in,line);
  ofstream o(dir+"/quartic_F"+to_string(p)+"_weil.csv");o<<"contact,slice_code,orbit_size,N1,N2,N3,a1,a2,a3,h\n";int rows=0;
  while(getline(in,line)){
   stringstream ss(line);string s;vector<int>v;while(getline(ss,s,','))v.push_back(stoi(s));vector<int>f(v.begin()+4,v.end());
   int N1=ks[0].count(f),N2=ks[1].count(f),N3=ks[2].count(f);if(N1!=v[3])throw 2;
   long long s1=p+1-N1,s2=p*p+1-N2,s3=p*p*p+1-N3;
   int a1=-s1,a2=(s1*s1-s2)/2,a3=(-s1*s1*s1+3*s1*s2-2*s3)/6;
   int h=1+a1+a2+a3+p*a2+p*p*a1+p*p*p;if(h<=0)throw 3;
   o<<v[0]<<','<<v[1]<<','<<v[2]<<','<<N1<<','<<N2<<','<<N3<<','<<a1<<','<<a2<<','<<a3<<','<<h<<'\n';rows++;
  }
  cout<<"F"<<p<<" rows="<<rows<<" exact three-field counts and genus3 Weil polynomials"<<endl;
 }
 cout<<"seconds="<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<endl;
}
