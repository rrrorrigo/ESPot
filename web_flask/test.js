window.addEventListener('DOMContentLoaded', (e) => {
    function updateAllEvents() { 
        fetch('http://35.243.197.246:5001/api/pots')
            .then(response => response.json())
            .then(data => console.log(data))
    }
    let display = setInterval(updateAllEvents, 2000);
});
