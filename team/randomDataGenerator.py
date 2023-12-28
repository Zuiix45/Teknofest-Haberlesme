import random
import string

# TODO: Solve Date bug

def generateRandomKamikazeInfo():
    starting_hour = random.randint(0, 23)
    starting_minute = random.randint(0, 59)
    starting_second = random.randint(0, 59)
    starting_millisecond = random.randint(0, 999)
    
    ending_hour = random.randint(starting_hour, 23)
    ending_minute = random.randint(starting_minute, 59)
    ending_second = random.randint(starting_second, 59)
    ending_millisecond = random.randint(starting_hour, 999)
    
    chars = string.ascii_letters + string.digits
    textLength = 10
    qrText = ''.join(random.choice(chars) for i in range(textLength))
    
    kamikazeInfo = {
        "kamikazeBaslangicZamani": {
            "saat": starting_hour,
            "dakika": starting_minute,
            "saniye": starting_second,
            "milisaniye": starting_millisecond
        },
        "kamikazeBitisZamani": {
            "saat": ending_hour,
            "dakika": ending_minute,
            "saniye": ending_second,
            "milisaniye": ending_millisecond
        },
        "qrMetni": qrText,
    }
    
    return kamikazeInfo

def generateRandomLockingInfo():
    starting_hour = random.randint(0, 23)
    starting_minute = random.randint(0, 59)
    starting_second = random.randint(0, 59)
    starting_millisecond = random.randint(0, 999)
    
    ending_hour = random.randint(starting_hour, 23)
    ending_minute = random.randint(starting_minute, 59)
    ending_second = random.randint(starting_second, 59)
    ending_millisecond = random.randint(starting_hour, 999)
    
    lockingInfo = {
        "kilitlenmeBaslangicZamani": {
            "saat": starting_hour,
            "dakika": starting_minute,
            "saniye": starting_second,
            "milisaniye": starting_millisecond
        },
        "kilitlenmeBitisZamani": {
            "saat": ending_hour,
            "dakika": ending_minute,
            "saniye": ending_second,
            "milisaniye": ending_millisecond
        },
        "otonom_kilitlenme": 1,
    }
    
    return lockingInfo

def generateRandomTelemetryInfo(team_number: int):
    telemetryInfo = {
        "takim_numarasi": team_number,
        "iha_enlem": random.uniform(0.0, 100.0),
        "iha_boylam": random.uniform(0.0, 100.0),
        "iha_irtifa": random.randint(0, 100),
        "iha_dikilme": random.randint(-90, 90),
        "iha_yonelme": random.randint(0, 360),
        "iha_yatis": random.randint(-90, 90),
        "iha_hiz": random.randint(0, 300),
        "iha_batarya": random.randint(0, 100),
        "iha_otonom": 1,
        "iha_kilitlenme": random.randint(0, 1),
        "hedef_merkez_X": random.randint(0, 640),
        "hedef_merkez_Y": random.randint(0, 480),
        "hedef_genislik": random.randint(0, 100),
        "hedef_yukseklik": random.randint(0, 100),
        "gps_saati": {
            "saat": random.randint(0, 23),
            "dakika": random.randint(0, 59),
            "saniye": random.randint(0, 59),
            "milisaniye": random.randint(0, 999)
        }
    }
    
    return telemetryInfo
