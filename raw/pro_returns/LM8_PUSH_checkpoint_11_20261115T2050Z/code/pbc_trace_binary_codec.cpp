// Exact reversible storage codec for proof JSONL, version 1.
// This is a serialization transform, not a proof simplification.
// Unrecognized/noncanonical records are retained verbatim.
#include <gmpxx.h>
#include <charconv>
#include <cstdint>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>
using Z=mpz_class;
static uint64_t previous=0;
static Z modulus;
static void putu(uint64_t x){while(x>=128){std::cout.put(char((x&127)|128));x>>=7;}std::cout.put(char(x));}
static uint64_t getu(){uint64_t x=0;int shift=0;for(;;){int c=std::cin.get();if(c<0||shift>63)throw std::runtime_error("bad varint");x|=uint64_t(c&127)<<shift;if(!(c&128))return x;shift+=7;}}
static void putz(const Z& x){if(x<0)throw std::runtime_error("negative magnitude");size_t n=0;std::vector<unsigned char>b((mpz_sizeinbase(x.get_mpz_t(),2)+7)/8);mpz_export(b.data(),&n,-1,1,0,0,x.get_mpz_t());putu(n);if(n)std::cout.write((char*)b.data(),n);}
static Z getz(){uint64_t n=getu();if(n>1000000000)throw std::runtime_error("bigint length");std::vector<unsigned char>b(n);if(n&&!std::cin.read((char*)b.data(),n))throw std::runtime_error("truncated bigint");Z x;mpz_import(x.get_mpz_t(),n,-1,1,0,0,b.data());return x;}
static bool uintpart(const std::string&s,size_t&a,uint64_t&n,char end){size_t b=a;while(a<s.size()&&s[a]>='0'&&s[a]<='9')++a;if(a==b||a>=s.size()||s[a]!=end||(a-b>1&&s[b]=='0'))return false;auto r=std::from_chars(s.data()+b,s.data()+a,n);if(r.ec!=std::errc())return false;++a;return true;}
static bool zpart(const std::string&s,size_t&a,Z&n,char end){size_t b=a;if(a<s.size()&&s[a]=='-')++a;size_t d=a;while(a<s.size()&&s[a]>='0'&&s[a]<='9')++a;if(a==d||a>=s.size()||s[a]!=end||(a-d>1&&s[d]=='0'))return false;std::string t=s.substr(b,a-b);if(mpz_set_str(n.get_mpz_t(),t.c_str(),10)||n.get_str()!=t)return false;++a;return true;}
static void update_raw(const std::string&s){if(s.rfind("[\"leaf\",",0)==0){size_t a=8;uint64_t n;if(uintpart(s,a,n,','))previous=n;}}
static void putq(const Z&q){Z best=abs(q);int kbest=0;bool neg=q<0;for(int k:{1,-1}){Z d=q-k*modulus;Z v=abs(d);if(v<best){best=v;kbest=k;neg=d<0;}}std::cout.put(char((kbest+1)*2+int(neg)));putz(best);}
static Z getq(){int c=std::cin.get();if(c<0||c>5)throw std::runtime_error("bad coefficient tag");Z v=getz();if(c&1)v=-v;return Z(c/2-1)*modulus+v;}
static void encode(){std::cout.write("PBCBIN01",8);putz(modulus);std::string s;uint64_t rows=0,packed=0;while(std::getline(std::cin,s)){if(!std::cin.eof())s.push_back('\n');int op=0;size_t a=0;uint64_t id=0,x=0,y=0;Z q;bool ok=false;
 if(s.rfind("[\"sub\",",0)==0){op=1;a=7;ok=uintpart(s,a,id,',')&&uintpart(s,a,x,',')&&zpart(s,a,q,',')&&uintpart(s,a,y,']');}
 else if(s.rfind("[\"mul\",",0)==0){op=2;a=7;ok=uintpart(s,a,id,',')&&zpart(s,a,q,',')&&uintpart(s,a,x,']');}
 else if(s.rfind("[\"neg\",",0)==0){op=3;a=7;ok=uintpart(s,a,id,',')&&uintpart(s,a,x,']');}
 ok=ok&&a+1==s.size()&&s[a]=='\n'&&id>=previous&&x<id&&(op!=1||y<id);
 if(ok){std::cout.put(char(op));putu(id-previous);putu(id-x);if(op==1)putu(y);if(op!=3)putq(q);previous=id;++packed;}
 else{std::cout.put(0);putu(s.size());std::cout.write(s.data(),s.size());update_raw(s);}
 ++rows;if(!std::cout)throw std::runtime_error("output failure");}
 std::cerr<<"encoded records="<<rows<<" packed="<<packed<<" last_node="<<previous<<"\n";
}
static void decode(){char magic[8];if(!std::cin.read(magic,8)||std::string(magic,8)!="PBCBIN01")throw std::runtime_error("bad magic");modulus=getz();uint64_t rows=0,packed=0;for(;;){int op=std::cin.get();if(op<0)break;if(op==0){auto n=getu();if(n>1000000000)throw std::runtime_error("raw length");std::string s(n,'\0');if(n&&!std::cin.read(s.data(),n))throw std::runtime_error("truncated raw");std::cout.write(s.data(),n);update_raw(s);}else{if(op>3)throw std::runtime_error("bad opcode");uint64_t delta=getu();if(delta>std::numeric_limits<uint64_t>::max()-previous)throw std::runtime_error("id overflow");uint64_t id=previous+delta,d=getu();if(d>id)throw std::runtime_error("reference underflow");uint64_t x=id-d,y=op==1?getu():0;Z q;if(op!=3)q=getq();if(op==1)std::cout<<"[\"sub\","<<id<<','<<x<<','<<q<<','<<y<<"]\n";else if(op==2)std::cout<<"[\"mul\","<<id<<','<<q<<','<<x<<"]\n";else std::cout<<"[\"neg\","<<id<<','<<x<<"]\n";previous=id;++packed;}++rows;if(!std::cout)throw std::runtime_error("output failure");}
 std::cerr<<"decoded records="<<rows<<" packed="<<packed<<" last_node="<<previous<<"\n";
}
int main(int argc,char**argv){try{std::ios::sync_with_stdio(false);std::cin.tie(nullptr);if(argc<2)throw std::runtime_error("usage: codec encode MODULUS | decode");if(std::string(argv[1])=="encode"){if(argc!=3||mpz_set_str(modulus.get_mpz_t(),argv[2],10)||modulus<0)throw std::runtime_error("bad modulus");encode();}else if(std::string(argv[1])=="decode")decode();else throw std::runtime_error("unknown mode");std::cout.flush();if(!std::cout)throw std::runtime_error("flush failure");}catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 1;}return 0;}
