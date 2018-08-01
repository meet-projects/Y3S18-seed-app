
//getdata is in html template "login"

$( document ).ready(function() {
  getdata = JSON.parse(getdata)
  console.log(getdata);
  var show = getdata["show"];
  if(show == null){
    show = 'login';
  }
  console.log(show);

  if(show == 'login'){
    console.log('will open login');
     open_login_form()
  }
  else{
    console.log('will open signup');
    open_signup_form()
  }

  var warning = getdata["err_msg"];
  console.log(warning)
  if(warning != null){
    console.log('warning confirmed')
    if(warning == "username cannot be empty"){
      var textbox = document.getElementById("signup_textbox_username");
      textbox.style["border-color"] = "red";
      var message = document.getElementById("username_error_message");
      message.innerText = "username cannot be empty";
      message.style["display"] = "block";
    }

    if(warning == "display name cannot be empty"){
      var textbox = document.getElementById("signup_textbox_displayname");
      textbox.style["border-color"] = "red";
      var message = document.getElementById("displayname_error_message");
      message.innerText = "display name cannot be empty";
      message.style["display"] = "block";
    }

    if(warning == "password cannot be empty"){
      var textbox = document.getElementById("signup_textbox_password");
      textbox.style["border-color"] = "red";
      var message = document.getElementById("password_err_msg");
      message.innerText = "password cannot be empty";
      message.style["display"] = "block";
    }

    if(warning == "name taken"){
      var textbox = document.getElementById("signup_textbox_username");
      textbox.style["border-color"] = "red";
      var message = document.getElementById("username_error_message");
      message.innerText = "username is taken";
      message.style["display"] = "block";
    }

    if(warning == "passwords do not match"){
      var textbox = document.getElementById("signup_textbox_password_confirm");
      textbox.style["border-color"] = "red";
      var message = document.getElementById("pass_dont_match_msg");
      message.innerText = "passwords do not match";
      message.style["display"] = "block";
    }

  }
});

open_signup_form = function(){
  console.log("opening signup")
	var login_form = document.getElementById("login_container");
	var signup_form = document.getElementById("signup_container");

  reset_warnings();

	login_form.style["display"] = 'none';
	signup_form.style["display"] = 'block';
}

open_login_form = function(){
	var login_form = document.getElementById("login_container");
	var signup_form = document.getElementById("signup_container");

  reset_warnings();

	login_form.style["display"] = 'block';
	signup_form.style["display"] = 'none';
}

reset_warnings = function(){
  console.log('cleaning')
  var warning_messages = document.getElementsByClassName("error_message");
  console.log(warning_messages.length)
  var login_textboxes = document.getElementsByClassName("login_page_textbox");
  console.log(login_textboxes.length)

  for (var i = 0; i < warning_messages.length; i++) {
    warning_messages[i].style["display"] = "none";
  }


  for (var i = 0; i < login_textboxes.length; i++) {
    login_textboxes[i].style["border-color"] = "white";
  }

}