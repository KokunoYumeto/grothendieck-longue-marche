from pathlib import Path
from record_page import save_page
content=(Path(__file__).resolve().parents[1]/'pages/MPL_152+120_152_scan001.tex').read_text().split('\\scanpage{1}\n',1)[1]
save_page(120,1,content,[('text','left large logo','IMAG'),('text','left middle','INSTITUT MONTPELLIERAIN'),('text','left lower','ALEXANDER GROTHENDIECK'),('drawing','right and bottom','faceted polyhedral logo with dotted hidden edges and border')],kind='cover',observations='Archive cover independently inspected in whole and both halves; printed wording and polyhedral logo match the cote 152 cover. No manuscript title, dating, pagination or page total is written on this cover.')
