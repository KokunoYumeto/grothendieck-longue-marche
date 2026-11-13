#include <stdint.h>
#include <stdlib.h>
#include <string.h>

/* Exact reduced row echelon form over F_3, represented by two bit planes.
   Returns rank, or -1 on allocation failure. Input/output is row-major. */
int de_rref3(uint8_t *a, int rows, int cols, int *pivots) {
    int words=(cols+63)/64, rank=0;
    size_t size=(size_t)rows*words;
    uint64_t *lo=calloc(size,sizeof(uint64_t)), *hi=calloc(size,sizeof(uint64_t));
    if (!lo || !hi) { free(lo); free(hi); return -1; }
    for(int i=0;i<rows;i++) for(int j=0;j<cols;j++) {
        uint8_t v=a[(size_t)i*cols+j]%3; uint64_t bit=(uint64_t)1<<(j%64);
        if(v==1) lo[(size_t)i*words+j/64]|=bit;
        if(v==2) hi[(size_t)i*words+j/64]|=bit;
    }
    for(int c=0;c<cols && rank<rows;c++) {
        int word=c/64; uint64_t bit=(uint64_t)1<<(c%64); int p=rank;
        while(p<rows && !((lo[(size_t)p*words+word]|hi[(size_t)p*words+word])&bit))p++;
        if(p==rows)continue;
        for(int w=word;w<words;w++) {
            uint64_t x=lo[(size_t)p*words+w];lo[(size_t)p*words+w]=lo[(size_t)rank*words+w];lo[(size_t)rank*words+w]=x;
            x=hi[(size_t)p*words+w];hi[(size_t)p*words+w]=hi[(size_t)rank*words+w];hi[(size_t)rank*words+w]=x;
        }
        if(hi[(size_t)rank*words+word]&bit)for(int w=word;w<words;w++) {
            uint64_t x=lo[(size_t)rank*words+w];lo[(size_t)rank*words+w]=hi[(size_t)rank*words+w];hi[(size_t)rank*words+w]=x;
        }
        for(int i=0;i<rows;i++)if(i!=rank) {
            int coefficient=(lo[(size_t)i*words+word]&bit)?1:(hi[(size_t)i*words+word]&bit)?2:0;
            if(!coefficient)continue;
            for(int w=word;w<words;w++) {
                uint64_t al=lo[(size_t)i*words+w],ah=hi[(size_t)i*words+w],az=~(al|ah);
                uint64_t pl=lo[(size_t)rank*words+w],ph=hi[(size_t)rank*words+w];
                uint64_t bl=coefficient==1?ph:pl,bh=coefficient==1?pl:ph,bz=~(bl|bh);
                lo[(size_t)i*words+w]=(az&bl)|(al&bz)|(ah&bh);
                hi[(size_t)i*words+w]=(az&bh)|(ah&bz)|(al&bl);
            }
        }
        pivots[rank++]=c;
    }
    for(int i=0;i<rows;i++) for(int j=0;j<cols;j++) {
        uint64_t bit=(uint64_t)1<<(j%64);size_t k=(size_t)i*words+j/64;
        a[(size_t)i*cols+j]=(lo[k]&bit)?1:(hi[k]&bit)?2:0;
    }
    free(lo);free(hi);return rank;
}

/* Exact binary companion, same interface. */
int de_rref2(uint8_t *a, int rows, int cols, int *pivots) {
    int words=(cols+63)/64,rank=0;
    uint64_t *packed=calloc((size_t)rows*words,sizeof(uint64_t));
    if(!packed)return -1;
    for(int i=0;i<rows;i++)for(int j=0;j<cols;j++)
        if(a[(size_t)i*cols+j]&1)packed[(size_t)i*words+j/64]|=(uint64_t)1<<(j%64);
    for(int c=0;c<cols && rank<rows;c++) {
        int word=c/64,p=rank;uint64_t bit=(uint64_t)1<<(c%64);
        while(p<rows && !(packed[(size_t)p*words+word]&bit))p++;
        if(p==rows)continue;
        for(int w=word;w<words;w++) {
            uint64_t x=packed[(size_t)p*words+w];packed[(size_t)p*words+w]=packed[(size_t)rank*words+w];packed[(size_t)rank*words+w]=x;
        }
        for(int i=0;i<rows;i++)if(i!=rank && (packed[(size_t)i*words+word]&bit))
            for(int w=word;w<words;w++)packed[(size_t)i*words+w]^=packed[(size_t)rank*words+w];
        pivots[rank++]=c;
    }
    for(int i=0;i<rows;i++)for(int j=0;j<cols;j++)a[(size_t)i*cols+j]=(packed[(size_t)i*words+j/64]>>(j%64))&1;
    free(packed);return rank;
}
