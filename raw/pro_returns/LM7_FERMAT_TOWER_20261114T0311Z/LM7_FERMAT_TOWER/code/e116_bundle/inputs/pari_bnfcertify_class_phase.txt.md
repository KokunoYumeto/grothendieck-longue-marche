bnfcertify0(GEN bnf, long flag)
{
  pari_sp av = avma;
  long N;
  GEN nf, cyc, B, U;
  ulong bound, p;
  struct check_pr S;
  forprime_t T;

  bnf = checkbnf(bnf);
  nf = bnf_get_nf(bnf);
  N = nf_get_degree(nf); if (N==1) return 1;
  B = zimmertbound(nf_get_disc(nf), N, nf_get_r2(nf));
  if (is_bigint(B))
    pari_warn(warner,"Zimmert's bound is large (%Ps), certification will take a long time", B);
  if (!is_pm1(nf_get_index(nf)))
  {
    GEN D = nf_get_diff(nf), L;
    if (DEBUGLEVEL>1) err_printf("**** Testing Different = %Ps\n",D);
    L = bnfisprincipal0(bnf, D, nf_FORCE);
    if (DEBUGLEVEL>1) err_printf("     is %Ps\n", L);
  }
  if (DEBUGLEVEL)
  {
    err_printf("PHASE 1 [CLASS GROUP]: are all primes good ?\n");
    err_printf("  Testing primes <= %Ps\n", B);
  }
  bnftestprimes(bnf, B);
  if (flag) return 1;

  U = bnf_build_units(bnf);
  cyc = bnf_get_cyc(bnf);
  S.w = bnf_get_tuN(bnf);
  S.mu = gel(U,1);
  S.fu = vecslice(U,2,lg(U)-1);
  S.cyc = cyc;
  S.cycgen = bnf_build_cycgen(bnf);
  init_bad(&S, nf, bnf_get_gen(bnf));

  B = bound_unit_index(bnf, S.fu);
  if (DEBUGLEVEL)
  {
    err_printf("PHASE 2 [UNITS/RELATIONS]: are all primes good ?\n");
    err_printf("  Testing primes <= %Ps\n", B);
