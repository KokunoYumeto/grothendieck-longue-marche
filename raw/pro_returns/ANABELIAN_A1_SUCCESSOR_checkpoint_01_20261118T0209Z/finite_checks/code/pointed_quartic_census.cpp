// Independent reconstruction of the pointed plane-quartic census.
// Exact orbit enumeration and algebraic-closure smoothness, no databases.
#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <chrono>
using namespace std;
using Form=array<int,15>;
vector<array<int,3>> b4,b7;
int ix4[5][5],ix7[8][8];
int mod(int a,int p){a%=p;return a<0?a+p:a;}
int powm(int a,int n,int p){int b=1;while(n-- >0)b=b*a%p;return b;}
int fac(int n){int a=1;while(n>1)a*=n--;return a;}
int choose(int n,int k){return fac(n)/fac(k)/fac(n-k);}
bool smooth(const Form& f,int p){
 int A[45][36]={};
 for(int h=0;h<3;h++)for(int j=0;j<15;j++)for(int t=0;t<15;t++){
  if(!f[t]||!b4[t][h])continue;
  auto e=b4[t];e[h]--;
  int col=ix7[e[0]+b4[j][0]][e[1]+b4[j][1]];
  A[15*h+j][col]=f[t]*b4[t][h]%p;
 }
 int r=0;
 for(int col=0;col<36;col++){
  int h=r;while(h<45&&!A[h][col])h++;
  if(h==45)return false;
  for(int j=col;j<36;j++)swap(A[h][j],A[r][j]);
  int v=powm(A[r][col],p-2,p);
  for(int j=col;j<36;j++)A[r][j]=A[r][j]*v%p;
  for(int i=r+1;i<45;i++)if(A[i][col]){
   int v=A[i][col];A[i][col]=0;
   for(int j=col+1;j<36;j++)A[i][j]=mod(A[i][j]-v*A[r][j],p);
  }
  r++;
 }
 return r==36;
}
int eval(const Form& f,array<int,3> a,int p){int z=0;for(int i=0;i<15;i++){
 int v=f[i];for(int j=0;j<3;j++)v=v*powm(a[j],b4[i][j],p)%p;z+=v;}return z%p;}
int points(const Form& f,int p){int n=0;for(int a=0;a<p;a++)for(int b=0;b<p;b++)n+=eval(f,{a,b,1},p)==0;
 for(int a=0;a<p;a++)n+=eval(f,{a,1,0},p)==0;n+=eval(f,{1,0,0},p)==0;return n;}
void writeform(ofstream& o,int typ,int code,int orbit,const Form& f,int p){
 o<<typ<<','<<code<<','<<orbit<<','<<points(f,p);for(int v:f)o<<','<<v;o<<'\n';}
Form decode(int code,const vector<int>& vars,int p,Form base){for(int j:vars){base[j]=code%p;code/=p;}return base;}
int main(int argc,char**argv){
 string dir=argc>1?argv[1]:".";
 for(int i=0;i<=4;i++)for(int j=0;j<=4-i;j++){ix4[i][j]=b4.size();b4.push_back({i,j,4-i-j});}
 for(int i=0;i<=7;i++)for(int j=0;j<=7-i;j++){ix7[i][j]=b7.size();b7.push_back({i,j,7-i-j});}
 auto start=chrono::steady_clock::now();
 ofstream o3(dir+"/pointed_quartic_F3_census.csv"),o5(dir+"/pointed_quartic_F5_census.csv");
 for(auto*o:{&o3,&o5}){*o<<"contact,slice_code,orbit_size,N1";for(auto e:b4)*o<<",c"<<e[0]<<e[1]<<e[2];*o<<'\n';}
 vector<int> vars3;for(int i=0;i<15;i++)if(i!=0&&i!=1&&i!=5)vars3.push_back(i);
 vector<array<array<int,15>,15>> acts;
 for(int aa=1;aa<3;aa++)for(int cc=1;cc<3;cc++)for(int bb=0;bb<3;bb++)for(int dd=0;dd<3;dd++)for(int ee=0;ee<3;ee++){
  array<array<int,15>,15>M={};
  for(int t=0;t<15;t++){
   int i=b4[t][0],j=b4[t][1],k=b4[t][2];
   for(int u=0;u<=i;u++)for(int v=0;v<=k;v++)for(int w=0;w<=k-v;w++){
    int z=choose(i,u)*powm(aa,u,3)*powm(bb,i-u,3)*powm(cc,j,3)*fac(k)/fac(v)/fac(w)/fac(k-v-w)*powm(dd,v,3)*powm(ee,w,3)*cc;
    int idx=ix4[u+v][i-u+j+w];M[idx][t]=(M[idx][t]+z)%3;
   }
  }
  acts.push_back(M);
 }
 vector<unsigned char> done(531441);long long smooth3=0;int classes3=0,total3=0;
 for(int code=0;code<531441;code++)if(!done[code]){
  Form base={};base[1]=1;Form f=decode(code,vars3,3,base);vector<int>orb;
  for(auto&M:acts){int n=0,pow=1;for(int j:vars3){int c=0;for(int t=0;t<15;t++)c+=M[j][t]*f[t];n+=(c%3)*pow;pow*=3;}done[n]=1;orb.push_back(n);}
  sort(orb.begin(),orb.end());orb.erase(unique(orb.begin(),orb.end()),orb.end());total3++;
  if(smooth(f,3)){classes3++;smooth3+=orb.size();int typ=f[9]?2:(f[12]?3:4);writeform(o3,typ,code,orb.size(),f,3);}
 }
 cout<<"F3 normalized_orbits="<<total3<<" smooth_classes="<<classes3<<" smooth_normalized_forms="<<smooth3<<endl;
 long long smooth5=0;int classes5=0,total5=0;int bycontact[5]={};
 for(int typ=2;typ<=4;typ++){
  Form base={};base[1]=1;vector<int> vars;
  if(typ==2){base[9]=1;vars={3,4,7,8,10,11,13,14};}
  if(typ==3){base[12]=1;vars={3,4,7,8,11,13,14};}
  if(typ==4){base[14]=1;vars={3,4,7,8,10,11};}
  int nmax=1;for(int j:vars)nmax*=5;
  int weights[4][15]={};for(int a=1;a<5;a++)for(int j:vars)weights[a-1][j]=powm(a,mod(b4[j][0]+typ*b4[j][1]-typ,4),5);
  for(int code=0;code<nmax;code++){
   Form f=decode(code,vars,5,base);vector<int> orb;
   for(int a=0;a<4;a++){int c=0,pow=1;for(int j:vars){c+=(f[j]*weights[a][j]%5)*pow;pow*=5;}orb.push_back(c);}
   if(*min_element(orb.begin(),orb.end())!=code)continue;
   total5++;sort(orb.begin(),orb.end());orb.erase(unique(orb.begin(),orb.end()),orb.end());
   if(smooth(f,5)){classes5++;bycontact[typ]++;smooth5+=500*orb.size();writeform(o5,typ,code,orb.size(),f,5);}
  }
  cout<<"F5 contact="<<typ<<" smooth_classes="<<bycontact[typ]<<endl;
 }
 cout<<"F5 slice_orbits="<<total5<<" smooth_classes="<<classes5<<" smooth_normalized_forms="<<smooth5<<endl;
 cout<<"seconds="<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<endl;
 if(classes3!=3001||smooth3!=315360||classes5!=94283||smooth5!=187512000)return 1;
 cout<<"PASS all four supplied census totals reproduced independently"<<endl;
}
