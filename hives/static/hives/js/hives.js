"use strict";
function secondWarning(){
    document.getElementById('firstWarning').style.display = "None";
    document.getElementById('secondary-confirm').innerHTML = `This can not be undone! To Permanently delete this hive please press Delete
                            <br> <input class="btn btn-danger confirmBut" type="submit" value="Delete"></input>`
}


document.getElementById("showHide").addEventListener("click", function(){
    const archive = document.getElementById('archiveRow');
    const buttonArchive = document.getElementById("showHide");
    if (archive.classList.contains('hide')){
        archive.classList.remove('hide');
        archive.classList.add('show');
        buttonArchive.innerHTML = 'Hide Archive';
    }else{
        archive.classList.remove('show');
        archive.classList.add('hide');
        buttonArchive.innerHTML = 'Show Archive';
    }
});