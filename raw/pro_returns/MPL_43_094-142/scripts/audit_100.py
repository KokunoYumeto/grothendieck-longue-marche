from audit_work import audit_page
changes=[(r'\gamma',r'\unsure{\sigma|\gamma}'),(r'(\Gamma^*G,',r'(\Gamma G^*,'),(r'\margin{$S\unsure{\sigma|\gamma}=(D\Delta\unsure{\sigma|\gamma}_K)(1)$}',r'''\margin{$S\unsure{\sigma|\gamma}=(D\Delta\unsure{\sigma|\gamma}_K)(1)$}
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[->](.7,0)..controls(-.6,0)and(-.5,.2)..(-.4,.7)..controls(-.4,1.1)and(.5,1.3)..(.8,1.6)..controls(1,1.9)and(.7,2.2)..(.3,2.6)..controls(-.1,3)and(.9,3.1)..(1.6,3.4);
\end{tikzpicture}}''')]
audit_page(100,changes,notes='Whole sheet reread and compared with the recurring closed-loop Greek coefficient sign on later pages, without context. It is now marked sigma/gamma, not silently fixed. The star in the second Gamma expression is above G, so its attachment is corrected. Added the upper-left enclosure/leader. Rechecked both unfinished displays and items1–8.',extra_elements=[('drawing','upper left','enclosure and long curved leader with arrowhead')])
