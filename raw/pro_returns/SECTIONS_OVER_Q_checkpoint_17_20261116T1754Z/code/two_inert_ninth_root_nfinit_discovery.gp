\\ Bounded field initialization only; no class-group or unit completeness.
default(parisizemax,2000000000);
default(parisize,128000000);
default(realprecision,160);
mc=polcompositum(x^9-3*649^6,polcyclo(9),3);
print("COMPOSITUM_DEGREE ",poldegree(mc[1])," TIME ",getwalltime());
mr=polredbest(mc[1],1);
mp=mr[1];mt=subst(lift(mc[2]),x,mr[2]);mz=subst(lift(mc[3]),x,mr[2]);
if(mt^9!=3*649^6 || mz^6+mz^3+1!=0,error("literal maps"));
print("POLYNOMIAL ",mp);
print("T_MAP ",lift(mt));
print("ZETA9_MAP ",lift(mz));
print("START_NFINIT ",getwalltime());
mn=nfinit([mp,[3,11,59]]);
print("ORDER_DISCRIMINANT ",factor(mn.disc));
print("NF_CERTIFY ",nfcertify(mn));
writebin("/tmp/birational_ninth_root_nfinit_cache.bin",[mn,mt,mz]);
print("DONE ",getwalltime());
quit;
