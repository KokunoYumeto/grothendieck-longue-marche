// All degree-seven Kummer branch vectors on P1(F8), modulo PGL2(F8)
// and multiplication by a nonzero element of F7. Exact orbit census.
#include <array>
#include <vector>
#include <set>
#include <fstream>
#include <iostream>
#include <algorithm>
using namespace std;
int mul(int a,int b){int z=0;while(b){if(b&1)z^=a;b>>=1;a<<=1;if(a&8)a^=11;}return z;}
int pw(int a,int n){int z=1;while(n){if(n&1)z=mul(z,a);a=mul(a,a);n>>=1;}return z;}
array<int,9> decode(int c){array<int,9>e={};int sum=0;for(int i=0;i<8;i++){e[i]=c%7;c/=7;sum+=e[i];}e[8]=(7-sum%7)%7;return e;}
int encode(array<int,9>e){int first=0;while(!e[first])first++;int inv=1;while(inv*e[first]%7!=1)inv++;int z=0,m=1;for(int i=0;i<8;i++){z+=e[i]*inv%7*m;m*=7;}return z;}
int main(int argc,char**argv){
 string name=argc>1?argv[1]:"b5_all_f8_orbits.csv";set<array<int,9>>unique;
 for(int a=0;a<8;a++)for(int b=0;b<8;b++)for(int c=0;c<8;c++)for(int d=0;d<8;d++)if(mul(a,d)!=mul(b,c)){
  array<int,9> perm={};for(int x=0;x<9;x++){
   int u=x==8?a:(mul(a,x)^b),v=x==8?c:(mul(c,x)^d);
   perm[x]=v?mul(u,pw(v,6)):8;
  }unique.insert(perm);
 }
 if(unique.size()!=504)return 1;vector<array<int,9>>perms(unique.begin(),unique.end());
 vector<unsigned char>done(5764801);ofstream out(name);out<<"branches,orbit_size,code";for(int i=0;i<9;i++)out<<",e"<<i;out<<'\n';
 long long weights[10]={};int nums[10]={};
 for(int code=1;code<5764801;code++)if(!done[code]){
  auto e=decode(code);int r=0,first=0;for(int a:e)r+=a!=0;while(!e[first])first++;
  if(r<8||e[first]!=1)continue;set<int>orbit;int chosen=code;
  for(auto perm:perms){array<int,9>v={};for(int i=0;i<9;i++)v[perm[i]]=e[i];int z=encode(v);done[z]=1;orbit.insert(z);if(r==8&&v[8]==0)chosen=z;}
  if(r==9)chosen=*orbit.begin();auto norm=decode(chosen);if(norm[0]!=1)return 2;
  if(r==8&&norm[8])return 3;nums[r]++;weights[r]+=orbit.size();out<<r<<','<<orbit.size()<<','<<chosen;for(int v:norm)out<<','<<v;out<<'\n';
 }
 for(int r=8;r<=9;r++)cout<<"branches "<<r<<" orbits "<<nums[r]<<" scalar-normalized vectors "<<weights[r]<<'\n';
 if(weights[8]!=359919||weights[9]!=239945)return 4;
 cout<<"PASS exact PGL2(F8) census for eight and nine branch points\n";
}
