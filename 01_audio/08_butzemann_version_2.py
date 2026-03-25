import music as mc
import microbit as mt

achtel_note = 100
viertel_note = 2 * achtel_note

c_1 = 262
d_1 = 294
g_1 = 392
a_1 = 440
h_1 = 494
c_2 = 2 * c_1
d_2 = 2 * d_1


def notenblock():
    mc.pitch(d_1, achtel_note)
    mc.pitch(g_1, achtel_note)
    mc.pitch(g_1, achtel_note)
    mc.pitch(d_2, achtel_note)
    mc.pitch(d_2, achtel_note)
    mc.pitch(h_1, achtel_note)
    mc.pitch(h_1, achtel_note)
    mc.pitch(g_1, achtel_note)
    mc.pitch(g_1, achtel_note)
    mc.pitch(a_1, achtel_note)
    mc.pitch(a_1, achtel_note)
    mc.pitch(d_1, achtel_note)
    mc.pitch(d_1, achtel_note)
    mc.pitch(g_1, viertel_note)
    mt.sleep(achtel_note)

for _ in range(10):
    notenblock()
    notenblock()
    
    for _ in range(2):
        mc.pitch(h_1, achtel_note)
        mc.pitch(a_1, achtel_note)
        mc.pitch(h_1, achtel_note)
        mc.pitch(c_2, achtel_note)
        mc.pitch(a_1, achtel_note)
        mc.pitch(h_1, achtel_note)
        mc.pitch(c_2, achtel_note)
        mc.pitch(d_2, achtel_note)
    
    notenblock()
