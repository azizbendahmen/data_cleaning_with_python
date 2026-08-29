from functools import reduce
import csv


donnees_brutes = [
    "Jean, 45, Paris, ACTIF",
    "Marie, 32, Lyon, INACTIF",
    "Pierre, 28, Marseille, ACTIF",
    "Sophie,  , Bordeaux, ACTIF" # Note l'âge manquant
]

final_liste =[]

for donne in donnees_brutes:
    print(donne)
    don=donne.split(",")
    don = [d.strip() for d in don]
    
    nom = don[0]
    age = don[1]
    ville = don[2]
    statut = don[3]
    
    if age =="":
        age = "Âge manquant"
    else : 
        age=int(age)
        
    utilisateur = {
        "nom": nom,
        "age": age,
        "ville": ville,
        "statut": statut
    }
    final_liste.append(utilisateur)
print(final_liste)



drilling_machine_two ={
  "machine_id": "DM-2",
  "name": "Land Rover 200",
  "location": {
    "latitude": 37.7749,
    "longitude": -107.9090,
    "region": "San Juan Basin",
    "country": "USA"
  },
  "status": "Under Maintenance",
  "specifications": {
    "type": "Onshore",
    "depth_capacity_miles": 7,
    "drilling_speed_miles_per_day": 0.3,
    "crew_size": 25,
    "power_source": "Electric"
  },
  "last_maintenance_date": "2024-07-15",
  "next_maintenance_due": "2025-01-15"
}

depth_capacity_miles = drilling_machine_two["specifications"]["depth_capacity_miles"]
depth_capacity_meters = depth_capacity_miles * 1609.34
drilling_machine_two["specifications"]["depth_capacity_meters"] = depth_capacity_meters
drilling_speed_miles_per_day = drilling_machine_two["specifications"]["drilling_speed_miles_per_day"]
drilling_speed_meters_per_day = drilling_speed_miles_per_day * 1609.34
drilling_machine_two["specifications"]["drilling_speed_meters_per_day"] = drilling_speed_meters_per_day


last_maintenance_date = drilling_machine_two["last_maintenance_date"]
x= last_maintenance_date.split("-")
year = x[0]
month = x[1]
day = x[2]
last_maintenance_date_formatted =f"{day}/{month}/{year}"
drilling_machine_two["last_maintenance_date_formatted"] = last_maintenance_date_formatted


next_maintenance_due = drilling_machine_two["next_maintenance_due"]
y = next_maintenance_due.split("-")
next_year = y[0]
next_month = y[1]
next_day = y[2]
next_maintenance_due_formatted = f"{next_day}/{next_month}/{next_year}"
drilling_machine_two["next_maintenance_due"] = next_maintenance_due_formatted


drilling_machine_two["contact_information"] = {
    "operator_company": None,
    "contact_person": None,
    "phone": None,
    "email": None
  }


ch1 = drilling_machine_two["machine_id"][:3]
ch2 = drilling_machine_two["machine_id"][-1].zfill(3)
ch_final = ch1 + ch2
drilling_machine_two["machine_id"] = ch_final


print (drilling_machine_two)


my_list = [1, 2, 3, 4, 5, 6]
new_list=[i*i for i in my_list if (i%2==0) and (i!=6)]

print(new_list)


def my_function(x):
    if x < 0:
        return "Negative"
    elif x == 0:
        return "Zero"
    else:
        return "Positive"
      
print(my_function(10))

def my_func(*x):
    print("Arguments passed:", x)
  
my_func(1, 2, 3, 4, 5)


def my_func2(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")  
        

my_func2(name="Alice", age=30, city="New York")


def addition(a, b):
    return a + b

var = addition(5, 10)
print(var)


add = lambda a, b: a + b
result = add(5, 10) 
print(result)




my_list =[1, 2, 3, 4, 5]

def square (x):
    return x * x

result = list(map(square , my_list))
print(result)



def square2 (x):
    if(x%2==0):
        return x*x
    
    
result2 = list(filter(square2 , my_list))
print(result2)


def add(a, b):
    return a + b

result = reduce(add, my_list)
print(result)  


x = "1"

try:
    if (x<0):
        print("Negative")
    else : 
        print("Positive")
except Exception as e :
    print(f"Error: {e}") 
finally:
    print("Execution completed.")
    


class employee():
    
    company_name = "Tech Solutions Inc."
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def change(self, company_name):
        employee.company_name = company_name

    
    #getter
    @property
    def info(self):
        print(f"Name: {self.name}, Age: {self.age}, Company: {self.company_name}")
    
    #setter
    @info.setter
    def info(self, value):
        self.name = value[0]
        self.age = value[1]
        
        
    
    @classmethod
    def change_company(cls, company_name):
        cls.company_name = company_name
    
    @staticmethod
    def addition(a, b):
        print(a + b)

emp1 = employee("John", 30)
emp1.info
emp2 = employee("Alice", 28)
emp2.change("Innovative Tech Ltd.") 
emp1.info

emp1.addition(5, 10)



emp1.info = ["Bob", 35]
emp1.info



class pere():
    def __int__(self, name):
        self.name = name            
    
    def info(self):
        print(f"Person: {self.name}")
        
        
class fils(pere):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"Person: {self.name}, Age: {self.age}")
    
    def super_info(self):
        super().info()

person1 = fils("Charlie", 25)
person1.info()  
person1.super_info()


# Écriture
chemin_fichier = "C:\\Users\\benda\\Downloads\\mon_pipeline.log\\mon_pipeline.txt"
with open(chemin_fichier, "w") as f:
    f.write("INFO: Début du pipeline.\n")
    f.write("INFO: Ingestion terminée.\n")
# Append
with open(chemin_fichier, "a") as f:
    f.write("INFO: Transformation terminée.\n")
    f.write("INFO: Chargement terminé.\n")
    
# Lecture
with open(chemin_fichier, "r") as f:
    contenu = f.read()
    print(contenu)




donnees_utilisateurs = [
    {"nom": "Alice", "age": 30, "ville": "Paris"},
    {"nom": "Bob",   "age": 25, "ville": "Lyon"}
]

with open("utilisateurs.csv", "w", newline="", encoding="utf-8") as f:
    # On définit les colonnes
    colonnes = ["nom", "age", "ville"]
    # Création de l'objet DictWriter
    writer = csv.DictWriter(f, fieldnames=colonnes)
    writer.writeheader()
    writer.writerows(donnees_utilisateurs)

print("Fichier CSV créé avec succès.")


# Lecture d'un fichier CSV
with open("utilisateurs.csv", "r", encoding="utf-8") as f:
    # Création de l'objet DictReader
    reader = csv.DictReader(f)
    for ligne in reader:
        # Chaque 'ligne' est un dictionnaire.
        print(f"Nom: {ligne['nom']}, Age brut: {ligne['age']} (type: {type(ligne['age'])})")
