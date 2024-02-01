import requests
from datetime import datetime, timezone, timedelta
import json
import urllib.parse

# Token d'autentification
def decode_token(encoded_token):
    # Vérifie si le token encodé est vide
    if not encoded_token.strip():
        raise ValueError("Le token encodé est vide. Veuillez réessayer.")
    
    # Décode le token encodé en URL
    decoded_json = urllib.parse.unquote(encoded_token)
    
    # Vérifie si le JSON décodé est valide
    try:
        return json.loads(decoded_json)
    except json.JSONDecodeError as e:
        raise ValueError("Le token décodé n'est pas un JSON valide. Veuillez vérifier et réessayer.") from e
def is_token_expired(token_info):
    # Vérifie si le token est expiré
    expiration_datetime = datetime.strptime(token_info[0]['expiration'], "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=None)
    return expiration_datetime < datetime.now()
def get_user_device_token():
    # Essayez de lire le token et la date d'expiration depuis un fichier
    try:
        with open('token_info.json', 'r') as file:
            token_info = json.load(file)
            if not is_token_expired(token_info):
                return token_info[0]['token']
            else:
                raise ValueError("Token expired")
    except (FileNotFoundError, ValueError):
        # Demande à l'utilisateur de coller le token encodé si non trouvé ou expiré
        encoded_token = input("Copier coller le 'AffluencesTrustedDeviceToken' trouvé dans les cookies : ")
        token_info = decode_token(encoded_token)
        # Stocke le token et la date d'expiration dans un fichier pour une utilisation ultérieure
        with open('token_info.json', 'w') as file:
            json.dump(token_info, file)
        return token_info[0]['token']


def load_place_resource_pairs(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def send_reservation_request(place_number, start_time, end_time, person_count, email, user_device_token, place_resource_pairs):
    date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    print(date)

    # Obtenez l'ID de ressource correspondant au numéro de place
    resource_id = place_resource_pairs.get(place_number)
    if not resource_id:
        print(f"No resource ID found for place number '{place_number}'")
        return

    payload = {
        "auth_type": None,
        "email": email,
        "date": date,
        "start_time": start_time,
        "end_time": end_time,
        "note": None,
        "user_firstname": None,
        "user_lastname": None,
        "user_phone": None,
        "person_count": person_count,
        "user_device_token": user_device_token
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "fr",
        "Content-Type": "application/json",
    }

    url = f"https://reservation.affluences.com/api/reserve/{resource_id}"
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(f"Reservation success for {start_time} to {end_time}: ", response.json())
    else:
        print(f"Reservation failed for {start_time} to {end_time}: ", response.status_code, response.text)

pairs_file_path = '/Users/leo/Document/Addon/Resa/Ressources/ressources.json'
place_resource_pairs = load_place_resource_pairs(pairs_file_path)

# Informations de réservation
email = 'leo.rocheteau1@etu.univ-nantes.fr'
person_count = 1
user_device_token = get_user_device_token()
place_number = "6073"

# Effectuer les réservations pour la date du jour
send_reservation_request(place_number, '10:00', '14:00', person_count, email, user_device_token, place_resource_pairs)
send_reservation_request(place_number, '14:30', '18:30', person_count, email, user_device_token, place_resource_pairs)
send_reservation_request(place_number, '19:00', '22:00', person_count, email, user_device_token, place_resource_pairs)
