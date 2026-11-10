from datetime import date, datetime, timedelta



# matplotlib.pyplot on graafikute joonistamise tööriist. "as plt" annab sellele
# lühikese nime, et ei peaks kirjutama iga kord pikka matplotlib.pyplot.
import matplotlib.pyplot as plt

import harjumus
import treening

def anna_nädal(kuupäev_tekst):
    """Tagastab kuupäeva aasta ja nädalanumbri tekstina, näiteks "2026-45".

    Seda kasutame, et grupeerida treeningud nädalate kaupa.
    """
    päev = datetime.strptime(kuupäev_tekst, "%Y-%m-%d") # tekst -> kuupäev
    # isocalendar() annab kolm numbrit: aasta, nädalanumber ja nädalapäev
    aasta, nädal, nädalapäev = päev.isocalendar()
    # zfill(2) lisab ette nulli, et "5" oleks "05" ja nädalad sorteeruksid õigesti
    return str(aasta) + "-" + str(nädal).zfill(2)


def näita_raskuse_graafikut(harjutus):
    """Joonistab valitud harjutuse suurima raskuse päeva kohta (joongraafik)."""

    # Kõigepealt leiame iga päeva suurima raskuse selle harjutuse kohta.
    # suurimad_raskused on sõnastik: võti on kuupäev, väärtus on suurim raskus.
    suurimad_raskused = {}
    for üks_treening in treening.anna_treeningud():
        if treening["harjutus"] == harjutus:
            päev = treening["kuupäev"]
            # Lisame päeva, kui seda veel pole, või uuendame, kui see raskus on suurem
            if päev not in suurimad_raskused or treening["raskus"] > suurimad_raskused[päev]:
                suurimad_raskused[päev] = treening["raskus"]

    # Kui andmeid pole, ei joonistata midagi, vaid tagastame teate.
    if len(suurimad_raskused) == 0:
        return "Selle harjutuse kohta pole treeninguid."

    # Teeme kaks listi: kuupäevad (x-telg) ja raskused (y-telg), samas järjekorras.
    kuupäevad = sorted(suurimad_raskused) # sorted annab sõnastiku võtmed järjekorras
    raskused = []
    for päev in kuupäevad:
        raskused.append(suurimad_raskused[päev])

    # Nüüd graafiku joonistamine. Iga plt rida teeb ühe asja:
    plt.figure("Raskuse graafik")                               # uus graafiku aken
    plt.plot(kuupäevad, raskused, marker="o", color="green")    # joon koos punktidega
    plt.title("Raskuse areng harjutusel: " + harjutus)          # pealkiri
    plt.xlabel("Kuupäev")                                       # x-telje nimi
    plt.ylabel("Suurim raskus (kg)")                            # y-telje nimi
    plt.xticks(rotation=45)                                     # kuupäevad viltu, et mahuksid
    plt.tight_layout()                                          # sätib kõik aknasse ära
    plt.show()                                                  # avab akna
    return ""


def näita_nädalate_graafikut():
    """Joonistab treeningupäevade arvu nädalate kaupa (tulpdiagramm)."""

    # nadala_paevad on sõnastik: võti on nädal ("2026-45"), väärtus on list
    # kuupäevadest, millal sel nädalal treeniti. Sama päeva me kaks korda ei loe,
    # sest tahame teada treeningupäevi, mitte harjutuste arvu.
    nädala_päevad = {}
    for üks_treening in treening.anna_treeningud():
        nädal = anna_nädal(treening["kuupäev"])
        if nädal not in nädala_päevad:
            nädala_päevad[nädal] = []
        if treening["kuupäev"] not in nädala_päevad[nädal]:
            nädala_päevad[nädal].append(treening["kuupäev"])

    if len(nädala_päevad) == 0:
        return "Treeninguid pole."

    # Võtame viimased 10 nädalat. [-10:] tähendab "listi viimased 10 elementi".
    nädalad = sorted(nädala_päevad)[-10:]
    arvud = []
    for nädal in nädalad:
        arvud.append(len(nädala_päevad[nädal])) # len annab listi pikkuse

    plt.figure("Treeningud nädalate kaupa")
    plt.bar(nädalad, arvud, color="green") # bar teeb tulpdiagrammi
    plt.title("Treeningupäevade arv nädalate kaupa")
    plt.xlabel("Nädal")
    plt.ylabel("Treeningupäevade arv")
    plt.yticks(range(0, max(arvud) +1)) # y-teljel ainult täisarvud
    plt.tight_layout()
    plt.show()
    return ""


def näita_harjumuste_graafikut():
    """Joonistab iga harjumuse täitmise protsendi viimase 30 päeva kohta."""

    if len(harjumus.anna_harjumused()) == 0:
        return "Harjumusi pole."

    # Algkuupäev = tänane päev miinus 29 päeva, nii saame kokku 30 päeva.
    # isoformat() teeb kuupäevast teksti kujul AAAA-KK-PP.
    algus_kuupäev = (date.today() - timedelta(days=29)).isoformat()

    nimed = []
    protsendid = []
    for nimi in harjumus.anna_harjumused():
        #loeme kokku, mitu päeva viimase 30 päeva jooksul harjumus täidetud on
        loendur = 0
        for kirje_nimi, kirje_kuupäev in harjumus.täidetud_list:
            # Tekstide võrdlus töötab kuupäevadega, sest need on kujul AAAA-KK-PP.
            if kirje_nimi == nimi and kirje_kuupäev >= algus_kuupäev:
                loendur += 1

        nimed.append(nimi)
        protsendid.append(loendur / 30 * 100) # täidetud päevi / 30 päeva * 100 = 

    plt.figure("Harjumuste täitmine")
    plt.barh(nimed, protsendid, color="green") # barh = rõhtsad tulbad
    plt.title("harjumuste täitmine viimase 30 päeva jooksul")
    plt.xlabel("Täidetud protsent")
    plt.xlim(0, 100) # x-telg 0-100%
    plt.tight_layout()
    plt.show()
    return ""


def näita_üldise_arengu_graafikut():
    """Joonistab üldise arengu: iga nädala kogu tõstetud raskus.

    Kogu tõstetud raskus = raskus x kordused x seeriad, summeeritud nädala kaupa.
    Kui see number aja jooksul kasvab, siis treeningud muutuvad raskemaks.
    """

    nädala_summad = {}  # nädal -> selle nädala kogu tõstetud raskus
    for üks_treening in treening.anna_treeningud():
        nädal = anna_nädal(treening["kuupäev"])
        kokku = treening["raskus"] * treening["kordused"] * treening["seeriad"]
        if nädal not in nädala_summad:
            nädala_summad[nädal] = 0
        nädala_summad[nädal] += kokku

    if len(nädala_summad) == 0:
        return "Treeninguid pole."

    nädalad = sorted(nädala_summad)[-10:]  # viimased 10 nädalat
    mahud = []
    for nädal in nädalad:
        mahud.append(nädala_summad[nädal])

    plt.figure("Üldine areng")
    plt.plot(nädalad, mahud, marker="o", color="green")
    plt.title("Kogu tõstetud raskus nädalate kaupa")
    plt.xlabel("Nädal")
    plt.ylabel("Raskus x kordused x seeriad (kg)")
    plt.tight_layout()
    plt.show()
    return ""


