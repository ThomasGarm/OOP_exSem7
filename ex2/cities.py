cities = [
    {'name': 'Paris', 'department': 92, 'country': 'France', 'population': 2190327, 'mayor': 'Anne Hidalgo', 'capital': True},
    {'name': 'Lille', 'department': 59, 'country': 'France', 'population': 232440, 'mayor': 'Martine Aubry', 'capital': False},
    {'name': 'Lyon', 'department': 69, 'country': 'France', 'population': 515695, 'mayor': 'Gérard Collomb', 'capital': False},
    {'name': 'Strasbourg', 'department': 67, 'country': 'France', 'population': 279284, 'mayor': 'Rolland Ries', 'capital': False},
]

class City:
    def __init__(self, data_dico):
        self.name = None
        self.department = None
        self.country = None
        self.population = None
        self.mayor = None
        self.capital = None
        self.hydratation(data_dico)

    def hydratation(self, data_dico):
        for key, value in data_dico.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def show_information(self):
       info = "=======================\n name: {}\n departement: {}\n country: {}\n population: {}\n mayor: {}\n capital: {}".format(self.name,
        self.department, self.country, self.population, self.mayor, self.capital)
       print(info) 
            