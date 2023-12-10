const express = require('express');
const bodyParser = require('body-parser');
const stableStringify = require('json-stable-stringify');
const app = express();
const fs = require('fs');

IP = "0.0.0.0"
PORT = 5000

JSON_SPACING = 4;

SERVER_CLOCK_JSON_PATH = "../example_data/server_clock.json";
OTHER_TEAMS_JSON_PATH = "../example_data/other_teams_telemetry.json";
QR_COORDS_JSON_PATH = "../example_data/qr_coords.json";

// Use JSON middleware to automatically parse JSON
app.use(bodyParser.json());

// TODO: validate json data according to the pdf

// Define a route for the login API
app.post('/api/giris', (req, res) => {
    const login_info = stableStringify(req.body, { space: JSON_SPACING });
    console.log(login_info);

    const response_data = stableStringify({ "takim_numarasi": 1 }, { space: JSON_SPACING });
    res.type('json').status(200).send(response_data);
});

// Define a route for the telemetry info API
app.post('/api/telemetri_gonder', (req, res) => {
    const telemetry_info = stableStringify(req.body, { space: JSON_SPACING });
    console.log(telemetry_info);

    fs.readFile(OTHER_TEAMS_JSON_PATH, 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading file:', err);
            return;
        }
    
        // Parse the JSON data
        const jsonData = JSON.parse(data);
    
        const response_data = stableStringify(jsonData, { space: JSON_SPACING });
        res.type('json').status(200).send(response_data);
    });
});

// Define a route for the locking info API
app.post('/api/kilitlenme_bilgisi', (req, res) => {
    const locking_info = stableStringify(req.body, { space: JSON_SPACING });
    console.log(locking_info);
    res.status(200).send();
});

// Define a route for the kamikaze info API
app.post('/api/kamikaze_bilgisi', (req, res) => {
    const kamikaze_info = stableStringify(req.body, { space: JSON_SPACING });
    console.log(kamikaze_info);
    res.status(200).send();
});

// Define a route for the server clock API
app.get('/api/sunucusaati', (req, res) => {
    fs.readFile(SERVER_CLOCK_JSON_PATH, 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading file:', err);
            return;
        }
    
        // Parse the JSON data
        const jsonData = JSON.parse(data);
    
        const response_data = stableStringify(jsonData, { space: JSON_SPACING });
        res.type('json').status(200).send(response_data);
    });
});

// Define a route for the qr coordinates API
app.get('/api/qr_koordinati', (req, res) => {
    fs.readFile(QR_COORDS_JSON_PATH, 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading file:', err);
            return;
        }
    
        // Parse the JSON data
        const jsonData = JSON.parse(data);
    
        const response_data = stableStringify(jsonData, { space: JSON_SPACING });
        res.type('json').status(200).send(response_data);
    });
});

// Start the server
app.listen(PORT, IP, () => {
    console.log("Server is running on", IP + ":" + PORT);
});
