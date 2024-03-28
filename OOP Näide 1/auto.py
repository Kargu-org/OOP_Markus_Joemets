class Auto:
    tootja = ""
    mudel = ""
    maxKiirus = 0
    maksumus = 0
    istekohtadeArv = 0
    hetkeKiirus = 0
    
    def valjastaAndmed(self):
        print("Tootja on:", self.tootja, "mudel on", self.mudel, "Hetkekiirus on", self.hetkeKiirus, "km/h", "maksimaalne kiirus", self.maxKiirus, "km/h", "Istekohtade arv", self.istekohtadeArv, "Maksumus on", self.maksumus, "€")
              
    def vahendaKohtadeArvu(self, mituKohta):
        if mituKohta > self.istekohtadeArv:
            print("Eemaldada ei saa rohkem kohti kui autos ")
        else:
            self.istekohtadeArv = self.istekohtadeArv - mituKohta
        
        
    def Kiirenda(self, kuiPalju):
        if self.hetkeKiirus + kuiPalju > self.maxKiirus:
            print("Saavutasin maksimaalse kiiruse.", self.maxKiirus,"km/h", "Rohkem kiirendada ei anna")
            self.hetkeKiirus = self.maxKiirus
        else:
            self.hetkeKiirus = self.hetkeKiirus + kuiPalju
    
    def Pidurda(self, kuiPalju):
        if self.hetkeKiirus - kuiPalju <= 0:
            print("Pidurdasin 0-i rohkem ei anna pidurdada")
            self.hetkeKiirus = 0
        else:
            self.hetkeKiirus = self.hetkeKiirus - kuiPalju
            
autoYks = Auto()
autoKaks = Auto()

autoYks.tootja = "BMW"
autoYks.mudel = "E39"
autoYks.maxKiirus = 250
autoYks.maksumus = 12000
autoYks.istekohtadeArv = 5
autoYks.hetkeKiirus = 90
autoYks.valjastaAndmed()

autoYks.Kiirenda(170)
#autoYks.Pidurda(90)      
autoYks.valjastaAndmed()
#############################
autoKaks.tootja = "Toyota"
autoKaks.mudel = "Corolla"
autoKaks.maxKiirus = 175
autoKaks.maksumus = 150
autoKaks.istekohtadeArv = 5
autoKaks.hetkeKiirus = 45
#autoKaks.valjastaAndmed()

#autoKaks.Kiirenda(135)
#autoKaks.valjastaAndmed()