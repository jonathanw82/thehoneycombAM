
function secondWarning(){
    document.getElementById('firstWarning').style.display = "None";
    document.getElementById('secondary-confirm').innerHTML = `This can not be undone! To Permanently delete this apiary please press Delete
                            <br> <input class="btn btn-danger confirmBut" type="submit" value="Delete"></input>`
}
 