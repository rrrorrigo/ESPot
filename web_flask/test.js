window.addEventListener('DOMContentLoaded', (e) => {
    function updateAllEvents() { 
        $.getJSON('http://35.243.197.246:5001/api/pots', function(data, status){
            console.log(data);
        });  
    }
    let display = setInterval(updateAllEvents, 2000);
});
