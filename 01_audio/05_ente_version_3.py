import music as mc

c_1 = 262
d_1 = 294
e_1 = 330
f_1 = 350
g_1 = 392
a_1 = 440

viertel_note = 200
halbe_note = 2 * viertel_note
ganze_note = 2 * halbe_note

mc.pitch(c_1, viertel_note)
mc.pitch(d_1, viertel_note)
mc.pitch(e_1, viertel_note)
mc.pitch(f_1, viertel_note)

for _ in range(2):
    mc.pitch(g_1, halbe_note)

for _ in range(4):
    mc.pitch(a_1, viertel_note)

mc.pitch(g_1, ganze_note)

for _ in range(4):
    mc.pitch(a_1, viertel_note)

mc.pitch(g_1, ganze_note)

for _ in range(4):
    mc.pitch(f_1, viertel_note)

for _ in range(2):
    mc.pitch(e_1, halbe_note)

for _ in range(4):
    mc.pitch(d_1, viertel_note)

mc.pitch(c_1, ganze_note)
 