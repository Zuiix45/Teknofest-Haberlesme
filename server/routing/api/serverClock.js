const express = require('express');
const stableStringify = require('json-stable-stringify');
const router = express.Router();
const logger = require('../../src/logger');
const controls = require('../../src/controls');

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

router.get('/', (req, res) => {
    if (!controls.isLoggedIn(req.ip)) {
        logger.logWarning(req.ip, 401);
        res.status(401).send();
        return;
    }

    const response_data = stableStringify(genServerClock());
    logger.logInfo(logger.getTeamNum(req.ip), "sunucu saati yollandi");
    res.type('json').status(200).send(response_data);
});

module.exports = router;