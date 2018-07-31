
open_signup_form = function(){
  console.log("rr")
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

// $(function() {
//   $('a#test').bind('click', function() {
//     $.getJSON('/background_process_test',
//         function(data) {
//       //do nothing
//     });
//     return false;
//   });
// });
$( document ).ready(function() {
    console.log( "ready!" );
});


$(function(){

  $('#register_submit').click(function() {
        $.ajax({
            url: '/register_test',
            data: $('#signup_form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

});


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
