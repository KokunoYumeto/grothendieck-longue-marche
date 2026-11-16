\\ Exact Tate-algorithm data for all Q_2 quadratic twists of y^2=x^3-x.
\\ Run: work/pari-2.19.1/gp -q deliverable/code/a_main_exceptional_twists.gp
\\ The eight representatives are a complete Q_2^*/Q_2^{*2} transversal.
print("d,c4,discriminant,minimal_discriminant_valuation,local_conductor_exponent,kodaira_code,tamagawa,global_conductor");
for(i=1,8, d=[1,-1,2,-2,5,-5,10,-10][i]; E=ellinit([0,0,0,-d^2,0]); R=elllocalred(E,2); G=ellglobalred(E); if(R[1] != if(d%2,5,6),error("unexpected conductor")); if(R[2] != if(d%2,3,-6),error("unexpected Kodaira symbol")); if(E.c4 != 48*d^2 || E.disc != 64*d^6,error("invariant identity failed")); if(R[3][1] != 1,error("unexpected minimal-model scaling")); md=valuation(E.disc,2)-12*valuation(R[3][1],2); if(md != if(d%2,6,12),error("unexpected minimal discriminant")); print(d,",",E.c4,",",E.disc,",",md,",",R[1],",",R[2],",",R[4],",",G[1]));
print("All eight exact local reductions passed; odd d: III, f_2=5; even d: I_2^*, f_2=6.");
quit;
