const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.use(express.static(__dirname + '/public'));

// register api routes
app.use('/api/kamikaze_bilgisi', require('./routing/api/kamikaze'));
app.use('/api/kilitlenme_bilgisi', require('./routing/api/locking'));
app.use('/api/giris', require('./routing/api/login'));
app.use('/api/qr_koordinati', require('./routing/api/qrCoords'));
app.use('/api/sunucusaati', require('./routing/api/serverClock'));
app.use('/api/telemetri_gonder', require('./routing/api/telemetry'));

// catch 404 and forward to error handler
app.use(function(req, res, next) {
    res.status(404).send("404 not found");
});

// error handler
app.use(function(err, req, res, next) {
    // set locals, only providing error in development
    res.locals.message = err.message;
    res.locals.error = req.app.get('env') === 'development' ? err : {};

    res.status(err.status || 500);
    res.send('error');
});

module.exports = app;