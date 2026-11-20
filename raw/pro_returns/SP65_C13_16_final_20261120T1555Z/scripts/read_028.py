from record_api import Page
p=Page(28)
p.r(r'\unsure{Notes.at|Notes at}','Notes.at')
p.d('M0287','first','Notes.at','small typed point between Notes and at is visible in the full-resolution lower half')
p.p['sheet_kind']='typescript'
for num,author in [(14,'author rule; Sur quelques points'),(15,'Hochschild, G.'),(16,'Hochschild, G. and Nakayama, T.'),(17,'Hochschild, G. and Serre, J.-P.'),(18,'Lang, S.'),(19,'Nakayama, T.'),(20,'Ogg, A. P.'),(21,'Rosenberg, A. and Zelinsky, D.'),(22,'Serre, J.-P.'),(23,'author rule; Dimension cohomologique'),(24,'author rule; Groupes Algébriques'),(25,'author rule; Sur la topologie'),(26,'Shatz, S.'),(27,'Tate, J.')]:
 p.inv(('text',f'bibliography [{num}]',author,'typewriter'))
p.inv(('text','bottom centre','45','typewriter'),('text','bottom left','27','hand not attributed, pencil'))
p.p['notes']='A typescript bibliography page, numbered 45, with pencil folio 27. Entries [14]–[27] concern homological algebra, class field theory, cohomology and abelian varieties. All author lines, titles, journal abbreviations, volumes, years and page ranges were read against the scan. The printed date range on this leaf runs from 1950 to 1962; [26] says “to appear”, and [27] refers to notes of May 1959. The small typed point in “Notes.at” at [23] is retained. No external bibliographic verification was made; witness H has no page here.'
p.p['certainty']=[['M0287','Notes.at confirmed; no change beyond removing the doubt wrapper.']]
p.p['notation']=[['Repeated-author rule','long typed underline before comma','028','entries [14], [23]–[25]'],['Quoted title','typewriter double quotes rendered with paired backticks/apostrophes','028','entry [23]']]
p.p['hand']=[['Bibliographic titles underlined word by word on the typewriter','028','underlined entries on this sheet','C wording and underlines retained']]
p.p['abbreviations']=[['Ann. of Math.','Annals of Mathematics'],['T.A.M.S.','Transactions of the American Mathematical Society'],['Cf.','confer / compare'],['No.','number']]
p.save()
