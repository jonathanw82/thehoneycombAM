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

/* This function looks and check to see if the correct window width had been 
reached by the even listener it then changes the class as required */

let x = window.matchMedia("(max-width: 425px)");
x.addEventListener("change", screensize(x)); // attach the event listerner and run the function.

function screensize(x) {
    const logoDiv1 = document.getElementById('logodiv1');
    const logoDiv2 = document.getElementById('logodiv2');
    const logoDiv3 = document.getElementById('logodiv3');
  
    if (x.matches) { // if x matches the window size do this
        logoDiv1 && logoDiv1.classList.remove("col-sm-3");
        logoDiv2 && logoDiv2.classList.remove("col-sm-3");
        logoDiv3 && logoDiv3.classList.remove("col-sm-3");
        logoDiv1 && logoDiv1.classList.add("col");
        logoDiv2 && logoDiv2.classList.add("col");
        logoDiv3 && logoDiv3.classList.add("col");
        
    } else {
        logoDiv1 && logoDiv1.classList.remove("col");
        logoDiv2 && logoDiv2.classList.remove("col");
        logoDiv3 && logoDiv3.classList.remove("col");
        logoDiv1 && logoDiv1.classList.add("col-sm-3");
        logoDiv2 && logoDiv2.classList.add("col-sm-3");
        logoDiv3 && logoDiv3.classList.add("col-sm-3");
    }
}
 
// This function injects a warning that something can not be undone after it is deleted.
function secondWarning(){
    document.getElementById('firstWarning').style.display = "None";
    document.getElementById('secondary-confirm').innerHTML = `This can not be undone! To Permanently delete this apiary please press Delete
                            <br> <input class="btn btn-danger confirmBut" type="submit" value="Delete"></input>`;
};

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