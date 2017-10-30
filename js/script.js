var ws;
var host = window.location.host;
var max = 5;
var logs = []

ws = new WebSocket('ws://' + host + '/websocket');
ws.onmessage = function(ev) {
    logs.push(ev.data);
    if (logs.length > 5) {
        logs.shift();
    }

    var txt = '';
    for (var i = 0; i < logs.length; ++i) {
        txt += logs[i] + '<br>';
    }

    document.getElementById('val').innerHTML = txt;
}
