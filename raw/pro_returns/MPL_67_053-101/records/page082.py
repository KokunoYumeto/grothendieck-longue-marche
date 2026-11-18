import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{82}
\mspage{15}
% archive foliation: 84
est étale, en calculant i.e. interprétant
son application tangente.
"""
save(82,tex,[('text','top two lines','est étale, en calculant')],leads=['Continuation of scan 81: proposed test of etaleness by interpreting the tangent map; no calculation supplied on this page.'])
