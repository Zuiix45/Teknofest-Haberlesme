
import json
import requests

class Client:
    """
    A class to communicate with the competition server.
    """
    def __init__(self, team_username: str, password: str, server_url="http://localhost:5000"):
        """
        Initializes a Client object.

        Args:
            team_username (str): The username of the team.
            password (str): The password for the team.
            server_url (str, optional): The URL of the competition server. Defaults to "http://localhost:5000".
        """
        self.__URL = server_url
        self.__team_username = team_username
        self.__password = password
        
        # API URLs
        self.__SERVER_CLOCK_URL = "/api/sunucusaati"
        self.__TELEMETRY_INFO_URL = "/api/telemetri_gonder"
        self.__LOCKING_INFO_URL = "/api/kilitlenme_bilgisi"
        self.__LOGIN_URL = "/api/giris"
        self.__KAMIKAZE_INFO_URL = "/api/kamikaze_bilgisi"
        self.__QR_COORDS_URL = "/api/qr_koordinati"
        
        self.__status_history = []
        
        # Initialize variables to communicate with the server
        self.__serverClock = {}
        self.__locking_info = {}
        self.__telemetry_info = {}
        self.__kamikaze_info = {}
        self.__qrCoords = {}
        
        self.__others_telemetry_info = []
        
        self.__team_num = 0
        
    def sendTelemetryInfo(self):
        """
        Sends telemetry information to the competition server.
        """
        data = json.dumps(self.__telemetry_info)
        loaded = json.loads(data)
        req = requests.post(self.__URL + self.__TELEMETRY_INFO_URL, json=loaded)
        
        self.__status_history.append(req.status_code)
        self.__others_telemetry_info = req.json()["konumBilgileri"]
        self.__serverClock = req.json()["sunucusaati"]
        
        req.close()
        
    def sendLockingInfo(self):
        """
        Sends locking information to the competition server.
        """
        data = json.dumps(self.__locking_info)
        loaded = json.loads(data)
        req = requests.post(self.__URL + self.__LOCKING_INFO_URL, json=loaded)
        
        self.__status_history.append(req.status_code)
        
        req.close()
        
    def login(self, team_username: str = None, password: str = None):
        """
        Logs in to the team using the provided username and password.

        Args:
            team_username (str, optional): The username of the team. If not provided, the default team username will be used.
            password (str, optional): The password for the team. If not provided, the default team password will be used.
        """
        if team_username is None:
            team_username = self.__team_username
        
        if password is None:
            password = self.__password
        
        login_details = {
            "kadi": team_username,
            "sifre": password
        }
        
        data = json.dumps(login_details)
        loaded = json.loads(data)
        req = requests.post(self.__URL + self.__LOGIN_URL, json=loaded)
        
        self.__status_history.append(req.status_code)
        
        try:
            self.__team_num = req.json()["takim_numarasi"]
        except:
            self.__team_num = 0
        
        req.close()
        
    def sendKamikazeInfo(self):
        """
        Sends kamikaze information to the competition server.
        """
        data = json.dumps(self.__kamikaze_info)
        loaded = json.loads(data)
        req = requests.post(self.__URL + self.__KAMIKAZE_INFO_URL, json=loaded)
        
        self.__status_history.append(req.status_code)
        
        req.close()
        
    def requestKamikazeQRCoords(self):
        """
        Gets the kamikaze QR coordinates from the competition server.
        """
        req = requests.get(self.__URL + self.__QR_COORDS_URL)
        
        self.__status_history.append(req.status_code)
        
        if req.status_code == 200:
            self.__qrCoords = req.json()
        
        req.close()
        
    def requestServerClock(self):
        """
        Gets the server clock information from the competition server.
        """
        req = requests.get(self.__URL + self.__SERVER_CLOCK_URL)
        
        self.__status_history.append(req.status_code)
        
        if req.status_code == 200:
            self.__serverClock = json.loads(json.dumps(req.json()))
        
        req.close()
        
    def readJsonFile(self, file_path: str):
        """
        Reads a JSON file.

        Args:
            file_path (str): The path of the JSON file.

        Returns:
            dict: The JSON file content.
        """
        with open(file_path, "r") as file:
            return json.load(file)
        
    def set_telemetryInfo(self, telemetry_info: dict):
        """
        Sets the telemetry information to be sent to the competition server.

        Args:
            telemetry_info (dict): The telemetry information to be sent to the competition server.
        """
        self.__telemetry_info = telemetry_info

    def set_lockingInfo(self, locking_info: dict):
        """
        Sets the locking information to be sent to the competition server.

        Args:
            locking_info (dict): The locking information to be sent to the competition server.
        """
        self.__locking_info = locking_info
        
    def set_kamikazeInfo(self, kamikaze_info: dict):
        """
        Sets the kamikaze information to be sent to the competition server.

        Args:
            kamikaze_info (dict): The kamikaze information to be sent to the competition server.
        """
        self.__kamikaze_info = kamikaze_info
    
    def get_serverClock(self):
        """
        Returns the server clock information.

        Returns:
            dict: The server clock information.
        """
        return self.__serverClock
    
    def get_othersTelemetryInfo(self):
        """
        Returns the telemetry information of other teams.

        Returns:
            dict: The telemetry information of other teams.
        """
        return self.__others_telemetry_info
    
    def get_teamNum(self):
        """
        Returns the team number.

        Returns:
            int: The team number.
        """
        return self.__team_num
    
    def get_QRCoords(self):
        """
        Returns the QR coordinates.

        Returns:
            dict: The QR coordinates.
        """
        return self.__qrCoords
    
    def get_statusCode(self, index: int = -1):
        """
        Returns the status code of specified index. If no index is provided, the status code of the last request will be returned.
        
        Args:
            index (int, optional): The index of the status code to be returned. Defaults to -1.
        
        Returns:
            int: The status code of the last request.
        """
        return self.__status_history[index]
    