const express = require('express');
const stableStringify = require('json-stable-stringify');
const router = express.Router();
const logger = require('../../src/logger');
const controls = require('../../src/controls');
const fs = require('fs');

function genServerClock() {
    date = new Date()
    
    return {
        "gun": date.getDay(),
        "saat": date.getHours(),
        "dakika": date.getMinutes(),
        "saniye": date.getSeconds(),
        "milisaniye": date.getMilliseconds()
    }
}

router.post('/', (req, res) => {
    if (!controls.isLoggedIn(req.ip)) {
        logger.logWarning(req.ip, 401);
        res.status(401).send();
        return;
    }

    const telemetry_info = stableStringify(req.body);
    logger.logInfo(logger.getTeamNum(req.ip), "telemetri verisi alindi");

    temp = JSON.parse(fs.readFileSync('./outputs/temp.json', 'utf8'));

    others_telemetry = {
        "sunucusaati": genServerClock(),
        "konumBilgileri": temp.konumBilgileri,
    };

    const response_data = stableStringify(others_telemetry);

    // find location data according to team number
    const team_num = logger.getTeamNum(req.ip);

    for (let i = 0; i < temp.takimlar.length; i++) {
        if (temp.takimlar[i].takim_numarasi == team_num) {
            temp.konumBilgileri[i] = JSON.parse(telemetry_info);
            break;
        }
    }

    fs.writeFileSync('./outputs/temp.json', JSON.stringify(temp), 'utf8');

    res.type('json').status(200).send(response_data);
});


module.exports = router;