# "import" toob kasutusele teise faili või teegi. Siin võtame teegist datetime
# ainult ühe asja: klassi datetime, millega saab kuupäevi kontrollida.
from datetime import datetime 

# ------------------------------------------------------------------
# ANDMED
# ------------------------------------------------------------------

# Harjumuste nimede list, näiteks ["Reading", "Water"]
harjumuste_list = []

# Täidetud harjumuste list. Iga kirje on paar [harjumuse nimi, kuupäev], näiteks
# ["Reading", "2026-11-07"] tähendab: "7. novembril loeti".
# Kui sellist paari listis pole, siis sel päeval harjumust ei täidetud.
täidetud_list = []


# ------------------------------------------------------------------
# FUNKTSIOONID
# ------------------------------------------------------------------


def lisa_harjumus(nimi):
    """Lisab uue harjumuse. Tagastab "" kui õnnestus, muidu veateate teksti."""

    nimi = nimi.strip() # kustutab tühikud nime algusest ja lõpust

    if nimi == "":
        return "Palun sisesta harjumuse nimi."

    # "in" kontrollib, kas nimi on juba listis. Kahte sama nimega harjumust ei lase.
    if nimi in harjumuste_list:
        return "Selline harjumus on juba olemas."

    harjumuste_list.append(nimi)
    return ""


def anna_harjumused():
    """Tagastab listi kõigist harjumustest."""
    return harjumuste_list


def kustuta_harjumus(nimi):
    """Kustutab harjumuse ja kõik selle täitmise kirjed."""
    # "global" ütleb Pythonile: allpool muudame faili alguses olevat täidetud_list'i
    # (mitte ei tee uut sama nimega muutujat funktsiooni sisse).
    global täidetud_list

    harjumuste_list.remove(nimi) # remove kustutab listist selle väärtuse

    # Teeme uue listi, kuhu paneme ainult TEISTE harjumuste kirjed.
    # Nii kaovad kustutatud harjumuse kirjed ära ega jää "orbudena" alles.

    uus_täidetud_list = []
    for kirje in täidetud_list:
        if kirje[0] != nimi: # kirje[0] on harjumuse nimi, kirje[1] on kuupäev
            uus_täidetud_list.append(kirje)
    täidetud_list = uus_täidetud_list


def kas_täidetud(nimi, kuupäev):
    """Tagastab True, kui harjumus on sellel kuupäeval täidetud, muidu False."""
    return [nimi, kuupäev] in täidetud_list


def vaheta_täidetud(nimi, kuupäev):
    """Vahetab märget: kui harjumus oli täidetud, võtab märke ära, muidu paneb märke.

    Seda funktsiooni kutsub nupp "Mark done / not done".
    """
    if kas_täidetud(nimi, kuupäev):
        täidetud_list.remove([nimi, kuupäev])
    else:
        täidetud_list.append([nimi, kuupäev])


def kas_kuupäev_korras(kuupäev):
    """Tagastab True, kui tekst on kuupäev kujul AAAA-KK-PP, muidu False."""
    try:
        datetime.strptime(kuupäev, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def mitu_täidetud_päeval(kuupäev):
    """Tagastab, mitu harjumust on antud kuupäeval täidetud.

    Dashboard kasutab seda, et näidata "2 / 4" (täidetud / kõik harjumused).
    """
    loendur = 0
    for kirje in täidetud_list:
        if kirje[1] == kuupäev:
            loendur += 1 
    return loendur

def anna_ajalugu():
    """Tagastab viimased 30 päeva, millal midagi täideti.

    Tulemus on list paaridest (kuupäev, täidetud harjumuste nimed tekstina),
    näiteks [("2026-11-07", "Reading, Water")]. Uuemad päevad on ees.
    """

    # Esimene samm: grupeerime täidetud harjumused päevade kaupa.
    # paevad on sõnastik: võti on kuupäev ja väärtus on selle päeva harjumuste list.
    päevad = {}
    for nimi, päev in täidetud_list: # kirje [nimi, paev] jagatakse kaheks muutujaks
        if päev not in päevad:
            päevad[päev] = [] # selle päeva jaoks tühi list
        päevad[päev].append(nimi)

    # Teine samm: teeme tulemuse. sorted(..., reverse=True) järjestab kuupäevad
    # uuematest vanemateni ja [:30] võtab neist ainult esimesed 30.
    tulemus = []
    for päev in sorted(päevad, reverse=True)[:30]:
        # ", ".join(list) ühendab list tekstiks, nt ["a", "b"] -> "a, b"
        tulemus.append((päev, ", ".join(päevad[päev])))
    return tulemus