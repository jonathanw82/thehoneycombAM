window.onload=(event)=>{
   tips();
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
