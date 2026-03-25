import music as mc
import microbit as mt

# Variablen für die Tonlänge

sechzehntel_note = 100
achtel_note = 2 * sechzehntel_note
viertel_note = 2 * achtel_note
halbe_note = 2 * viertel_note
ganze_note = 2 * halbe_note
punktierte_achtel_note_note = sechzehntel_note + achtel_note

# Variablen für die Tonhöhe

h = 247
c_1 = 262
d_1 = 294
e_1 = 330
f_1 = 350
g_1 = 392
a_1 = 440
c_2 = 2 * c_1

# Notenfolge definieren

mc.pitch(e_1, viertel_note)
mc.pitch(f_1, viertel_note)
mc.pitch(g_1, viertel_note)
mt.sleep(achtel_note)


# Funktionsdefinition
def notenblock():  # Funktionskopf
    # Funktionskörper
    mc.pitch(c_2, achtel_note)
    mc.pitch(g_1, achtel_note)
    mc.pitch(f_1, achtel_note)
    mc.pitch(e_1, achtel_note)
    mc.pitch(d_1, achtel_note)
    mc.pitch(c_1, viertel_note)


notenblock()
mt.sleep(achtel_note)

for _ in range(2):
    mc.pitch(g_1, achtel_note)
    mc.pitch(f_1, achtel_note)
    mc.pitch(e_1, achtel_note)
    mc.pitch(d_1, achtel_note)
    mc.pitch(c_1, achtel_note)
    mc.pitch(h, achtel_note)
    mc.pitch(c_1, achtel_note)
    mc.pitch(d_1, achtel_note)

mc.pitch(c_1, achtel_note)
mc.pitch(f_1, punktierte_achtel_note_note)
mc.pitch(f_1, sechzehntel_note)
mc.pitch(e_1, achtel_note)
mc.pitch(c_1, achtel_note)
mc.pitch(a_1, punktierte_achtel_note_note)
mc.pitch(a_1, sechzehntel_note)
mc.pitch(g_1, achtel_note)
notenblock()
mt.sleep(viertel_note)
