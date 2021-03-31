window.onload=(event)=>{
   tips();
} 

// This finction changes the behaviour of the display tips button.
function displaytips(){
    document.getElementById("apiarytips").classList.add("desktop-tips-show");
    var but = document.getElementById("mobileButton");
    but.setAttribute('onclick','hideTips()');
    but.value = "Hide Tips";
}

// This reverses the behaviour changed but the previouse function.
function hideTips(){
    let tips = document.getElementById("apiarytips");
    tips.classList.remove("desktop-tips-show");
    tips.classList.add("desktop-tips");
    var but = document.getElementById("mobileButton");
    but.setAttribute('onclick','displaytips()');
    but.value = "Show Tips";
}

/* This finction looks and check to see if the correct window width had been 
reached by the even listener it then changes the class as required */
var x = window.matchMedia("(max-width: 425px)");
x.addEventListener("change", screensize(x)); // attach the event listerner and run the function.

function screensize(x) {
    logoDiv1 = document.getElementById('logodiv1');
    logoDiv2 = document.getElementById('logodiv2');
    logoDiv3 = document.getElementById('logodiv3');

    if (x.matches) { // if x matches the window size do this
        logoDiv1.classList.remove("col-sm-3");
        logoDiv2.classList.remove("col-sm-3");
        logoDiv3.classList.remove("col-sm-3");
        logoDiv1.classList.add("col");
        logoDiv2.classList.add("col");
        logoDiv3.classList.add("col");
        
    } else {
        console.log("back to original");
        logoDiv1.classList.remove("col");
        logoDiv2.classList.remove("col");
        logoDiv3.classList.remove("col");
        logoDiv1.classList.add("col-sm-3");
        logoDiv2.classList.add("col-sm-3");
        logoDiv3.classList.add("col-sm-3");
    }
}
 
// This function injects a warning that something can not be undone after it is deleted.
function secondWarning(){
    document.getElementById('firstWarning').style.display = "None";
    document.getElementById('secondary-confirm').innerHTML = `This can not be undone! To Permanently delete this apiary please press Delete
                            <br> <input class="btn btn-danger confirmBut" type="submit" value="Delete"></input>`;
};

/* The tips function uses a switch case and the browser date feature to 
decide on what month it is then display's the relevent tip pulled for the 
apiaryTips.js page that then get injected into the dom.
*/
function tips(){
    let info = document.getElementById('apiarytips');
    switch(new Date().getMonth()){
        case 0:
            info.innerHTML = jan;
            break;
        case 1:
            info.innerHTML = feb;
            break;
        case 2:
            info.innerHTML = mar;
            break;
        case 3:
            info.innerHTML = apr;
            break;
        case 4:
            info.innerHTML = may;
            break;
        case 5:
            info.innerHTML = jun;
            break;
        case 6:
            info.innerHTML = jul;
            break;
        case 7:
            info.innerHTML = aug;
            break;
        case 8:
            info.innerHTML = sep;
            break;
        case 9:
            info.innerHTML = oct;
            break;
        case 10:
            info.innerHTML = nov;
            break;
        case 11:
            info.innerHTML = dec;
            break;
    }
}
