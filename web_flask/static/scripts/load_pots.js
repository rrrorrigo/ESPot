window.addEventListener('DOMContentLoaded', (e) => {
    let user_id = document.getElementById('user_id').value;
    let img_path = "";
    let images = {"Rosa":"../static/img/rose.png", "Kalanchoe":"../static/img/kalanchoe.png","Snake plant":"../static/img/snake_plant.png"}
    fetch(`http://35.243.197.246:5001/api/user_pots/${user_id}`)
		.then(response => response.json())
		.then(data => {
            data.forEach(element => {
                if (element.name in images) {
                    img_path = images[element.name]
                } else {
                    img_path = "../static/img/plant.png"
                }
                const article = `<div class="choose" style="cursor: pointer;" onclick="window.location='http://myespot.tech/${user_id}/my_plants/${element.id}';">
                <div class="title_box">
                <h2>${element.name}</h2>
                </div>
                <div class="plantImage">
                <img src="${img_path}" class="plant_img"></div>
                <h6>${element.id}</h6>
                </div>`;
                $('.main').append(article);
            });
            const article = `<div class="choose" style="cursor: pointer;" onclick="window.location='http://myespot.tech/${user_id}/add_pot';">
                <div class="title_box"><h2>Register new plant</h2></div>
                <div class="plantImage">
                <img src="../static/img/empty_pot.png" class="plant_img"></div>
                </div>`;
                $('.main').append(article);
        });
});
