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

