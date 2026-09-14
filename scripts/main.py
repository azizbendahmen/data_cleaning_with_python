from drill_utils import convert_miles_to_meters, convert_date_to_iso, ajout_contact_information, format_machine_id
import json

file_to_read = "drilling_machine1.json"
file_to_write = f"Updated_{file_to_read}"


with open(file_to_read, "r") as file:
    drill_machine_data = json.load(file)
    
if "miles" in drill_machine_data["specifications"].keys():
    drill_machine_data = convert_miles_to_meters(drill_machine_data)

updated_machine = convert_date_to_iso(drill_machine_data)

if "contact_information" not in updated_machine.keys():
    updated_machine = ajout_contact_information(updated_machine)
    
if "machine_id" in updated_machine.keys():
    updated_machine = format_machine_id(updated_machine)

print(updated_machine)

with open(file_to_write, "w") as file:
    json.dump(updated_machine, file)
