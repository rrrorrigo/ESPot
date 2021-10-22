window.addEventListener('DOMContentLoaded', (e) => {
        loadPlantName();

        function loadPlantName() {
        const plantName = document.querySelector('.plantName');
        const selectedPlant = document.querySelector('#selected');
        fetch("http://35.243.197.246:5001/api/selected/dce9b75c-d8ac-4971-9024-a52fb359f7eb")
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
                        url: 'http://35.243.197.246:5001/api/selected/dce9b75c-d8ac-4971-9024-a52fb359f7eb',
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
        }
});
