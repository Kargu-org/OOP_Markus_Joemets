class Koer:
 # klassimuutuja
    nimi = "Mingi nimi"

    def __init__(self, uus_nimi):
        Koer.nimi = uus_nimi

    def haugu(self):
        print(self.nimi + " Ütleb: Woofh")
    def veere(self):
        print(self.nimi + " *Veereb*")
    def tervita(self):
        print(self.nimi + " *Annab käppa*")
    def raagi(self):
        print("????")
 # Tagastab koera nime, mis on objekti talletatud
    def get_name(self):
        return self.nimi
 # Tagastab viite objektile.
    def get_this_dog(self):
        return self
# Loome Koer klassi alusel objekti ja talletame ta muutujasse Muri
Koer1 = Koer("Muri")
Koer1.haugu()
Koer1.veere()
Koer1.tervita()
Koer1.raagi()
print(Koer1.get_name())
print(Koer1.get_this_dog())
print(Koer1)
# Loome veel ühe objekti klassi Koer baasil ning talletame
#muutujasse Rex
Koer2 = Koer("Rex")
Koer2.haugu()
Koer2.veere()
print(Koer2.get_name())
print(Koer2.get_this_dog())
print(Koer2)