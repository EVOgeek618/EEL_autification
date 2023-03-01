
// Onclick of the button
document.querySelector("button").onclick = function () {
  // Call python's random_python function
    var login = document.getElementsByClassName('login')[0].value
    var password = document.getElementsByClassName('password')[0].value
    eel.check(login, password)(function(data) {
        if (data[0] != "Done"){
        document.querySelector(".error").innerHTML = data[0];
    }
        else{
           document.querySelector(".error").innerHTML = "Привествую, "+data[1];
           document.getElementsByClassName('form')[0].style.display = "none"
            document.getElementsByClassName('submit')[0].style.display = "none"
            document.querySelector("a").style.display = "none"
        }
    })
}