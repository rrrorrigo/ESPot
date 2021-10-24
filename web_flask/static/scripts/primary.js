window.addEventListener('DOMContentLoaded', (e) => {
    const onoff = document.getElementById("onoff");
    const pot_id = document.getElementById('id').value;
    const plant = document.getElementById('plant').value;
    const images = {"Rosa":"../static/img/rose.png", "Kalanchoe":"../static/img/kalanchoe.png","Snake plant":"../static/img/snake_plant.png"};
    updateAllEvents();
    if (plant in images) {
        document.getElementsByClassName("plant").src=images[plant];
    }
    $('#onoff').ready(function (){
        $.get(`http://35.243.197.246:5001/api/pots/${pot_id}`, function(data) {
                if (data[0].Turned_ON) {
                    onoff.style.color = "rgb(70, 117, 70)";
                } else {
                    onoff.style.color = "rgb(128, 141, 128)";
                }});
    });

    $('#onoff').click(function (){
            $.get(`http://35.243.197.246:5001/api/pots/${pot_id}`, function(data) {
                if (data[0].Turned_ON) {
                    onoff.style.color = "rgb(128, 141, 128)";
                    const statFalse = {
                        "Turned_ON": false
                    };
                    $.ajax({
                        url: `http://35.243.197.246:5001/api/send_data/${pot_id}`,
                        type: 'PUT',
                        contentType: "application/json",
                        data: JSON.stringify(statFalse),
                        success: function(response) {
                            console.log("stat updated to false")
                        }
                    });
                } else {
                    onoff.style.color = "rgb(70, 117, 70)";
                    const statTrue = {
                        "Turned_ON": true
                    }
                    $.ajax({
                        url: `http://35.243.197.246:5001/api/send_data/${pot_id}`,
                        type: 'PUT',
                        contentType: "application/json",
                        data: JSON.stringify(statTrue),
                        success: function(response) {
                            console.log("stat updated to true")
                        }
                    }) 
                }});
        });
            
    function updateAllEvents() { 
    const tank_text = document.querySelector(".alertext");

    fetch(`http://35.243.197.246:5001/api/pots/${pot_id}`)
    .then(response => response.json())
    .then(data => {
        const hum = document.querySelector(".numberHum");
        const irri = document.querySelector(".numberIrri");
        hum.innerHTML = "<span class='numberHum'>" + data[0].Actual_humidity + "%</span>"
        irri.innerHTML = "<span class='numberIrri'>" + data[0].Last_irrigation + "</span>"
        if (data[0].Is_empty) {
            $(".alerticon").css({"background": "url('/../static/img/alertt.png') bottom center", "background-repeat": "no-repeat"});
            tank_text.innerHTML = "<h5>Warning</h5><h6>The water level is low, please add water to the tank!</h6>"
        } else {
            $(".alerticon").css({"background": "url('/../static/img/tankfull.png') bottom center", "background-repeat": "no-repeat"});
            tank_text.innerHTML = "<h5>The tank has enough water</h5>"
        }
    })   
    }
    let display = setInterval(updateAllEvents, 4000);
});
