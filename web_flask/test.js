window.addEventListener('DOMContentLoaded', (e) => {
    function updateAllEvents() { 
        fetch('http://35.243.197.246:5001/api/pots')
            .then(response => response.json())
            .then(data => {
                const hum = document.querySelector(".hum")
                hum.innerText = "Humidity: " + data[0].Actual_humidity

                const irri = document.querySelector(".irri")
                irri.innerText = "Time of last irrigation: " + data[0].Last_irrigation
                
                const tank = document.querySelector(".tank")
                tank.innerText = "Is the tank empty: " + data[0].Is_empty
            })   
    }
    let display = setInterval(updateAllEvents, 2000);
});
