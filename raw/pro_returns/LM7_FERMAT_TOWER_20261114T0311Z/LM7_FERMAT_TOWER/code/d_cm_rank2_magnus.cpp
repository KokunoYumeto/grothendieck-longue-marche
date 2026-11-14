// Exact truncated mod-two Magnus path evaluation, two generators, degree9.
// Word coordinates are little-endian: appending generator i places bit i
// in the next position.  This makes right multiplication by a generator
// an exact shift/copy, with no floating-point operations.
#include <array>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>

struct Poly {
    std::array<std::array<uint64_t,8>,10> v{};
    Poly(){v[0][0]=1;}
    void letter(int a){
        int i=(a<0?-a:a)-1;
        for(int step=1;step<=9;++step){
            int d=a>0?10-step:step;
            if(d<=6) v[d][0]^=v[d-1][0]<<(i*(1<<(d-1)));
            else {
                int nw=1<<(d-7),off=i*nw;
                for(int j=0;j<nw;++j)v[d][off+j]^=v[d-1][j];
            }
        }
    }
    void print() const {
        for(int d=1;d<=9;++d){
            int nw=d<=6?1:1<<(d-6);
            std::cout<<std::hex<<v[d][nw-1];
            for(int j=nw-2;j>=0;--j)
                std::cout<<std::setfill('0')<<std::setw(16)<<v[d][j];
            std::cout<<std::dec<<(d==9?'\n':' ');
        }
    }
};
int main(int argc,char** argv){
    if(argc!=3)return 2;
    std::ifstream cfg(argv[1]);
    std::ifstream in(argv[2],std::ios::binary);
    if(!cfg||!in)return 3;
    std::vector<unsigned char> word((std::istreambuf_iterator<char>(in)),{});
    for(int graph=0;graph<2;++graph){
        std::array<int,6> rs,rr,rr2,ch;
        for(auto& x:rs)cfg>>x;
        for(auto& x:rr)cfg>>x;
        for(auto& x:ch)cfg>>x;
        for(int j=0;j<6;++j)rr2[j]=rr[rr[j]];
        for(int start=0;start<6;++start){
            int q=start;uint64_t letters=0;Poly p;
            for(auto a:word){
                if(a==0)q=rs[q];
                else {
                    int h=(a==1?rr[q]:rr2[q]);
                    if(ch[q]){p.letter(ch[q]);++letters;}
                    if(ch[h]){p.letter(-ch[h]);++letters;}
                    q=h;
                }
            }
            std::cout<<graph<<' '<<start<<' '<<q<<' '<<letters<<' ';
            p.print();
        }
    }
}
