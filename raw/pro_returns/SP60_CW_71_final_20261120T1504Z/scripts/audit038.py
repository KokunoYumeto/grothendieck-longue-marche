from record import *
change(38,'038-H13','manuscript folio XI',r'$\underline{\overline{\mathrm{XI}}}$','not transcribed',r'$\underline{\overline{\mathrm{XI}}}$','Second reading: XI is present at the upper right with an upper and a lower rule. The whole image settles the folio; no new crop needed.',h=True,kind='omission')
with (ROOT/'progress.log').open('a') as f:
 f.write('scan 038 audited '+utc()+' — complete second reading against whole image; folio coverage omission added for H; page text unchanged.\n')
render()
