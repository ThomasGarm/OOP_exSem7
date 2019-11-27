class city:
    def __init__(self, name, departement):
        self.name = name
        self.departement = departement

    def show_location(self):   
        return ("la ville {} est dans le département {}.".format(self.name, self.departement))

    def change_location(self):
        Roubaix = city("Roubaix", 59100)
        return "Poor guy, you move to {} in district {}. :(".format(Roubaix.name, Roubaix.departement)