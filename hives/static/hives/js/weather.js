// if the current temp is less than 20 makle the weather box blue
// if greater or equal to 20 then make it red 
temp = document.getElementById('current_tempdisp').innerHTML;
boxcolor = document.getElementById('weatherbox');
separator = document.getElementById('separator');
if (temp >= 20) {
    boxcolor.classList.add('weatherboxhot');
    separator.classList.add('separatorhot');
}


let weatherAlert = document.getElementById('alert_heading');
let opacity = 0;
let intervalID = 0;
// if there is a westher alert
if (weatherAlert) {
    // get the opacity
    opacity = Number(window.getComputedStyle(weatherAlert).getPropertyValue("opacity"));
    // start the show function
    show();
    function show() {
        // set the interval to 100 miliseconds
        intervalID = setInterval(function () {
            if (opacity < 1) {
                opacity = opacity + 0.1;
                weatherAlert.style.opacity = opacity;
            }
            else {
                // clear the timer
                clearInterval(intervalID);
                // start the next function
                hide();
            }
        }, 100);
    }
    function hide() {
        intervalID = setInterval(function () {
            if (opacity > 0) {
                opacity = opacity - 0.1;
                weatherAlert.style.opacity = opacity;
            }
            else {
                clearInterval(intervalID);
                show();
            }
        }, 100);
    }
}
