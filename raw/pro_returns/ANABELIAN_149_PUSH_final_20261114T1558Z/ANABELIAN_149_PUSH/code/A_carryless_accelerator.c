/* Exact binary-polynomial multiplication, using the PCLMULQDQ instruction.
 * Inputs and output are little-endian arrays of 64-bit polynomial blocks.
 * The caller allocates na+nb output blocks. There are no carries: overlapping
 * block products are accumulated by XOR. No field reduction occurs here.
 */
#include <stddef.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <wmmintrin.h>

void a_clmul(const uint64_t *a, size_t na, const uint64_t *b, size_t nb,
             uint64_t *out) {
    for (size_t k=0; k<na+nb; ++k) out[k]=0;
    for (size_t i=0; i<na; ++i) {
        if (!a[i]) continue;
        const __m128i x=_mm_set_epi64x(0,(long long)a[i]);
        for (size_t j=0; j<nb; ++j) {
            if (!b[j]) continue;
            const __m128i y=_mm_set_epi64x(0,(long long)b[j]);
            const __m128i p=_mm_clmulepi64_si128(x,y,0x00);
            out[i+j]^=(uint64_t)_mm_cvtsi128_si64(p);
            out[i+j+1]^=(uint64_t)_mm_cvtsi128_si64(_mm_srli_si128(p,8));
        }
    }
}

static unsigned gf_mul(unsigned a,unsigned b,unsigned e,unsigned mod) {
    unsigned r=0;
    while(b) {
        if(b&1)r^=a;
        a<<=1;if(a&(1u<<e))a^=mod;b>>=1;
    }
    return r;
}

/* Plane i contains the binary polynomial multiplying the field basis w^i. */
int a_gf_mul(unsigned e,unsigned mod,const uint64_t *a,size_t na,
             const uint64_t *b,size_t nb,uint64_t *out) {
    size_t nc=na+nb;
    uint64_t *raw=calloc((2*e-1)*nc,sizeof(uint64_t));
    uint64_t *tmp=calloc(nc,sizeof(uint64_t));
    if(!raw||!tmp){free(raw);free(tmp);return -1;}
    for(unsigned i=0;i<e;++i)for(unsigned j=0;j<e;++j){
        a_clmul(a+i*na,na,b+j*nb,nb,tmp);
        for(size_t k=0;k<nc;++k)raw[(i+j)*nc+k]^=tmp[k];
    }
    for(int i=(int)(2*e-2);i>=(int)e;--i)
        for(unsigned j=0;j<e;++j)if((mod>>j)&1)
            for(size_t k=0;k<nc;++k)raw[(i-e+j)*nc+k]^=raw[i*nc+k];
    memcpy(out,raw,e*nc*sizeof(uint64_t));free(raw);free(tmp);return 0;
}

/* Exact leading-term polynomial division over F_(2^e). Both output arrays
 * have e planes of na blocks. The precomputed multiples are exact scalar
 * multiples of the entire divisor; each loop cancels its current leading
 * term. Quotient and remainder are returned, without presuming exactness.
 */
int a_gf_div(unsigned e,unsigned mod,const uint64_t *a,size_t na,long da,
             const uint64_t *b,size_t nb,long db,uint64_t *quot,uint64_t *rem) {
    unsigned q=1u<<e,lc=0,inv=1;
    for(unsigned i=0;i<e;++i)lc|=((b[i*nb+db/64]>>(db%64))&1)<<i;
    if(!lc)return -2;
    for(unsigned n=0;n<q-2;++n)inv=gf_mul(inv,lc,e,mod);
    uint64_t *multiple=calloc(q*e*nb,sizeof(uint64_t));
    if(!multiple)return -1;
    for(unsigned c=1;c<q;++c)for(unsigned i=0;i<e;++i){
        unsigned s=gf_mul(c,1u<<i,e,mod);
        for(unsigned j=0;j<e;++j)if((s>>j)&1)
            for(size_t k=0;k<nb;++k)multiple[(c*e+j)*nb+k]^=b[i*nb+k];
    }
    memset(quot,0,e*na*sizeof(uint64_t));memcpy(rem,a,e*na*sizeof(uint64_t));
    for(long d=da;d>=db;--d){
        unsigned lead=0;
        for(unsigned i=0;i<e;++i)lead|=((rem[i*na+d/64]>>(d%64))&1)<<i;
        if(!lead)continue;
        unsigned c=gf_mul(lead,inv,e,mod);long shift=d-db;
        size_t word=(size_t)shift/64;unsigned bit=(unsigned)shift%64;
        for(unsigned i=0;i<e;++i){
            if((c>>i)&1)quot[i*na+word]^=UINT64_C(1)<<bit;
            for(size_t k=0;k<nb;++k){
                uint64_t v=multiple[(c*e+i)*nb+k];
                if(word+k<na)rem[i*na+word+k]^=v<<bit;
                if(bit&&word+k+1<na)rem[i*na+word+k+1]^=v>>(64-bit);
            }
        }
    }
    free(multiple);return 0;
}
