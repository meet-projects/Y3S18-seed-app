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

open_add_art = function(id){
	var modal = document.getElementById("");
	modal.style["display"] = 'block';
}