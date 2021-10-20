function onoff() {
let onoff = document.getElementById("onoff");
if (compareColour("#B6CFB6", onoff.style.color)) {
    onoff.style.color = "rgb(128, 141, 128)";
} else {
    onoff.style.color = "rgb(182, 207, 182)";
}
}

function compareColour(col1, col2) {
    var e = document.createElement('span')
    document.body.appendChild(e);
    // standardise
    e.style.color = col1;
    col1 = window.getComputedStyle(e).color;
    e.style.color = col2;
    col2 = window.getComputedStyle(e).color;
    // cleanup
    document.body.removeChild(e);
    return col1 === col2;
}
