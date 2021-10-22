window.addEventListener('DOMContentLoaded', (e) => {
        loadPlantName();

        function loadPlantName() {
        const plantName = document.querySelector('.plantName');
        const selectedPlant = document.querySelector('#selected');
        fetch("http://35.243.197.246:5001/api/selected/10fe8791-7ab2-4302-8848-b0a6d280ae48")
		.then(response => response.json())
		.then(data => {
		    console.log(data);
                plantName.innerHTML =  data[1].Plant_name
                selectedPlant.innerHTML = "<a class='dropdown-item' href='#' id='selected'>" + data[1].Plant_name +"</a>"
        });}

        $('#p').click(function () {
                const name = this.getAttribute('name');
                selectPlantName(name);
        });

        function selectPlantName(name) {
                const data = {
                        "Plant_name": "rosaaa"
                };
                $.ajax({
                        url: 'http://35.243.197.246:5001/api/selected/10fe8791-7ab2-4302-8848-b0a6d280ae48 ',
                        type: 'PUT',
                        contentType: "application/json",
                        data: JSON.stringify(data),
                        success: function(response) {
                            console.log("selected")
                        }
                    }).fail(function (msg) {
                            console.log(msg);
                    });
        }
});