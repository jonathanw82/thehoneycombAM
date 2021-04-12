'use strict'

window.onload=(event)=>{
   tipsMonthData();
} 

const tips = document.getElementById("apiarytips");
const but = document.getElementById("mobileButton");

function displaytips(){
    // This finction changes the behaviour of the display tips button.
    tips.classList.add("desktop-tips-show");
    but.setAttribute('onclick','hideTips()');
    but.value = "Hide Tips";
}

function hideTips(){
    // This reverses the behaviour changed but the previouse function.
    tips.classList.remove("desktop-tips-show");
    tips.classList.add("desktop-tips");
    but.setAttribute('onclick','displaytips()');
    but.value = "Show Tips";
}

/* The tips function gets the browser date feature and the month as a
number 0 = Jan 11 = Dec that number is then used as the Index on the month array
displaying the relevent tip pulled for the apiaryTips.js page that then get injected into the dom.
*/

function tipsMonthData(){
    const month = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec];
    const info = document.getElementById('apiarytips');
    const monthIndex = new Date().getMonth();
    if(info){
        info.innerHTML = month[monthIndex];
    };   
}

/* This function looks and check to see if the correct window width had been 
reached by the event listener it then changes the class as required  by iterating 
over the array and changing the relevent logoDiv */

let x = window.matchMedia("(max-width: 425px)");
x.addEventListener("change", screensize(x)); // attach the event listerner and run the function.

function screensize(x) {
    const logoDiv1 = document.getElementById('logodiv1');
    const logoDiv2 = document.getElementById('logodiv2');
    const logoDiv3 = document.getElementById('logodiv3');
    const dives = [logoDiv1, logoDiv2, logoDiv3]; // add the loggo dives to the array

    if (x.matches) { // if x matches the window size do this
        for(const i of dives){ // on each iteration give access to each varaiable in dives array
            i && i.classList.remove("col-sm-3"); //if logoDiv1 exists logoDiv1.classlist.remove etc
            i && i.classList.add("col");
        }
    } else {
        for(const i of dives){
            i && i.classList.remove("col");
            i && i.classList.add("col-sm-3");
        }
    }
}
 
// This function injects a warning that something can not be undone after it is deleted.
function secondWarning(){
    document.getElementById('firstWarning').style.display = "None";
    document.getElementById('secondary-confirm').innerHTML = `This can not be undone! To Permanently delete this apiary please press Delete
                            <br> <input class="btn btn-danger confirmBut" type="submit" value="Delete"></input>`;
};