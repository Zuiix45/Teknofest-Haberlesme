const express = require('express');
const stableStringify = require('json-stable-stringify');
const router = express.Router();
const logger = require('../../src/logger');
const controls = require('../../src/controls');
const fs = require('fs');

router.post('/', (req, res) => {
    let temp = JSON.parse(fs.readFileSync('./outputs/temp.json', 'utf8'));
    let teamCount = temp.takimlar.length + 1;
    
    const response_data = stableStringify({ "takim_numarasi": teamCount });

    temp.takimlar.push({
        "takim_numarasi": teamCount,
        "kullanici_adi": req.body.kadi,
        "sifre": req.body.sifre,
        "ip": req.ip,
    });

    fs.writeFileSync('./outputs/temp.json', JSON.stringify(temp), 'utf8');

    const info = "kullanici_adi: " + req.body.kadi + " - sifre: " + req.body.sifre + " - ip: " + req.ip;
    logger.logInfo(logger.getTeamNum(req.ip), info);

    res.type('json').status(200).send(response_data);
});

module.exports = router;