from api.rc import APIStellarium
import json
from time import sleep

while True:
    api = APIStellarium('sun')
    response = api.get_all_object_informations()

    CAP = 127.0
    AZIMUTH = float(json.loads(response).get('azimuth'))
    ALTITUDE = float(json.loads(response).get('altitude'))

    def servomoteur_hozizontal():
        if CAP - AZIMUTH > 0:
            return CAP - AZIMUTH
        else:
            return AZIMUTH - CAP

    def servomoteur_vertical():
        return ALTITUDE


    print(f"Servo moteur horizontal = {servomoteur_hozizontal()}°")
    print(f"Server moteur vertical = {servomoteur_vertical()}°")
    sleep(1)
