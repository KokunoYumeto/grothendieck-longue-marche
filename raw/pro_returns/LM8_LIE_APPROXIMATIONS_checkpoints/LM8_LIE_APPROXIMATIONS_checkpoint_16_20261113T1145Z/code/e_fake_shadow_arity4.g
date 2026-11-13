a:=PermList([2, 6, 1, 12, 15, 17, 20, 22, 3, 21, 26, 29, 4, 32, 19, 5, 34, 35, 36, 38, 7, 39, 8, 37, 9, 10, 14, 11, 46, 13, 45, 42, 16, 49, 30, 18, 50, 52, 28, 53, 23, 24, 25, 27, 54, 51, 31, 33, 44, 43, 40, 47, 48, 41]);;
b:=PermList([4, 7, 10, 14, 1, 18, 17, 2, 5, 27, 3, 20, 31, 29, 21, 23, 11, 9, 6, 35, 12, 36, 15, 8, 41, 13, 45, 16, 34, 44, 48, 38, 42, 30, 26, 28, 19, 49, 25, 22, 24, 51, 33, 53, 32, 52, 50, 54, 47, 39, 37, 40, 43, 46]);;
x:=a^2;;y:=b^2;;z:=b*x/b;;
BlockPerm:=function(ps,d) local v,k,j; v:=[]; for k in [1..Length(ps)] do for j in [1..d] do Add(v,(k-1)*d+j^ps[k]); od; od; return PermList(v); end;;
pairs:=[[1,2],[2,3],[1,3],[1,4],[2,4],[3,4]];;
pgs:=[];;
for pair in pairs do
 blocks:=[];;
 for del in [1..4] do
  if del in pair then Add(blocks,());
  else
   pp:=[];;for ii in pair do if ii>del then Add(pp,ii-1);else Add(pp,ii);fi;od;
   if pp=[1,2] then Add(blocks,x); elif pp=[2,3] then Add(blocks,y); else Assert(0,pp=[1,3]);Add(blocks,z);fi;
  fi;
 od;
 Add(pgs,BlockPerm(blocks,54));
od;
p4:=Group(pgs);;Print("PB4_QUOTIENT_ORDER ",Size(p4),"\n");
g12:=pgs[1];;g23:=pgs[2];;g13:=pgs[3];;g14:=pgs[4];;g24:=pgs[5];;g34:=pgs[6];;
fx:=[g12,g13*g23,g12*g13,g12,g23];;fy:=[g23,g34,g24*g34,g23*g24,g34];;fz:=[g13,g14*g24,g14,g13*g14,g24];;
p3:=Group(BlockPerm(fx,216),BlockPerm(fy,216),BlockPerm(fz,216));;Assert(0,Size(p3)=2187);
Print("INDUCED_PB3_QUOTIENT_ORDER ",Size(p3),"\n");
ff:=List([1..5],j->fx[j]*fy[j]/fx[j]/fy[j]);;Assert(0,ff[5]*ff[3]*ff[1]=ff[4]*ff[2]);Print("PENTAGON_VERIFIED true\n");
QUIT_GAP(0);
