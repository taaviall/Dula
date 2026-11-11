from datetime import date, datetime, timedelta

<<<<<<< HEAD


# matplotlib.pyplot on graafikute joonistamise tööriist. "as plt" annab sellele
# lühikese nime, et ei peaks kirjutama iga kord pikka matplotlib.pyplot.
import matplotlib.pyplot as plt

import harjumus
import treening

=======
import harjumus
import treening

# Kõik graafikufunktsioonid saavad esimese argumendina "ax", ehk joonistusala,
# mis asub Statistika_frame'i sees. Nad tagastavad "" kui kõik õnnestus,
# või veateate teksti, mida aken kasutajale näitab.


>>>>>>> origin/Kaarel
def anna_nädal(kuupäev_tekst):
    """Tagastab kuupäeva aasta ja nädalanumbri tekstina, näiteks "2026-45".

    Seda kasutame, et grupeerida treeningud nädalate kaupa.
    """
<<<<<<< HEAD
    päev = datetime.strptime(kuupäev_tekst, "%Y-%m-%d") # tekst -> kuupäev
=======
    päev = datetime.strptime(kuupäev_tekst, "%Y-%m-%d")  # tekst -> kuupäev
>>>>>>> origin/Kaarel
    # isocalendar() annab kolm numbrit: aasta, nädalanumber ja nädalapäev
    aasta, nädal, nädalapäev = päev.isocalendar()
    # zfill(2) lisab ette nulli, et "5" oleks "05" ja nädalad sorteeruksid õigesti
    return str(aasta) + "-" + str(nädal).zfill(2)


<<<<<<< HEAD
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
=======
def näita_raskuse_graafikut(ax, harjutus):
    """Joonistab valitud harjutuse suurima raskuse päeva kohta (joongraafik)."""

    # suurimad_raskused on sõnastik: võti on kuupäev, väärtus on suurim raskus.
    suurimad_raskused = {}
    for üks_treening in treening.anna_treeningud():
        if üks_treening["harjutus"] == harjutus:
            päev = üks_treening["kuupäev"]
            # Lisame päeva, kui seda veel pole, või uuendame, kui see raskus on suurem
            if päev not in suurimad_raskused or üks_treening["raskus"] > suurimad_raskused[päev]:
                suurimad_raskused[päev] = üks_treening["raskus"]

    if len(suurimad_raskused) == 0:
        return "Selle harjutuse kohta pole treeninguid."

    # Kaks listi: kuupäevad (x-telg) ja raskused (y-telg), samas järjekorras.
    kuupäevad = sorted(suurimad_raskused)
>>>>>>> origin/Kaarel
    raskused = []
    for päev in kuupäevad:
        raskused.append(suurimad_raskused[päev])

<<<<<<< HEAD
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
=======
    ax.plot(kuupäevad, raskused, marker="o", color="green")
    ax.set_title("Raskuse areng harjutusel: " + harjutus)
    ax.set_xlabel("Kuupäev")
    ax.set_ylabel("Suurim raskus (kg)")
    ax.tick_params(axis="x", labelrotation=45)
    return ""


def näita_nädalate_graafikut(ax):
    """Joonistab treeningupäevade arvu nädalate kaupa (tulpdiagramm)."""

    # nädala_päevad on sõnastik: võti on nädal ("2026-45"), väärtus on list
>>>>>>> origin/Kaarel
    # kuupäevadest, millal sel nädalal treeniti. Sama päeva me kaks korda ei loe,
    # sest tahame teada treeningupäevi, mitte harjutuste arvu.
    nädala_päevad = {}
    for üks_treening in treening.anna_treeningud():
<<<<<<< HEAD
        nädal = anna_nädal(treening["kuupäev"])
        if nädal not in nädala_päevad:
            nädala_päevad[nädal] = []
        if treening["kuupäev"] not in nädala_päevad[nädal]:
            nädala_päevad[nädal].append(treening["kuupäev"])
=======
        nädal = anna_nädal(üks_treening["kuupäev"])
        if nädal not in nädala_päevad:
            nädala_päevad[nädal] = []
        if üks_treening["kuupäev"] not in nädala_päevad[nädal]:
            nädala_päevad[nädal].append(üks_treening["kuupäev"])
>>>>>>> origin/Kaarel

    if len(nädala_päevad) == 0:
        return "Treeninguid pole."

<<<<<<< HEAD
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
=======
    # Viimased 10 nädalat. [-10:] tähendab "listi viimased 10 elementi".
    nädalad = sorted(nädala_päevad)[-10:]
    arvud = []
    for nädal in nädalad:
        arvud.append(len(nädala_päevad[nädal]))

    ax.bar(nädalad, arvud, color="green")
    ax.set_title("Treeningupäevade arv nädalate kaupa")
    ax.set_xlabel("Nädal")
    ax.set_ylabel("Treeningupäevade arv")
    ax.set_yticks(range(0, max(arvud) + 1))  # y-teljel ainult täisarvud
    return ""


def näita_harjumuste_graafikut(ax):
>>>>>>> origin/Kaarel
    """Joonistab iga harjumuse täitmise protsendi viimase 30 päeva kohta."""

    if len(harjumus.anna_harjumused()) == 0:
        return "Harjumusi pole."

    # Algkuupäev = tänane päev miinus 29 päeva, nii saame kokku 30 päeva.
<<<<<<< HEAD
    # isoformat() teeb kuupäevast teksti kujul AAAA-KK-PP.
=======
>>>>>>> origin/Kaarel
    algus_kuupäev = (date.today() - timedelta(days=29)).isoformat()

    nimed = []
    protsendid = []
    for nimi in harjumus.anna_harjumused():
<<<<<<< HEAD
        #loeme kokku, mitu päeva viimase 30 päeva jooksul harjumus täidetud on
=======
        # Loeme kokku, mitu päeva viimase 30 päeva jooksul harjumus täidetud on
>>>>>>> origin/Kaarel
        loendur = 0
        for kirje_nimi, kirje_kuupäev in harjumus.täidetud_list:
            # Tekstide võrdlus töötab kuupäevadega, sest need on kujul AAAA-KK-PP.
            if kirje_nimi == nimi and kirje_kuupäev >= algus_kuupäev:
                loendur += 1

        nimed.append(nimi)
<<<<<<< HEAD
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
=======
        protsendid.append(loendur / 30 * 100)  # täidetud päevi / 30 päeva * 100

    ax.barh(nimed, protsendid, color="green")  # barh = rõhtsad tulbad
    ax.set_title("Harjumuste täitmine viimase 30 päeva jooksul")
    ax.set_xlabel("Täidetud protsent")
    ax.set_xlim(0, 100)  # x-telg 0-100%
    return ""


def näita_üldise_arengu_graafikut(ax):
>>>>>>> origin/Kaarel
    """Joonistab üldise arengu: iga nädala kogu tõstetud raskus.

    Kogu tõstetud raskus = raskus x kordused x seeriad, summeeritud nädala kaupa.
    Kui see number aja jooksul kasvab, siis treeningud muutuvad raskemaks.
    """

    nädala_summad = {}  # nädal -> selle nädala kogu tõstetud raskus
    for üks_treening in treening.anna_treeningud():
<<<<<<< HEAD
        nädal = anna_nädal(treening["kuupäev"])
        kokku = treening["raskus"] * treening["kordused"] * treening["seeriad"]
=======
        nädal = anna_nädal(üks_treening["kuupäev"])
        kokku = üks_treening["raskus"] * üks_treening["kordused"] * üks_treening["seeriad"]
>>>>>>> origin/Kaarel
        if nädal not in nädala_summad:
            nädala_summad[nädal] = 0
        nädala_summad[nädal] += kokku

    if len(nädala_summad) == 0:
        return "Treeninguid pole."

    nädalad = sorted(nädala_summad)[-10:]  # viimased 10 nädalat
    mahud = []
    for nädal in nädalad:
        mahud.append(nädala_summad[nädal])

<<<<<<< HEAD
    plt.figure("Üldine areng")
    plt.plot(nädalad, mahud, marker="o", color="green")
    plt.title("Kogu tõstetud raskus nädalate kaupa")
    plt.xlabel("Nädal")
    plt.ylabel("Raskus x kordused x seeriad (kg)")
    plt.tight_layout()
    plt.show()
    return ""


=======
    ax.plot(nädalad, mahud, marker="o", color="green")
    ax.set_title("Kogu tõstetud raskus nädalate kaupa")
    ax.set_xlabel("Nädal")
    ax.set_ylabel("Raskus x kordused x seeriad (kg)")
    return ""
>>>>>>> origin/Kaarel
