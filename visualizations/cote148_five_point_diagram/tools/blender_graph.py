"""Blender (4.5) render of the cote 148 five-point diagram: 542 objects as spheres, 1,620 arrows as glowing tubes
coloured by family, on a D5-symmetric layout. Run:
blender -b -P blender_graph.py -- LAYOUT.json KEY OUT.png WIDTH SAMPLES VIEW [FRAMES]
VIEW: 'oblique' | 'axis' | 'turntable' (turntable writes OUT_####.png frames, FRAMES frames)."""
import bpy, bmesh, json, math, sys
from mathutils import Vector, Matrix
argv = sys.argv[sys.argv.index('--') + 1:]
layout_path, key, out_path, width, samples, view = argv[0], argv[1], argv[2], int(argv[3]), int(argv[4]), argv[5]
frames = int(argv[6]) if len(argv) > 6 else 1
L = json.load(open(layout_path)); P = json.load(open(layout_path.replace('layout_c5.json', 'tools/palette.json')))
X = [Vector(p) for p in L[key]]; types = L['types']; edges = L['edges']
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
def lin(h):
    h = h.lstrip('#'); c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
def mat(name, hexcol, emit, rough=0.35, alpha=1.0):
    m = bpy.data.materials.new(name); m.use_nodes = True; nt = m.node_tree; nt.nodes.clear()
    o = nt.nodes.new('ShaderNodeOutputMaterial'); b = nt.nodes.new('ShaderNodeBsdfPrincipled')
    c = (*lin(hexcol), 1.0)
    b.inputs['Base Color'].default_value = c; b.inputs['Roughness'].default_value = rough
    b.inputs['Emission Color'].default_value = c; b.inputs['Emission Strength'].default_value = emit
    b.inputs['Alpha'].default_value = alpha
    nt.links.new(b.outputs['BSDF'], o.inputs['Surface']); return m
# nodes: one mesh per type
R = {'I10': 0.034, 'I6': 0.028, 'I4': 0.024}
for t in sorted(set(types)):
    bm = bmesh.new()
    r = R.get(t, 0.012 if t.startswith('III') else 0.016)
    for i, tt in enumerate(types):
        if tt == t:
            bmesh.ops.create_icosphere(bm, subdivisions=3, radius=r, matrix=Matrix.Translation(X[i]))
    me = bpy.data.meshes.new('nodes_' + t); bm.to_mesh(me); bm.free()
    for p in me.polygons: p.use_smooth = True
    ob = bpy.data.objects.new('nodes_' + t, me); sc.collection.objects.link(ob)
    ob.data.materials.append(mat('m_' + t, P['TC'][t], 1.6 if t.startswith('I') and not t.startswith('II') else 0.7))
# edges: one curve object per family; parallel arrows bent apart
from collections import Counter, defaultdict
mult = Counter((min(s, t), max(s, t)) for f, s, t in edges); seen = defaultdict(int)
byfam = defaultdict(list)
for f, s, t in edges:
    k = (min(s, t), max(s, t)); j = seen[k]; seen[k] += 1
    byfam[f].append((s, t, j, mult[k]))
for f, lst in byfam.items():
    cu = bpy.data.curves.new('arrows_' + f, 'CURVE'); cu.dimensions = '3D'
    cu.bevel_depth = 0.0024; cu.bevel_resolution = 2; cu.use_fill_caps = True
    for s, t, j, m in lst:
        a, b = X[s], X[t]; mid = (a + b) / 2; d = b - a
        off = Vector((0, 0, 0))
        if m > 1:
            side = d.cross(mid if mid.length > 1e-6 else Vector((0, 0, 1)))
            if side.length < 1e-9: side = d.orthogonal()
            side.normalize(); off = side * (j - (m - 1) / 2) * 0.35 * d.length
        pts = [a + d * u + off * (4 * u * (1 - u)) for u in [i / 8 for i in range(9)]] if m > 1 else [a, b]
        sp = cu.splines.new('POLY'); sp.points.add(len(pts) - 1)
        for p, q in zip(sp.points, pts): p.co = (q.x, q.y, q.z, 1)
    ob = bpy.data.objects.new('arrows_' + f, cu); sc.collection.objects.link(ob)
    ob.data.materials.append(mat('m_' + f, P['FAM'][f], 1.1, 0.5, alpha=0.55))
# world, camera, render settings
w = bpy.data.worlds.new('w'); sc.world = w; w.use_nodes = True
w.node_tree.nodes['Background'].inputs['Color'].default_value = (*lin('#05060c'), 1)
w.node_tree.nodes['Background'].inputs['Strength'].default_value = 1.0
cam = bpy.data.objects.new('cam', bpy.data.cameras.new('cam')); sc.collection.objects.link(cam); sc.camera = cam
cam.data.lens = 50
pivot = bpy.data.objects.new('pivot', None); sc.collection.objects.link(pivot)
cam.parent = pivot
def place(elev_deg, dist=3.9):
    e = math.radians(elev_deg)
    cam.location = (0, -dist * math.cos(e), dist * math.sin(e))
    cam.rotation_euler = (math.pi / 2 - e, 0, 0)
if view == 'axis': place(89.9)
else: place(28)
cam.data.dof.use_dof = True; cam.data.dof.focus_distance = 3.9; cam.data.dof.aperture_fstop = 4.0
sc.render.engine = 'CYCLES'
try:
    pr = bpy.context.preferences.addons['cycles'].preferences
    pr.compute_device_type = 'OPTIX'; pr.get_devices()
    for d in pr.devices: d.use = d.type == 'OPTIX'
    sc.cycles.device = 'GPU'
except Exception as ex:
    print('GPU setup failed:', ex)
sc.cycles.samples = samples; sc.cycles.use_denoising = True
sc.render.resolution_x = width; sc.render.resolution_y = width; sc.render.film_transparent = False
sc.view_settings.view_transform = 'Standard'; sc.view_settings.look = 'None'; sc.view_settings.exposure = -0.3
# compositor bloom
sc.use_nodes = True; tr = sc.node_tree; tr.nodes.clear()
rl = tr.nodes.new('CompositorNodeRLayers'); gl = tr.nodes.new('CompositorNodeGlare'); co = tr.nodes.new('CompositorNodeComposite')
for attr, val in [('glare_type', 'BLOOM'), ('quality', 'HIGH'), ('size', 7), ('mix', 0.0), ('threshold', 0.6)]:
    try: setattr(gl, attr, val)
    except Exception: pass
for name, val in [('Threshold', 0.5), ('Strength', 0.6), ('Size', 0.5)]:
    try: gl.inputs[name].default_value = val
    except Exception: pass
tr.links.new(rl.outputs['Image'], gl.inputs['Image']); tr.links.new(gl.outputs['Image'], co.inputs['Image'])
sc.render.image_settings.file_format = 'PNG'
if view == 'turntable':
    sc.frame_start = 1; sc.frame_end = frames
    pivot.rotation_euler = (0, 0, 0); pivot.keyframe_insert('rotation_euler', frame=1)
    pivot.rotation_euler = (0, 0, 2 * math.pi / 5); pivot.keyframe_insert('rotation_euler', frame=frames + 1)
    for fc in pivot.animation_data.action.fcurves:
        for kp in fc.keyframe_points: kp.interpolation = 'LINEAR'
    sc.render.filepath = out_path; bpy.ops.render.render(animation=True)
else:
    sc.render.filepath = out_path; bpy.ops.render.render(write_still=True)
print('DONE', out_path)
