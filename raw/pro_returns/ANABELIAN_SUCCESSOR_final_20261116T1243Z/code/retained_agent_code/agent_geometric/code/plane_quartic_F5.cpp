// Exact pointed plane-quartic census and Jacobian character tests over F5.
// No external arithmetic library is used.  See AG.23 for the divisor algorithm.
#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
constexpr int BASE=5;
int modp(int x){x%=BASE;return x<0?x+BASE:x;}
int invp(int x){static const int a[5]={0,1,3,2,4};return a[x];}
void need(bool x,const string&s){if(!x)throw runtime_error(s);}
struct Field{
 int d,q;vector<int> modulus;int ad[125][125]{},mu[125][125]{},iv[125]{},ng[125]{};
 Field(int dd,vector<int> mm):d(dd),q(1),modulus(mm){
  for(int i=0;i<d;i++)q*=BASE;
  for(int a=0;a<q;a++)for(int b=0;b<q;b++){
   int aa=a,bb=b,p=1,s=0;vector<int>A(d),B(d),C(2*d-1);
   for(int i=0;i<d;i++){A[i]=aa%BASE;B[i]=bb%BASE;aa/=BASE;bb/=BASE;s+=((A[i]+B[i])%BASE)*p;p*=BASE;}
   ad[a][b]=s;
   for(int i=0;i<d;i++)for(int j=0;j<d;j++)C[i+j]=modp(C[i+j]+A[i]*B[j]);
   for(int i=2*d-2;i>=d;i--)for(int j=0;j<d;j++)C[i-d+j]=modp(C[i-d+j]-C[i]*modulus[j]);
   p=1;s=0;for(int i=0;i<d;i++){s+=C[i]*p;p*=BASE;}mu[a][b]=s;
  }
  for(int a=0;a<q;a++){for(int b=0;b<q;b++){if(ad[a][b]==0)ng[a]=b;if(mu[a][b]==1)iv[a]=b;}if(a)need(iv[a]!=0,"field modulus not irreducible");}
 }
 int power(int a,int n)const{int b=1;while(n){if(n&1)b=mu[b][a];a=mu[a][a];n>>=1;}return b;}
};
vector<Field> fields;
vector<array<int,3>> mons[8];
int mi(int d,array<int,3>e){for(int i=0;i<(int)mons[d].size();i++)if(mons[d][i]==e)return i;throw runtime_error("monomial");}
struct ClosedPoint{int field,degree;array<int,3>p;vector<int> m4;};
vector<ClosedPoint> ambient;
int evalmon(const Field&F,array<int,3>e,array<int,3>p){int z=1;for(int i=0;i<3;i++)z=F.mu[z][F.power(p[i],e[i])];return z;}
void init(){
 for(int d=0;d<=7;d++)for(int i=0;i<=d;i++)for(int j=0;j<=d-i;j++)mons[d].push_back({i,j,d-i-j});
 fields.emplace_back(1,vector<int>{0});fields.emplace_back(2,vector<int>{2,0});fields.emplace_back(3,vector<int>{1,1,0});
 for(int fi=0;fi<3;fi++){
  const Field&F=fields[fi];vector<array<int,3>> all{{0,0,1}};
  for(int a=0;a<F.q;a++)all.push_back({0,1,a});
  for(int a=0;a<F.q;a++)for(int b=0;b<F.q;b++)all.push_back({1,a,b});
  for(auto p:all){auto r=p,mn=p;int period=0;do{for(auto&x:r)x=F.power(x,BASE);mn=min(mn,r);period++;}while(r!=p);
   if(period!=F.d||p!=mn)continue;
   ClosedPoint c{fi,F.d,p,{}};for(auto e:mons[4])c.m4.push_back(evalmon(F,e,p));ambient.push_back(c);
  }
 }
 need(ambient.size()==31+310+5240,"closed projective points");
}
vector<int> polymul(const vector<int>&a,int da,const vector<int>&b,int db){
 vector<int>c(mons[da+db].size());
 for(int i=0;i<(int)a.size();i++)if(a[i])for(int j=0;j<(int)b.size();j++)if(b[j]){
  array<int,3>e;for(int k=0;k<3;k++)e[k]=mons[da][i][k]+mons[db][j][k];
  int v=mi(da+db,e);c[v]=modp(c[v]+a[i]*b[j]);
 }return c;
}
struct Slice{int weight,offset,size;vector<int>variables;int fixed;};
vector<Slice>slices;
void init_slices(){
 int a=mi(4,{2,0,2}),b=mi(4,{1,1,2}),c=mi(4,{0,2,2});
 int d=mi(4,{3,0,1}),e=mi(4,{2,1,1}),u=mi(4,{4,0,0}),v=mi(4,{3,1,0});
 vector<set<int>>zeroes{{b,c,d},{a,b,c,e},{a,b,c,d,v}};
 vector<int>fixed{a,d,u};int offset=0;
 for(int type=0;type<3;type++){
  Slice S{type+2,offset,1,{},fixed[type]};
  for(int i=0;i<15;i++)if(i!=mi(4,{0,0,4})&&i!=mi(4,{1,0,3})&&i!=mi(4,{0,1,3})&&i!=S.fixed&&!zeroes[type].count(i)){S.variables.push_back(i);S.size*=BASE;}
  need((int)S.variables.size()==8-type,"slice dimension");slices.push_back(S);offset+=S.size;
 }
 need(offset==484375,"slice count");
}
const Slice& get_slice(int code){for(auto&S:slices)if(code<S.offset+S.size)return S;throw runtime_error("slice code");}
vector<int> decode(int code){const auto&S=get_slice(code);code-=S.offset;vector<int>f(15);f[mi(4,{0,1,3})]=1;f[S.fixed]=1;for(int i:S.variables){f[i]=code%BASE;code/=BASE;}return f;}
int rankp(vector<vector<int>>a,int n){int r=0;for(int j=0;j<n&&r<(int)a.size();j++){
 int k=r;while(k<(int)a.size()&&!a[k][j])k++;if(k==(int)a.size())continue;swap(a[k],a[r]);int u=invp(a[r][j]);for(int t=j;t<n;t++)a[r][t]=modp(a[r][t]*u);
 for(k=r+1;k<(int)a.size();k++)if(a[k][j]){u=a[k][j];for(int t=j;t<n;t++)a[k][t]=modp(a[k][t]-u*a[r][t]);}
 r++;
 }return r;}
vector<int> kernelp(vector<vector<int>>a,int n){
 vector<int>piv;int r=0;for(int j=0;j<n&&r<(int)a.size();j++){
  int k=r;while(k<(int)a.size()&&!a[k][j])k++;if(k==(int)a.size())continue;swap(a[k],a[r]);int u=invp(a[r][j]);for(int t=j;t<n;t++)a[r][t]=modp(a[r][t]*u);
  for(k=0;k<(int)a.size();k++)if(k!=r&&a[k][j]){u=a[k][j];for(int t=j;t<n;t++)a[k][t]=modp(a[k][t]-u*a[r][t]);}
  piv.push_back(j);r++;
 }
 if(r==n)return {};
 int free=0;while(find(piv.begin(),piv.end(),free)!=piv.end())free++;vector<int>v(n);v[free]=1;for(int i=0;i<r;i++)v[piv[i]]=modp(-a[i][free]);return v;
}
bool smooth(const vector<int>&f){
 vector<int>der[3];for(auto&v:der)v.assign(10,0);
 for(int i=0;i<15;i++)if(f[i])for(int j=0;j<3;j++)if(mons[4][i][j]%BASE){auto e=mons[4][i];int c=f[i]*e[j]--;der[j][mi(3,e)]=modp(c);}
 for(auto&cp:ambient)if(cp.degree==1){int nonzero=0;for(int j=0;j<3;j++){int z=0;for(int t=0;t<10;t++)z=modp(z+der[j][t]*evalmon(fields[0],mons[3][t],cp.p));nonzero|=z;}if(!nonzero)return false;}
 vector<vector<int>>matrix(36,vector<int>(45));
 for(int j=0;j<3;j++)for(int k=0;k<15;k++)for(int t=0;t<10;t++)if(der[j][t]){array<int,3>e;for(int u=0;u<3;u++)e[u]=mons[3][t][u]+mons[4][k][u];matrix[mi(7,e)][15*j+k]=der[j][t];}
 return rankp(matrix,45)==36;
}
vector<int> seriesmul(const Field&F,const vector<int>&a,const vector<int>&b,int n){vector<int>c(n+1);for(int i=0;i<=n&&i<(int)a.size();i++)if(a[i])for(int j=0;i+j<=n&&j<(int)b.size();j++)if(b[j])c[i+j]=F.ad[c[i+j]][F.mu[a[i]][b[j]]];return c;}
struct PointJets{ClosedPoint cp;vector<vector<int>>cubic,linear;};
PointJets makejets(const vector<int>&f,const ClosedPoint&cp){
 const Field&F=fields[cp.field];int chart=cp.p[2]?2:(cp.p[1]?1:0),n=12/cp.degree;
 array<int,3>p=cp.p;for(auto&x:p)x=F.mu[x][F.iv[cp.p[chart]]];
 vector<int>others;for(int i=0;i<3;i++)if(i!=chart)others.push_back(i);
 auto derivative=[&](int j){int z=0;for(int i=0;i<15;i++)if(f[i]&&mons[4][i][j]%BASE){auto e=mons[4][i];int a=modp(f[i]*e[j]);e[j]--;z=F.ad[z][F.mu[a][evalmon(F,e,p)]];}return z;};
 int dep=others[1],ind=others[0],der=derivative(dep);if(!der){swap(dep,ind);der=derivative(dep);}need(der!=0,"jet smoothness");
 vector<int>coord[3];for(int i=0;i<3;i++){coord[i].assign(n+1,0);coord[i][0]=p[i];}coord[ind][1]=1;
 auto getpowers=[&](int upto){vector<vector<vector<int>>>P(3,vector<vector<int>>(5));for(int j=0;j<3;j++){P[j][0]=vector<int>(upto+1);P[j][0][0]=1;for(int k=1;k<=4;k++)P[j][k]=seriesmul(F,P[j][k-1],coord[j],upto);}return P;};
 for(int t=1;t<=n;t++){auto powers=getpowers(t);int z=0;for(int i=0;i<15;i++)if(f[i]){auto e=mons[4][i];auto a=seriesmul(F,powers[0][e[0]],powers[1][e[1]],t);a=seriesmul(F,a,powers[2][e[2]],t);z=F.ad[z][F.mu[f[i]][a[t]]];}coord[dep][t]=F.mu[F.ng[z]][F.iv[der]];}
 auto powers=getpowers(n);vector<int>check(n+1);
 for(int i=0;i<15;i++)if(f[i]){auto e=mons[4][i];auto a=seriesmul(F,powers[0][e[0]],powers[1][e[1]],n);a=seriesmul(F,a,powers[2][e[2]],n);for(int t=0;t<=n;t++)check[t]=F.ad[check[t]][F.mu[f[i]][a[t]]];}
 need(all_of(check.begin(),check.end(),[](int z){return z==0;}),"curve jet identity");
 PointJets out{cp,{},{}};for(auto e:mons[3]){auto a=seriesmul(F,powers[0][e[0]],powers[1][e[1]],n);out.cubic.push_back(seriesmul(F,a,powers[2][e[2]],n));}
 for(auto e:mons[1]){auto a=seriesmul(F,powers[0][e[0]],powers[1][e[1]],n);out.linear.push_back(seriesmul(F,a,powers[2][e[2]],n));}return out;
}
using Div=string;
struct Curve{
 int code,N1=0,N2=0,N3=0,h=0,a1=0,a2=0,a3=0,np=0;vector<int>f;vector<PointJets>points;vector<Div>eff3,eff2,reps;vector<int>effclass,second;unordered_map<Div,int>effindex;unordered_map<long long,int>addcache;vector<int>pointclasses;int kappa;
 Curve(int id):code(id),f(decode(id)){
  for(auto&cp:ambient){const Field&F=fields[cp.field];int z=0;for(int i=0;i<15;i++)z=F.ad[z][F.mu[f[i]][cp.m4[i]]];if(!z){points.push_back(makejets(f,cp));if(cp.degree==1)N1++;else if(cp.degree==2)N2+=2;else N3+=3;}}
  np=points.size();N2+=N1;N3+=N1;need(points[0].cp.p==array<int,3>{0,0,1},"point at infinity");
  a1=N1-6;int s1=-a1,s2=26-N2,s3=126-N3;need((s1*s1-s2)%2==0,"Newton2");a2=(s1*s1-s2)/2;need((-s3-a1*s2-a2*s1)%3==0,"Newton3");a3=(-s3-a1*s2-a2*s1)/3;h=126+26*a1+6*a2+a3;need(h>0,"class number");
  Div d(np,0);enumerate(3,0,d,eff3);enumerate(2,0,d,eff2);for(int i=0;i<(int)eff3.size();i++)effindex[eff3[i]]=i;
  map<string,int>classes;map<int,int>specialcounts;vector<int>special;
  for(auto&D:eff3){auto l=section(D,1);string key;if(l.empty())key="N"+D;else{Div r=residual(D,l,1);int j=0;while(j<np&&!r[j])j++;need(j<np&&points[j].cp.degree==1&&r[j]==1,"special residual point");key="S"+to_string(j);specialcounts[j]++;}auto it=classes.find(key);if(it==classes.end()){int c=reps.size();classes[key]=c;reps.push_back(D);effclass.push_back(c);}else effclass.push_back(it->second);}
  need((int)reps.size()==h,"Pic3 count != zeta class number");need((int)eff3.size()==h+BASE*N1,"effective3 count");for(int j=0;j<N1;j++)need(specialcounts[j]==BASE+1,"special linear system size");
  Div base(np,0);base[0]=3;int zero=effclass[effindex.at(base)];if(zero){swap(reps[0],reps[zero]);for(auto&c:effclass){if(c==0)c=zero;else if(c==zero)c=0;}}
  second.resize(eff3.size());for(int i=0;i<(int)eff3.size();i++){Div v=eff3[i];v[0]+=6;auto l=section(v,3);need(!l.empty(),"second cubic section");Div r=residual(v,l,3);second[i]=effclass[effindex.at(r)];}
  for(int j=0;j<N1;j++){Div v(np,0);v[0]=2;v[j]++;pointclasses.push_back(effclass[effindex.at(v)]);}
  Div zeroD(np,0);zeroD[0]=3;auto specialP=classes.at("S0");kappa=specialP==zero?0:(specialP==0?zero:specialP);
  for(int x=0;x<h;x++){need(rawadd(x,0)==x,"raw identity");need(scale(x,h)==0,"group order annihilation");}
  for(int t=0;t<min(35,h*h);t++){int x=(7*t+3)%h,y=(11*t+1)%h,z=(13*t+2)%h;need(add(add(x,y),z)==add(x,add(y,z)),"associativity");}
 }
 void enumerate(int rem,int start,Div&d,vector<Div>&out){if(!rem){out.push_back(d);return;}for(int i=start;i<np;i++)if(points[i].cp.degree<=rem){d[i]++;enumerate(rem-points[i].cp.degree,i,d,out);d[i]--;}}
 vector<int> section(const Div&d,int deg){int n=mons[deg].size();vector<vector<int>>rows;
  for(int i=0;i<np;i++)if(d[i]){auto&J=points[i];auto&jets=deg==1?J.linear:J.cubic;for(int t=0;t<(int)(unsigned char)d[i];t++){vector<int>v(n);for(int j=0;j<n;j++)v[j]=jets[j][t];for(int k=0;k<J.cp.degree;k++){vector<int>r(n);for(int j=0;j<n;j++){r[j]=v[j]%BASE;v[j]/=BASE;}rows.push_back(r);}}}
  return kernelp(rows,n);
 }
 Div residual(const Div&d,const vector<int>&s,int deg){Div r(np,0);int total=0;for(int i=0;i<np;i++){
  const auto&J=points[i];const Field&F=fields[J.cp.field];const auto&jets=deg==1?J.linear:J.cubic;int maxv=4*deg/J.cp.degree,v=0;
  for(;v<=maxv;v++){int z=0;for(int j=0;j<(int)s.size();j++)z=F.ad[z][F.mu[s[j]][jets[j][v]]];if(z)break;}
  need(v<=maxv,"section vanishes beyond Bezout");need(v>=(int)(unsigned char)d[i],"section misses imposed divisor");r[i]=v-(unsigned char)d[i];total+=r[i]*J.cp.degree;
 }int imposed=0;for(int i=0;i<np;i++)imposed+=(unsigned char)d[i]*points[i].cp.degree;need(total==4*deg-imposed,"residual incomplete");return r;}
 int rawadd(int a,int b){Div d=reps[a];for(int i=0;i<np;i++)d[i]+=reps[b][i];d[0]+=3;auto s=section(d,3);need(!s.empty(),"first cubic section");Div r=residual(d,s,3);return second[effindex.at(r)];}
 int add(int a,int b){if(!a)return b;if(!b)return a;if(a>b)swap(a,b);long long key=(long long)a*h+b;auto it=addcache.find(key);if(it!=addcache.end())return it->second;int c=rawadd(a,b);addcache[key]=c;return c;}
 int scale(int a,int n){int b=0;while(n){if(n&1)b=add(a,b);a=add(a,a);n>>=1;}return b;}
};
void trim(vector<int>&v){while(!v.empty()&&!v.back())v.pop_back();}
vector<int> remainder(vector<int>a,const vector<int>&b){need(!b.empty(),"polynomial division");while(a.size()>=b.size()&&!a.empty()){int t=modp(a.back()*invp(b.back())),shift=a.size()-b.size();for(int i=0;i<(int)b.size();i++)a[i+shift]=modp(a[i+shift]-t*b[i]);trim(a);}return a;}
int powpscalar(int a,int n){int b=1;while(n){if(n&1)b=b*a%BASE;a=a*a%BASE;n>>=1;}return b;}
int resultantp(vector<int>a,vector<int>b){trim(a);trim(b);if(b.empty())return 0;if(b.size()==1)return powpscalar(b[0],a.size()-1);int m=a.size()-1,n=b.size()-1;if(m<n){int z=resultantp(b,a);return (m*n%2)?modp(-z):z;}auto r=remainder(a,b);if(r.empty())return 0;int factor=powpscalar(b.back(),m-(int)r.size()+1);if(m*n%2)factor=modp(-factor);return factor*resultantp(b,r)%BASE;}
void jsonvec(ostream&o,const vector<int>&v){o<<'[';for(int i=0;i<(int)v.size();i++){if(i)o<<',';o<<v[i];}o<<']';}
void jsondiv(ostream&o,const Div&v){o<<'[';bool first=true;for(int i=0;i<(int)v.size();i++)if(v[i]){if(!first)o<<',';first=false;o<<'['<<i<<','<<(int)(unsigned char)v[i]<<']';}o<<']';}
struct QData{int ell,rank;vector<int>basis,coords;};
QData quotient(Curve&C,int ell){
 vector<int>H;vector<bool>isH(C.h);for(int i=0;i<C.h;i++)isH[C.scale(i,ell)]=true;for(int i=0;i<C.h;i++)if(isH[i])H.push_back(i);
 vector<int>coset(C.h,-1),creps;for(int i=0;i<C.h;i++)if(coset[i]<0){int n=creps.size();creps.push_back(i);for(int j:H){int x=C.add(i,j);need(coset[x]<0||coset[x]==n,"coset disjointness");coset[x]=n;}}
 int nc=creps.size();need(nc*(int)H.size()==C.h,"quotient size");vector<int>cc(nc,-1),span{0},basis;cc[0]=0;int radix=1;
 while((int)span.size()<nc){int g=0;while(cc[g]>=0)g++;basis.push_back(creps[g]);vector<int>old=span;for(int t=1;t<ell;t++){int tg=C.scale(creps[g],t);for(int u:old){int v=coset[C.add(creps[u],tg)];need(cc[v]<0,"quotient basis independence");cc[v]=cc[u]+t*radix;span.push_back(v);}}radix*=ell;}
 need(radix==nc,"elementary quotient");vector<int>coords(C.h);for(int i=0;i<C.h;i++)coords[i]=cc[coset[i]];
 return {ell,(int)basis.size(),basis,coords};
}
int evaluate_character(int coord,const vector<int>&v,int ell){int a=0;for(int z:v){a=(a+z*(coord%ell))%ell;coord/=ell;}return a;}
int tests(Curve&C,ostream&out,ostream&csv){
 vector<int>primes;int m=C.h;for(int ell=2;ell<=m;ell++)if(m%ell==0){if(ell!=2&&ell!=BASE)primes.push_back(ell);while(m%ell==0)m/=ell;}
 out<<"{\"normalized_code\":"<<C.code<<",\"quartic_coefficients\":";jsonvec(out,C.f);out<<",\"N5\":"<<C.N1<<",\"N25\":"<<C.N2<<",\"N125\":"<<C.N3<<",\"Jacobian_order\":"<<C.h<<",\"zeta_numerator\":";jsonvec(out,{1,C.a1,C.a2,C.a3,BASE*C.a2,BASE*BASE*C.a1,BASE*BASE*BASE});
 out<<",\"closed_points\":[";for(int i=0;i<C.np;i++){if(i)out<<',';auto&p=C.points[i].cp;out<<"{\"degree\":"<<p.degree<<",\"coordinates\":["<<p.p[0]<<','<<p.p[1]<<','<<p.p[2]<<"]}";}out<<"],\"Pic3_representatives\":[";for(int i=0;i<C.h;i++){if(i)out<<',';jsondiv(out,C.reps[i]);}out<<"],\"tests\":[";
 bool first=true;int success=0,totaltests=0;
 for(int ell:primes){QData Q=quotient(C,ell);int nc=1;for(int i=0;i<Q.rank;i++)nc*=ell;
  vector<int>e2classes;for(auto D:C.eff2){D[0]++;e2classes.push_back(C.effclass[C.effindex.at(D)]);}
  for(int vcode=1;vcode<nc;vcode++){int n=vcode,firstnonzero=0;vector<int>v(Q.rank);for(int i=0;i<Q.rank;i++){v[i]=n%ell;n/=ell;if(!firstnonzero&&v[i])firstnonzero=v[i];}if(firstnonzero!=1)continue;
   vector<int>S1(ell),S2(ell),S3(ell),S4(ell);int kap=evaluate_character(Q.coords[C.kappa],v,ell);
   for(int x:C.pointclasses)S1[evaluate_character(Q.coords[x],v,ell)]++;
   for(int x:e2classes)S2[evaluate_character(Q.coords[x],v,ell)]++;
   for(int i=0;i<ell;i++)S3[(kap-i+ell)%ell]+=BASE*S1[i];
   S4[kap]=BASE*BASE;
   // Check the entire cubic coefficient independently by enumerating all
   // effective divisors of degree3.  The difference is exactly (h/ell) Phi_ell.
   vector<int>direct3(ell);for(int x:C.effclass)direct3[evaluate_character(Q.coords[x],v,ell)]++;
   for(int i=0;i<ell;i++)need(direct3[i]-S3[i]==C.h/ell,"direct cubic L coefficient");
   vector<int>value(ell),phi(ell,1);for(int i=0;i<ell;i++)value[i]=modp(S1[i]+S2[i]+(i==0));int norm=resultantp(phi,value);int gcddegree=0;auto aa=phi,bb=value;trim(bb);while(!bb.empty()){auto rr=remainder(aa,bb);aa=bb;bb=rr;}gcddegree=aa.size()-1;need((norm!=0)==(gcddegree==0),"resultant/gcd agreement");
   if(norm&&!success)success=ell;
   if(!first)out<<',';
   first=false;totaltests++;
   out<<"{\"ell\":"<<ell<<",\"character\":";jsonvec(out,v);out<<",\"quotient_basis_class_indices\":";jsonvec(out,Q.basis);out<<",\"quotient_coordinates_all_classes\":";jsonvec(out,Q.coords);out<<",\"L_coefficients_in_Z_zeta\":[[1],";jsonvec(out,S1);out<<',';jsonvec(out,S2);out<<',';jsonvec(out,S3);out<<',';jsonvec(out,S4);out<<"],\"relative_class_number_mod5\":"<<norm<<",\"mod5_gcd_degree\":"<<gcddegree<<'}';
   csv<<C.code<<",5,"<<ell<<",\"";for(int i=0;i<Q.rank;i++){if(i)csv<<';';csv<<v[i];}csv<<"\","<<norm<<','<<gcddegree<<','<<(norm?"witness over F5":"fails over F5")<<'\n';
  }
 }
 out<<"],\"least_successful_base_field_prime\":"<<success<<",\"group_checks\":\"Pic3 count, all order annihilations, identity, sampled associativity\"}\n";out.flush();csv.flush();return success;
}
int main(int argc,char**argv){
 try{
  string prefix=argc>1?argv[1]:"plane_quartic_F5";int limit=argc>2?stoi(argv[2]):0,startcode=argc>3?stoi(argv[3]):0;
  init();init_slices();vector<bool>seen(484375);vector<pair<int,int>>reps;long long weighted=0;
  for(int code=0;code<484375;code++)if(!seen[code]){
   const auto&S=get_slice(code);auto f=decode(code);set<int>orbit;
   for(int A=1;A<BASE;A++){int out=S.offset,power=1;for(int i:S.variables){int exponent=mons[4][i][0]+S.weight*mons[4][i][1]-S.weight;need(exponent>=0,"diagonal exponent");int factor=fields[0].power(A,exponent);out+=modp(f[i]*factor)*power;power*=BASE;}seen[out]=true;orbit.insert(out);}
   need(*orbit.begin()==code,"slice orbit minimum");if(smooth(f)){int size=500*orbit.size();reps.push_back({code,size});weighted+=size;}
  }
  cerr<<"Normalized forms244140625, slice forms484375, smooth pointed orbits "<<reps.size()<<", smooth normalized forms "<<weighted<<'\n';
  ofstream census(prefix+"_census.csv");census<<"normalized_code,orbit_size\n";for(auto [c,s]:reps)census<<c<<','<<s<<'\n';
  ofstream out(prefix+"_tests.jsonl"),csv(prefix+"_tests.csv"),summary(prefix+"_summary.json");csv<<"normalized_code,L_q,ell,character,relative_class_number_mod5,gcd_degree,status\n";
  int done=0,good=0,least3=0;map<int,int>byprime;auto began=chrono::steady_clock::now();
  for(auto [code,orb]:reps)if(code>=startcode){Curve C(code);int prime=tests(C,out,csv);done++;if(prime){good++;byprime[prime]++;if(prime==3)least3++;}if(done%25==0)cerr<<"done "<<done<<" code "<<code<<" witnesses "<<good<<" seconds "<<chrono::duration<double>(chrono::steady_clock::now()-began).count()<<'\n';if(limit&&done>=limit)break;}
  summary<<"{\"field\":5,\"normalized_forms\":244140625,\"slice_forms\":484375,\"smooth_normalized_forms\":"<<weighted<<",\"smooth_pointed_isomorphism_classes\":"<<reps.size()<<",\"tested_pointed_classes\":"<<done<<",\"base_field_witnesses\":"<<good<<",\"proved_global_least_prime_3\":"<<least3<<",\"least_successful_base_field_prime_distribution\":{";bool first=true;for(auto [p,n]:byprime){if(!first)summary<<',';first=false;summary<<'\"'<<p<<"\":"<<n;}summary<<"},\"scope\":\"all odd prime cyclic quotients over F5; no extension tests\",\"seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-began).count()<<"}\n";
  cerr<<"Completed "<<done<<" pointed classes; "<<good<<" witnesses.\n";
 }catch(const exception&e){cerr<<"ERROR: "<<e.what()<<'\n';return 1;}
}
