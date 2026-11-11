import customtkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
import calendar
import harjumus
import treening
import statistika2


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue") 

#-----------------------
#Pea akna ülesehitus
#-----------------------
class App(customtkinter.CTk):
    def __init__(self):
        #Algse frame parameetrid
        super().__init__()
        self.title("Projekt Dula")
        self.geometry("1000x700")
        
        #Frame sisene ülesehitus, 1 rida ja 2 veergu
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        #Kõrvalmenüü ülesehitus, 1 rida ja 1 veerg 
        self.navigation = KõrvalMenüü(self, controller=self)
        self.navigation.grid(row=0, column=0, sticky="nesw")

        #Kõrvalmenüü valikute ülesehitus
        self.Harjumused_frame = Harjumused_frame(self, controller=self)
        self.Statistika_frame = Statistika_frame(self, controller=self)
        self.Treening_frame = Treening_frame(self, controller=self)
        self.Harjumused_frame.grid(row=0, column=1, sticky="nsew")
        self.Statistika_frame.grid(row=0, column=1, sticky="nsew")
        self.Treening_frame.grid(row=0, column=1, sticky="nsew")

        
class KõrvalMenüü(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        #Kõrvalmenüü parameetrid
        super().__init__(parent)
        
        #self.controller = controller laseb kasutada frame, mis said loodud App klassis
        self.controller = controller
        self.configure(fg_color = "grey15")
        
        title = customtkinter.CTkLabel(self, text = "Navigatsioon", anchor = "center", font=("Arial", 20))
        title.grid(row = 0, column = 0, padx =(20, 20))
        
        #Kõrvalmenüü nupud
        harjumus_nupp = customtkinter.CTkButton(self, text = "Harjumused", anchor = "center", fg_color = "transparent",
                                                border_color = "#3B8ED0", border_width=2, command=self.harjumus_nupp_event)
        harjumus_nupp.grid(row=1, column=0, padx=(20, 20), pady=(15,15))
        
        statistika_nupp = customtkinter.CTkButton(self,text="Statistika", anchor="center", fg_color="transparent",
                                                  border_color="#3B8ED0", border_width=2, command=self.statistika_nupp_event)
        statistika_nupp.grid(row=2, column=0, padx=(20, 20), pady=(15,15))
        
        treening_nupp = customtkinter.CTkButton(self,text="Treening", anchor="center", fg_color="transparent",
                                                  border_color="#3B8ED0", border_width=2, command=self.treening_nupp_event)
        treening_nupp.grid(row=3, column=0, padx=(20, 20), pady=(15,15))

#Kõrvalmenüü nuppude funktsioonid, kutsuvad välja App klassi child framed
    def harjumus_nupp_event(self):
        self.controller.Harjumused_frame.tkraise()
    def statistika_nupp_event(self):
        self.controller.Statistika_frame.tkraise()
    def treening_nupp_event(self):
        self.controller.Treening_frame.tkraise()

#------------------------------------
#Harjumuse frame ja selle alam framed
#------------------------------------
class Harjumused_frame(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        harjumus_nupp_täna = customtkinter.CTkButton(self, text = "Täna", anchor = "center", fg_color = "transparent",
                                                     border_color = "#3B8ED0", border_width=2,
                                                     command=self.harjumus_nupp_täna_event)
        harjumus_nupp_täna.grid(row=0, column=0, padx=(20, 20), pady=(15,15))
        
        harjumus_nupp_ülevaade = customtkinter.CTkButton(self, text = "Ülevaade", anchor = "center", fg_color = "transparent",
                                                         border_color = "#3B8ED0", border_width=2,
                                                         command=self.harjumus_nupp_ülevaade_event)
        harjumus_nupp_ülevaade.grid(row=0, column=1, padx=(20, 20), pady=(15,15))
        
        self.täna_frame = Harjumused_täna_frame(self)
        self.ülevaade_frame = Harjumused_ülevaade_frame(self)
        self.täna_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.ülevaade_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")
        
    def harjumus_nupp_täna_event(self):
        self.täna_frame.tkraise()
    def harjumus_nupp_ülevaade_event(self):
        self.ülevaade_frame.tkraise()

class Harjumused_täna_frame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Frame ülesehitus, 2 rida ja 3 veergu, uniformile väärtuse andmine teeb veerud ühtsete mõõtmetega
        self.grid_columnconfigure(0, weight=1, uniform="veerg")
        self.grid_columnconfigure(1, weight=1, uniform="veerg")
        self.grid_columnconfigure(2, weight=2, uniform="veerg")  # viimane veerg on 2x laiem kui teised
        self.grid_rowconfigure(1, weight=1) # 2. rida võtab kõik vaba ruumi enda alla
        
        self.lisa_nupp = customtkinter.CTkButton(self, text="Lisa harjumus", command=self.lisa_harjumus)
        self.lisa_nupp.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
        
        self.kustuta_nupp = customtkinter.CTkButton(self, text="Kustuta harjumus", command = self.kustuta_nupp__event)
        self.kustuta_nupp.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")
        
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Sisesta harjumuse nimi")
        self.entry.grid(row=0, column=2, padx=20, pady=(20, 10), sticky="nsew")
        self.vaikimisi_värv = self.entry.cget("placeholder_text_color") # Salvestab praeguse värvi, et hiljem saaks taastada
        
        # Loob kaks alam akent, mis lähevad kõrvuti
        self.kõik_harjumused_frame = customtkinter.CTkScrollableFrame(self, label_text="harjumused")
        self.kõik_harjumused_frame.grid(row=1, column=0, columnspan = 2, padx=20, pady=10, sticky="nsew")
        self.kõik_harjumused_frame.grid_columnconfigure(0, weight=1)
        
        self.tehtud_harjumused_frame = customtkinter.CTkScrollableFrame(self, label_text="tehtud")
        self.tehtud_harjumused_frame.grid(row=1, column=2, padx=20, pady=10, sticky="nsew")
        self.tehtud_harjumused_frame.grid_columnconfigure(0, weight=1)
        
        self.joonista_harjumused()
        
        
    def kustuta_nupp__event(self):
        # Kui selline harjumus on listis, siis see kustutatakse, kui ei ole tuleb placeholder teksti asemele veateade
        if self.entry.get().strip() in harjumus.harjumuste_list:
            harjumus.kustuta_harjumus(self.entry.get().strip())
            self.entry.delete(0, "end")
            self.focus()
            self.entry.configure(placeholder_text="Sisesta harjumuse nimi", placeholder_text_color=self.vaikimisi_värv)
            self.joonista_harjumused()
        else:
            self.entry.delete(0, "end")
            self.focus()
            self.entry.configure(placeholder_text="Sellist harjumust ei ole", placeholder_text_color="red")
        
                
    def lisa_harjumus(self, event=None):
        # Kui harjumuse välja pole midagi kirjutatud, ei tee funktsioon midagi
        nimi = self.entry.get().strip()
        if not nimi:
            return

        # Võrdleb kas harjumus on juba olemas, kui on, muudab entry placeholder teksti veateateks, kui ei ole, lisab listi
        if nimi.lower() in [h.lower() for h in harjumus.harjumuste_list]:
            self.entry.delete(0, "end")
            self.focus()
            self.entry.configure(placeholder_text="See harjumus on juba olemas!", placeholder_text_color="red")
        else:
            harjumus.harjumuste_list.append(nimi)
            self.entry.delete(0, "end")
            self.focus()
            self.entry.configure(placeholder_text="Sisesta harjumuse nimi", placeholder_text_color=self.vaikimisi_värv)
            self.joonista_harjumused()
            
    def muuda_kas_tehtud(self, name):
        # Kui harjumus ei olnud enne täidetute listis, lisab sinna, muidu võtab ära
        harjumus.vaheta_täidetud(name, datetime.today().strftime('%Y-%m-%d'))
        self.joonista_harjumused()
            
    def joonista_harjumused(self):
        # Hävitab vanad widgetid ja loob uued listi järgi
        for widget in self.kõik_harjumused_frame.winfo_children():
            widget.destroy()

        # Tekitab listi rows[(index, harjumuse_nimi)]
        rows = list(enumerate(harjumus.harjumuste_list))
        
        # tekitab igas rows harjumuse nime ja nupu, mis kutsub välja muuda_kas_tehtud()
        for row, (index, (name)) in enumerate(rows):
            name_label = customtkinter.CTkLabel(self.kõik_harjumused_frame, text=name, anchor="w")
            name_label.grid(row=row, column=0, padx=(5, 10), pady=2, sticky="ew")

            remove_button = customtkinter.CTkButton(self.kõik_harjumused_frame, text="Muuda", width=70,
                                                    command=lambda name=name: self.muuda_kas_tehtud(name))
            remove_button.grid(row=row, column=2, padx=(0, 5), pady=2)
        
        # Hävitab vanad widgetid ja loob uued listi järgi
        for widget in self.tehtud_harjumused_frame.winfo_children():
            widget.destroy()
        
        # Tekitab listi rows[(index, harjumuse_nimi)]
        rows = list(enumerate(harjumus.täidetud_list))

        # tekitab igas rows harjumuse nime ja nupu, mis kutsub välja muuda_kas_tehtud()
        for row, (index, (name, time)) in enumerate(rows):
            name_label = customtkinter.CTkLabel(self.tehtud_harjumused_frame, text=name, anchor="w")
            name_label.grid(row=row, column=0, padx=(5, 10), pady=2, sticky="ew")

            remove_button = customtkinter.CTkButton(self.tehtud_harjumused_frame, text="Muuda", width=70,
                                                    command=lambda name=name: self.muuda_kas_tehtud(name))
            remove_button.grid(row=row, column=2, padx=(0, 5), pady=2)


class Harjumused_ülevaade_frame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        # Loob 8x8 gridi, kuhu kalender tekitada
        for veerg in range(8):
            self.grid_columnconfigure(veerg, weight=1, uniform="veerg")
        for rida in range(8):
            self.grid_rowconfigure(rida, weight=1, uniform="rida")
            
        # Salvestab aasta ja kuu, hetkel ainult praegused
        self.aasta = datetime.today().strftime('%Y')
        self.kuu = datetime.today().strftime('%m')
        
        self.päeva_labelid = []  # Tekitab tühja listi, kuhu tekitan päevade widgetid kalendris
        
        # Ülemine valikriba: aasta, kuu ja harjumuse valikuga
        self.päis = customtkinter.CTkFrame(self, fg_color="transparent")
        self.päis.grid(row=0, column=0, columnspan=8, sticky="ew", padx=20, pady=(10, 0))
        self.päis.grid_columnconfigure(0, weight=1)

        self.kuu_label = customtkinter.CTkLabel(self.päis, text=self.aasta+"-"+self.kuu)
        self.kuu_label.grid(row=0, column=0, sticky="ew")

        self.harjumus_valik = customtkinter.CTkOptionMenu(self.päis, values=["-"], command=self.muuda_harjumus)
        self.harjumus_valik.grid(row=0, column=1, sticky="ew")
        
        # Loob kalendri ja kontrollib mis päevadel valitud harjumus on täidetud
        self.nädalapäevad()
        self.uuenda_päevad_nädalas()
        
    # 
    def nädalapäevad(self):
        nädalapäevad = ("E", "T", "K", "N", "R", "L", "P",)
        for i in range (0, 7):
            label = customtkinter.CTkLabel(self, text=nädalapäevad[i])
            label.grid(row=1, column=1+i)
    
    # Funktsioon mida kutsutakse välja iga kord kui mõni valikutest muudetakse, hetkel kuud muuta ei saa
    def uuenda_päevad_nädalas(self):
            global nädalad
            # Loob kaheastmelise listi selle aasta selle kuu nädalate ja nende päevadega stiilis [[0, 0, 1, 2, 3, 4, 5][6, 7, 8, 9, 10, 11, 12]], kui päev on 0, siis see ei ole selle kuu päev
            nädalad = calendar.monthcalendar(int(self.aasta), int(self.kuu))
            
            # Puhastab akna vanadest widgetitest
            for label in self.päeva_labelid:
                label.destroy()
            self.päeva_labelid.clear()
            
            # tekitab uued widgetid, salvestab rea ja veeru eraldi, et saaks seda positsioneerida
            for rida, nädal in enumerate(nädalad, start=2):
                for veerg, päev in enumerate(nädal, start=1):
                    if päev != 0:
                        # tekitab widgetid ilma .grid()-ita
                        if harjumus.kas_täidetud(self.harjumus_valik.get(), self.aasta+"-"+self.kuu+"-"+str(päev)):
                            uus_label = customtkinter.CTkLabel(self, text=str(päev), fg_color="green")
                        else:
                            uus_label = customtkinter.CTkLabel(self, text=str(päev), fg_color="red")
                            
                        #Tekitab widgetitile .grid()-i
                        uus_label.grid(row=rida, column=veerg, sticky="nsew", padx=2, pady=2)
                        
                        # Salvestab widgetid listi, et saaks hiljem muuta või kustutada
                        self.päeva_labelid.append(uus_label)
                        
    # Kutsutakse välja kui dropdown menüüs uus valik tehakse
    def muuda_harjumus(self, valik):
        self.uuenda_päevad_nädalas()
                    
    def tkraise(self):
        # Koostab listi kõikidest harjumuste nimedest
        harjumused = []
        for harjumus1 in harjumus.anna_harjumused():
            if harjumus1 not in harjumused:
                harjumused.append(harjumus1)

        # Kui harjumusi pole, näitab ainult "-"
        if len(harjumused) == 0:
            harjumused = ["-"]

        # Uuendab rippmenüü valikud
        self.harjumus_valik.configure(values=harjumused)

        # Kui praegu valitud harjumust enam listis pole, valib esimese
        if self.harjumus_valik.get() not in harjumused:
            self.harjumus_valik.set(harjumused[0])
            self.uuenda_päevad_nädalas()

        # Toob frame nähtavale
        super().tkraise()
        
#------------------------------------
#Treening frame ja selle alam framed
#------------------------------------
        
class Treening_frame(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Frame ülesehitus, 6 veergu ja 3 rida
        self.grid_columnconfigure(0, weight=1, uniform="veerg")
        self.grid_columnconfigure(1, weight=1, uniform="veerg")
        self.grid_columnconfigure(2, weight=1, uniform="veerg")
        self.grid_columnconfigure(3, weight=1, uniform="veerg")
        self.grid_columnconfigure(4, weight=1, uniform="veerg")
        self.grid_columnconfigure(5, weight=2, uniform="veerg")
        self.grid_rowconfigure(2, weight=1)
        
        #Salvestusel tekkivate errorite kuvamise label
        self.viga_label = customtkinter.CTkLabel(self, text="", text_color="red")
        self.viga_label.grid(row=3, column=0, columnspan=6, pady=(0, 10))
        
        # Tekitab tekstiväljad
        self.kuupäev_entry = customtkinter.CTkEntry(self, placeholder_text="Kuupäev")
        self.kuupäev_entry.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")

        self.harjutus_entry = customtkinter.CTkEntry(self, placeholder_text="Harjutus")
        self.harjutus_entry.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="nsew")

        self.raskus_entry = customtkinter.CTkEntry(self, placeholder_text="Raskus")
        self.raskus_entry.grid(row=0, column=2, padx=20, pady=(20, 10), sticky="nsew")

        self.kordused_entry = customtkinter.CTkEntry(self, placeholder_text="Kordused")
        self.kordused_entry.grid(row=0, column=3, padx=20, pady=(20, 10), sticky="nsew")

        self.seeriad_entry = customtkinter.CTkEntry(self, placeholder_text="Seeriad")
        self.seeriad_entry.grid(row=0, column=4, padx=20, pady=(20, 10), sticky="nsew")

        self.komentaar_entry = customtkinter.CTkEntry(self, placeholder_text="Lisa komentaar")
        self.komentaar_entry.grid(row=1, column=0, columnspan=5, padx=20, pady=(20, 10), sticky="nsew")
        
        #Iga klahvivajutusel kohustuslike tekstiväljade sees, jooksutab chech_input funktsiooni
        for entry in (self.kuupäev_entry, self.harjutus_entry, self.raskus_entry,
                      self.kordused_entry, self.seeriad_entry):
            entry.bind("<KeyRelease>", self.check_input)

        # Loob tühista nupu, see kutsub välja tühista_nupp_event(), kui vajutada
        self.tühista_nupp = customtkinter.CTkButton(self, text="Tühista", command=self.tühista_nupp_event)
        self.tühista_nupp.grid(row=0, column=5, padx=20, pady=10, sticky="nsew")
        
        # Loob tühista nupu, see kutsub välja salvesta_nupp_event(), kui vajutada
        self.salvesta_nupp = customtkinter.CTkButton(self, text="Salvesta", state="disabled",command=self.salvesta_nupp_event)
        self.salvesta_nupp.grid(row=1, column=5, padx=20, pady=10, sticky="nsew")
        
        # Loob tühista nupu, see kutsub välja kustuta_nupp_event, kui vajutada
        self.kustuta_nupp = customtkinter.CTkButton(self, text="Kustuta", command=self.kustuta_nupp_event)
        self.kustuta_nupp.grid(row=2, column=5, padx=20, pady=10, sticky="new")
        
        # Loob alamakna ajalugu, kuhu tekitame kõik varasemad harjutused ajaliselt uuemas järjekorras
        self.ajalugu_frame = Ajalugu_frame(self, label_text="Ajalugu", values=treening.treeningute_list)
        self.ajalugu_frame.grid(row=2, column=0, columnspan = 5, padx=20, pady=10, sticky="nsew")
        
    def salvesta_nupp_event(self):
        #tekitab kõigi tekstiväljade sisuga listi ja kutsub sellega välja lisa_treening funtsiooni
        väärtused = [entry.get().strip() for entry in (self.kuupäev_entry, self.harjutus_entry, self.raskus_entry,
                                                       self.kordused_entry, self.seeriad_entry, self.komentaar_entry)]
        
        viga = treening.lisa_treening(*väärtused)
        #Kui tekib viga, kuvab seda viga_label-lis ja lõpetame funktsiooni
        if viga:
            self.viga_label.configure(text=viga)
            return
        #kui viga ei teki, kustutame veateate, uuendame ajaloo frame, puhastame tekstiväljad ja kutsub check_inputi, et salvestusenupu olekut uuendada
        self.viga_label.configure(text="")
        self.ajalugu_frame.uuenda(treening.treeningute_list)
        self.tühista_nupp_event()
        self.check_input()   
        
        
    def check_input(self, *args):
        # Kontrollib, et igas kohustuslikus tekstiväljas oleks midagi kirjas, kuni ei ole, on salvesta nupp disabled
        entries = (self.kuupäev_entry, self.harjutus_entry, self.raskus_entry,
               self.kordused_entry, self.seeriad_entry)

        kõik_täidetud = all(entry.get().strip() != "" for entry in entries)
        self.salvesta_nupp.configure(state="normal" if kõik_täidetud else "disabled")
        
    def tühista_nupp_event(self):
        # Tühistab kõik tekstiväljad, kui nendesse on midagi kirjutatud
        for entry in (self.kuupäev_entry, self.harjutus_entry, self.raskus_entry,
                      self.kordused_entry, self.seeriad_entry, self.komentaar_entry):
            tekst = entry.get()
            if tekst and tekst != entry.cget("placeholder_text"):
                entry.delete(0, "end")
        self.focus()
        self.check_input()
        
    def kustuta_nupp_event(self):
        # Kustutab valitud checkboxidega harjutused, uuendab ajaloo frame
        valitud = []
        for i, box in enumerate(self.ajalugu_frame.checkboxes):
            if box.get() == 1:
                valitud.append(i)
        for i in reversed(valitud):
            treening.kustuta_treening(i)
        self.ajalugu_frame.uuenda(treening.treeningute_list)
            
        
class Ajalugu_frame(customtkinter.CTkScrollableFrame): # CTkScrollableFrame Lisab scrollbari ja laseb elementidel minna framest välja
    def __init__(self, master, label_text, values):
        super().__init__(master, label_text=label_text)
        # Ajaloo klassi frame ülesehitus - üks suur veerg, kus sees on checkboxide loend
        self.grid_columnconfigure(0, weight=1)
        self.checkboxes = []
        
        for value in values:  # Tekitab checkboxi igale loendis olevale elemendile
            self.add_checkbox(value)

    def add_checkbox(self, value): # Tekitab checkboxi, mis kuvab sisseantud sõnastikku ilusalt, kutsudes iga elemendi eraldi välja
        tekst = (f"{value['kuupäev']}  {value['harjutus']}  "
                 f"{value['raskus']} kg  {value['kordused']}x{value['seeriad']}")
        checkbox = customtkinter.CTkCheckBox(self, text=tekst)
        checkbox.grid(row=len(self.checkboxes), column=0, padx=10, pady=(10, 0), sticky="w") 
        self.checkboxes.append(checkbox) # Lisab loendisse
    
    def uuenda(self, values): # Hävitab kõik elemendid listis ja loob uuesti add_checkbox() fuktsiooniga
        for checkbox in self.checkboxes:
            checkbox.destroy()
        self.checkboxes.clear()
        for value in values:
            self.add_checkbox(value)
        
        
#------------------------------------
#Statistika frame
#------------------------------------
        
class Statistika_frame(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid_columnconfigure(0, weight=1) # üks veerg
        self.grid_rowconfigure(1, weight=1) # 2 rida

        # Tekitab ülemise valikuriba esimesse ritta
        riba = customtkinter.CTkFrame(self, fg_color="transparent")
        riba.grid(row=0, column=0, sticky="ew", padx=20, pady=(20, 10))
        
        # Tekitab dropdown menüü, algväärtusega "-"
        self.harjutus_valik = customtkinter.CTkOptionMenu(riba, values=["-"])
        self.harjutus_valik.grid(row=0, column=0, padx=(0, 10))
        
        # Tekitab nupu, mis kutsub välja näita_raskus funktsiooni
        self.raskus_nupp = customtkinter.CTkButton(riba, text="Raskus", width=100,
                                                   command=self.näita_raskus)
        self.raskus_nupp.grid(row=0, column=1, padx=5)
        # Tekitab nupu, mis kutsub välja näita_nädalaid funktsiooni
        self.nädalad_nupp = customtkinter.CTkButton(riba, text="Nädalad", width=100,
                                                    command=self.näita_nädalaid)
        self.nädalad_nupp.grid(row=0, column=2, padx=5)
        # Tekitab nupu, mis kutsub välja näita_harjumusi funktsiooni
        self.harjumused_nupp = customtkinter.CTkButton(riba, text="Harjumused", width=100,
                                                       command=self.näita_harjumusi)
        self.harjumused_nupp.grid(row=0, column=3, padx=5)
        # Tekitab nupu, mis kutsub välja näita_arengut funktsiooni
        self.areng_nupp = customtkinter.CTkButton(riba, text="Areng", width=100,
                                                  command=self.näita_arengut)
        self.areng_nupp.grid(row=0, column=4, padx=5)

        # Loon charti ekraani
        self.fig = Figure(figsize=(5, 4), dpi=100) # Tekitab algse ekraani tollides, annab iga tolli väärtuseks 100 pikslit
        self.ax = self.fig.add_subplot(111) # Lisab joonistusala, 111 - 1 rida, 1 veerg, esimene ala
        self.canvas = FigureCanvasTkAgg(self.fig, master=self) # Ühendab matplotlibi paberilehe tkinteri aknaga.
        self.canvas.get_tk_widget().grid(row=1, column=0, sticky="nsew", padx=20, pady=10) # Tekitab sellest widgeti

        # Veateate tekstiriba
        self.teade_label = customtkinter.CTkLabel(self, text="", text_color="red")
        self.teade_label.grid(row=2, column=0, pady=(0, 10))

    def tkraise(self):
        # Koostame listi kõikidest harjutuste nimedest
        harjutused = []
        for üks_treening in treening.anna_treeningud():
            if üks_treening["harjutus"] not in harjutused:
                harjutused.append(üks_treening["harjutus"])

        # Kui harjutusi pole, näitame ainult "-"
        if len(harjutused) == 0:
            harjutused = ["-"]

        # Uuendame rippmenüü valikud
        self.harjutus_valik.configure(values=harjutused)

        # Kui praegu valitud harjutust enam listis pole, valime esimese
        if self.harjutus_valik.get() not in harjutused:
            self.harjutus_valik.set(harjutused[0])

        # Toome frame nähtavale
        super().tkraise()

    # Valikuriba funktsioonid
    def näita_raskus(self):
        self.joonista(statistika2.näita_raskuse_graafikut, self.harjutus_valik.get())
        
    def näita_nädalaid(self):
        self.joonista(statistika2.näita_nädalate_graafikut)

    def näita_harjumusi(self):
        self.joonista(statistika2.näita_harjumuste_graafikut)

    def näita_arengut(self):
        self.joonista(statistika2.näita_üldise_arengu_graafikut)
    
    # Kustutab vana graafiku ja joonistab uue
    def joonista(self, funktsioon, *args):
        self.ax.clear() # Kustutame eelmise graafiku
            # Käivitame valitud graafikufunktsiooni ja anname talle joonistusala (self.ax).
            # Funktsioon joonistab sinna ja tagastab "" (kõik OK) või veateate teksti.
        teade = funktsioon(self.ax, *args)
        self.teade_label.configure(text=teade) # Väljastab veateate, kui on
        if not teade:
            self.fig.tight_layout() # Sätib graafiku layouti, et see ei jääks äärte taha
        self.canvas.draw() # Joonistab uue canvase


app = App()
app.mainloop()

