function displaywetherdata(wetherdata) {

    console.log(wetherdata);

    let area = document.getElementById("area");
    area.innerHTML = wetherdata.name;
    let description = document.getElementById("description");
    description.innerHTML = wetherdata.weather[0].description;
    // var description = document.getElementById("icon");
    // description.innerHTML = wetherdata.weather[0].icon;
    let temp = document.getElementById("temp");
    temp.innerHTML = wetherdata.main.temp + "&#8451;";
    let temp_min = document.getElementById("temp_min");
    temp_min.innerHTML = wetherdata.main.temp_min + "&#8451;";
    let temp_max = document.getElementById("temp_max");
    temp_max.innerHTML = wetherdata.main.temp_max + "&#8451;";
    let wind = document.getElementById("windspeed");
    wind.innerHTML = wetherdata.wind.speed + "Mph";
    // take the wind direction in deg assign it to compuss and send it to degtocompuss funtion
    let compuss = wetherdata.wind.deg;
    degToCompass(compuss);
    let wind_direction = document.getElementById("wind_direction");
    wind_direction.innerHTML = directionCompuss;


};

// This function takes the wind direction in deg and converts it to compus.
// Thanks to these guys for this.
// https://stackoverflow.com/questions/7490660/converting-wind-direction-in-angles-to-text-words/7490772#7490772
function degToCompass(direction) {
    var val = Math.floor((direction / 22.5) + .5);
    var arr = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"];
    directionCompuss = arr[(val % 16)];
}

window.onload = function(){
    // get the input value and make it all capital
    var user_input = document.getElementById("user_input").value.toUpperCase();
    console.log(user_input);
    // if there is white spaces (weston super mare) remove the white space and  
    // replace it with hyphons.
    for (let i = 0; i < user_input.length; i++) {
        user_input = user_input.replace(" ", "-");
    }
    // if the input is null user london as default
    if (user_input) {
        inputUser = user_input;
    }
    else {
        inputUser = "LONDON";
    }

    var api_request = new XMLHttpRequest();
    api_request.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            the_response = api_request.responseText;
            console.log(the_response);
            wetherdata = JSON.parse(the_response);
            displaywetherdata(wetherdata);
        }
        else {
            console.log("this stuff is not working");
        }
    };

    endpoint = "https://api.openweathermap.org/data/2.5/weather?";    // who (www.example.com) - what server
    query = "q=" + inputUser + ",GB&units=metric";                 // what data do you want ?
    key = "&appid=7816d9f235c88adc096427a68ca872f2";                  // key to identify yourself to the server
    the_url = endpoint + query + key                                  // elemants for all api call(maybe not the key if open api)

    api_request.open("GET", the_url, true);         // Admit "GET" (method) and "true"
    api_request.send();
};