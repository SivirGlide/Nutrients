
function init() {
    document.getElementById('signupBtn').addEventListener('click', function(){
    navigateTo('/auth/signup')
})
}

function navigateTo(url) {
    window.location.href = url;
}

window.onload = init;