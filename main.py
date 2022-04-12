import os
import json

input_file_path: str = os.getenv("INPUT_FILE", "input.json")

with open(input_file_path, 'r') as f:
    app_settings: list = json.loads(f.read())
print (f"Input succeessfully read from {input_file_path}")

return_list = []

def iterate_dict(input: dict, parent_key: str = None) -> list:
    for key, value in input.items():
        key_with_parent = f"{parent_key}__{key}" if parent_key is not None else key
        if type(value) == dict:
            iterate_dict(value, key_with_parent)
        else:
            return_list.append({
                'name': key_with_parent,
                'value': value,
                'slotSetting': False
            })



iterate_dict(app_settings)
print("Parsed successfully")
print ("Writing output to output.json")

with open('output.json', 'w') as of:
    of.writelines(json.dumps(return_list))

print("Done!")
        

