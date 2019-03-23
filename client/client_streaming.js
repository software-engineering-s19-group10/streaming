// Set port and URL
PORT = 8080;
URL = "localhost:8080";

console.log("Creating Socket")
const socket = new WebSocket('ws://' + URL);
console.log("Tewerqwerqerwqwqrqwerst here");


socket.onopen = function(event) {
    console.log("Connected.");
}


function b64EncodeUnicode(str) {
    // first we use encodeURIComponent to get percent-encoded UTF-8,
    // then we convert the percent encodings into raw bytes which
    // can be fed into btoa.
    console.log("Test hqwerere");
    return btoa(encodeURIComponent(str).replace(/%([0-9A-F]{2})/g,
        function toSolidBytes(match, p1) {
            console.log("Testqwerwqreqwerhere");
            return String.fromCharCode('0x' + p1);
    }));
}


window.onload = function(event) {
    console.log("Test here");

    while(!window.closed) {
        console.log("Receiving frame.");
        /*socket.onmessage = function(event) {
            console.log("adata redcg");

            let frameSTR = event.data;

            let jpgbuffer = b64EncodeUnicode(frameSTR);

            // TODO: display jpg somehow
            var datajpg = "data:image/jpg;base64," + b64encoded;
            document.getElementById("vid_feed").src = datajpg;

            console.log("Received data");
        }*/
    }
}


window.onbeforeunload = function(event) {
    console.log("Closing connection.");

    socket.close();
}