import navigateTo from "./routing.js";


export default function initNav() {
    document.getElementById('signupBtnNav').addEventListener('click', function (){
        navigateTo('auth/signup')
    })

    document.getElementById('loginBtn').addEventListener('click', function (){
        navigateTo('auth/signin')
    })

    document.getElementById('aboutBtn').addEventListener('click', function (){
        navigateTo('/about')
    })
}