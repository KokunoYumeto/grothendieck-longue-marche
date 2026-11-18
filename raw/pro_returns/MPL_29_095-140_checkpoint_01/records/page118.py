from save_page import save_page

save_page(118, r'''
\scanpage{118}
% archive foliation: 117
% The reversed pale body text is show-through of scan 117.
% The cancelled typescript fragment below is upside down on this face.
\deleted{(2.1.14.6)
\diagram{\(\begin{array}{ccc}
P&\unsure{\otimes}&Q\\
\underline a&&\underline b
\end{array}\)}}
\figure{\begin{tikzpicture}\draw[line width=0.8pt] (0,0.20) .. controls (0.02,0.12) and (0.04,0.05) .. (0.05,0);\end{tikzpicture}}
''', [
('deletion','bottom upside-down fragment','(2.1.14.6), P⊗Q, underlined a,b'),
('text','within cancelled fragment','(2.1.14.6)'),
('diagram','within cancelled fragment','P ⊗ Q over underlined a,b'),
('drawing','near cancelled fragment','isolated short slanting ink stroke'),
], [
('cancelled operator between P,Q','⊗','circled overprint obscured by strike; no original connector added beneath','low'),
('isolated stroke by fragment','short pen stroke','could be a numeral 1; not secure enough to identify authorial pagination','low'),
('pale reversed text','show-through of scan 117','not repeated as a second text on this face','high'),
], leads=[
'Only an isolated cancelled typescript formula (2.1.14.6) and a small stroke occur on the face; the apparent body text is reverse-side show-through of scan117. No secure new statement or page count can be inferred.',
], sheet_kind='reused_typed')
