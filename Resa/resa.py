import requests
from datetime import datetime, timedelta

def send_reservation_requests(email_token_id_triples, start_time, end_time, person_count):
    # Obtenez la date actuelle formatée en YYYY-MM-DD
    date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')

    headers = {
        "User-Agent": "",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "fr",
        "Content-Type": "application/json",
    }

    for email, user_device_token, reserve_id in email_token_id_triples:
        # Construire l'URL avec l'ID spécifique
        url = f"https://reservation.affluences.com/api/reserve/{reserve_id}"
        
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

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 201:
            print(f"Reservation success for {email} from {start_time} to {end_time} with ID {reserve_id}: ", response.json())
        else:
            print(f"Reservation failed for {email} from {start_time} to {end_time} with ID {reserve_id}: ", response.status_code, response.text)

# Liste de triples email-token-ID
email_token_id_triples = [
    ('leo.rocheteau1@etu.univ-nantes.fr', '36e6ef75-e52c-41cf-8614-ff123b65e06e', '49142'),
    
    # Ajoutez plus de triples email-token-ID ici
]

person_count = 1

# Effectuer les réservations pour chaque triple
for start_time, end_time in [('10:00', '14:00'), ('14:30', '18:30'), ('19:00', '22:00')]:
    send_reservation_requests(email_token_id_triples, start_time, end_time, person_count)
