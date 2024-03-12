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

current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"Current time: {current_time}")

# Liste de triples email-token-ID
email_token_id_triples = [
    ('leo.rocheteau1@etu.univ-nantes.fr', '01bfc060-fb6c-4726-9bec-e012608f5a1c', '49142'), 
    # Expiration: "2024-04-01"
    ('sixtine.audousset@etu.univ-nantes.fr', '99092a1a-a473-420c-a5fc-5853897490e7', '49128'),
    # Expiration: "2024-03-06"
    ('clarisse.lubrano@etu.univ-nantes.fr', 'ab271895-d8d8-4225-9dc5-b2c24f312a02', '49129'),
    # Expiration: "2024-03-07"
    ('louis.savaete@etu.univ-nantes.fr', '98f40772-132e-4102-8a18-60cbff09ad60', '49127'),
    # Expiration: "2024-03-07"
    ('alban.rousseau@etu.univ-nantes.fr', '48d7addc-6240-4dc7-8f77-a8eb02f3ee84', '49139'),
    # Expiration: "2024-04-05"
    ('louise.beaugendre@etu.univ-nantes.fr', 'a1af5a5a-fa07-4b06-9ed8-3c51c50957e6', '49141'),
    # Expiration: "2024-04-11"
    ('margaux.ouertal@etu.univ-nantes.fr', 'fb20d9e3-4c63-4483-9cf2-1096eeb1c8a5', '49137'),
    # Expiration: "2024-03-09"
    ('castille.de-lavenne-de-la-montoise@etu.univ-nantes.fr', 'c61fa463-1dae-4354-900d-c2da142099f5', '49140'),
    # Expiration: "2024-03-22"
    ('iklil.el-makhzoumi@etu.univ-nantes.fr', 'b444a245-d6af-42c6-9042-78c599d10176', '49143'),
    # Expiration: "2024-04-05"

]

person_count = 1

# Effectuer les réservations pour chaque triple
for start_time, end_time in [('10:00', '14:00'), ('14:30', '18:30'), ('19:00', '22:00')]:
    send_reservation_requests(email_token_id_triples, start_time, end_time, person_count)
