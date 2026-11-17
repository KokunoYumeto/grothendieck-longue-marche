import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
s=r'''\scanpage{57}
% archive foliation: 56
la vérification de la formule
\[
\operatorname{Hom}_{\unsure{\bullet}}(\lambda_\bullet,L_\bullet)
\xrightarrow{\sim}\operatorname{Hom}(L_\bullet^\vee,\lambda_\bullet^\vee)
\]
est élémentaire.
'''
e=[('text','top line','la vérification de la formule'),('display','top second line','Hom(lambda,L) isom Hom(L dual,lambda dual)'),('text','top third line','est élémentaire')]
save(57,s,e)
