from save_page import save_page

save_page(124, r'''
\scanpage{124}
% archive foliation: 123
\begin{flushright}
``\uline{Vrai}'' groupe\\
fondamental

[pour les\\
\unsure{ensembles|schémas}]
\end{flushright}
''', [
('text','top right ink title','“Vrai” groupe fondamental'),
('text','pencil subtitle below title','[pour les ensembles]'),
], [
('pencilled subtitle last word','ensembles','schémas possible; very faint compressed strokes, first reading follows visible loop pattern','low'),
], [
'Cover headed “‘‘Vrai’’ groupe fondamental”, with Vrai underlined and a faint pencilled bracketed subtitle read uncertainly “[pour les ensembles|schémas]”. No date or page count is visible; preserve the subtitle as a reading question.',
], sheet_kind='cover')
