// Exact pointed plane-quartic census and Jacobian character tests over F3.
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
int mod3(int x){x%=3;return x<0?x+3:x;}
void need(bool x,const string&s){if(!x)throw runtime_error(s);}
struct Field{
 int d,q;vector<int> modulus;int ad[27][27]{},mu[27][27]{},iv[27]{},ng[27]{};
 Field(int dd,vector<int> mm):d(dd),q(1),modulus(mm){
  for(int i=0;i<d;i++)q*=3;
  for(int a=0;a<q;a++)for(int b=0;b<q;b++){
   int aa=a,bb=b,p=1,s=0;vector<int>A(d),B(d),C(2*d-1);
   for(int i=0;i<d;i++){A[i]=aa%3;B[i]=bb%3;aa/=3;bb/=3;s+=((A[i]+B[i])%3)*p;p*=3;}
   ad[a][b]=s;
   for(int i=0;i<d;i++)for(int j=0;j<d;j++)C[i+j]=mod3(C[i+j]+A[i]*B[j]);
   for(int i=2*d-2;i>=d;i--)for(int j=0;j<d;j++)C[i-d+j]=mod3(C[i-d+j]-C[i]*modulus[j]);
   p=1;s=0;for(int i=0;i<d;i++){s+=C[i]*p;p*=3;}mu[a][b]=s;
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
 fields.emplace_back(1,vector<int>{0});fields.emplace_back(2,vector<int>{1,0});fields.emplace_back(3,vector<int>{1,2,0});
 for(int fi=0;fi<3;fi++){
  const Field&F=fields[fi];vector<array<int,3>> all{{0,0,1}};
  for(int a=0;a<F.q;a++)all.push_back({0,1,a});
  for(int a=0;a<F.q;a++)for(int b=0;b<F.q;b++)all.push_back({1,a,b});
  for(auto p:all){auto r=p,mn=p;int period=0;do{for(auto&x:r)x=F.power(x,3);mn=min(mn,r);period++;}while(r!=p);
   if(period!=F.d||p!=mn)continue;
   ClosedPoint c{fi,F.d,p,{}};for(auto e:mons[4])c.m4.push_back(evalmon(F,e,p));ambient.push_back(c);
  }
 }
 need(ambient.size()==13+39+248,"closed projective points");
}
vector<int> polymul(const vector<int>&a,int da,const vector<int>&b,int db){
 vector<int>c(mons[da+db].size());
 for(int i=0;i<(int)a.size();i++)if(a[i])for(int j=0;j<(int)b.size();j++)if(b[j]){
  array<int,3>e;for(int k=0;k<3;k++)e[k]=mons[da][i][k]+mons[db][j][k];
  int v=mi(da+db,e);c[v]=mod3(c[v]+a[i]*b[j]);
 }return c;
}
vector<int> variable_indices;vector<array<array<int,13>,12>> actions;
void init_actions(){
 int yz=mi(4,{0,1,3});for(int i=0;i<15;i++)if(i!=mi(4,{0,0,4})&&i!=mi(4,{1,0,3})&&i!=yz)variable_indices.push_back(i);
 for(int A:{1,2})for(int C:{1,2})for(int B=0;B<3;B++)for(int D=0;D<3;D++)for(int E=0;E<3;E++){
  vector<int>lin[3];for(auto&v:lin)v.assign(3,0);
  lin[0][mi(1,{1,0,0})]=A;lin[0][mi(1,{0,1,0})]=B;
  lin[1][mi(1,{0,1,0})]=C;
  lin[2][mi(1,{1,0,0})]=D;lin[2][mi(1,{0,1,0})]=E;lin[2][mi(1,{0,0,1})]=1;
  vector<int>powers[3][5];for(int v=0;v<3;v++){powers[v][0]={1};for(int k=1;k<=4;k++)powers[v][k]=polymul(powers[v][k-1],k-1,lin[v],1);}
  array<array<int,13>,12> mat{};
  for(int col=0;col<13;col++){
   int ind=col==12?yz:variable_indices[col];auto e=mons[4][ind];
   auto temp=polymul(powers[0][e[0]],e[0],powers[1][e[1]],e[1]);temp=polymul(temp,e[0]+e[1],powers[2][e[2]],e[2]);
   for(int row=0;row<12;row++)mat[row][col]=mod3(C*temp[variable_indices[row]]);
  }actions.push_back(mat);
 }need(actions.size()==108,"stabilizer size");
}
vector<int> decode(int code){vector<int>f(15);f[mi(4,{0,1,3})]=1;for(int i:variable_indices){f[i]=code%3;code/=3;}return f;}
int rank3(vector<vector<int>>a,int n){int r=0;for(int j=0;j<n&&r<(int)a.size();j++){
 int k=r;while(k<(int)a.size()&&!a[k][j])k++;if(k==(int)a.size())continue;swap(a[k],a[r]);int u=a[r][j];for(int t=j;t<n;t++)a[r][t]=mod3(a[r][t]*u);
 for(k=r+1;k<(int)a.size();k++)if(a[k][j]){u=a[k][j];for(int t=j;t<n;t++)a[k][t]=mod3(a[k][t]-u*a[r][t]);}
 r++;
 }return r;}
vector<int> kernel3(vector<vector<int>>a,int n){
 vector<int>piv;int r=0;for(int j=0;j<n&&r<(int)a.size();j++){
  int k=r;while(k<(int)a.size()&&!a[k][j])k++;if(k==(int)a.size())continue;swap(a[k],a[r]);int u=a[r][j];for(int t=j;t<n;t++)a[r][t]=mod3(a[r][t]*u);
  for(k=0;k<(int)a.size();k++)if(k!=r&&a[k][j]){u=a[k][j];for(int t=j;t<n;t++)a[k][t]=mod3(a[k][t]-u*a[r][t]);}
  piv.push_back(j);r++;
 }
 if(r==n)return {};
 int free=0;while(find(piv.begin(),piv.end(),free)!=piv.end())free++;vector<int>v(n);v[free]=1;for(int i=0;i<r;i++)v[piv[i]]=mod3(-a[i][free]);return v;
}
bool smooth(const vector<int>&f){
 vector<int>der[3];for(auto&v:der)v.assign(10,0);
 for(int i=0;i<15;i++)if(f[i])for(int j=0;j<3;j++)if(mons[4][i][j]%3){auto e=mons[4][i];int c=f[i]*e[j]--;der[j][mi(3,e)]=mod3(c);}
 for(auto&cp:ambient)if(cp.degree==1){int nonzero=0;for(int j=0;j<3;j++){int z=0;for(int t=0;t<10;t++)z=mod3(z+der[j][t]*evalmon(fields[0],mons[3][t],cp.p));nonzero|=z;}if(!nonzero)return false;}
 vector<vector<int>>matrix(36,vector<int>(45));
 for(int j=0;j<3;j++)for(int k=0;k<15;k++)for(int t=0;t<10;t++)if(der[j][t]){array<int,3>e;for(int u=0;u<3;u++)e[u]=mons[3][t][u]+mons[4][k][u];matrix[mi(7,e)][15*j+k]=der[j][t];}
 return rank3(matrix,45)==36;
}
vector<int> seriesmul(const Field&F,const vector<int>&a,const vector<int>&b,int n){vector<int>c(n+1);for(int i=0;i<=n&&i<(int)a.size();i++)if(a[i])for(int j=0;i+j<=n&&j<(int)b.size();j++)if(b[j])c[i+j]=F.ad[c[i+j]][F.mu[a[i]][b[j]]];return c;}
struct PointJets{ClosedPoint cp;vector<vector<int>>cubic,linear;};
PointJets makejets(const vector<int>&f,const ClosedPoint&cp){
 const Field&F=fields[cp.field];int chart=cp.p[2]?2:(cp.p[1]?1:0),n=12/cp.degree;
 array<int,3>p=cp.p;for(auto&x:p)x=F.mu[x][F.iv[cp.p[chart]]];
 vector<int>others;for(int i=0;i<3;i++)if(i!=chart)others.push_back(i);
 auto derivative=[&](int j){int z=0;for(int i=0;i<15;i++)if(f[i]&&mons[4][i][j]%3){auto e=mons[4][i];int a=mod3(f[i]*e[j]);e[j]--;z=F.ad[z][F.mu[a][evalmon(F,e,p)]];}return z;};
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
  a1=N1-4;int s1=-a1,s2=10-N2,s3=28-N3;need((s1*s1-s2)%2==0,"Newton2");a2=(s1*s1-s2)/2;need((-s3-a1*s2-a2*s1)%3==0,"Newton3");a3=(-s3-a1*s2-a2*s1)/3;h=28+10*a1+4*a2+a3;need(h>0,"class number");
  Div d(np,0);enumerate(3,0,d,eff3);enumerate(2,0,d,eff2);for(int i=0;i<(int)eff3.size();i++)effindex[eff3[i]]=i;
  map<string,int>classes;map<int,int>specialcounts;vector<int>special;
  for(auto&D:eff3){auto l=section(D,1);string key;if(l.empty())key="N"+D;else{Div r=residual(D,l,1);int j=0;while(j<np&&!r[j])j++;need(j<np&&points[j].cp.degree==1&&r[j]==1,"special residual point");key="S"+to_string(j);specialcounts[j]++;}auto it=classes.find(key);if(it==classes.end()){int c=reps.size();classes[key]=c;reps.push_back(D);effclass.push_back(c);}else effclass.push_back(it->second);}
  need((int)reps.size()==h,"Pic3 count != zeta class number");need((int)eff3.size()==h+3*N1,"effective3 count");for(int j=0;j<N1;j++)need(specialcounts[j]==4,"special linear system size");
  Div base(np,0);base[0]=3;int zero=effclass[effindex.at(base)];if(zero){swap(reps[0],reps[zero]);for(auto&c:effclass){if(c==0)c=zero;else if(c==zero)c=0;}}
  second.resize(eff3.size());for(int i=0;i<(int)eff3.size();i++){Div v=eff3[i];v[0]+=6;auto l=section(v,3);need(!l.empty(),"second cubic section");Div r=residual(v,l,3);second[i]=effclass[effindex.at(r)];}
  for(int j=0;j<N1;j++){Div v(np,0);v[0]=2;v[j]++;pointclasses.push_back(effclass[effindex.at(v)]);}
  Div zeroD(np,0);zeroD[0]=3;auto specialP=classes.at("S0");kappa=specialP==zero?0:(specialP==0?zero:specialP);
  for(int x=0;x<h;x++){need(rawadd(x,0)==x,"raw identity");need(scale(x,h)==0,"group order annihilation");}
  for(int t=0;t<min(35,h*h);t++){int x=(7*t+3)%h,y=(11*t+1)%h,z=(13*t+2)%h;need(add(add(x,y),z)==add(x,add(y,z)),"associativity");}
 }
 void enumerate(int rem,int start,Div&d,vector<Div>&out){if(!rem){out.push_back(d);return;}for(int i=start;i<np;i++)if(points[i].cp.degree<=rem){d[i]++;enumerate(rem-points[i].cp.degree,i,d,out);d[i]--;}}
 vector<int> section(const Div&d,int deg){int n=mons[deg].size();vector<vector<int>>rows;
  for(int i=0;i<np;i++)if(d[i]){auto&J=points[i];auto&jets=deg==1?J.linear:J.cubic;for(int t=0;t<(int)(unsigned char)d[i];t++){vector<int>v(n);for(int j=0;j<n;j++)v[j]=jets[j][t];for(int k=0;k<J.cp.degree;k++){vector<int>r(n);for(int j=0;j<n;j++){r[j]=v[j]%3;v[j]/=3;}rows.push_back(r);}}}
  return kernel3(rows,n);
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
vector<int> remainder(vector<int>a,const vector<int>&b){need(!b.empty(),"polynomial division");while(a.size()>=b.size()&&!a.empty()){int t=mod3(a.back()*b.back()),shift=a.size()-b.size();for(int i=0;i<(int)b.size();i++)a[i+shift]=mod3(a[i+shift]-t*b[i]);trim(a);}return a;}
int pow3scalar(int a,int n){int b=1;while(n){if(n&1)b=b*a%3;a=a*a%3;n>>=1;}return b;}
int resultant3(vector<int>a,vector<int>b){trim(a);trim(b);if(b.empty())return 0;if(b.size()==1)return pow3scalar(b[0],a.size()-1);int m=a.size()-1,n=b.size()-1;if(m<n){int z=resultant3(b,a);return (m*n%2)?mod3(-z):z;}auto r=remainder(a,b);if(r.empty())return 0;int factor=pow3scalar(b.back(),m-(int)r.size()+1);if(m*n%2)factor=mod3(-factor);return factor*resultant3(b,r)%3;}
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
 vector<int>primes;int m=C.h;for(int ell=2;ell<=m;ell++)if(m%ell==0){if(ell!=2&&ell!=3)primes.push_back(ell);while(m%ell==0)m/=ell;}
 out<<"{\"normalized_code\":"<<C.code<<",\"quartic_coefficients\":";jsonvec(out,C.f);out<<",\"N3\":"<<C.N1<<",\"N9\":"<<C.N2<<",\"N27\":"<<C.N3<<",\"Jacobian_order\":"<<C.h<<",\"zeta_numerator\":";jsonvec(out,{1,C.a1,C.a2,C.a3,3*C.a2,9*C.a1,27});
 out<<",\"closed_points\":[";for(int i=0;i<C.np;i++){if(i)out<<',';auto&p=C.points[i].cp;out<<"{\"degree\":"<<p.degree<<",\"coordinates\":["<<p.p[0]<<','<<p.p[1]<<','<<p.p[2]<<"]}";}out<<"],\"Pic3_representatives\":[";for(int i=0;i<C.h;i++){if(i)out<<',';jsondiv(out,C.reps[i]);}out<<"],\"tests\":[";
 bool first=true;int success=0,totaltests=0;
 for(int ell:primes){QData Q=quotient(C,ell);int nc=1;for(int i=0;i<Q.rank;i++)nc*=ell;
  vector<int>e2classes;for(auto D:C.eff2){D[0]++;e2classes.push_back(C.effclass[C.effindex.at(D)]);}
  for(int vcode=1;vcode<nc;vcode++){int n=vcode,firstnonzero=0;vector<int>v(Q.rank);for(int i=0;i<Q.rank;i++){v[i]=n%ell;n/=ell;if(!firstnonzero&&v[i])firstnonzero=v[i];}if(firstnonzero!=1)continue;
   vector<int>S1(ell),S2(ell),S3(ell),S4(ell);int kap=evaluate_character(Q.coords[C.kappa],v,ell);
   for(int x:C.pointclasses)S1[evaluate_character(Q.coords[x],v,ell)]++;
   for(int x:e2classes)S2[evaluate_character(Q.coords[x],v,ell)]++;
   for(int i=0;i<ell;i++)S3[(kap-i+ell)%ell]+=3*S1[i];
   S4[kap]=9;
   // Check the entire cubic coefficient independently by enumerating all
   // effective divisors of degree3.  The difference is exactly (h/ell) Phi_ell.
   vector<int>direct3(ell);for(int x:C.effclass)direct3[evaluate_character(Q.coords[x],v,ell)]++;
   for(int i=0;i<ell;i++)need(direct3[i]-S3[i]==C.h/ell,"direct cubic L coefficient");
   vector<int>value(ell),phi(ell,1);for(int i=0;i<ell;i++)value[i]=mod3(S1[i]+S2[i]+(i==0));int norm=resultant3(phi,value);int gcddegree=0;auto aa=phi,bb=value;trim(bb);while(!bb.empty()){auto rr=remainder(aa,bb);aa=bb;bb=rr;}gcddegree=aa.size()-1;need((norm!=0)==(gcddegree==0),"resultant/gcd agreement");
   if(norm&&!success)success=ell;
   if(!first)out<<',';
   first=false;totaltests++;
   out<<"{\"ell\":"<<ell<<",\"character\":";jsonvec(out,v);out<<",\"quotient_basis_class_indices\":";jsonvec(out,Q.basis);out<<",\"quotient_coordinates_all_classes\":";jsonvec(out,Q.coords);out<<",\"L_coefficients_in_Z_zeta\":[[1],";jsonvec(out,S1);out<<',';jsonvec(out,S2);out<<',';jsonvec(out,S3);out<<',';jsonvec(out,S4);out<<"],\"relative_class_number_mod3\":"<<norm<<",\"mod3_gcd_degree\":"<<gcddegree<<'}';
   csv<<C.code<<",3,"<<ell<<",\"";for(int i=0;i<Q.rank;i++){if(i)csv<<';';csv<<v[i];}csv<<"\","<<norm<<','<<gcddegree<<','<<(norm?"witness over F3":"fails over F3")<<'\n';
  }
 }
 out<<"],\"least_successful_base_field_prime\":"<<success<<",\"group_checks\":\"Pic3 count, all order annihilations, identity, sampled associativity\"}\n";out.flush();csv.flush();return success;
}
int main(int argc,char**argv){
 try{
  string prefix=argc>1?argv[1]:"plane_quartic_F3";int limit=argc>2?stoi(argv[2]):0,startcode=argc>3?stoi(argv[3]):0;
  init();init_actions();vector<bool>seen(531441);vector<pair<int,int>>reps;long long weighted=0;
  for(int code=0;code<531441;code++)if(!seen[code]){vector<int>v(13);int z=code;for(int i=0;i<12;i++){v[i]=z%3;z/=3;}v[12]=1;set<int>orbit;for(auto&A:actions){int out=0,p=1;for(int i=0;i<12;i++){int t=0;for(int j=0;j<13;j++)t+=A[i][j]*v[j];out+=(t%3)*p;p*=3;}seen[out]=true;orbit.insert(out);}need(*orbit.begin()==code,"orbit minimum");if(smooth(decode(code))){reps.push_back({code,(int)orbit.size()});weighted+=orbit.size();}}
  cerr<<"Normalized forms531441, smooth pointed orbits "<<reps.size()<<", smooth normalized forms "<<weighted<<'\n';
  ofstream census(prefix+"_census.csv");census<<"normalized_code,orbit_size\n";for(auto [c,s]:reps)census<<c<<','<<s<<'\n';
  ofstream out(prefix+"_tests.jsonl"),csv(prefix+"_tests.csv"),summary(prefix+"_summary.json");csv<<"normalized_code,L_q,ell,character,relative_class_number_mod3,gcd_degree,status\n";
  int done=0,good=0,least5=0;map<int,int>byprime;auto began=chrono::steady_clock::now();
  for(auto [code,orb]:reps)if(code>=startcode){Curve C(code);int prime=tests(C,out,csv);done++;if(prime){good++;byprime[prime]++;if(prime==5)least5++;}if(done%25==0)cerr<<"done "<<done<<" code "<<code<<" witnesses "<<good<<" seconds "<<chrono::duration<double>(chrono::steady_clock::now()-began).count()<<'\n';if(limit&&done>=limit)break;}
  summary<<"{\"field\":3,\"normalized_forms\":531441,\"smooth_normalized_forms\":"<<weighted<<",\"smooth_pointed_isomorphism_classes\":"<<reps.size()<<",\"tested_pointed_classes\":"<<done<<",\"base_field_witnesses\":"<<good<<",\"proved_global_least_prime_5\":"<<least5<<",\"least_successful_base_field_prime_distribution\":{";bool first=true;for(auto [p,n]:byprime){if(!first)summary<<',';first=false;summary<<'\"'<<p<<"\":"<<n;}summary<<"},\"scope\":\"all odd prime cyclic quotients over F3; no extension tests\",\"seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-began).count()<<"}\n";
  cerr<<"Completed "<<done<<" pointed classes; "<<good<<" witnesses.\n";
 }catch(const exception&e){cerr<<"ERROR: "<<e.what()<<'\n';return 1;}
}
