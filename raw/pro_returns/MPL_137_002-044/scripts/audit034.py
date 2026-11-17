from audit_support import revise
revise(34,replacements=[
(r'\tau',r'\unsure{\mathcal{T}|\tau}'),
(r'\unsure{\mathbf Z|k}',r'\unsure{k|\mathbf Z}'),
(r"\unsure{\forall\text{ objet de }}C'\text{ est }",r"\unsure{\forall\text{ objet de }}\unsure{C|C'}\text{ est }"),
(r'\unsure{repartons}',r'\unsure{reprenons|repartons}')],
doubts=[('cancelled equivalence continuation','C','C prime','low'),('final paragraph opening','reprenons','repartons','medium')],
notation=[('additivity coefficient',r'\unsure{k|\mathbf Z}','The small coefficient has a descending oblique stem and right hook; k is preferred with Z explicitly retained, as on scan 030.')],
note='Second visual audit, including the underlined à vérifier margin and the cancelled equivalence clause. Harmonized only visually compared looped type signs and ambiguous coefficient order; added a prime doubt inside the cancelled text and refined the final verb doubt.')
