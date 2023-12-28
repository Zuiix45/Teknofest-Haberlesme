const express = require('express');
const router = express.Router();
const logger = require('../../src/logger');
const controls = require('../../src/controls');

router.post('/', (req, res) => {
    if (!controls.isLoggedIn(req.ip)) {
        logger.logWarning(req.ip, 401);
        res.status(401).send();
        return;
    }

    const start = req.body.kilitlenmeBaslangicZamani;
    const end = req.body.kilitlenmeBitisZamani;
    const autonomus = req.body.otonom_kilitlenme;

    const start_time = start.saat + ":" + start.dakika + ":" + start.saniye + "." + start.milisaniye;
    const end_time = end.saat + ":" + end.dakika + ":" + end.saniye + "." + end.milisaniye;
    const info = "kilitlenme_suresi: " + start_time + "-" + end_time + " - otonom_modu: " + autonomus;

    logger.logInfo(logger.getTeamNum(req.ip), info);

    res.status(200).send();
});

module.exports = router;