import navigateTo from "./routing.js";


function init() {
    document.getElementById('signupBtn').addEventListener('click', function (){
        navigateTo('auth/signup')
    })
}

window.onload = init;