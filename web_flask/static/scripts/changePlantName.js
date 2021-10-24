window.addEventListener('DOMContentLoaded', (e) => {
        const pot_id = document.getElementById('id').value;
        const user_id = document.getElementById('user_id').value;
        const images = {"Rosa":"http://35.243.197.246:5000/static/img/rose.png",
                    "Kalanchoe":"http://35.243.197.246:5000/static/img/kalanchoe.png",
                    "Snake plant":"http://35.243.197.246:5000/static/img/snake_plant.png",
                    "Pink tulip":"http://35.243.197.246:5000/static/img/pink_tulip.png"};
        loadPlantName();

        function loadPlantName() {
        const plantName = document.querySelector('.plantName');
        const selectedPlant = document.querySelector('#selected');
        fetch(`http://35.243.197.246:5001/api/selected/${user_id}/${pot_id}`)
		.then(response => response.json())
		.then(data => {
		    console.log(data);
                plantName.innerHTML =  data[1].Plant_name
                selectedPlant.innerHTML = "<a class='dropdown-item' href='#' id='selected'>" + data[1].Plant_name +"</a>"
        });}

        $('.p').click(function () {
                const name = this.getAttribute('name-plant');
                selectPlantName(name);
        });

        function selectPlantName(name) {
                const data = {
                        "Plant_name": String(name)
                };
                $.ajax({
                        url: `http://35.243.197.246:5001/api/selected/${user_id}/${pot_id}`,
                        type: 'PUT',
                        contentType: "application/json",
                        dataType: "json",
                        data: JSON.stringify(data),
                        success: function(response) {
                                alert("Attention, your plant configuration is now changed");
                                loadPlantName();
                        }
                    }).fail(function (msg) {
                            console.log(msg);
                    });
                if (data["Plant_name"] in images) {
                        document.getElementById("dyn_plant_img").src=images[data["Plant_name"]];
                }
        }
});
