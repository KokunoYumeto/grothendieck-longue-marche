"""First-reader proposal for 149_scan003. No OCR, web or TeX compilation."""
from pathlib import Path
import json

ROOT=Path('/workspace/scratch/f28c4f52d3ec')
PAGE='149_scan003'
C=(ROOT/'packets'/PAGE/'C.tex').read_text(encoding='utf-8')
TEX=C.replace('se reconstitue','se réconstitue').replace(
    'la variance des clôtures alg. de',
    r'la variance des clôtures alg\unsure{.|-} de')

BOX={
 'heading':[260,22,1225,155],
 'profini':[790,218,1450,365],
 'automorphisms':[280,650,1665,1025],
 'point':[280,970,1665,1110],
 'variance':[285,1085,1665,1560],
 'reconstitue':[280,1495,1640,1785],
 'ensembles':[280,1870,1660,2202],
 'folio':[20,2298,100,2350],
}
FULL={'automorphisms','variance','reconstitue'}
def crop(place):
    return f'crops/{PAGE}_{place}'+('_full' if place in FULL else '')+'.png'

data={
 'page':PAGE,'reader':'reader_b','lines_read':21,'places_cropped':8,
 'changes':[],'decisions':[],'implicit_decisions':[],'doubts':[],
 'inventory':[],'notes':[],'check_events':[],'notation':[],'abbreviations':[],
 'second_boxes':[],
}
def change(place,where,c,h,final,evidence,kind,error,dc=False,dh=True,
           confidence='high',marked=False,consequential=False):
    data['changes'].append({
        'id':f'{PAGE}-{len(data["changes"])+1:02d}','place':where,
        'c':c,'h':h,'final':final,'diff_c':dc,'diff_h':dh,
        'kind':kind,'error_kind':error,'evidence':evidence,
        'crop':crop(place),'box':BOX[place],'confidence':confidence,
        'marked_in_h':marked,'consequential':consequential,
    })

change('heading','Numbered and underlined heading',
       r'1. \uline{Résultats de fidélité}','absent',
       r'1. \uline{Résultats de fidélité}',
       'The large numeral has an oblique entry, upright and lower foot, followed by a separate point. Résultats has its initial capital R, acute accent, tall l/t strokes and final ts. Fidélité has a long descending f, two dotted i positions, tall d/l/t and accents. A single line runs beneath the words, not beneath the numeral.',
       'omission','Omissions')
change('variance','After foncteurs fibres',
       "à l'opposé", "i.e. l'opposée", "à l'opposé",
       'After the comma there is one compact lower a-shaped body with a detached slanted accent. There is no dotted i followed by e. The following word ends in one accented e and has no further e loop. The earlier à l’opposé in the same crop provides a matching local form.',
       'misread word','Words')
change('reconstitue','Initial accent in réconstitue',
       'reconstitue','reconstitue','réconstitue',
       'A separate short accent-like stroke lies above the initial e, around original x1180,y1560. It is detached from the preceding se and from the previous line. The accent is therefore retained in the written form réconstitue.',
       'misread word','Words',dc=True)
change('reconstitue','Punctuation before à partir',
       r'se reconstitue à partir',r'se reconstitue : à partir',
       r'se réconstitue à partir',
       'The group at the right end of the first line consists of a small lower oval/body and one slanted upper accent: it is the à before next-line partir. There is no second pair of marks making an independent colon.',
       'text not on the page','Text that is not on the page')
change('ensembles','Capital in Ensembles',
       'Ensembles',r'\uncertain{ensembles}','Ensembles',
       'The initial letter has a tall upright/loop and distinct upper and lower arms, rising above the following low n/s/e/m run. It is a capital E. The remainder n/s/e/m/b/l/e/s is separately legible.',
       'misread word','Words',marked=True)
change('folio','Lower-left pale folio annotation',
       r'\margin{2}','absent',r'\margin{2}',
       'The small pale mark has a curved upper entry, descending diagonal and extended lower foot, giving 2. It is separate from the final prose line and from the page border.',
       'omission','Omissions')

data['decisions']=[{
 'id':'M0951','decision':'undecided','reading':r'\mspage{\unsure{1}}',
 'evidence':'The small dark upper mark has an oblique rising entry and a short downstroke. It lacks a secure lower foot or other feature that would settle the numeral beyond doubt. The large section number 1 to the left is a separate mark and is not used to resolve this one.',
 'crop':crop('heading'),'box':BOX['heading'],'confidence':'low',
}]
data['doubts']=[
 {'place':'Small upper page annotation',
  'reading':r'\mspage{\unsure{1}}','alternatives':'1; another short angle-like annotation',
  'confidence':'low','reason':'Oblique entry and downstroke are visible, but the base is not distinctive enough for an unconditional numeral reading.'},
 {'place':'Terminal after the second alg, in the variance parenthesis',
  'reading':r'alg\unsure{.|-}','alternatives':'abbreviation point; short hyphen',
  'confidence':'medium','reason':'The detached terminal is horizontally elongated, although shorter and lighter than an ordinary hyphen. The letters alg themselves are clear. This is a certainty-only punctuation doubt, with the witness reading first.'},
]

specs=[
 ('margin note','upper right beside the heading','small doubtful 1',
  'unnamed hand (page annotation; attribution uncertain)'),
 ('text','top','1. Résultats de fidélité','his hand'),
 ('text','upper paragraph, first five lines','À tout corps K ... clôtures alg. séparables de K','his hand'),
 ('insertion','above pro in the second prose line','fini','his hand'),
 ('text','middle of first paragraph','Si K-bar est une telle clôture ... automorphismes','his hand'),
 ('insertion','above the first automorphismes','K-','his hand'),
 ('deletion','before the second automorphismes','K-','his hand'),
 ('insertion','above pt / associé','de B_K','his hand'),
 ('text','parenthetical continuation of first paragraph','il vaut peut-être mieux de dire ... points...','his hand'),
 ('deletion','after ce groupe —','K-bar','his hand'),
 ('text','lower paragraph','Bien entendu, B_K se réconstitue ...','his hand'),
 ('text','last prose line','Pour un hom de corps K to K-prime,','his hand'),
 ('margin note','bottom left','2','unnamed hand (folio annotation; attribution uncertain)'),
]
for i,(kind,position,objects,hand) in enumerate(specs,1):
    data['inventory'].append({'element':f'E{i:02d}','sheet_kind':'text','hand':hand,
      'kind':kind,'position':position,'first_words_or_objects':objects,'transcribed':'yes'})

def note(text,event=None,outcome=None):
    nid=f'{PAGE}-N{len(data["notes"])+1:02d}'
    data['notes'].append({'id':nid,'text':text})
    if event:data['check_events'].append({'statement_id':nid,'type':event,'outcome':outcome})
    return nid

note('The page associates the étale topos B_K to a field K and names its groupoid of points Π_K. It states a canonical antiequivalence with the category of separable algebraic closures. The bars on K, the K subscripts and all three E_{K-bar/K} occurrences were read individually; no group letter or index was supplied from mathematical expectation.',
     'carried as background without fault found',
     'The definitions and antiequivalence assertion were transcribed from the ink. No proof of the antiequivalence was carried out in this first reading.')
note('The parenthesis explicitly reconsiders the automorphism-group variance: it suggests using the opposite group and says that closures have the variance of fibre functors, opposite to that of points. The inserted K- before the first automorphismes, cancelled K- before the second, inserted de B_K and cancelled K-bar are preserved with their visible scopes.',
     'carried as background without fault found',
     'The author’s variance caveat was recorded without resolving it by an external convention or substituting a mathematical correction.')
note('The next paragraph states that B_K is recovered from continuous local systems on Π_K, or from discrete sets with a continuous E_{K-bar/K} action. The final clause starts with a field homomorphism K→K′ and ends with a comma at the page boundary; no continuation is supplied.',
     'carried as background without fault found',
     'The reconstruction assertion is carried as background, without an independent proof in this reading.')
note('The compact à forms after fibres and after réconstitue have a small lower body plus a detached upper accent. They explain H’s i.e. and added-colon readings. The source also has a separate accent over the initial e of réconstitue; the written spelling is retained. The capital E of Ensembles is visible and is preserved.')
note('The upper small page mark remains doubtful despite H’s editorial identification of author page 1. The large section number 1 and lower pale folio 2 are distinct annotations. Authorship is not inferred from the darkness or paleness of either folio mark.')
note('The original was viewed once for layout and both prepared top/bottom halves once, line by line. All 21 principal text baselines, including the heading and final fragment, were read; marginal numbers and raised additions are inventoried separately. Eight distinct places were enlarged. Three fuller boundary versions complete s’identifie’s descender, the variance passage’s tall strokes and final fibres descender, and the réconstitue/partir letter bounds. All 11 canonical PNG versions were viewed and retained; no whole image or half was reopened.')
note('The second alg terminal remains an explicit punctuation doubt only. The letters are secure, but the short detached horizontal mark can be an elongated abbreviation point or a hyphen. No reading-change row is counted for adding this uncertainty. Pure macro differences, overline/bar syntax, arrow length, and three dots versus a typographic ellipsis do not constitute separate ink readings.')

data['notation']=[
 {'sign':'à',
  'meaning_or_form':'A compact lower oval/body plus a detached slanted accent can resemble two punctuation marks.',
  'places':'After fibres; after réconstitue; compared with à l’opposé earlier in the same parenthesis and à K-bar/K',
  'universality':'Checked at these local occurrences; no claim about every a on other pages.',
  'witness_errors':'H expands the compact group after fibres to i.e. and supplies an extra colon after reconstitue.'},
 {'sign':'réconstitue',
  'meaning_or_form':'A separate short accent lies over the initial e; preserve the written accented spelling.',
  'places':'Opening of the lower paragraph',
  'universality':'One occurrence on this sheet.',
  'witness_errors':'Both witnesses omit the visible accent.'},
 {'sign':r'\Pi_K',
  'meaning_or_form':'Two tall uprights joined by a broad upper bar; a separate smaller K below/right.',
  'places':'Groupoid definition; both occurrences in the reconstruction paragraph',
  'universality':'All three occurrences were checked against the ink.',
  'witness_errors':'Neither witness changes these symbols; the capital Pi is not inferred solely from terminology.'},
 {'sign':r'E_{\bar K/K}',
  'meaning_or_form':'Plain capital E with a lower K-bar/K index; only the first K in that index carries a bar.',
  'places':'After Gal(K-bar/K); both later occurrences in the reconstruction paragraph',
  'universality':'All three occurrences were read separately.',
  'witness_errors':'No symbol departure; these repeated agreements were checked directly.'},
 {'sign':'Ensembles',
  'meaning_or_form':'A tall initial capital E rises above the following lower-case letters.',
  'places':'Discrete-action description',
  'universality':'One occurrence.',
  'witness_errors':'H gives doubtful lower-case ensembles.'},
 {'sign':'Curved insertion leader',
  'meaning_or_form':'A curve runs beneath raised text and bends toward the baseline gap, without striking the inserted letters.',
  'places':'fini; K- before first automorphismes; de B_K after pt',
  'universality':'The three additions were inspected separately.',
  'witness_errors':'Both witnesses preserve their insertion state; the separate cancelled K- is not confused with the live raised prefix.'},
]
data['abbreviations']=[
 {'form':'alg.','expansion':'algébriques'},
 {'form':'pt','expansion':'point'},
 {'form':'hom','expansion':'homomorphisme'},
 {'form':'Gal','expansion':'Galois (group notation)'},
]

# Each second-reading unit is a complete target; no second-pass crop is made.
units=[
 ('handwritten number',[260,22,1225,155],
  r'\mspage{\unsure{1}}'+'\n'+r'1. \uline{Résultats de fidélité}'),
 ('insertion',[790,218,1450,365],
  r'topos (pro\inserted{fini})galoisien.'),
 ('struck passage',[280,650,1665,1025],
  r"Si $\bar K$ est une telle clôture, son groupe des \inserted{$K$-}automorphismes $\operatorname{Gal}(\bar K/K)$ ou $E_{\bar K/K}$ s'identifie au groupe des \deleted{$K$-}automorphismes"),
 ('insertion',[280,970,1665,1560],
  r"du pt \inserted{de $B_K$} associé à $\bar K/K$ (il vaut peut-être mieux de dire : à l'opposé de ce groupe -- \deleted{$\bar K$} la variance des clôtures alg\unsure{.|-} de $K$ est comme celle des foncteurs fibres, à l'opposé de celle des points...)"),
 ('different words',[280,1495,1640,1785],
  r'Bien entendu, $B_K$ se réconstitue à partir de $\Pi_K$, comme le topos des'),
 ('different words',[280,1990,1660,2202],
  r'Ensembles discrets à action continue de $E_{\bar K/K}$.'),
 ('margin note',[20,2298,100,2350],r'\margin{2}'),
]
for i,(kind,box,reading) in enumerate(units,1):
    data['second_boxes'].append({'box':f'B{i:02d}','kind':kind,
      'x0':box[0],'y0':box[1],'x1':box[2],'y1':box[3],'reading':reading})

(ROOT/'proposed'/f'{PAGE}.tex').write_text(TEX,encoding='utf-8')
(ROOT/'proposed'/f'{PAGE}.json').write_text(
    json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(ROOT/'proposed'/f'{PAGE}_units.json').write_text(
    json.dumps(units,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
