import unittest
import randomDataGenerator as rdg
from teamClient import Client

addr = input("Teknofest Deneme Sunucusu adresini girin: ")
client = Client("takimkadi", "takimsifresi", addr)
outputs_path = "./team/outputs/"

class TestClient(unittest.TestCase):
    def test_login(self):
        self.assertEqual(client.login(), 200)
        client.writeJsonFile(outputs_path + "team_number.json", client.get_teamNum())
    
    def test_requestServerClock(self):
        self.assertEqual(client.requestServerClock(), 200)
        client.writeJsonFile(outputs_path + "server_clock.json", client.get_serverClock())
        
    def test_telemetryInfo(self):
        telemetry_info = rdg.generateRandomTelemetryInfo(client.get_teamNum())
        
        client.set_telemetryInfo(telemetry_info)
        
        self.maxDiff = None # to see the whole diff
        
        self.assertEqual(client.sendTelemetryInfo(), 200)
        
        client.writeJsonFile(outputs_path + "other_teams_telemetry_info.json", client.get_othersTelemetryInfo())
        client.writeJsonFile(outputs_path + "server_clock.json", client.get_serverClock())
    
    def test_lockingInfo(self):
        client.set_lockingInfo(rdg.generateRandomLockingInfo())
        self.assertEqual(client.sendLockingInfo(), 200)
       
    def test_kamikazeInfo(self):
        client.set_kamikazeInfo(rdg.generateRandomKamikazeInfo())
        self.assertEqual(client.sendKamikazeInfo(), 200)
    
    def test_requestKamikazeQRCoords(self):
        self.assertEqual(client.requestKamikazeQRCoords(), 200)
        client.writeJsonFile(outputs_path + "kamikaze_qr_coords.json", client.get_kamikazeQrCoords())

if __name__ == '__main__':
    unittest.main()
    