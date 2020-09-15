
/*  On document load this code looks at the window size and looks to see 
if it is greater that 425px wide, if so remove one class and add another
and vice versa. */

document.addEventListener("DOMContentLoaded", function(){

var screensize = document.documentElement.clientWidth;
var windowSize = document.getElementById('login-boxsize');
if (screensize > 426 && screensize < 769){
    
    windowSize.classList.remove('col-md-6');
    windowSize.classList.add('col-md-7');
}
else{
    windowSize.classList.remove('col-md-7');
    windowSize.classList.add('col-md-6');
}
});