import requests
from datetime import datetime, timedelta

def send_reservation_request(start_time, end_time, person_count, email, user_device_token):
    # Obtenez la date actuelle formatée en YYYY-MM-DD
    date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')

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

    url = "https://reservation.affluences.com/api/reserve/49143"
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print(f"Reservation success for {start_time} to {end_time}: ", response.json())
    else:
        print(f"Reservation failed for {start_time} to {end_time}: ", response.status_code, response.text)

# Informations de réservation
email = 'leo.rocheteau1@etu.univ-nantes.fr'
user_device_token = '36e6ef75-e52c-41cf-8614-ff123b65e06e'
person_count = 1

# Effectuer les réservations pour la date du jour
send_reservation_request('10:00', '14:00', person_count, email, user_device_token)
send_reservation_request('14:30', '18:30', person_count, email, user_device_token)
send_reservation_request('19:00', '22:00', person_count, email, user_device_token)

