"""Generate the data-only exact witness reducer with original-row proof DAG."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
source = HERE / "pbc_hermite_cached_witness.g"
s = source.read_text()
s = s.replace(
    "PBC_HermiteWitnessCached:=function(G,s,r,bs,br,cs,cr)",
    "PBC_HermiteDataWitness:=function(data)",
)
s = s.replace(
    "initialExtras,normalizeWeights,depthIndex,inversePowers;",
    "initialExtras,normalizeWeights,cs,cr,traceStream,traceId,"
    "newLeaf,newOp,newNeg,basisproof,targetproof,currentRelation;",
)
start = s.index(" g:=Igs(G);")
end = s.index(" inverse:=function(w)", start)
s = s[:start] + r'''
 orders:=data.orders;n:=Length(orders);m:=n*(n+1)/2;
 cs:=data.cs;cr:=data.cr;
 traceStream:=OutputTextFile(Concatenation(data.trace_stem,".jsonl"),false);
 SetPrintFormattingStatus(traceStream,false);
 PrintTo(traceStream,"[\"source\",\"",data.source_sha256,"\",",n,",",m,"]\n");
 traceId:=0;
 newLeaf:=function(kind,meta,v)
  traceId:=traceId+1;
  PrintTo(traceStream,"[\"leaf\",",traceId,",\"",kind,"\",",meta,",",v,"]\n");
  return traceId;
 end;
 newOp:=function(a,q,b)
  traceId:=traceId+1;
  PrintTo(traceStream,"[\"sub\",",traceId,",",a,",",q,",",b,"]\n");
  return traceId;
 end;
 newNeg:=function(a)
  traceId:=traceId+1;PrintTo(traceStream,"[\"neg\",",traceId,",",a,"]\n");
  return traceId;
 end;
''' + s[end:]
s = s.replace("e:=word(g[i]^orders[i]);", "e:=ShallowCopy(data.powers[i]);")
s = s.replace(
    "e:=word(inversePowers[j][2]*g[i]*g[j]);",
    "e:=ShallowCopy(data.conjugates[i][j]);",
)
s = s.replace(
    "sw:=word(s);rw:=word(r);bsw:=word(bs);brw:=word(br);",
    "sw:=data.s;rw:=data.r;bsw:=data.bs;brw:=data.br;",
)
s = s.replace("for a in cs do e:=word(a);", "for a in cs do e:=a;")
s = s.replace("for a in cr do e:=word(a);", "for a in cr do e:=a;")
s = s.replace(
    "basis:=[];basisweights:=[];pivots:=0;",
    "basis:=[];basisweights:=[];basisproof:=[];pivots:=0;",
)
s = s.replace(
    "found:=false;targetw:=[];",
    'found:=false;targetw:=[];targetproof:=newLeaf("target",[],target);'
    "currentRelation:=[];",
)
s = s.replace("reduce:=function(v,w)", "reduce:=function(v,w,proof)")
s = s.replace(
    "active,ii,idx,row,d,q,ww,out,coef;",
    "active,ii,idx,row,d,q,ww,out,coef,pr;",
)
s = s.replace(
    "active:=[];ww:=ShallowCopy(w);",
    "active:=[];ww:=ShallowCopy(w);pr:=proof;",
)
s = s.replace(
    "ww:=normalizeWeights(PBC_SparseAdd(ww,basisweights[row[1]],-q));",
    "ww:=normalizeWeights(PBC_SparseAdd(ww,basisweights[row[1]],-q));"
    "pr:=newOp(pr,q,basisproof[row[1]]);",
)
s = s.replace("return [out,ww];", "return [out,ww,pr];")
s = s.replace("insert:=function(v,w)", "insert:=function(v,w,proof)")
s = s.replace(
    "local reduced,idx,old,oldw,ii;",
    "local reduced,idx,old,oldw,oldproof,ii;",
)
s = s.replace(
    "reduced:=reduce(v,w);v:=reduced[1];w:=reduced[2];",
    "reduced:=reduce(v,w,proof);v:=reduced[1];w:=reduced[2];proof:=reduced[3];",
)
s = s.replace(
    "for ii in [2,4..Length(w)] do w[ii]:=-w[ii];od;",
    "for ii in [2,4..Length(w)] do w[ii]:=-w[ii];od;proof:=newNeg(proof);",
)
s = s.replace(
    "basis[idx]:=v;basisweights[idx]:=w;pivots:=pivots+1;",
    "basis[idx]:=v;basisweights[idx]:=w;basisproof[idx]:=proof;pivots:=pivots+1;",
)
s = s.replace(
    "old:=basis[idx];oldw:=basisweights[idx];basis[idx]:=v;"
    "basisweights[idx]:=w;v:=old;w:=oldw;",
    "old:=basis[idx];oldw:=basisweights[idx];oldproof:=basisproof[idx];"
    "basis[idx]:=v;basisweights[idx]:=w;basisproof[idx]:=proof;"
    "v:=old;w:=oldw;proof:=oldproof;",
)
s = s.replace(
    "red:=reduce(target,targetw);target:=red[1];targetw:=red[2];",
    "red:=reduce(target,targetw,targetproof);target:=red[1];"
    "targetw:=red[2];targetproof:=red[3];",
)
s = s.replace(
    "initial_target:=initialTarget,initial_extras:=initialExtras);",
    "initial_target:=initialTarget,initial_extras:=initialExtras,"
    "proof_node:=targetproof);",
)
s = s.replace(
    'found:=true;Print("witness_found',
    'PrintTo(traceStream,"[\\"success\\",",targetproof,",",coeffs,"]\\n");'
    'CloseStream(traceStream);found:=true;Print("witness_found',
)
s = s.replace(
    "for i in [1..Length(extras)] do insert(extras[i],[i,1]);od;",
    'for i in [1..Length(extras)] do '
    'insert(extras[i],[i,1],newLeaf("extra",[i],extras[i]));od;',
)
s = s.replace(
    "insert(tail,[]);profile[1]",
    'insert(tail,[],newLeaf("identity",currentRelation,tail));profile[1]',
)
s = s.replace(
    "if j>=abelStart then exteriorRelation(i,j,k);",
    "if j>=abelStart then currentRelation:=[2,i,j,k];exteriorRelation(i,j,k);",
)
s = s.replace(
    "w1:=ShallowCopy(zero);w1[k]:=1;CollectWordOrFail(coll,w1,ps[j][i]);",
    "currentRelation:=[1,i,j,k];"
    "w1:=ShallowCopy(zero);w1[k]:=1;CollectWordOrFail(coll,w1,ps[j][i]);",
)
s = s.replace(
    "w1:=ShallowCopy(zero);w1[j]:=orders[j]-1;",
    "currentRelation:=[3,i,j];"
    "w1:=ShallowCopy(zero);w1[j]:=orders[j]-1;",
)
s = s.replace(
    "w1:=ShallowCopy(zero);w1[k]:=1;CollectWordOrFail(coll,w1,ps[i][i]);",
    "currentRelation:=[4,i,k];"
    "w1:=ShallowCopy(zero);w1[k]:=1;CollectWordOrFail(coll,w1,ps[i][i]);",
)
s = s.replace(
    "w1:=makevec(ps[i][i]);CollectWordOrFail(coll,w1,[i,1]);",
    "currentRelation:=[5,i];"
    "w1:=makevec(ps[i][i]);CollectWordOrFail(coll,w1,[i,1]);",
)
s = s.replace(
    'Print("witness_complete_nonzero_remainder ",target,"\\n");',
    'PrintTo(traceStream,"[\\"failure\\",",targetproof,",",target,"]\\n");'
    'CloseStream(traceStream);'
    'Print("witness_complete_nonzero_remainder ",target,"\\n");',
)
assert "word(g[" not in s
assert "reduce(v,w);" not in s
assert "insert(tail,[]);" not in s
assert "basisproof[idx]:=proof" in s
destination = HERE / "pbc_hermite_data_witness.g"
destination.write_text(s)
metadata = {
    "input": source.name,
    "input_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "output": destination.name,
    "output_sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
    "proof": "DAG of exact integer operations on original unprocessed tail rows",
    "label_reductions": "only boundary-commutator coefficient labels mod2/mod3; DAG unreduced",
}
(HERE / "pbc_hermite_data_generation.json").write_text(json.dumps(metadata, indent=2) + "\n")
print(json.dumps(metadata, indent=2))
