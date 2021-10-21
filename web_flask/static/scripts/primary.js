window.addEventListener('DOMContentLoaded', (e) => {
    const hum = document.querySelector(".hum");
    const irri = document.querySelector(".irri");
    $('#onoff').click(function(){
        let onoff = document.getElementById("onoff");
        fetch('http://35.243.197.246:5001/api/pots')
            .then(response => response.json())
            .then(data => {
                on = data[0].Turned_ON;
                if (on) {
                    onoff.style.color = "rgb(70, 117, 70)";
                    const statFalse = {
                        "Turned_ON": false
                    };
                    $.ajax({
                        url: 'http://35.243.197.246:5001/api/send_data/10fe8791-7ab2-4302-8848-b0a6d280ae48',
                        type: 'PUT',
                        contentType: "application/json",
                        data: JSON.stringify(statFalse),
                        success: function(response) {
                            //...
                        }
                    });
                } else {
                    const statTrue = {
                        "Turned_ON": true
                    }
                    onoff.style.color = "rgb(128, 141, 128)";
                    $.ajax({
                        url: 'http://35.243.197.246:5001/api/send_data/10fe8791-7ab2-4302-8848-b0a6d280ae48',
                        type: 'PUT',
                        contentType: "application/json",
                        data: JSON.stringify(statTrue),
                        success: function(response) {
                            //...
                        }
                    });
                }
            })
        
    })
    function updateAllEvents() { 
    const tank_text = document.querySelector(".alertext");

    const empty = fetch('http://35.243.197.246:5001/api/pots')
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
        return data[0].Is_empty;
    })   
    }
    let display = setInterval(updateAllEvents, 2000);
});
