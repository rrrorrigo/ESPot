window.addEventListener('DOMContentLoaded', (e) => {
    function updateAllEvents() { 
        const hum = document.querySelector(".hum")
        
        const irri = document.querySelector(".irri")
        
        const tank = document.querySelector(".tank")
        fetch('http://35.243.197.246:5001/api/pots')
        .then(response => response.json())
        .then(data => {
            hum.innerText = "Humidity: " + data[0].Actual_humidity
            irri.innerText = "Time of last irrigation: " + data[0].Last_irrigation
            tank.innerText = "Is the tank empty: " + data[0].Is_empty
            })   
    }
    let display = setInterval(updateAllEvents, 2000);
});
