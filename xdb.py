import os
import json


def find_matching_name(target_name):
    root_directory = '../xdb/titles'

    for root, _, files in os.walk(root_directory):
        for filename in files:
            if filename == 'info.json':
                file_path = os.path.join(root, filename)
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)
                    if data.get('name') == target_name:
                        return data.get('title_id')

    return None


target_name = "Ninja Gaiden Black"

matching_data = find_matching_name(target_name)

if matching_data:
    print("Matching data found:", matching_data)
else:
    print("No matching data found.")

