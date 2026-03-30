import music
import microbit

achtel = 150
viertel = 2 * achtel
halbe = 2 * viertel

c_1 = 262
d_1 = 294
e_1 = 330
f_1 = 350
g_1 = 392
a_1 = 440
h_1 = 494
c_2 = 2 * c_1
d_2 = 2 * d_1
fis_1 = 370
cis_1 = 277


def zeile_1():
    music.pitch(d_1, viertel + achtel)
    music.pitch(fis_1, achtel)
    music.pitch(a_1, viertel)
    music.pitch(d_2, viertel)
    music.pitch(h_1, viertel)
    music.pitch(d_2, achtel)
    music.pitch(h_1, achtel)
    music.pitch(a_1, halbe)
    music.pitch(g_1, viertel + achtel)
    music.pitch(a_1, achtel)
    music.pitch(fis_1, viertel)
    music.pitch(d_1, viertel)
    music.pitch(e_1, halbe)
    music.pitch(d_1, viertel)
    microbit.sleep(viertel)


for _ in range(3):
    zeile_1()
    for _ in range(2):
        for _ in range(2):
            music.pitch(a_1, viertel)

        for _ in range(2):
            music.pitch(g_1, viertel)

        music.pitch(fis_1, viertel)
        music.pitch(a_1, achtel)
        music.pitch(fis_1, achtel)
        music.pitch(e_1, halbe)

    zeile_1()
