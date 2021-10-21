function onoff() {
let onoff = document.getElementById("onoff");
if (compareColour("#808D80", onoff.style.color)) {
    onoff.style.color = "rgb(70, 117, 70)";
} else {
    onoff.style.color = "rgb(128, 141, 128)";
}
}

function compareColour(col1, col2) {
    var e = document.createElement('span')
    document.body.appendChild(e);
    // standardise
    e.style.color = col1;
    col1 = window.getComputedStyle(e).color;
    e.style.color = col2;
    col2 = window.getComputedStyle(e).color;
    // cleanup
    document.body.removeChild(e);
    return col1 === col2;
}

window.addEventListener('DOMContentLoaded', (e) => {
    function updateAllEvents() { 
        const hum = document.querySelector(".hum")
        const irri = document.querySelector(".irri")
        const tank_text = document.querySelector(".alertext")
        
        fetch('http://35.243.197.246:5001/api/pots')
        .then(response => response.json())
        .then(data => {
            hum.innerText = "Humidity: " + data[0].Actual_humidity
            irri.innerText = "Last irrigation: " + data[0].Last_irrigation
            if (data[0].Is_empty) {
                $(".alertt").attr("background", "url('/../static/img/alertt.png') center center");
                tank_text.innerHTML = "<h5>Warning</h5><br><h6>The water level is low, please add water to the tank!</h6>"
            } else {
                $(".alertt").attr("background", "url('/../static/img/tankfull.png') center center");
                tank_text.innerHTML = "<h5>The tank has enough water</h5>"
            }
        })   
    }
    let display = setInterval(updateAllEvents, 2000);
});
