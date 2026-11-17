from workflow import save_page
save_page(52,r'''
\scanpage{52}
% archive foliation: 51
HARVARD UNIVERSITY

DEPARTMENT OF MATHEMATICS

\textsc{Area Code 617}

495--2170

\figure{\begin{tikzpicture}[scale=.8]
\draw (-.8,1)--(.8,1)--(.8,.35) .. controls (.8,-.25) and (.4,-.65) .. (0,-.9)
.. controls (-.4,-.65) and (-.8,-.25) .. (-.8,.35)--cycle;
\foreach \x/\y/\l/\r in {-.4/.5/V/E,.4/.5/R/I,0/-.25/T/AS}{
\draw (\x-.27,\y-.24) rectangle (\x+.27,\y+.24);
\draw (\x-.3,\y-.2)--(\x-.35,\y-.17)--(\x-.3,\y-.11)--(\x-.3,\y+.1)--(\x-.35,\y+.16)--(\x-.3,\y+.2);
\draw (\x+.3,\y-.2)--(\x+.35,\y-.17)--(\x+.3,\y-.11)--(\x+.3,\y+.1)--(\x+.35,\y+.16)--(\x+.3,\y+.2);
\draw (\x-.23,\y-.2)--(\x-.23,\y+.2)--(\x,\y+.18)--(\x+.23,\y+.2)--(\x+.23,\y-.2)--(\x,\y-.18)--cycle;
\draw (\x,\y+.18)--(\x,\y-.18);
\node[font=\scriptsize,inner sep=0] at (\x-.11,\y){\l};
\node[font=\scriptsize,inner sep=0] at (\x+.11,\y){\r};}
\end{tikzpicture}}

\textsc{Science Center}

\textsc{One Oxford Street}

\textsc{Cambridge, Massachusetts 02138}

June 10, 1978

Dear Friend,

This letter concerns the 80th birthday of Oscar Zariski. This will take place
on April 24th, 1979. I have been talking to Jun-Ichi Igusa, who together with
Jerry Sampson has recently taken over the Editorship of the \uline{American Journal
of Mathematics}, and they agreed that it would be a fine thing to dedicate one
(and perhaps two) issue(s) of the \uline{American Journal} to Oscar on this occasion.
I'm sending this letter out to about thirty of his friends, colleagues and
students to ask if they would like to dedicate a paper to Oscar in this issue.
Unfortunately, as you can guess from the date of his birthday, we can only do
this by adhering to a strict deadline. I sincerely apologize for launching
a project like this at such a late date and must take full blame for this my-\\
self. However, the upshot is that the absolute deadline for contributions
must be November 1st (or January 1st, \uline{if we get enough submissions for a second
issue}): The issue(s) will then be the first one (or first two) of the \uline{American
Journal} in 1979.

I will be very pleased if you find it possible to send me a paper for Oscar's
80th birthday. But I fully understand if the short notice makes this impos-\\
sible. In any case, to help in our planning I would be very grateful if you
would drop me a line now indicating whether or not you expect to be in a posi-\\
tion to send us a manuscript, and, if so, roughly what length it might be.
(We have a maximum of 460 printed pages to use and if we are deluged there is
a small chance that we may have to limit the length of individual submissions.)
Please write me at:

Wallston Road

Tenants Harbor, Maine\quad 04860

U.S.A.

where I will be until about September 10th.

Best regards,

David Mumford/mjm

David Mumford

DM/mjm
''',[
('text','top centre letterhead','HARVARD UNIVERSITY; DEPARTMENT OF MATHEMATICS'),
('text','top left phone block','Area Code 617; 495–2170'),
('drawing','top centre shield','three open books: V E; R I; T AS'),
('text','top right address','Science Center; One Oxford Street; Cambridge, Massachusetts 02138'),
('text','date line','June 10, 1978'),
('text','salutation','Dear Friend,'),
('text','first paragraph','This letter concerns the 80th birthday of Oscar Zariski'),
('text','second paragraph','I will be very pleased'),
('text','postal address','Wallston Road; Tenants Harbor, Maine 04860; U.S.A.'),
('text','below address','where I will be until about September 10th.'),
('text','closing','Best regards,'),
('text','handwritten signature','David Mumford/mjm'),
('text','typed signature','David Mumford'),
('text','bottom left initials','DM/mjm')],sheet_kind='reused_typed')
