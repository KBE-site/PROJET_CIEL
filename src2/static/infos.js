var socket = io();

socket.on('server_response', function(msg) {
    console.log('Received message from server:', msg.data);
});