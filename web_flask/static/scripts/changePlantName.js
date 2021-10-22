window.addEventListener('DOMContentLoaded', (e) => {
        loadPlantName();

        function loadPlantName() {
        const plantName = document.getElementByClass('plantName')
        const selectedPlant = document.getElementById('selected')
        fetch("http://35.243.197.246:5001/api/selected/10fe8791-7ab2-4302-8848-b0a6d280ae48")
        .then(response => response.json())
        .then(data => {
                plantName.innerHTML = "<div class='plantName'>" + data.Plant.Plant_name + "</div>"
                selectedPlant.innerHTML = "<a class='dropdown-item' href='#' id='selected'>" + data.Plant.Plant_name +"</a>"
        });}

        $('#p').click(function () {
                const name = this.getAttribute('name');
                selectPlantName(name);
        })

        function selectPlantName(name) {
                data = {
                        "Plant_name": name
                }
                $.ajax({
                        url: 'http://35.243.197.246:5001/api/selected/10fe8791-7ab2-4302-8848-b0a6d280ae48 ',
                        type: 'PUT',
                        contentType: "application/json",
                        data: JSON.stringify(data),
                        success: function(response) {
                            console.log("selected")
                        }
                    });
        }
});