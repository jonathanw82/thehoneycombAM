window.onload=(event)=>{
   tips();
} 

function displaytips(){
    document.getElementById("apiarytips").classList.add("desktop-tips-show");
    var but = document.getElementById("mobileButton");
    but.setAttribute('onclick','hideTips()');
    but.value = "Hide Tips";
}

function hideTips(){
    let tips = document.getElementById("apiarytips");
    tips.classList.remove("desktop-tips-show");
    tips.classList.add("desktop-tips");
    var but = document.getElementById("mobileButton");
    but.setAttribute('onclick','displaytips()');
    but.value = "Show Tips";
}

var x = window.matchMedia("(max-width: 425px)");
x.addEventListener("change", screensize(x));

function screensize(x) {
    logoDiv1 = document.getElementById('logodiv1');
    logoDiv2 = document.getElementById('logodiv2');
    logoDiv3 = document.getElementById('logodiv3');

    if (x.matches) {
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
 

function secondWarning(){
    document.getElementById('firstWarning').style.display = "None";
    document.getElementById('secondary-confirm').innerHTML = `This can not be undone! To Permanently delete this apiary please press Delete
                            <br> <input class="btn btn-danger confirmBut" type="submit" value="Delete"></input>`;
};


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
            iinfo.innerHTML = mar;
            break;
        case 3:
            iinfo.innerHTML = apr;
            break;
        case 4:
            iinfo.innerHTML = may;
            break;
        case 5:
            iinfo.innerHTML = jun;
            break;
        case 6:
            iinfo.innerHTML = jul;
            break;
        case 7:
            iinfo.innerHTML = aug;
            break;
        case 8:
            iinfo.innerHTML = sep;
            break;
        case 9:
            iinfo.innerHTML = oct;
            break;
        case 10:
            iinfo.innerHTML = nov;
            break;
        case 11:
            info.innerHTML = dec;
            break;
    }
}