$(document).ready(function() {
	var islogged = <% session["user_id"] %>
	isNaN(islogged) alert("nan");
	else alert(<%= session["user_id"] %>)
});
