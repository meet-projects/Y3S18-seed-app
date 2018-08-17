$(document).ready(function() {
    debugger;
});

//index.html
function switch_login_signup(){
	if(document.getElementById("signup").style.display=="none"){
		document.getElementById("login").style.display = "none";
		document.getElementById("signup").style.display = "block";
		document.getElementById("login_signup_text").innerHTML = "Already have an account? <b>Login!</b>";
		document.getElementById("login_signup_title").innerHTML = "Sign up";
	}
	else{
		document.getElementById("login").style.display = "block";
		document.getElementById("signup").style.display = "none";
		document.getElementById("login_signup_text").innerHTML = "Don't have an account? <b>Sign up!</b>";
		document.getElementById("login_signup_title").innerHTML = "Login";
	}
}

//option.html
function student_hover(){
	var text = document.getElementById("student-option");
	var size = 6;
	var elem = document.getElementById("student-choice"); 
    var pos = 100;
    var id = setInterval(frame, 10);
    function frame() {
        if (pos == 120) {
            clearInterval(id);
        } else {
        	size = size+0.05;
        	text.style.fontSize = size + 'em';
            pos++; 
            elem.style.backgroundSize = pos + '%'; 
        }
    }
}

function reverse_student_hover(){
	var text = document.getElementById("student-option");
	var size = 7;
	var elem = document.getElementById("student-choice"); 
    var pos = 120;
    var id = setInterval(frame, 10);
    function frame() {
        if (pos == 100) {
            clearInterval(id);
        } else {
        	size = size-0.05;
        	text.style.fontSize = size + 'em';
            pos--; 
            elem.style.backgroundSize = pos + '%'; 
        }
    }
}

function instructor_hover(){
	var text = document.getElementById("instructor-option");
	var size = 6;
	var elem = document.getElementById("instructor-choice"); 
    var pos = 100;
    var id = setInterval(frame, 10);
    function frame() {
        if (pos == 120) {
            clearInterval(id);
        } else {
        	size = size+0.05;
        	text.style.fontSize = size + 'em';
            pos++; 
            elem.style.backgroundSize = pos + '%'; 
        }
    }
}

function reverse_instructor_hover(){
	var text = document.getElementById("instructor-option");
	var size = 7;
	var elem = document.getElementById("instructor-choice"); 
    var pos = 120;
    var id = setInterval(frame, 10);
    function frame() {
        if (pos == 100) {
            clearInterval(id);
        } else {
        	size = size-0.05;
        	text.style.fontSize = size + 'em';
            pos--; 
            elem.style.backgroundSize = pos + '%'; 
        }
    }
}