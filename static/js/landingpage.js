import navigateTo from "./routing.js";
import initNav from "./navbar.js";


function init() {
    //init the navbar functionality
    initNav()
    document.getElementById('signupBtn').addEventListener('click', function (){
        navigateTo('auth/signup')
    })
}

window.onload = init;