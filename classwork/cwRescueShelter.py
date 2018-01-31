class Rescue:
    idnumber = 0
    def __init__(self, name, species = "Dog"):
        Animal.idnumber += 1
        self.id = Rescue.idnumber
        self.name = name
        self.species = species
        self.arrivaldate = time.strftime("%d/%m/%Y")
        self.adoptiondate = ""

    def adoptiondate(self, date):
        self.adoptiondate = date

    def __str__(self):
        animalstr = "Name: " + str(self.name) + " Type: " + str(self.species) + " ID: " + str(self.idnumber) + " Arrival Date: " + arrivaldate + " Adoption Date: " + adoptiondate
        return animalstr
