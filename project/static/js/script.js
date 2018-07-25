$(document).ready(function() {
    debugger;
});

var config = {
    apiKey: "AIzaSyCMcif23MajRqImpvSj34QcE7Br47Q_Sbw",
    authDomain: "easylicense-e9174.firebaseapp.com",
    databaseURL: "https://easylicense-e9174.firebaseio.com",
    projectId: "easylicense-e9174",
    storageBucket: "easylicense-e9174.appspot.com",
    messagingSenderId: "467829835580"};

app = firebase.initializeApp(config);
auth = firebase.auth(app);
db = firebase.database(app);
databaseRef = db.ref();

function book(teacher_id){
	var booking = {
    	name : document.forms["booking_form"]["name"].value;
    	phone_num : document.forms["booking_form"]["num"].value;
    	teacher :  document.forms["booking_form"]["teacher"].value;
    	done : false;
	}
	databaseRef.child("bookings").child(document.forms["booking_form"]["num"].value).set(booking);
}