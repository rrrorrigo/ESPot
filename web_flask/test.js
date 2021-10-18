window.addEventListener('DOMContentLoaded', (e) => {
    function updateAllEvents() { 
        fetch('http://35.243.197.246:5001/api/pots')
            .then(response => response.json())
            .then(data => {
                const hum = document.querySelector(".hum")
                hum.innerHTML = "Humidity: " + data[0].hum
                const irri = document.querySelector(".hum")
                irri.innerHTML = "Time of last irrigation: " + data[0].irri
                const tank = document.querySelector(".hum")
                tank.innerHTML = "Is the tank empty: " + data[0].tank
            })   
    }
    let display = setInterval(updateAllEvents, 2000);
});
