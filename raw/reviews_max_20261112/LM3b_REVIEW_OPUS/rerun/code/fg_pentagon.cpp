// Independent direct computation in t4 / centre = Lie(u,v,w) semidirect Lie(a,b).
// Sparse associative-word model, modular arithmetic. No precomputed GT dimensions.
#include <bits/stdc++.h>
using namespace std;
const int P=65521;
struct Poly {int d;vector<pair<int,int>> t;};
vector<int> pw(16,1);
int norm(long long x){x%=P;if(x<0)x+=P;return x;}
Poly zero(int d){return Poly{d,{}};}
Poly gen(int i){return Poly{1,{{i,1}}};}
Poly fromDense(int d,const vector<long long>&a){Poly z=zero(d);for(int i=0;i<(int)a.size();i++){int c=norm(a[i]);if(c)z.t.push_back({i,c});}return z;}
Poly add(const Poly&a,const Poly&b,int sign=1){if(a.d!=b.d)throw runtime_error("degree add");vector<long long>c(pw[a.d]);for(auto [i,x]:a.t)c[i]+=x;for(auto[i,x]:b.t)c[i]+=sign*x;return fromDense(a.d,c);}
Poly neg(Poly a){for(auto&[i,x]:a.t)x=P-x;return a;}
Poly br(const Poly&a,const Poly&b){int d=a.d+b.d;vector<long long>c(pw[d]);for(auto[i,x]:a.t)for(auto[j,y]:b.t){long long k=1LL*x*y;c[i*pw[b.d]+j]+=k;c[j*pw[a.d]+i]-=k;}return fromDense(d,c);}
using Der=array<Poly,3>;
Poly der(const Der&D,const Poly&f){int e=D[0].d-1,n=f.d;vector<long long>c(pw[e+n]);for(auto[w,x]:f.t){for(int pos=0;pos<n;pos++){int suf=n-1-pos,b=pw[suf],letter=(w/b)%3,pre=w/(b*3),post=w%b;for(auto[v,y]:D[letter].t){int code=pre*pw[e+1+suf]+v*b+post;c[code]+=1LL*x*y;}}}return fromDense(e+n,c);}
Der db(const Der&A,const Der&B){Der z;for(int i=0;i<3;i++)z[i]=add(der(A,B[i]),der(B,A[i]),-1);return z;}
bool lynd(const string&w){for(int i=1;i<(int)w.size();i++)if(w>=w.substr(i))return false;return true;}
pair<string,string> split(const string&w){for(int i=1;i<(int)w.size();i++)if(lynd(w.substr(i)))return {w.substr(0,i),w.substr(i)};throw runtime_error("split");}
map<string,Der> dc;
map<string,array<Poly,4>> ec;
Der da,dbb;
const Der& action(const string&w){auto it=dc.find(w);if(it!=dc.end())return it->second;auto[u,v]=split(w);return dc.emplace(w,db(action(u),action(v))).first->second;}
Poly baseAct(const string&w,int k,const Poly&f){ // base of evaluation k at word w
 if(k==0)return der(action(w),f);
 if(w!="0")return zero((int)w.size()+f.d);
 if(k==1)return neg(der(da,f));
 if(k==2)return der(dbb,f);
 return neg(der(dbb,f));
}
array<Poly,4> calc(const string&w){auto it=ec.find(w);if(it!=ec.end())return it->second;auto[u,v]=split(w);auto A=calc(u),B=calc(v);array<Poly,4>Z;for(int k=0;k<4;k++){Z[k]=br(A[k],B[k]);Z[k]=add(Z[k],baseAct(u,k,B[k]));Z[k]=add(Z[k],baseAct(v,k,A[k]),-1);}return Z;}
int inv(int a){int b=P-2,z=1;while(b){if(b&1)z=1LL*z*a%P;a=1LL*a*a%P;b>>=1;}return z;}
int main(){for(int i=1;i<16;i++)pw[i]=pw[i-1]*3;auto u=gen(0),v=gen(1),w=gen(2);da={br(u,v),br(v,u),zero(2)};dbb={zero(2),br(v,w),br(w,v)};dc["0"]=da;dc["1"]=dbb;auto s=add(add(u,v),w);ec["0"]={zero(1),neg(s),zero(1),neg(s)};ec["1"]={v,w,w,add(v,w)};
 int N;cin>>N;
 cout<<"prime "<<P<<"\nweight candidates pentagon_rank solutions pivot_words\n";
 for(int n=1;n<=N;n++){
 int nn,r,k;cin>>nn>>r>>k;if(nn!=n)return 2;vector<string>words(r);for(auto&x:words)cin>>x;vector<vector<int>>coeff(k,vector<int>(r));for(auto&row:coeff)for(auto&x:row)cin>>x;
 vector<vector<int>> images(k,vector<int>(pw[n]));
 if(n>=3){for(int j=0;j<r;j++){auto z=calc(words[j]);if(n<N)ec[words[j]]=z;auto pent=add(add(z[0],z[1]),add(z[2],z[3]),-1);for(int h=0;h<k;h++)if(coeff[h][j])for(auto[t,c]:pent.t)images[h][t]=norm(images[h][t]+1LL*coeff[h][j]*c);}}
 else { // W1 and W2 are independently forced zero by pentagon and 3-cycle.
 }
 int rank=(n==1 ? k : 0);vector<int>piv;
 for(int row=0;row<pw[n]&&rank<k;row++){int j=rank;while(j<k&&!images[j][row])j++;if(j==k)continue;swap(images[j],images[rank]);int a=inv(images[rank][row]);for(int t=row;t<pw[n];t++)images[rank][t]=1LL*images[rank][t]*a%P;for(int h=rank+1;h<k;h++){int q=images[h][row];if(q)for(int t=row;t<pw[n];t++)images[h][t]=norm(images[h][t]-1LL*q*images[rank][t]);}piv.push_back(row);rank++;}
 cout<<n<<" "<<k<<" "<<rank<<" "<<(k-rank)<<" ";for(auto x:piv)cout<<x<<",";cout<<endl;
 }
}
