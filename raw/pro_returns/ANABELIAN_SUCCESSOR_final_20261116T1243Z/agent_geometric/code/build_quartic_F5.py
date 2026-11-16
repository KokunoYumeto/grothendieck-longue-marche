"""Produce the F5 specialization of the audited cubic-complement engine.

This file records every mechanical change.  The three transverse slices are
proved in AG.25; this is not a sample of the full normalized coefficient space.
"""
from pathlib import Path

P=Path(__file__).parent
s=(P/'plane_quartic_F3.cpp').read_text()
s=s.replace('F3','F5').replace('over F3','over F5')
s=s.replace('mod3','modp').replace('rank3','rankp').replace('kernel3','kernelp')
s=s.replace('resultant3','resultantp').replace('pow3scalar','powpscalar')
s=s.replace('int modp(int x){x%=3;return x<0?x+3:x;}',
            'constexpr int BASE=5;\nint modp(int x){x%=BASE;return x<0?x+BASE:x;}\nint invp(int x){static const int a[5]={0,1,3,2,4};return a[x];}')
s=s.replace('[27][27]','[125][125]').replace('iv[27]','iv[125]').replace('ng[27]','ng[125]')
s=s.replace('q*=3','q*=BASE').replace('aa%3','aa%BASE').replace('bb%3','bb%BASE')
s=s.replace('aa/=3','aa/=BASE').replace('bb/=3','bb/=BASE').replace(')%3',')%BASE')
s=s.replace('p*=3','p*=BASE').replace('F.power(x,3)','F.power(x,BASE)')
s=s.replace('fields.emplace_back(2,vector<int>{1,0});fields.emplace_back(3,vector<int>{1,2,0});',
            'fields.emplace_back(2,vector<int>{2,0});fields.emplace_back(3,vector<int>{1,1,0});')
s=s.replace('13+39+248','31+310+5240')
start=s.index('vector<int> variable_indices;')
end=s.index('int rankp(',start)
s=s[:start]+r'''struct Slice{int weight,offset,size;vector<int>variables;int fixed;};
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
''' +s[end:]
s=s.replace('int u=a[r][j];for(int t=j;t<n;t++)','int u=invp(a[r][j]);for(int t=j;t<n;t++)')
s=s.replace('mons[4][i][j]%3','mons[4][i][j]%BASE')
s=s.replace('r[j]=v[j]%3;v[j]/=3','r[j]=v[j]%BASE;v[j]/=BASE')
s=s.replace('a1=N1-4;int s1=-a1,s2=10-N2,s3=28-N3;',
            'a1=N1-6;int s1=-a1,s2=26-N2,s3=126-N3;')
s=s.replace('h=28+10*a1+4*a2+a3','h=126+26*a1+6*a2+a3')
s=s.replace('need((-s3-a1*s2-a2*s1)%BASE==0','need((-s3-a1*s2-a2*s1)%3==0')
s=s.replace('==h+3*N1','==h+BASE*N1').replace('specialcounts[j]==4','specialcounts[j]==BASE+1')
s=s.replace('a.back()*b.back()','a.back()*invp(b.back())')
s=s.replace('b=b*a%3;a=a*a%3','b=b*a%BASE;a=a*a%BASE')
s=s.replace('resultantp(b,r)%3','resultantp(b,r)%BASE')
s=s.replace('if(ell!=2&&ell!=3)','if(ell!=2&&ell!=BASE)')
s=s.replace('3*C.a2,9*C.a1,27','BASE*C.a2,BASE*BASE*C.a1,BASE*BASE*BASE')
s=s.replace('+=3*S1[i]','+=BASE*S1[i]').replace('S4[kap]=9','S4[kap]=BASE*BASE')
s=s.replace('relative_class_number_mod3','relative_class_number_mod5').replace('mod3_gcd_degree','mod5_gcd_degree')
s=s.replace('relative_class_number_modp','relative_class_number_mod5').replace('modp_gcd_degree','mod5_gcd_degree')
s=s.replace('mod3 resultant','mod5 resultant').replace('mod3','mod5')
s=s.replace('csv<<C.code<<",3,"','csv<<C.code<<",5,"')
s=s.replace('\\\"N3\\\":','\\\"N5\\\":').replace('\\\"N9\\\":','\\\"N25\\\":').replace('\\\"N27\\\":','\\\"N125\\\":')
start=s.index('  init();init_actions();')
end=s.index('  ofstream census(',start)
s=s[:start]+r'''  init();init_slices();vector<bool>seen(484375);vector<pair<int,int>>reps;long long weighted=0;
  for(int code=0;code<484375;code++)if(!seen[code]){
   const auto&S=get_slice(code);auto f=decode(code);set<int>orbit;
   for(int A=1;A<BASE;A++){int out=S.offset,power=1;for(int i:S.variables){int exponent=mons[4][i][0]+S.weight*mons[4][i][1]-S.weight;need(exponent>=0,"diagonal exponent");int factor=fields[0].power(A,exponent);out+=modp(f[i]*factor)*power;power*=BASE;}seen[out]=true;orbit.insert(out);}
   need(*orbit.begin()==code,"slice orbit minimum");if(smooth(f)){int size=500*orbit.size();reps.push_back({code,size});weighted+=size;}
  }
  cerr<<"Normalized forms244140625, slice forms484375, smooth pointed orbits "<<reps.size()<<", smooth normalized forms "<<weighted<<'\n';
''' +s[end:]
s=s.replace('least5','least3').replace('prime==5','prime==3')
s=s.replace('\\\"field\\\":3','\\\"field\\\":5').replace('\\\"normalized_forms\\\":531441','\\\"normalized_forms\\\":244140625,\\\"slice_forms\\\":484375')
s=s.replace('proved_global_least_prime_5','proved_global_least_prime_3')
s=s.replace('F5_trial','F5_trial')
(P/'plane_quartic_F5.cpp').write_text(s)
print('Wrote plane_quartic_F5.cpp; variables8,7,6; residual diagonal group order4.')
