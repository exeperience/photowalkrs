$(function() {
		// set opacity to nill on page load
		$("ul#menu span").css("opacity","0");
		// on mouse over
		$("ul#menu span").hover(function () {
			// animate opacity to full
			$(this).stop().animate({
				opacity: 1
			}, 'slow');
		},
		// on mouse out
		function () {
			// animate opacity to nill
			$(this).stop().animate({
				opacity: 0
			}, 'slow');
		});
	});

$(document).ready(function() {
	$("div.panel_button").click(function(){
		$("div#lpanel").animate({
			height: "500px"
		})
		.animate({
			height: "400px"
		}, "fast");
		$("div.panel_button").toggle();
	
	});	
	
   $("div#hide_button").click(function(){
		$("div#lpanel").animate({
			height: "30px"
		}, "fast");
		
	
   });	
	
});

$(document).ready(function() {
	$("div.create").click(function(){
		$("div.upload_form").animate({
			height: "300px"
		})
		.animate({
			height: "200px"
		}, "fast");
		$("div.create").toggle();
	
	});	
	
   $("div#hd").click(function(){
		$("div.upload_form").animate({
			height: "0px"
		}, "fast");
		
	
   });	
	
});

$("div.desc > p").hide();
$("div.desc > p:nth-child(1)").fadeIn("slow");
$('.imgs').load('1.html');
 
    /*submenu jquery*/
	$("div.sitems > div").click(function() {
        var index = $(this).index();
		$(this).parent().children().removeClass("now");
  		$("div.desc > p").hide();
  		$("div.desc > p").eq(index-6).fadeIn("slow");
  		$(this).addClass("now");
		$('.imgs').load((index+1)+'.html');
        /*$("p.test").show();
		$("p.test").html("Index " + index + " was clicked");*/
    });
	/*main menu sublist jquery*/
	 $("#trans-nav > li").children().children().click(function() {
        var index = $(this).index();
		$("div.sitems").children().removeClass("now");
  		$("div.desc > p").hide();
  		$("div.desc > p").eq(index-6).fadeIn("slow");
  		$("div.sitems > div").eq(index).addClass("now");
		$('.imgs').load((index+1)+'.html');
    });
	/*main menu selection jqeury*/
	$("#trans-nav > li").click(function() {
        var index = $(this).index();
		$(this).parent().children().removeClass("selected");
  		$(this).addClass("selected");
    });