#!/usr/bin/env python3
"""Transcribe root's scan020 journal choices into implementation fields."""
from pathlib import Path
import hashlib
import json
import re
import sys
sys.dont_write_bytecode=True
from scan020_prepare_sources import span

BASE=Path('/workspace/scratch/94548b74fbe0')
OUT=BASE/'out/checks'
JP='out/checks/scan020_main_decisions.md'
J=(BASE/JP).read_text()
ROWS=[]


def add(n,key,final,confidence,kind,alternatives=(),status=None,**extra):
    did=f'L020-{n:02d}'
    match=re.search(r'^'+did+r'\b',J,re.M)
    assert match,did
    nextrow=re.search(r'^L020-\d+\b|^## ',J[match.end():],re.M)
    end=match.end()+nextrow.start() if nextrow else len(J)
    literal=J[match.start():end]
    counts=re.search(r'\bC([01])/H([01])\b',literal)
    assert counts,(did,'missing exact root count')
    assert confidence in literal,(did,confidence)
    row=dict(id=did,source='SRC020-'+key,final=final,confidence=confidence,kind=kind,
        C=int(counts[1]),H=int(counts[2]),remaining_doubt=bool(alternatives),alternatives=list(alternatives),
        C_doubt_status=status,hand='his hand',main_approved=False,
        root_choice_source=span(JP,J,match.start(),end),**extra)
    ROWS.append(row)


SYMBOL='misread symbol or index'
DRAW='drawing or diagram'
ILL=r'readable ink left as \ill{}'
HEAD=('head retrace','independent upper bar')
add(1,'RING1',r'\Pi_I^{\unsure{\circ|0}}','medium',SYMBOL,['0'],'retained',printed_qualifier=True,first_qualifier=True)
add(2,'RING2',r'\Pi_J^\circ; local zero alternative retained','medium',SYMBOL,['0'],'retained',printed_qualifier=False)
add(3,'PI-PREDECESSOR',r'\deleted{\Pi}U_{J,i},','high','omission')
add(4,'CLAS-WORD',r'\unsure{clas|deux}.','low','misread word',['deux'],'retained',
    decision_scope='Lexical reading only; separate terminal point is L020-05.')
add(5,'CLAS-POINT','A distinct terminal point follows either clas/deux candidate once.','high','omission')
add(6,'PAIR-INDEX',r'\Sigma_{\unsure{\deleted{J}i|j|i}}^+; complete glyph in R020-G01','low',SYMBOL,[r'j',r'i'],'retained',
    selected_source_group='R020-G01',H_count_parent='L020-06')
add(7,'POSITIVE-SIGMA-HEAD','R020-G01: one complete positive Sigma with a separate short upper run; its head-retrace/upper-bar role stays qualified.','medium',DRAW,HEAD,
    selected_source_group='R020-G01',H_count_parent='L020-06',printed_qualifier=True,first_qualifier=True)
add(8,'NEGATIVE-SIGMA-HEAD',r'R020-G02: complete two-run Sigma_i^- with its attached index hook/point and raised minus; local short-head role remains unresolved.','medium',DRAW,HEAD,
    selected_source_group='R020-G02',printed_qualifier=False)
add(9,'CANCELLED-SIGMA',r'R020-G03: cancelled \Sigma_{\unsure{j|i}}, complete body and two crossing runs.','low',ILL,['i'],'retained',
    selected_source_group='R020-G03',H_placeholder_parent='H020-ILL-01',physical_count_parent='L020-09')
add(10,'CANCELLED-SIGMA-HEAD','R020-G03: short separate upper head retained once within the cancelled Sigma cluster.','medium',DRAW,HEAD,
    selected_source_group='R020-G03',physical_count_parent='L020-09',C_count_parent='L020-09',H_count_parent='L020-09',printed_qualifier=False)
add(11,'VOISINAGE-POINT','A020-G02: one qualified gray rounded point below the gap after voisinage.','medium','omission',
    ['Character, role, hand and surface origin remain unassigned.'],selected_source_group='A020-G02')
ROWS[-1]['hand']='undetermined hand'
add(12,'E-INDEX',r'E_{\unsure{i|j}}','medium','other',['j'],'retained')
add(13,'E-PREDECESSOR',r'\deleted{\Sigma}E','high','omission')
add(14,'E-COMMA','Comma after the voisinage E index before et.','high','omission')
add(15,'BAR1-E-PREDECESSOR',r'\deleted{\Sigma}E_i in first nonemptiness formula','high','omission')
add(16,'BAR1',r'Long outer bar of \overline{\Sigma_i^+}, retained once in R020-G04.','high','other',
    selected_source_group='R020-G04',S_id='SA01-K81-06',S_status='local closure bar confirmed, already present in both current witnesses')
add(17,'BAR1-SIGMA-HEAD','R020-G04: complete positive Sigma, separate short head and already-present long outer bar, each retained once.','medium',DRAW,HEAD,
    selected_source_group='R020-G04',printed_qualifier=False)
add(18,'BAR2-SIGMA-PREDECESSOR',r'\overline{\deleted{E}\Sigma_i^-}','high','omission')
add(19,'BAR2-E-PREDECESSOR',r'\deleted{\Sigma}E_i in second nonemptiness formula','high','omission')
add(20,'BAR2',r'Long outer bar of \overline{\deleted{E}\Sigma_i^-}, retained.','high','other',
    S_id='SA01-K81-06',S_status='local closure bar confirmed, already present in both current witnesses')
add(21,'VOIT','sait','medium','misread word',status='resolved')
add(22,'EN','en, live between est and the cancelled word.','high','omission')
add(23,'COUNT-WORD',r'R020-G05: \deleted{\unsure{tout|est}} with literal crossings, including interrupted initial flecks of the second run.','low',ILL,['est'],'retained',
    selected_source_group='R020-G05',H_placeholder_parent='H020-ILL-02',physical_count_parent='L020-23')
add(24,'AUSSI',r'\unsure{aussi|ainsi}','medium','other',['ainsi'],'retained')
add(25,'LA-POINT','A020-G04: one qualified detached triangular point after la; the word remains outside the point-only group.','medium',DRAW,
    ['Role, character, hand and relation to the writing remain unassigned.'],selected_source_group='A020-G04')
ROWS[-1]['hand']='undetermined hand'
add(26,'DEM',r'\unsure{dèm.|dém.|dem.}','low','misread word',['dém.','dem.'],'retained')
add(27,'PAR',r'\unsure{par|p}','low','other',['p'])
add(28,'RING3',r'\Pi_I^\circ; local zero alternative retained','medium',SYMBOL,['0'],'retained',printed_qualifier=False)
add(29,'UNION','B_G03: three literal union paths, with the complete group and X setminus in its enclosing math source.','high',DRAW,selected_source_group='B_G03')
add(30,'UNION-INDEX',r'\alpha\in\deleted{I}K','medium',SYMBOL,status='resolved',selected_source_group='B_G03')
add(31,'BRACE','B_G03: main brace/step/right hook, closed left loop and dark left retrace, each retained once.','high',DRAW,selected_source_group='B_G03')
add(32,'HAT-LABEL',r'\inserted{\widehat{\Sigma}_\alpha^+} above the brace','high','insertion or placement',selected_source_group='B_G03')
add(33,'NONVIDE','C_G03--G04: inserted and cancelled non vide, with literal G03 crossing/pointed return.','medium',
    'deletion state (struck given live or live given struck)',selected_source_group='C_G03--G04')
add(34,'GUIDE','C_G03--G04: one complete curved G04 guide; group owns partie, non vide and de I,; et remains outside.','high',DRAW,selected_source_group='C_G03--G04')
add(35,'ONA',r'\deleted{on a}','high',ILL,H_placeholder_parent='H020-ILL-03',physical_count_parent='L020-35')
add(36,'MEMBERSHIP',r'R020-G06: literal reworked relation; primary \deleted{\Rightarrow}\in, alternatives \deleted{\to}\in and \in in an invisible complete-state annotation.','low',DRAW,
    [r'\deleted{\to}\in',r'\in'],'retained',selected_source_group='R020-G06')
add(37,'MEMBERSHIP-E',r'{\unsure{E|\deleted{\Sigma}E}}_\alpha','low','other',[r'\deleted{\Sigma}E'])
add(38,'MARGIN',r'\rotatebox{23}{\shortstack[l]{$K$ est $\ne\varnothing$\\si $I\ne\varnothing$}}','high','other')
add(39,'ARCHIVE','19, retained only in the archive-sheet comment and inventory.','high','other')
ROWS[-1]['hand']='undetermined hand'

add(40,'CONVENTION',r'\scanpage{20}; archive numeral remains a comment; H page19 and apparatus convention retained.','high','other',
    root_ink_choice_applied=False,root_source_audit_choice_applied=True,
    decision_scope='Source-only administrative convention.',confidence_scope='High for the exact source convention and page-map correspondence.')
ROWS[-1]['hand']='source-only administration'
add(41,'S-AUDIT','SA01-K81-06 source attribution and page coverage retained; no further bar or witness correction selected.','high','other',
    S_id='SA01-K81-06',
    S_status='Exact quoted index-1/i.e. expressions, strict-inclusion chain and U_s example absent from the three complete independent page readings; local bars individually confirmed at L020-16/L020-20 and already present in C/H.',
    root_ink_choice_applied=False,root_source_audit_choice_applied=True,
    decision_scope='Source attribution and coverage only; local root ink confirmations have their own rows.',
    confidence_scope='High for source attribution and the reported page coverage, without a new root whole-page view.')
ROWS[-1]['hand']='source-only attribution'
add(42,'AGREED-REMAINDER','Twelve exact agreed source scopes retained subject to the root-selected local replacements L020-01–39.','high','other',
    root_ink_choice_applied=False,root_source_audit_choice_applied=True,
    decision_scope='Source-only selection of agreed remainder; every original reader span retained.',
    confidence_scope='High for the exact source selections; no new root ink view or mathematical verification.')
ROWS[-1]['hand']='source-only coverage of selected manuscript text'

out=dict(scan=20,source_journal=dict(path=JP,sha256=hashlib.sha256(J.encode()).hexdigest()),
    scope='Exact root-selected readings copied into implementation fields; counts copied literally from each root paragraph. No clerk ink choice.',
    choices=ROWS,main_adjudicated=False,main_approved=False)
path=OUT/'scan020_root_choices.json'
path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(path=path.relative_to(BASE).as_posix(),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
    applied_through=ROWS[-1]['id'],C=sum(r['C'] for r in ROWS),H=sum(r['H'] for r in ROWS),doubts=sum(r['remaining_doubt'] for r in ROWS)),ensure_ascii=False))
