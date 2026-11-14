E=ellinit([0,0,0,1,0]);
print("E invariants=",[E.c4,E.c6,E.disc]);
print("local2=",elllocalred(E,2));
print("global=",ellglobalred(E));
quit;
