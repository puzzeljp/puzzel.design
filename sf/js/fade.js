$(function() {

$("#header").css("opacity","1.0");
		
$("#header").hover(function () {
										  
$(this).stop().animate({
opacity: 0.8
}, "slow");
},
		
function () {
			
$(this).stop().animate({
opacity: 1.0
}, "slow");
});
});

$(function() {

$("li").css("opacity","0.4");
		
$("li").hover(function () {
										  
$(this).stop().animate({
opacity: 1.0
}, "slow");
},
		
function () {
			
$(this).stop().animate({
opacity: 0.4
}, "slow");
});
});

$(function() {

$(".now").css("opacity","1.0");
		
$(".now").hover(function () {
										  
$(this).stop().animate({
opacity: 0.4
}, "slow");
},
		
function () {
			
$(this).stop().animate({
opacity: 1.0
}, "slow");
});
});

$(function() {

$("h2").css("opacity","1.0");
		
$("h2").hover(function () {
										  
$(this).stop().animate({
opacity: 0.5
}, "slow");
},
		
function () {
			
$(this).stop().animate({
opacity: 1.0
}, "slow");
});
});


$(function() {

$(".is").css("opacity","1.0");
		
$(".is").hover(function () {
										  
$(this).stop().animate({
opacity: 0.2
}, "fast");
},
		
function () {
			
$(this).stop().animate({
opacity: 1.0
}, "slow");
});
});


$(function() {

$(".none").css("opacity","0.2");
		
$(".none").hover(function () {
										  
$(this).stop().animate({
opacity: 1.0
}, "fast");
},
		
function () {
			
$(this).stop().animate({
opacity: 0.2
}, "slow");
});
});