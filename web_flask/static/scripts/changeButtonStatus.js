window.addEventListener('DOMContentLoaded', (e) => {
    changeTextButton();
    const onoff = document.getElementById("onofftext");

    $('#onoff').click(function (){
        changeTextButton();
        });
    function changeTextButton() {
    fetch(`http://35.243.197.246:5001/api/pots/${pot_id}`).then(response => response.json())
    .then(data => {
        if (data[0].Turned_ON) {
            onoff.textContent = "ON";
            onoff.style.color = "rgb(70, 117, 70)";
            onoff.style.paddingLeft = "27%";
        } else {
            onoff.innerHTML = "OFF";
            onoff.style.color = "rgb(128, 141, 128)";
            onoff.style.paddingLeft = "23%";
        }});
    };
});