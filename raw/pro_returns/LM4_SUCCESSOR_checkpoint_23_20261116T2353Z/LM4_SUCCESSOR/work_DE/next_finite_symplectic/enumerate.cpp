#include <array>
#include <vector>
#include <unordered_set>
#include <iostream>
#include <fstream>
#include <cassert>
#include <chrono>
using namespace std;
using Mat=array<unsigned short,10>;
struct Hash{size_t operator()(const Mat&m)const{size_t h=1469598103934665603ULL;for(auto x:m){h^=x;h*=1099511628211ULL;}return h;}};
const int Q=59049;
int powers[10],negrow[Q];
int addrow(int a,int b){int r=0;for(int j=0;j<10;j++){r+=((a%3+b%3)%3)*powers[j];a/=3;b/=3;}return r;}
Mat canonical(Mat m){for(int i=0;i<10;i++){int a=m[i];for(int j=0;j<10;j++){int c=a%3;a/=3;if(c){if(c==2)for(auto &x:m)x=negrow[x];return m;}}}assert(false);return m;}
Mat identity(){Mat m{};for(int i=0;i<10;i++)m[i]=powers[i];return m;}
Mat readmat(ifstream&f){Mat m{};for(int i=0;i<10;i++)for(int j=0;j<10;j++){int x;f>>x;m[i]+=x*powers[j];}return canonical(m);}
vector<unsigned short> action(const Mat&m){vector<unsigned short> t(Q);for(int i=1;i<Q;i++){int j=0,r=i;while(r%3==0){r/=3;j++;}int d=r%3;int a=m[j];if(d==2)a=negrow[a];t[i]=addrow(t[i-d*powers[j]],a);}return t;}
Mat right(const Mat&m,const vector<unsigned short>&a){Mat r;for(int i=0;i<10;i++)r[i]=a[m[i]];return canonical(r);}
struct Group{vector<Mat> elements;unordered_set<Mat,Hash> set;};
Group generate(const vector<Mat>&gens,size_t cap=1000000){
 vector<vector<unsigned short>> acts;for(auto&m:gens)acts.push_back(action(m));
 Group g;g.elements.push_back(identity());g.set.insert(identity());
 for(size_t i=0;i<g.elements.size();i++){
  Mat m=g.elements[i];for(auto&a:acts){Mat r=right(m,a);if(g.set.insert(r).second){g.elements.push_back(r);if(g.elements.size()>cap){cerr<<"CAP "<<cap<<" exceeded\n";exit(3);}}}
 }
 return g;
}
int main(){
 powers[0]=1;for(int i=1;i<10;i++)powers[i]=3*powers[i-1];
 for(int i=0;i<Q;i++){int a=i,r=0;for(int j=0;j<10;j++){r+=((2*(a%3))%3)*powers[j];a/=3;}negrow[i]=r;}
 ifstream f("matrices.txt");vector<vector<Mat>> gens(2);
 for(int k=0;k<2;k++){int n;f>>n;for(int i=0;i<n;i++)gens[k].push_back(readmat(f));}
 Mat h=readmat(f),b=readmat(f);
 auto start=chrono::steady_clock::now();
 Group T=generate(gens[0]);cout<<"Exact projective T image order "<<T.elements.size()<<endl;
 Group F=generate(gens[1]);cout<<"Exact projective C5 image order "<<F.elements.size()<<endl;
 for(int k=0;k<2;k++){ofstream out(k==0?"T_matrices.txt":"C5_matrices.txt");for(auto&m:(k==0?T.elements:F.elements)){for(auto x:m)out<<x<<" ";out<<"\n";}}
 vector<Mat> common;for(auto&m:T.elements)if(F.set.count(m))common.push_back(m);
 cout<<"Exact projective subgroup intersection order "<<common.size()<<endl;
 auto order=[](Mat m){auto a=action(m);Mat x=identity();for(int k=1;k<1000000;k++){x=right(x,a);if(x==identity())return k;}return -1;};
 cout<<"h order "<<order(h)<<" b0 order "<<order(b)<<" h in C5 image "<<F.set.count(h)<<" b0 in T image "<<T.set.count(b)<<endl;
 vector<int> hist(1000);for(auto&m:common){int o=order(m);assert(o>=1&&o<1000);hist[o]++;}
 cout<<"Intersection element orders:";for(int i=1;i<1000;i++)if(hist[i])cout<<" "<<i<<":"<<hist[i];cout<<endl;
 ofstream out("intersection_matrices.txt");for(auto&m:common){for(auto x:m)out<<x<<" ";out<<"\n";}
 cout<<"PASS complete finite subgroup enumeration; elapsed "<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<" seconds"<<endl;
}
