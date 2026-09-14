import json
from drill_utils import (convert_miles_to_meters, convert_dates, add_contact_info, format_machine_id , remove_useless_data) 


# expected_keys = [
#     "machine_id",
#     "machine_ID",
#     "name",
#     "location",
#     "status",
#     "specifications",
#     "last_maintenance_date",
#     "next_maintenance_due",
#     "contact_information",
# ]


# keys_to_remove = []

# for i in range(5):
#     file_name = f"data/raw/drilling_machine{i+1}.json"
#     with open(file_name, "r") as f:
#         data = json.load(f)
#         for key in data.keys():
#             if key not in expected_keys:
#                 keys_to_remove.append(key)
                
#         for key in keys_to_remove:
#                 del data[key]
#         print(data)
        


files = [
    "drilling_machine1.json",
    "drilling_machine2.json",
    "drilling_machine3.json",
    "drilling_machine4.json",
    "drilling_machine5.json",
]


for file_name in files:
    input_path = f"data/raw/{file_name}"
    output_path = f"data/processed/{file_name}"
    
    with open (input_path , "r") as f :
        data = json.load(f)
        
        
    processed_data = remove_useless_data(data)
    
    if "miles" in processed_data["specifications"].keys():
        processed_data = convert_miles_to_meters(processed_data)
        
        
    processed_data = convert_dates(processed_data)
    
    if "contact_information" not in processed_data.keys():
        processed_data = add_contact_info(processed_data)

    if "machine_id" in processed_data.keys() or "machine_ID" in processed_data.keys():
        processed_data = format_machine_id(processed_data)
    
    with open (output_path , "w") as f:
        json.dump(processed_data , f)
        
        



