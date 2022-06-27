document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#form').onsubmit = () => {
        // initialize request
        const request = new XMLHttpRequest();

        const currency = document.querySelector("#currency").value;
        request.open('POST', '/convert');

        //Callback function when request completes
        request.onload = () => {
            // extract json from request
            const data = JSON.parse(request.responseText);

            //Update the result div 

            if (data.success){
                const contents = `1 USD is ${data.rate} ${currency}`;
                document.querySelector('#result').innerHTML = contents;

            }else{
                document.querySelector('#result').innerHTML = "Error.";

            }
        }

        //Add data to send with request
        const data = new FormData();
        data.append('currency', currency);

        //Send request
        request.send(data);
        return false;

    }
});