class Team {

    #username;
    #password;
    #ip;
    #telemetry_history = [];
    #locking_history = [];
    #kamikaze_history = [];

    constructor(ip, username, password) {
        this.#username = username;
        this.#password = password;
        this.#ip = ip;
    }

    addTelemetry(telemetry) {
        this.#telemetry_history.push(telemetry);
    }

    addLocking(locking) {
        this.#locking_history.push(locking);
    }

    addKamikaze(kamikaze) {
        this.#kamikaze_history.push(kamikaze);
    }

    printTelemetryHistory() {
        console.log(this.#telemetry_history);
    }

    printLockingHistory() {
        console.log(this.#locking_history);
    }

    printKamikazeHistory() {
        console.log(this.#kamikaze_history);
    }

    getLastTelemetry() {
        return this.#telemetry_history[this.#telemetry_history.length - 1];
    }

    getLastLocking() {
        return this.#locking_history[this.#locking_history.length - 1];
    }

    getLastKamikaze() {
        return this.#kamikaze_history[this.#kamikaze_history.length - 1];
    }

    get username() {
        return this.#username;
    }

    get password() {
        return this.#password;
    }

    get ip() {
        return this.#ip;
    }
}