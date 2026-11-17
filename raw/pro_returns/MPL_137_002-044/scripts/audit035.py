from audit_support import revise
revise(35,replacements=[
(r'\unsure{\mathbf Z|k}',r'\unsure{k|\mathbf Z}'),
("d'où un sens inverse",r"d'où \unsure{en|un} sens inverse"),
(r'D\arrow[d,hook]',r'D\arrow[d,phantom,"\cap" description]'),
(r'\inserted{$k_0$-}',r'\inserted{$\unsure{k_0|k}$-}')],
doubts=[('line 2','en sens inverse','un sens inverse','medium'),('inserted coefficient before module','k subscript 0','k','medium')],
note='Second visual audit of whole scan and enlarged bands. Preserved the tensor-product subscript C and the later k despite earlier k_0. Reproduced the vertical cap-shaped inclusion between D and the functor category without an invented arrowhead; harmonized the visibly recurring coefficient doubt.')
