"""Export the retained exact finite group certificate to a fresh GAP replay."""
import json
from pathlib import Path

base = Path(__file__).resolve().parent
data = json.loads((base / "check_descent_central_full_certificate.json").read_text())
lines = ["# Independent replay from the exported full PC presentation."]
for key in ["full_cover_pc", "candidate14_f", "candidate14_beta", "candidate14_A"]:
    lines.append(f"cert_{key}:=" + json.dumps(data[key], separators=(",", ":")) + ";")
lines.append(r'''
BuildCertificatePC:=function(dat)
 local n,fg,g,coll,word,i,rel,gr;
 n:=Length(dat[1]);fg:=FreeGroup(n);g:=GeneratorsOfGroup(fg);
 coll:=SingleCollector(g,dat[1]);
 word:=v->Product([1..n],j->g[j]^v[j]);
 for i in [1..n] do SetPower(coll,i,word(dat[2][i]));od;
 for rel in dat[3] do SetConjugate(coll,rel[1],rel[2],word(rel[3]));od;
 gr:=GroupByRws(coll);return gr;
end;
certGroup:=BuildCertificatePC(cert_full_cover_pc);certPc:=Pcgs(certGroup);
Print("REPLAY constructed consistent PC presentation.\n");
CertElement:=v->Product([1..Length(certPc)],j->certPc[j]^v[j]);
certS:=CertElement(cert_full_cover_pc[4]);certR:=CertElement(cert_full_cover_pc[5]);
certF:=CertElement(cert_candidate14_f);
certBeta:=CertElement(cert_candidate14_beta);certA:=CertElement(cert_candidate14_A);
if Size(certGroup)<>9393093476352 or Size(Group(certS,certR))<>Size(certGroup) then Error("certificate size or generation failure");fi;
Print("REPLAY source generation checked.\n");
if certS^2<>One(certGroup) or certR^3<>One(certGroup) then Error("certificate source torsion failure");fi;
if certBeta*certS*certBeta^-1<>certS*certF or certA*certR*certA^-1<>certF^-1*certR then Error("literal certificate frames fail");fi;
Print("REPLAY literal frames checked.\n");
certAuto:=GroupHomomorphismByImages(certGroup,certGroup,[certS,certR],[certS*certF,certF^-1*certR]);
if certAuto=fail or not IsBijective(certAuto) then Error("certificate automorphism failure");fi;
certX:=(certS*certR)^-2;certY:=certS*certX*certS;certPure:=Group(certX,certY);
if not certBeta in certPure or not certA in certPure or not certF in DerivedSubgroup(certPure) then Error("certificate pure normalization failure");fi;
Print("REPLAY PASS: exact source generators, full order, automorphism, pure-derived f, and both literal positive frames.\n");
if not IsBound(CERTIFICATE_REPLAY_CONTINUE) or not CERTIFICATE_REPLAY_CONTINUE then QUIT_GAP(0);fi;
''')
(base / "check_central_certificate_replay.g").write_text("\n".join(lines))
print("Exported exact independent PC-presentation replay.")
