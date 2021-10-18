window.addEventListener('DOMContentLoaded', (e) => {
    setInterval(async function(){
    const response = await fetch('http://35.243.197.246:5001/api/pots/0b9e88b6-7663-47c0-8ac4-b91954bd818e');
    const json = await response.json();
        hum.textContent = json;
    }, 2000);
});
