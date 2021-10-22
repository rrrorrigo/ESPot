window.addEventListener('DOMContentLoaded', (e) => {
        loadPlantName();

        function loadPlantName() {
        const plantName = document.querySelector('.plantName');
        const selectedPlant = document.querySelector('#selected');
        fetch("http://35.243.197.246:5001/api/selected/823cd38c-5fae-4fda-8836-6511fa60da6e")
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
                        url: 'http://35.243.197.246:5001/api/selected/823cd38c-5fae-4fda-8836-6511fa60da6e',
                        type: 'PUT',
                        contentType: "application/json",
                        dataType: "json",
                        data: JSON.stringify(data),
                        success: function(response) {
                                loadPlantName();
                        }
                    }).fail(function (msg) {
                            console.log(msg);
                    });
        }
});
