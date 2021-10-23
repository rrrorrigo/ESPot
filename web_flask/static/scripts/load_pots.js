window.addEventListener('DOMContentLoaded', (e) => {
    fetch("http://35.243.197.246:5001/api/user_pots/dce9b75c-d8ac-4971-9024-a52fb359f7eb")
		.then(response => response.json())
		.then(data => {
            data.forEach(element => {
                const article = `<div class="choose" style="cursor: pointer;" onclick="window.location='http://35.243.197.246:5000/${element.user_id}/${element.id}';">
                <div class="title_box">
                <h2>${element.name}</h2>
                <h1>${element.Actual_humidity}%</h1>
                </div>
                <div>
                <img src="../static/img/plant.png" class="plant_img"></div>
                </div>`;
                $('.main').append(article);
            });
            const article = `<div class="choose" style="cursor: pointer;" onclick="window.location='http://35.243.197.246:5000/${element.user_id}/add_pot';">>
                <div class="title_box">Register new plant</div>
                <div class="botonzito">
                <div class="botonfondo">+</div>
                </div>
                </div>`;
                $('.main').append(article);
        });
});
