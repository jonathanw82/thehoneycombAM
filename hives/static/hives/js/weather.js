// encrypted keys
var weather_key = "81op2521sr2q808222668qn88ss490ps".keyHelper();
var geo_key = "71449q7rsn1296418593s99p378462oo".keyHelper();

function displaywetherdata(wetherdata) {

    let area = document.getElementById("area");
    area.innerHTML = wetherdata.name;
    let description = document.getElementById("description");
    description.innerHTML = wetherdata.weather[0].description;
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
    // get the weather from open weather map api
    var api_request = new XMLHttpRequest();
    api_request.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            the_response = api_request.responseText;
            wetherdata = JSON.parse(the_response);
            displaywetherdata(wetherdata);
        }
    };
    endpoint = "https://api.openweathermap.org/data/2.5/weather?";
    query = "q=" + inputUser + ",GB&units=metric";                 
    key = '&appid=' + weather_key;                  
    the_url = endpoint + query + key                                  

    api_request.open("GET", the_url, true); 
    api_request.send();

    // Get the land and lat of the user input from the geocage api
    var api_requestGeo = new XMLHttpRequest();
    api_requestGeo.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            geo_response = api_requestGeo.responseText;
            geo = JSON.parse(geo_response);
            displaygeodata(geo);
            console.log(geo);
        }
    };                              
    endpointGeo = "https://api.opencagedata.com/geocode/v1/json?q=" + inputUser + ',UK&key=' + geo_key;

    api_requestGeo.open("GET", endpointGeo, true); 
    api_requestGeo.send();
};

function displaygeodata(){
    let long = document.getElementById("long");
    long.innerHTML = geo.results[0].geometry.lng;
    let lat = document.getElementById("lat");
    lat.innerHTML = geo.results[0].geometry.lat;
}