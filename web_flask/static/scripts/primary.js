window.addEventListener('DOMContentLoaded', (e) => {
    const onoff = document.getElementById("onoff");
    const hum = document.querySelector(".numberHum");
    const irri = document.querySelector(".numberIrri");
    updateAllEvents();

    $('#onoff').ready(function (){
        $.get('http://35.243.197.246:5001/api/pots', function(data) {
                if (data[0].Turned_ON) {
                    onoff.style.color = "rgb(70, 117, 70)";
                } else {
                    onoff.style.color = "rgb(128, 141, 128)";
                }});
    });

    $('#onoff').click(function (){
            $.get('http://35.243.197.246:5001/api/pots', function(data) {
                if (data[0].Turned_ON) {
                    onoff.style.color = "rgb(128, 141, 128)";
                    const statFalse = {
                        "Turned_ON": false
                    };
                    $.ajax({
                        url: 'http://35.243.197.246:5001/api/send_data/10fe8791-7ab2-4302-8848-b0a6d280ae48',
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
                        url: 'http://35.243.197.246:5001/api/send_data/10fe8791-7ab2-4302-8848-b0a6d280ae48',
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

    fetch('http://35.243.197.246:5001/api/pots')
    .then(response => response.json())
    .then(data => {
        hum.text = data[0].Actual_humidity
        irri.text = data[0].Last_irrigation
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
