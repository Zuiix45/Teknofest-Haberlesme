const path = require('path');
const fs = require('fs');

history = []

function logWarning(teamNum, statusCode) {
    history.push({
        type: "warning",
        teamNum: teamNum,
        statusCode: statusCode
    })

    console.log(`[WARNING] takim_${teamNum} - durum kodu: ${statusCode}`)
}

function logInfo(teamNum, message) {
    history.push({
        type: "info",
        teamNum: teamNum,
        message: message
    })

    console.log(`[INFO] takim_${teamNum}: ${message}`)
}

function logError(message) {
    history.push({
        type: "error",
        message: message
    })

    console.log(`[ERROR] ${message}`)
}

function writeHistory(filePath) {
    const normalizedPath = path.normalize(filePath);
    fs.writeFileSync(normalizedPath, JSON.stringify(history));
}

/**
 * Retrieves the team number based on the client IP address.
 * @param {string} clientIP - The IP address of the client.
 * @returns {number|undefined} - The team number if found, otherwise undefined.
 */
function getTeamNum(clientIP) {
    try {
        const data = fs.readFileSync('./outputs/temp.json', 'utf8');
        const temp = JSON.parse(data);
        const teamCount = temp.takimlar.length;

        for (let i = 0; i < teamCount; i++) {
            if (temp.takimlar[i].ip == clientIP) {
                return i + 1;
            }
        }
    } catch (err) {
        logError(err);
    }
}

module.exports = {
    logInfo,
    logWarning,
    logError,
    getTeamNum,
    writeHistory
}
