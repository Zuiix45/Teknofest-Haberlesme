const fs = require('fs');

function isLoggedIn(ip) {
    try {
        const data = fs.readFileSync('./outputs/temp.json', 'utf8');
        const temp = JSON.parse(data);
        const teamCount = temp.takimlar.length;

        for (let i = 0; i < teamCount; i++) {
            if (temp.takimlar[i].ip == ip) {
                return true;
            }
        }
    } catch (err) {
        logError(err);
    }

    return false;
}

function validateLoginData(data) {
    if (data.kadi && data.sifre) {
        return true;
    } else {
        return false;
    }
}

// TODO
function validateTelemetryFormat(data) {
    return true;
}

// TODO
function validateKamikazeFormat(data) {
    return true;
}

// TODO
function validateLockingFormat(data) {
    return true;
}

module.exports = {
    isLoggedIn,
    validateLoginData,
    validateTelemetryFormat,
    validateKamikazeFormat,
    validateLockingFormat
}