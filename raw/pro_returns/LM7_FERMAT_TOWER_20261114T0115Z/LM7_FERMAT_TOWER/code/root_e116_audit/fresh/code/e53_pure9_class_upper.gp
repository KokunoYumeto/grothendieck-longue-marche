\\ Deliberately certify only the class-group upper presentation, flag1.
\\ This is sufficient for the S-class quotient after verified prime relations.
default(parisize,128000000);
default(parisizemax,1000000000);
{
 my(V=read("e53_pure9_candidate.bin"),B=V[1]);
 print("{\"type\":\"start\",\"operation\":\"bnfcertify flag1 class-quotient bound\"}");
 my(c=bnfcertify(B,1));
 if(c!=1,error("class-quotient certification failed"));
 print("{\"type\":\"certified_class_upper_bound\",\"flag\":1,\"return\":",c,",\"presentation_cyclic\":",B.cyc,",\"meaning\":\"actual class group is a quotient; no unit saturation or exact class order asserted\"}");
 writebin("e53_pure9_class_upper.bin",[B,c]);
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
