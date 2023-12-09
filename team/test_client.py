import unittest
from client import Client

team = Client("takimkadi", "takimsifresi")

class TestClient(unittest.TestCase):
    def test_login(self):
        team.login()
        self.assertEqual(team.getTeamNum(), 1)
        self.assertEqual(team.getStatusCode(), 200)
    
    def test_requestServerClock(self):
        team.requestServerClock()
        self.assertEqual(team.getServerClock(), team.readJsonFile("example_data/server_clock.json"))
        self.assertEqual(team.getStatusCode(), 200)
        
    def test_telemetryThread(self):
        telemetry_info = team.readJsonFile("example_data/telemetry_info.json")
        others_telemetry_info = team.readJsonFile("example_data/other_teams_telemetry.json")["konumBilgileri"]
        server_clock = team.readJsonFile("example_data/other_teams_telemetry.json")["sunucusaati"]
        
        team.setTelemetryInfo(telemetry_info)
        team.sendTelemetryInfo()
        
        self.maxDiff = None # to see the whole diff
        
        self.assertEqual(team.getOthersTelemetryInfo(), others_telemetry_info)
        self.assertEqual(team.getServerClock(), server_clock)
        self.assertEqual(team.getStatusCode(), 200)
    
    def test_lockingInfo(self):
        team.setLockingInfo(team.readJsonFile("example_data/locking_info.json"))
        team.sendLockingInfo()
        self.assertEqual(team.getStatusCode(), 200)
       
    def test_kamikazeInfo(self):
        team.setKamikazeInfo(team.readJsonFile("example_data/kamikaze_info.json"))
        team.sendKamikazeInfo()
        self.assertEqual(team.getStatusCode(), 200)
    
    def test_requestKamikazeQRCoords(self):
        team.requestKamikazeQRCoords()
        self.assertEqual(team.getQRCoords(), team.readJsonFile("example_data/qr_coords.json"))
        self.assertEqual(team.getStatusCode(), 200)

if __name__ == '__main__':
    unittest.main()