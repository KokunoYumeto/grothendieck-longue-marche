"""The three most symmetric ways to put five labelled points on the Riemann sphere: the special objects of
Grothendieck's five-point diagram (cote 148, scan 31; EXIT_TOWER B.12):
  I10: a regular pentagon on the equator (stabilizer D5, 12 labelled versions);
  I6:  a triangle on the equator and the two poles, "bitetrahedral" (stabilizer S3 acting on 3+2 by its sign, 20);
  I4:  a square on the equator and one pole (stabilizer C4, 30).
Each label of K = {0,...,4} has one colour, the same in every picture of the page.
blender -b -P blender_fivepoint.py -- OUT.png WIDTH SAMPLES"""
import bpy, math, sys
from mathutils import Vector, Matrix, Quaternion
argv = sys.argv[sys.argv.index('--') + 1:]
out, width, samples = argv[0], int(argv[1]), int(argv[2])
LABEL = ['#ff4d6d', '#ffb000', '#06d6a0', '#4895ef', '#c77dff']
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene


def lin(h):
    h = h.lstrip('#'); c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]


def emit_mat(name, hexcol, strength):
    m = bpy.data.materials.new(name); m.use_nodes = True; nt = m.node_tree; nt.nodes.clear()
    o = nt.nodes.new('ShaderNodeOutputMaterial'); e = nt.nodes.new('ShaderNodeEmission')
    e.inputs['Color'].default_value = (*lin(hexcol), 1); e.inputs['Strength'].default_value = strength
    nt.links.new(e.outputs['Emission'], o.inputs['Surface']); return m


def shell_mat():
    """A see-through sphere with a soft rim glow (layer-weight facing)."""
    m = bpy.data.materials.new('shell'); m.use_nodes = True; nt = m.node_tree; nt.nodes.clear()
    o = nt.nodes.new('ShaderNodeOutputMaterial'); mix = nt.nodes.new('ShaderNodeMixShader')
    tr = nt.nodes.new('ShaderNodeBsdfTransparent'); em = nt.nodes.new('ShaderNodeEmission')
    lw = nt.nodes.new('ShaderNodeLayerWeight'); lw.inputs['Blend'].default_value = 0.25
    ramp = nt.nodes.new('ShaderNodeValToRGB')
    ramp.color_ramp.elements[0].position = 0.0; ramp.color_ramp.elements[0].color = (0, 0, 0, 1)
    ramp.color_ramp.elements[1].position = 1.0; ramp.color_ramp.elements[1].color = (0.32, 0.32, 0.32, 1)
    em.inputs['Color'].default_value = (*lin('#7aa2ff'), 1); em.inputs['Strength'].default_value = 0.55
    nt.links.new(lw.outputs['Facing'], ramp.inputs['Fac'])
    nt.links.new(ramp.outputs['Color'], mix.inputs['Fac'])
    nt.links.new(tr.outputs['BSDF'], mix.inputs[1]); nt.links.new(em.outputs['Emission'], mix.inputs[2])
    nt.links.new(mix.outputs['Shader'], o.inputs['Surface'])
    return m


SHELL = shell_mat(); WIRE = emit_mat('wire', '#3a4a7a', 0.6); EDGE = emit_mat('edge', '#e8ecff', 0.9)
AXIS = emit_mat('axis', '#ffd23f', 1.2)
PT = [emit_mat(f'label{i}', c, 1.7) for i, c in enumerate(LABEL)]


def curve(name, pts, depth, mat):
    cu = bpy.data.curves.new(name, 'CURVE'); cu.dimensions = '3D'; cu.bevel_depth = depth; cu.bevel_resolution = 3
    sp = cu.splines.new('POLY'); sp.points.add(len(pts) - 1)
    for p, q in zip(sp.points, pts): p.co = (q.x, q.y, q.z, 1)
    ob = bpy.data.objects.new(name, cu); sc.collection.objects.link(ob); ob.data.materials.append(mat); return ob


def arc(a, b, n=48):
    a = a.normalized(); b = b.normalized(); om = math.acos(max(-1, min(1, a.dot(b))))
    if om < 1e-6: return [a, b]
    return [(a * math.sin((1 - t) * om) + b * math.sin(t * om)) / math.sin(om) for t in [i / n for i in range(n + 1)]]


def sphere_at(center, pts, cyc, axis_dir, name):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1.0, segments=128, ring_count=64, location=center)
    s = bpy.context.active_object; s.name = name; bpy.ops.object.shade_smooth(); s.data.materials.append(SHELL)
    c = Vector(center)
    for k in range(-2, 3):  # latitude circles
        z = k * 0.33; r = math.sqrt(max(0, 1 - z * z))
        curve(f'{name}_lat{k}', [c + Vector((r * math.cos(t), r * math.sin(t), z)) * 1.001 for t in [2 * math.pi * i / 128 for i in range(129)]], 0.0035, WIRE)
    for k in range(6):  # meridians
        ph = math.pi * k / 6
        curve(f'{name}_mer{k}', [c + Vector((math.sin(t) * math.cos(ph), math.sin(t) * math.sin(ph), math.cos(t))) * 1.001 for t in [math.pi * i / 64 for i in range(65)] + [math.pi + math.pi * i / 64 for i in range(1, 65)]], 0.0035, WIRE)
    for (i, j) in cyc:  # the polygon on the sphere
        curve(f'{name}_e{i}{j}', [c + pts[i], c + pts[j]], 0.009, EDGE)  # straight chords: the convex hull
    for lab, p in pts.items():
        bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=4, radius=0.085, location=c + p)
        o = bpy.context.active_object; bpy.ops.object.shade_smooth(); o.data.materials.append(PT[lab])
    d = Vector(axis_dir).normalized()
    curve(f'{name}_axis', [c - d * 1.45, c + d * 1.45], 0.006, AXIS)


def eq(theta):
    return Vector((math.cos(theta), math.sin(theta), 0))


# I10: regular pentagon 0,1,2,3,4 on the equator; the 5-fold axis vertical
pent = {i: eq(2 * math.pi * i / 5 - math.pi / 2 + 0.25) for i in range(5)}
sphere_at((-2.7, 0, 0), pent, [(i, (i + 1) % 5) for i in range(5)], (0, 0, 1), 'I10')
# I6: J = {0,1,2} an equilateral triangle on the equator, eps = {3,4} the poles; 3-fold axis vertical
tri = {0: eq(-math.pi / 2 + 0.35), 1: eq(-math.pi / 2 + 0.35 + 2 * math.pi / 3), 2: eq(-math.pi / 2 + 0.35 + 4 * math.pi / 3),
       3: Vector((0, 0, 1)), 4: Vector((0, 0, -1))}
sphere_at((0, 0, 0), tri, [(0, 1), (1, 2), (2, 0), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2)], (0, 0, 1), 'I6')
# I4: the oriented square 1,3,2,4 on the equator (stabilizer (1 3 2 4)), P = 0 at the north pole; 4-fold axis vertical
sq = {0: Vector((0, 0, 1)), 1: eq(math.pi / 4 - 0.3), 3: eq(3 * math.pi / 4 - 0.3), 2: eq(5 * math.pi / 4 - 0.3), 4: eq(7 * math.pi / 4 - 0.3)}
sphere_at((2.7, 0, 0), sq, [(1, 3), (3, 2), (2, 4), (4, 1), (0, 1), (0, 3), (0, 2), (0, 4)], (0, 0, 1), 'I4')

w = bpy.data.worlds.new('w'); sc.world = w; w.use_nodes = True
w.node_tree.nodes['Background'].inputs['Color'].default_value = (*lin('#05060c'), 1)
cam = bpy.data.objects.new('cam', bpy.data.cameras.new('cam')); sc.collection.objects.link(cam); sc.camera = cam
e = math.radians(20); dist = 12.8
cam.location = (0, -dist * math.cos(e), dist * math.sin(e)); cam.rotation_euler = (math.pi / 2 - e, 0, 0)
cam.data.lens = 50
sc.render.engine = 'CYCLES'
try:
    pr = bpy.context.preferences.addons['cycles'].preferences; pr.compute_device_type = 'OPTIX'; pr.get_devices()
    for d in pr.devices: d.use = d.type == 'OPTIX'
    sc.cycles.device = 'GPU'
except Exception as ex:
    print('GPU setup failed:', ex)
sc.cycles.samples = samples; sc.cycles.use_denoising = True; sc.cycles.transparent_max_bounces = 16
sc.render.resolution_x = width; sc.render.resolution_y = int(width * 0.38)
sc.view_settings.view_transform = 'Standard'; sc.view_settings.look = 'None'
sc.use_nodes = True; tr = sc.node_tree; tr.nodes.clear()
rl = tr.nodes.new('CompositorNodeRLayers'); gl = tr.nodes.new('CompositorNodeGlare'); co = tr.nodes.new('CompositorNodeComposite')
for attr, val in [('glare_type', 'BLOOM'), ('quality', 'HIGH'), ('size', 7), ('mix', 0.0), ('threshold', 0.6)]:
    try: setattr(gl, attr, val)
    except Exception: pass
tr.links.new(rl.outputs['Image'], gl.inputs['Image']); tr.links.new(gl.outputs['Image'], co.inputs['Image'])
sc.render.filepath = out; sc.render.image_settings.file_format = 'PNG'
bpy.ops.render.render(write_still=True); print('DONE', out)
