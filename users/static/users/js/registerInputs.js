
// Capitalize user inputs (Firstname and last name)
document.querySelector("#id_first_name").addEventListener("change", function (){
    var splitStr = document.querySelector("#id_first_name").value.toLowerCase().split(' ');
       for (var i = 0; i < splitStr.length; i++) {
           splitStr[i] = splitStr[i].charAt(0).toUpperCase() + splitStr[i].substring(1);
       }
    var resFirstName = splitStr.join(' ');
    document.querySelector("#id_first_name").value = resFirstName;
});
document.querySelector("#id_last_name").addEventListener("change", function (){
    var splitStr = document.querySelector("#id_last_name").value.toLowerCase().split(' ');
       for (var i = 0; i < splitStr.length; i++) {
           splitStr[i] = splitStr[i].charAt(0).toUpperCase() + splitStr[i].substring(1);
       }
    var resFirstName = splitStr.join(' ');
    document.querySelector("#id_last_name").value = resFirstName;
});
// Setting firstName and Lastname required because by default they're not
document.querySelectorAll(".col-form-label")[1].innerHTML += "*";
document.querySelectorAll(".col-form-label")[2].innerHTML += "*";
document.querySelector("#id_first_name").required = true;
document.querySelector("#id_last_name").required = true;

// alert message when checkBox is not checked
document.querySelector("#signUp").addEventListener("click", function (){
if (!document.getElementById("checkBox").checked){
  document.getElementById('errorMessage').innerHTML ="You must agree to the terms.";
  document.getElementById("errorMessage").className = "alert alert-danger";
}
});
