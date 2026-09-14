from typing import Dict


def convert_miles_to_meters(machine: dict) -> dict:
    """Convert miles to meters."""
    specs = machine["specifications"]
    
    depth_capacity_miles = specs["depth_capacity_miles"]
    specs["depth_capacity_meters"] = depth_capacity_miles * 1609.34
      
    drilling_speed_miles_per_day = specs["drilling_speed_miles_per_day"]
    specs["drilling_speed_meters_per_day"] = drilling_speed_miles_per_day * 1609.34
    
    
    del specs["depth_capacity_miles"]
    del specs["drilling_speed_miles_per_day"]
    
    return machine


def convert_date_to_iso(machine: dict) -> dict:
    """Convert date strings to ISO format."""
    
    last_maintenance_date = machine["last_maintenance_date"]
    cleaned_last_maintenance_date = last_maintenance_date.split("-")
    day , month , year = cleaned_last_maintenance_date[2], cleaned_last_maintenance_date[1], cleaned_last_maintenance_date[0]
    machine["last_maintenance_date"] = f"{day}/{month}/{year}"
    
    next_maintenance_due = machine["next_maintenance_due"]
    cleaned_next_maintenance_due = next_maintenance_due.split("-")
    day , month , year = cleaned_next_maintenance_due[2], cleaned_next_maintenance_due[1], cleaned_next_maintenance_due[0]
    machine["next_maintenance_due"] = f"{day}/{month}/{year}"
    
    return machine


def ajout_contact_information(machine : dict) -> dict:
    """Add contact information to the machine data."""
    
    machine["contact_information"] = {
        "operator_company": None ,
        "contact_person": None,
        "phone": None,
        "email": None
      }
    return machine
  
  
def format_machine_id(machine: dict) -> dict:
    """Format the machine ID to a specific pattern."""
    
    id_alp , id_num = machine["machine_id"].split("-")
    id_num_padded = id_num.zfill(3)
    cleaned_machine_id = f"{id_alp}-{id_num_padded}"
    machine["machine_id"] = cleaned_machine_id
    return machine



