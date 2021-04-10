"use strict"

window.onload = (event) => {
   get_queen_color();
};

function get_queen_color(){
    const queenColor = document.getElementById('queen_colour');
    const date = new Date(), fullYear = date.getFullYear(), year = fullYear.toString(), yearend = year.charAt(year.length-1);
    let color;

    if (yearend == '1' || yearend == '6'){
        color = 'White';
    }
    else if(yearend == '2' || yearend == '7'){
        color = 'Yellow';
    }
    else if(yearend == '3' || yearend == '8'){
        color = 'Red';
    }
    else if(yearend == '4' || yearend == '9'){
        color = 'Green';
    }
    else if(yearend == '5' || yearend == '0'){
        color = 'Blue';
    }
    queenColor.innerHTML= `Recomended Queen colour is ${color}, as the year ends with a ${yearend},
    <a type="button" data-toggle="modal" data-target="#queenColorModal"><span class="queen_color_info_button">More Info?</span></a>`;
}