# Derived from GAP 4.16.1 / Polycyclic 2.18 colftl.gi.
# Original package copyright/license apply; see generation metadata.
PBC_CentralCollectV2:=function(pcp,ev,w,baseN,centralConj)

    local   ngens,  pow,  exp,  com,  wst,  west,  sst,  est,  bottom,
            stp,  g,  word,  exponent,  i,  h,  m,  u,  j,  cnj,
            icnj,  hh, moveSign, tt;

    if Length( w ) = 0 then return true; fi;


    ngens := pcp![PC_NUMBER_OF_GENERATORS];

    pow := pcp![ PC_POWERS ];
    exp := pcp![ PC_EXPONENTS ];
    com := pcp![ PC_COMMUTE ];

    wst  := [ ];
    west := [ ];
    sst  := [ ];
    est  := [ ];

    bottom    := 0;
    stp       := bottom + 1;
    wst[stp]  := w;
    west[stp] := 1;
    sst[stp]  := 1;
    est[stp]  := w[ 2 ];

    # collect
    while stp > bottom do

        if est[stp] = 0 then
            # initialise est
            sst[stp] := sst[stp] + 1;
            if sst[stp] > Length(wst[stp])/2 then
                west[stp] := west[stp] - 1;
                if west[stp] <= 0 then
                    ## clear stacks before going down
                    wst[  stp ] := 0;
                    west[ stp ] := 0;
                    sst[  stp ] := 0;
                    est[  stp ] := 0;

                    stp := stp - 1;
                else
                    sst[stp] := 1;
                    est[stp] := wst[stp][2];
                fi;
            else
                est[stp] := wst[stp][ 2*sst[stp] ];
            fi;
        else

            # get next generator
            g := wst[stp][ 2*sst[stp]-1 ];

            if stp > 1 and sst[stp] = 1 and g = com[g] and g > baseN then
                ## collect word ^ exponent in one go

                word      := wst[stp];
                exponent  := west[stp];
                ##  Add the word into ev
                for i in [1,3..Length(word)-1] do
                    h     := word[ i ];
                    ev[h] := ev[h] + word[ i+1 ] * exponent;
                od;

                # Every index in this branch is an infinite-order
                # central tail.  There is no exponent to reduce.

                west[ stp ] := 0;
                est[  stp ] := 0;
                sst[  stp ] := Length( word );


            elif g = com[g] then
                # The finite suffix commutes modulo the central tails.
                # Insert its whole current exponent using the central
                # bilinear correction, then keep its base exponent.
                if g<=baseN then
                    for hh in [g+1..baseN] do
                        if ev[hh]<>0 and IsBound(centralConj[hh][g]) then
                            for tt in [1,3..Length(centralConj[hh][g])-1] do
                                ev[centralConj[hh][g][tt]] :=
                                  ev[centralConj[hh][g][tt]] +
                                  est[stp]*ev[hh]*centralConj[hh][g][tt+1];
                            od;
                        fi;
                    od;
                fi;
                # move generator directly to its correct position
                ev[g] := ev[g] + est[stp];
                est[stp] := 0;
            else

                if est[stp] > 0 then
                    est[stp] := est[stp] - 1;moveSign:=1;
                    ev[g] := ev[g] + 1;
                    cnj   := pcp![ PC_CONJUGATES ];
                    icnj  := pcp![ PC_INVERSECONJUGATES ];
                else
                    est[stp] := est[stp] + 1;moveSign:=-1;
                    ev[g] := ev[g] - 1;
                    cnj   := pcp![ PC_CONJUGATESINVERSE ];
                    icnj  := pcp![ PC_INVERSECONJUGATESINVERSE ];
                fi;


                # The deleted conjugates have unchanged finite base
                # generator and only a central correction.  Insert that
                # correction once for every old higher-generator copy.
                if g<=baseN then
                    for hh in [g+1..baseN] do
                        if ev[hh]<>0 and IsBound(centralConj[hh][g]) then
                            for tt in [1,3..Length(centralConj[hh][g])-1] do
                                ev[centralConj[hh][g][tt]] :=
                                  ev[centralConj[hh][g][tt]] +
                                  moveSign*ev[hh]*centralConj[hh][g][tt+1];
                            od;
                        fi;
                    od;
                fi;
                h := com[g];

                # Find first position where we need to collect
                while h > g do
                    if ev[h] <> 0 then
                        if ev[h] > 0 then
                            if IsBound(  cnj[h][g] ) then break; fi;
                        else
                            if IsBound( icnj[h][g] ) then break; fi;
                        fi;
                    fi;
                    h := h-1;
                od;


                # Put that part on the stack, if necessary
                if h > g or
                   ( IsBound(exp[g])
                     and (ev[g] < 0 or ev[g] >= exp[g])
                     and IsBound(pow[g]) ) then

                    for hh in [com[g],com[g]-1..h+1] do
                        if ev[hh] <> 0 then
                            stp := stp+1;
                            if ev[hh] > 0 then
                                wst[stp]  := pcp![ PC_GENERATORS ][hh];
                                west[stp] := ev[hh];
                            else
                                wst[stp]  := pcp![ PC_INVERSES ][hh];
                                west[stp] := -ev[hh];
                            fi;
                            sst[stp] := 1;
                            est[stp] := wst[stp][ 2 ];
                            ev[hh] := 0;
                        fi;
                    od;
                fi;


                # move generator across the exponent vector
                while h > g do
                    if ev[h] <> 0 then
                        stp := stp+1;
                        if ev[h] > 0 then
                            if IsBound( cnj[h][g] ) then
                                wst[stp]  := cnj[h][g];
                                west[stp] := ev[h];
                            else
                                wst[stp]  := pcp![ PC_GENERATORS ][h];
                                west[stp] := ev[h];
                            fi;
                        else
                            if IsBound( icnj[h][g] ) then
                                wst[stp]  := icnj[h][g];
                                west[stp] := -ev[h];
                            else
                                wst[stp]  := pcp![ PC_INVERSES ][h];
                                west[stp] := -ev[h];
                            fi;
                        fi;
                        sst[stp] := 1;
                        est[stp] := wst[stp][ 2 ];
                        ev[h] := 0;
                    fi;
                    h := h-1;
                od;
            fi;

            # reduce exponent if necessary
            if IsBound( exp[g] ) and ev[g] >= exp[g] then
                ev[g] := ev[g] - exp[g];
                if IsBound( pow[g] ) then
                    stp := stp+1;
                    wst[stp]  := pow[g];
                    west[stp] := 1;
                    sst[stp]  := 1;
                    est[stp] := wst[stp][ 2 ];
                fi;
            fi;
        fi;
    od;
    return true;
end;;
