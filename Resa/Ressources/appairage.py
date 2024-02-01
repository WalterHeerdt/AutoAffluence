import json

def load_data_from_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def modify_keys(data):
    modified_data = {}
    for key, value in data.items():
        modified_key = key.split()[-1]
        if modified_key in modified_data:
            print(f"Collision detected: {key} -> {modified_key} (Existing ID: {modified_data[modified_key]}, New ID: {value})")
        modified_data[modified_key] = value
    return modified_data

# Chemin vers votre fichier JSON source
source_file_path = '/Users/leo/Document/Addon/Resa/Ressources/ressources.json'

# Charger les données depuis le fichier JSON source
data = load_data_from_json(source_file_path)

# Modifier les clés pour ne garder que le numéro de la place
modified_data = modify_keys(data)

# Afficher le nombre de valeurs avant et après la modification
print(f"Nombre de valeurs avant la modification : {len(data)}")
print(f"Nombre de valeurs après la modification : {len(modified_data)}")
