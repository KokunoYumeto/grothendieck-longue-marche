default(parisize,64000000);
run()={
  my(a=read("research_e84/code/e_ramified_class_action.bin"));
  my(b=read("root_e84_audit/code/e_ramified_class_action.bin"));
  if(#a!=11 || #b!=11,error("component count"));
  my(e=vector(11,i,a[i]==b[i]));
  if(vecmin(e)!=1 || a!=b,error("complete object comparison"));
  print("{\"status\":\"PASS\",\"whole_object_equal\":true,\"component_count\":11,\"component_equalities\":",e,"}");
};
run();
quit;
