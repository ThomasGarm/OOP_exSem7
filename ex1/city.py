class City:
    def __init__(self, name, departement):
        self.name = name
        self.departement = departement

    def show_location(self):   
        return ("la ville {} est dans le département {}.".format(self.name, self.departement))

    def change_location(self, name, departement):
        self.name = name
        self.departement = departement
       