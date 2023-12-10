import unittest
from teamClient import Client

team = Client("takimkadi", "takimsifresi")

class TestClient(unittest.TestCase):
    def test_login(self):
        team.login()
        self.assertEqual(team.get_teamNum(), 1)
        self.assertEqual(team.get_statusCode(), 200)
    
    def test_requestServerClock(self):
        team.requestServerClock()
        self.assertEqual(team.get_serverClock(), team.readJsonFile("example_data/server_clock.json"))
        self.assertEqual(team.get_statusCode(), 200)
        
    def test_telemetryThread(self):
        telemetry_info = team.readJsonFile("example_data/telemetry_info.json")
        others_telemetry_info = team.readJsonFile("example_data/other_teams_telemetry.json")["konumBilgileri"]
        server_clock = team.readJsonFile("example_data/other_teams_telemetry.json")["sunucusaati"]
        
        team.set_telemetryInfo(telemetry_info)
        team.sendTelemetryInfo()
        
        self.maxDiff = None # to see the whole diff
        
        self.assertEqual(team.get_othersTelemetryInfo(), others_telemetry_info)
        self.assertEqual(team.get_serverClock(), server_clock)
        self.assertEqual(team.get_statusCode(), 200)
    
    def test_lockingInfo(self):
        team.set_lockingInfo(team.readJsonFile("example_data/locking_info.json"))
        team.sendLockingInfo()
        self.assertEqual(team.get_statusCode(), 200)
       
    def test_kamikazeInfo(self):
        team.set_kamikazeInfo(team.readJsonFile("example_data/kamikaze_info.json"))
        team.sendKamikazeInfo()
        self.assertEqual(team.get_statusCode(), 200)
    
    def test_requestKamikazeQRCoords(self):
        team.requestKamikazeQRCoords()
        self.assertEqual(team.get_QRCoords(), team.readJsonFile("example_data/qr_coords.json"))
        self.assertEqual(team.get_statusCode(), 200)

if __name__ == '__main__':
    unittest.main()
    