from pathlib import Path
import subprocess,json
base=Path(__file__).resolve().parents[2]
queries={
'E01':r'conormal|exterior|determinant|invariants normaux|immersion réguli|fibrés projectifs',
'E02':r'20\.6\.26|conormal|homotopy|cotangent|duality|Riemann',
'E03':r'ellip|Picard|inversible|Symm|projectifs',
'E04':r'discrimin|resultant|résultant|hypersurface',
'E05':r'discrimin|geometrically regular|smoothness|lisse|17\.5',
'E06':r'invertible|projective|faisceaux inversibles|fibrés projectifs',
'E07':r'integrab|Kodaira|Spencer|deformation|differential|20\.6\.26',
'E08':r'exponential|exponentielle|logarithm|20\.1\.4|Campbell|Hausdorff',
'E09':r'primitive|multiplicative|hyperalg|Cartier|20\.1\.4',
'E10':r'group algebra|groupe.*Z|dual|hyperalg|20\.4\.13',
'E11':r'augmentation|square zero|nilpotent|18\.2\.3',
'E12':r'universally exact|universal.*exact|kernel|flat|20\.5\.5',
'E13':r'primitive|multiplicative|exponential|20\.1\.4',
'E14':r'Cartier|group-like|primitive|Lie algebra|Schémas de groupes',
'E15':r'Poincar|Birkhoff|Witt|enveloping|Cartier|regular local',
'E16':r'group.*smooth|smooth.*group|Cartier|Schémas de groupes',
'E17':r'derivation|automorph|20\.1\.4|bilinear',
'E18':r'20\.1\.4|20\.1\.6|augmentation|nilpotent',
'E19':r'20\.4\.8|20\.5\.5|20\.5\.6|base change',
'E20':r'augmentation|tensor product|20\.5\.5|20\.1\.6',
'E21':r'20\.1\.4|Campbell|Hausdorff|infinitesimal',
'E22':r'integrab|Kodaira|Spencer|Campbell|Hausdorff|20\.1\.3'
}
log=[]
for nid,q in queries.items():
 r=subprocess.run(['rg','-n','-i','--',q,str(base/'context')],capture_output=True,text=True)
 matches=r.stdout.splitlines(); log.append(f'## {nid}\nrg -n -i -- {q!r} context\nreturn code: {r.returncode}; hits: {len(matches)}\n')
 log.extend(matches[:100] or ['NO MATCH'])
 if len(matches)>100:log.append(f'[first100hits retained; {len(matches)-100} further matches not printed]')
 log.append('')
out=Path(__file__).with_name('research_root_searches.txt');out.write_text('\n'.join(log))
print('Recorded',len(queries),'independent note searches in',out.name)
