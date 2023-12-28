const express = require('express');
const stableStringify = require('json-stable-stringify');
const router = express.Router();
const logger = require('../../src/logger');
const controls = require('../../src/controls');

function genQrCoords() {
    return {
        "qrEnlem": Math.random() * 78.0 + 36.0,
        "qrBoylam": Math.random() * 71.0 + 26.0
    }
}

router.get('/', (req, res) => {
    if (!controls.isLoggedIn(req.ip)) {
        logger.logWarning(req.ip, 401);
        res.status(401).send();
        return;
    }

    const response_data = stableStringify(genQrCoords());
    logger.logInfo(logger.getTeamNum(req.ip), "qr koordinati yollandi");
    res.type('json').status(200).send(response_data);
});

module.exports = router;