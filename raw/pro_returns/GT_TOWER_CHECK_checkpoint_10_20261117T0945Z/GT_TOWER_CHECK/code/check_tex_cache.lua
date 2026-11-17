kpse.set_program_name("luahbtex")
local p = os.getenv("TEXMFCACHE")
print("cache env", p)
print("cache expanded", kpse.expand_var("$TEXMFCACHE"))
print("cache mode", lfs.attributes(p, "mode"))
print("cache native writable", lfs.iswritablefile and tostring(lfs.iswritablefile(p)))
local f,err=io.open(p.."/write_test.tmp","wb")
print("cache actual open",tostring(f),tostring(err))
if f then f:write("test\n");f:close();os.remove(p.."/write_test.tmp") end
