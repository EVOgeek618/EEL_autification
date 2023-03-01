
document.querySelector(".submit").onclick = function () {
    var login = document.getElementsByClassName('login')[0].value
    var email = document.getElementsByClassName('email')[0].value
    var password = document.getElementsByClassName('password')[0].value
    var password_2 = document.getElementsByClassName('password_2')[0].value

    eel.register(login, email, password, password_2)(function(data) {
        if (data != "Done"){
        document.querySelector(".error").innerHTML = data;
    }
        else{
           window.location.href="result.html";
        }
    })
}