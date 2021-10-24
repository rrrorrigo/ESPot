window.addEventListener('DOMContentLoaded', (e) => {
    let user_id = document.getElementById('user_id').value;
    let images = {"Rosa":"../static/img/rose.png", "Kalanchoe":"../static/img/kalanchoe.png"}
    fetch(`http://35.243.197.246:5001/api/user_pots/${user_id}`)
		.then(response => response.json())
		.then(data => {
            data.forEach(element => {
                const article = `<div class="choose" style="cursor: pointer;" onclick="window.location='http://myespot.tech/${user_id}/my_plants/${element.id}';">
                <div class="title_box">
                <h2>${element.name}</h2>
                <h1>${element.Actual_humidity}%</h1>
                </div>
                <div>
                <img src="${img}" class="plant_img"></div>
                </div>`;
                $('.main').append(article);
            });
            const article = `<div class="choose" style="cursor: pointer;" onclick="window.location='http://myespot.tech/${user_id}/add_pot';">
                <div class="title_box">Register new plant</div>
                
                </div>`;
                $('.main').append(article);
        });
});
