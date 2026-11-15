kpse.set_program_name('luahbtex')
local p=os.getenv('TEXMFCACHE')
print('cache',p,kpse.expand_var('$TEXMFCACHE'))
print('mode',lfs.attributes(p,'mode'))
if lfs.iswritablefile then print('iswritablefile',lfs.iswritablefile(p)) end
local f,e=io.open(p..'/probe.tmp','w')
print('write',f~=nil,e)
if f then f:write('probe');f:close();os.remove(p..'/probe.tmp') end
