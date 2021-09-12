document.addEventListener('DOMContentLoaded', ()=>{

    //Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    
    
    //When connected configure buttions
    socket.on('connect', ()=>{

        //Each button should emit a 'submit vote' event
        document.querySelectorAll('button').forEach(button => {
            button.onclick = () => {
                const selection = button.dataset.value;
                socket.emit("submit", {'selection': selection});
                console.log(selection);
            };
        });

    });

    // When a new vote is announced, add to the unordered list
    socket.on('totals', data =>{
        console.log(data);
        document.querySelector('#yes').innerHTML = data.yes;
        document.querySelector('#no').innerHTML = data.no;
        document.querySelector('#maybe').innerHTML = data.maybe;
    });


});