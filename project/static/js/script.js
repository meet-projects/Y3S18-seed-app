open_signup_form = function(){
	var login_form = document.getElementById("login_form");
	var signup_form = document.getElementById("signup_form");

	login_form.style["display"] = 'none';
	signup_form.style["display"] = 'block';
}

open_login_form = function(){
	var login_form = document.getElementById("login_form");
	var signup_form = document.getElementById("signup_form");

	login_form.style["display"] = 'block';
	signup_form.style["display"] = 'none';
}




function myFunction() {
  var dots = document.getElementById("dots");
  var moreText = document.getElementById("more");
  var btnText = document.getElementById("myBtn");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more"; 
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less"; 
    moreText.style.display = "inline";
  }
}