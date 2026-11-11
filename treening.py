# "import" toob kasutusele teise faili või teegi. Siin võtame teegist datetime
# ainult ühe asja: klassi datetime, millega saab kuupäevi kontrollida.
from datetime import datetime 


# ------------------------------------------------------------------
# ANDMED
# ------------------------------------------------------------------

# Siin on kõik treeningud. See on list ehk nimekiri: [treening1, treening2, ...]
# Iga treening on sõnastik (dict) ehk "vorm", kus igal väljal on nimi, näiteks:
# {"kuupaev": "2026-11-07", "harjutus": "Squat", "raskus": 60.0,
#  "kordused": 5, "seeriad": 3, "kommentaar": ""}
# Sõnastikust väärtuse küsimiseks kirjutame nime nurksulgudes: treening["raskus"]
treeningute_list = []


# ------------------------------------------------------------------
# FUNKTSIOONID
# ------------------------------------------------------------------


def anna_kuupäev(treening):
    """Tagastab ühe treeningu kuupäeva.

    Seda väikest funktsiooni on vaja sorteerimiseks: Pythonile tuleb öelda,
    mille järgi treeninguid järjestada, ja see "mille järgi" on kuupäev.
    """
    return treening["kuupäev"]

    

def lisa_treening(kuupäev, harjutus, raskus, kordused, seeriad, kommentaar):
    """Kontrollib sisestatud andmeid ja lisab treeningu listi.

    Kõik sisendid tulevad aknast tekstina (str), sest sisestuslahtrist saab alati teksti.
    Tagastab tühja teksti "", kui kõik õnnestus.
    Kui midagi on valesti, tagastab veateate teksti, mida aken kasutajale näitab.
    """

    # 1. Kuupäeva kontroll.
    # try/except tähendab: "proovi seda, ja kui tuleb viga, tee hoopis teist".
    # strptime proovib teksti kuupäevaks muuta. Kui tekst pole kujul AAAA-KK-PP,
    # tekib ValueError ja programm läheb except-ossa, mitte ei jookse kokku.
    try:
        datetime.strptime(kuupäev, "%Y-%m-%d")
    except ValueError:
        return "Viga: Kuupäev pole korrektses vormingus. Kasutage vormingut 'YYYY-MM-DD'."

# 2. Harjutuse nime kontroll. strip() kustutab tühikud nime algusest ja lõpust.
    if harjutus.strip() == "":
        return "Viga: Harjutus ei tohi olla tühi."


    # 3. Numbrite kontroll.
    # float() teeb tekstist komaga arvu, int() täisarvu. Kui tekst pole number
    # (näiteks "abc"), tekib jälle ValueError. Kõigepealt asendame koma punktiga,
    # sest Python tunneb komakohana ainult punkti (52,5 -> 52.5).
    try:
        raskus = float(raskus.replace(",", "."))
        kordused = int(kordused)
        seeriad = int(seeriad)
    except ValueError:
        return "Viga: Raskus, kordused ja seeriad peavad olema numbrid."


    # 4. Numbrite mõistlikkuse kontroll: raskus ei saa olla negatiivne,
    # kordusi ja seeriaid peab olema vähemalt 1.
    if raskus < 0 or kordused < 1 or seeriad < 1:
        return "Viga: Raskus peab olema mitte-negatiivne, kordused ja seeriad peavad olema vähemalt 1."


    # 5. Teeb treeningu sõnastiku ja lisab selle listi lõppu.
    treening = {
        "kuupäev": kuupäev,
        "harjutus": harjutus.strip(),
        "raskus": raskus,
        "kordused": kordused,
        "seeriad": seeriad,
        "kommentaar": kommentaar
    }
    treeningute_list.append(treening)

    # 6. Sorteerib listi kuupäeva järgi nii, et uuemad treeningud on listi alguses.
    # key=anna_kuupaev ütleb, mille järgi sorteerida. reverse=True paneb suurema
    # (uuema) kuupäeva ette. See töötab, sest kuupäev on kujul AAAA-KK-PP.
    treeningute_list.sort(key=anna_kuupäev, reverse=True)

    return "" # tühi tekst = "viga puudub"


def anna_treeningud():
    """Tagastab kõik treeningud (uuemad enne).

    main.py kasutab seda ajaloo, Dashboardi ja graafikute jaoks.
    """
    return treeningute_list


def kustuta_treening(index):
    """Kustutab treeningu, mis on listis kohal 'indeks'.

    Indeks on koha number listis ja see algab nullist: esimene treening on 0,
    teine on 1 jne. Akna nimekirjas on treeningud samas järjekorras kui siin
    listis, seepärast on kasutaja valitud rea number sama mis koht listis.
    """
    del treeningute_list[index] # del kustutab listist selle koha


def anna_harjutuste_nimed():
    """Tagastab tähestikulise listi harjutuste nimedest, mida on juba kasutatud.

    Iga nimi on listis ainult üks kord. Statistika leht kasutab seda rippmenüü jaoks.
    """
    nimed = []

    for treening in treeningute_list:
        # "not in" tähendab "ei ole listis". Nii ei lisa me sama nime kaks korda.
        if treening["harjutus"] not in nimed:
            nimed.append(treening["harjutus"])

    nimed.sort() # sorteerib nimed tähestiku järjekorda
    return nimed