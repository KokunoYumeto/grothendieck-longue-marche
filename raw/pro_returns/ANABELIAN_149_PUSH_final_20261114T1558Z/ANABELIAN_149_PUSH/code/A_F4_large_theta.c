/* Exact small-genus divisor arithmetic over binary finite fields.
 * Polynomial formula: Y^2+hY=f, h=X^2+X+alpha,
 * f=h*(X^3+X^2+X+alpha^2).  Divisors are reduced Mumford pairs.
 * Composition uses two polynomial extended gcds and exact norm reduction;
 * every claimed division is checked. No floating-point arithmetic occurs.
 */
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

typedef struct {uint32_t d,u[3],v[2];} Div;
typedef struct {int d;uint32_t c[16];} Poly;
static uint32_t Q,MOD,ALPHA,*LG=NULL,*EX=NULL,*AS=NULL;
static unsigned E;
static int ERR;
static Poly H,F;

static uint32_t rawmul(uint32_t a,uint32_t b){uint32_t r=0;while(b){if(b&1)r^=a;a<<=1;if(a&Q)a^=MOD;b>>=1;}return r;}
static uint32_t fm(uint32_t a,uint32_t b){return a&&b?EX[LG[a]+LG[b]]:0;}
static uint32_t fi(uint32_t a){if(!a){ERR=1;return 0;}return EX[Q-1-LG[a]];}
static uint32_t fp(uint32_t a,uint64_t n){if(!a)return n?0:1;return EX[((uint64_t)LG[a]*(n%(Q-1)))%(Q-1)];}
static Poly zero(void){Poly a;memset(&a,0,sizeof(a));a.d=-1;return a;}
static Poly one(void){Poly a=zero();a.d=0;a.c[0]=1;return a;}
static void trim(Poly *a){while(a->d>=0&&!a->c[a->d])--a->d;}
static Poly pa(Poly a,Poly b){if(b.d>a.d)a.d=b.d;for(int i=0;i<=b.d;++i)a.c[i]^=b.c[i];trim(&a);return a;}
static Poly ps(Poly a,uint32_t c){for(int i=0;i<=a.d;++i)a.c[i]=fm(a.c[i],c);trim(&a);return a;}
static Poly pm(Poly a,Poly b){Poly c=zero();if(a.d<0||b.d<0)return c;c.d=a.d+b.d;if(c.d>=16){ERR=2;return zero();}for(int i=0;i<=a.d;++i)for(int j=0;j<=b.d;++j)c.c[i+j]^=fm(a.c[i],b.c[j]);trim(&c);return c;}
static void pd(Poly a,Poly b,Poly *quot,Poly *rem){
    *quot=zero();if(b.d<0){ERR=3;*rem=a;return;}uint32_t inv=fi(b.c[b.d]);
    if(a.d>=b.d)quot->d=a.d-b.d;
    while(a.d>=b.d){int k=a.d-b.d;uint32_t c=fm(a.c[a.d],inv);quot->c[k]^=c;for(int j=0;j<=b.d;++j)a.c[k+j]^=fm(c,b.c[j]);trim(&a);}
    trim(quot);*rem=a;
}
static Poly remp(Poly a,Poly b){Poly q,r;pd(a,b,&q,&r);return r;}
static Poly exact(Poly a,Poly b){Poly q,r;pd(a,b,&q,&r);if(r.d>=0)ERR=4;return q;}
static void xgcd(Poly a,Poly b,Poly *d,Poly *s,Poly *t){
    Poly s0=one(),s1=zero(),t0=zero(),t1=one();
    while(b.d>=0){Poly q,r;pd(a,b,&q,&r);a=b;b=r;r=pa(s0,pm(q,s1));s0=s1;s1=r;r=pa(t0,pm(q,t1));t0=t1;t1=r;}
    if(a.d<0){ERR=5;*d=*s=*t=zero();return;}uint32_t inv=fi(a.c[a.d]);*d=ps(a,inv);*s=ps(s0,inv);*t=ps(t0,inv);
}
static Poly pu(const Div *a){Poly r=zero();r.d=(int)a->d;for(unsigned i=0;i<=a->d;++i)r.c[i]=a->u[i];return r;}
static Poly pv(const Div *a){Poly r=zero();r.d=(int)a->d-1;for(unsigned i=0;i<a->d;++i)r.c[i]=a->v[i];trim(&r);return r;}
static Div identity(void){Div r;memset(&r,0,sizeof(r));r.u[0]=1;return r;}
static Div pack(Poly u,Poly v){Div r=identity();if(u.d<0||u.d>2||v.d>=u.d){ERR=6;return r;}r.d=(uint32_t)u.d;memset(r.u,0,sizeof(r.u));for(int i=0;i<=u.d;++i)r.u[i]=u.c[i];for(int i=0;i<=v.d;++i)r.v[i]=v.c[i];return r;}
static Div reduce(Poly u,Poly v){
    if(u.d<0){ERR=7;return identity();}u=ps(u,fi(u.c[u.d]));v=remp(v,u);
    while(u.d>2){Poly newu=exact(pa(pa(pm(v,v),pm(H,v)),F),u);if(newu.d<0){ERR=8;return identity();}newu=ps(newu,fi(newu.c[newu.d]));v=remp(pa(v,H),newu);u=newu;}
    if(u.d==0)v=zero();return pack(u,v);
}
static Div add(const Div *L,const Div *R){
    Poly u1=pu(L),v1=pv(L),u2=pu(R),v2=pv(R),d1,a,b,d,e,c;
    xgcd(u1,u2,&d1,&a,&b);xgcd(d1,pa(pa(v1,v2),H),&d,&e,&c);a=pm(e,a);b=pm(e,b);
    Poly u=exact(pm(u1,u2),pm(d,d));
    Poly num=pa(pa(pm(pm(a,u1),v2),pm(pm(b,u2),v1)),pm(c,pa(pm(v1,v2),F)));
    return reduce(u,exact(num,d));
}
static Div neg(const Div *a){return pack(pu(a),remp(pa(pv(a),H),pu(a)));}
static Div times(const Div *a,uint64_t n){Div r=identity(),b=*a;while(n){if(n&1)r=add(&r,&b);n>>=1;if(n)b=add(&b,&b);}return r;}
static uint32_t pe(Poly a,uint32_t x){uint32_t r=0;for(int i=a.d;i>=0;--i)r=fm(r,x)^a.c[i];return r;}

int a_init(unsigned e,unsigned modulus){
    free(LG);free(EX);free(AS);E=e;Q=1u<<e;MOD=modulus;ERR=0;
    LG=malloc(Q*sizeof(uint32_t));EX=malloc(2*Q*sizeof(uint32_t));AS=malloc(Q*sizeof(uint32_t));
    if(!LG||!EX||!AS)return -1;
    unsigned gen;
    for(gen=2;gen<Q;++gen){
        memset(LG,255,Q*sizeof(uint32_t));uint32_t x=1,i;
        for(i=0;i<Q-1;++i){if(LG[x]!=UINT32_MAX)break;LG[x]=i;EX[i]=x;x=rawmul(x,gen);}
        if(i==Q-1&&x==1)break;
    }
    if(gen==Q)return -2;
    for(uint32_t i=Q-1;i<2*Q;++i)EX[i]=EX[i-(Q-1)];
    memset(AS,255,Q*sizeof(uint32_t));for(uint32_t y=0;y<Q;++y){uint32_t a=fm(y,y)^y;if(AS[a]==UINT32_MAX)AS[a]=y;}
    ALPHA=EX[(Q-1)/3];if((fm(ALPHA,ALPHA)^ALPHA)!=1)return -3;
    H=zero();H.d=2;H.c[0]=ALPHA;H.c[1]=H.c[2]=1;
    Poly G=zero();G.d=3;G.c[0]=fm(ALPHA,ALPHA);G.c[1]=G.c[2]=G.c[3]=1;F=pm(H,G);
    return (int)gen;
}
uint32_t a_alpha(void){return ALPHA;}
uint32_t a_field_mul(uint32_t a,uint32_t b){return fm(a,b);}
uint32_t a_field_inv(uint32_t a){return fi(a);}
uint32_t a_field_pow(uint32_t a,uint64_t n){return fp(a,n);}
uint32_t a_asroot(uint32_t a){return AS[a];}
int a_add(const Div *a,const Div *b,Div *out){ERR=0;*out=add(a,b);return ERR;}
int a_neg(const Div *a,Div *out){ERR=0;*out=neg(a);return ERR;}
int a_times(const Div *a,uint64_t n,Div *out){ERR=0;*out=times(a,n);return ERR;}
int a_check(const Div *a){ERR=0;Poly u=pu(a),v=pv(a);if(u.d<0||u.c[u.d]!=1||v.d>=u.d)return -1;Poly r=remp(pa(pa(pm(v,v),pm(H,v)),F),u);return ERR?ERR:r.d+1;}
int a_point_eta(uint32_t x,uint32_t y,Div *out){
    ERR=0;uint32_t h=pe(H,x);if(!h)return -1;uint32_t Y=fm(h,y);
    if((fm(Y,Y)^fm(h,Y))!=pe(F,x))return -2;
    Div P=identity();P.d=1;P.u[0]=x;P.u[1]=1;P.v[0]=Y;
    Div T=pack(H,zero());*out=add(&P,&T);return ERR;
}
int a_curve_point(uint32_t x,uint32_t *y){
    uint32_t h=pe(H,x);if(!h)return -1;
    uint32_t value=fm(pe(F,x),fi(fm(h,h)));uint32_t root=AS[value];
    if(root==UINT32_MAX)return 0;*y=root;return 1;
}
