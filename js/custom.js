$(document).ready(function() {

//REMOVES JAVASCRIPT FIX CLASSES
	$('#portfolio-content').removeClass("js-off-overflow");
	$('.portfolio-thumbs').removeClass("js-off-position");
	
//INITIALIZES PRETTYPHOTO PLUGIN

	$("a[rel^='prettyPhoto']").prettyPhoto({theme:'light_square'}); //choose between different styles / dark_rounded / light_rounded / dark_square / light_square / facebook /

	
//INITIALIZES TWITTER FEED PLUGIN

	$('#twitter-feed').tweet({
		username: "yt_astro",  //just enter your twitter username
		join_text: "auto",
		avatar_size: null,
		count: 2, //number of tweets showing
		auto_join_text_default: "",
		loading_text: "loading latest tweets..." //text displayed while loading tweets
	});

//ANYTHING SLIDER NAVIGATION BUTTONS
	
	var q = ["#prev-button", "#next-button", ".arrow", ".forward", ".back"];
	var buttons = q.join(", ");
	
	$(".featured").hover( function() {
		$(buttons).stop().show()
	}).mouseleave( function() {
		$(buttons).stop().hide()
	});
	
	
//NAVIGATION
	
	$('#navigation').localScroll();
	$('#navigation li a').click( function () {
		$('#navigation li a').removeClass("active");
		$(this).addClass("active");
	});

	$('#logo h1 a').click(function(){ 		
		$('#navigation li a').removeClass("active");
		$('#navigation li:first a').addClass("active");
		$('html, body').animate({scrollTop: 0});
		
	});

// CONTACT FORM 
		
	$('#contact_form').ajaxForm({
		target: '#message-outcome',
			beforeSubmit: function() {
				$('#message-outcome').addClass('visible');
			},
				success: function() {
					$('#message-outcome').show();
				}
	});
		
	$('.textbox, #message, #comment').focus(function (){
		$(this).css({borderColor : '#d1d1d1'});
			$(this).blur(function (){
				$(this).css({borderColor : '#e1e1e1'});
			});
	});

	
//PORTFOLIO NAVIGATION
	
	$("ul.portfolio-nav").tabs("#portfolio > #portfolio-content > ul.portfolio-thumbs", {effect: 'fade', fadeInSpeed: 800, fadeOutSpeed: 800});


// PORTFOLIO HOVER EFFECT	

 $('ul.portfolio-thumbs li').hover(function(){  
         $(".overlay", this).stop().animate({top:'0px'},{queue:false,duration:300});  
     }, function() {  
        $(".overlay", this).stop().animate({top:'190px'},{queue:false,duration:300});  
    });  

	
//TOGGLE PANELS

	$('.toggle-content').hide();  //hides the toggled content, if the javascript is disabled the content is visible

	$('.toggle-link').click(function () {
		if ($(this).is('.toggle-close')) {
			$(this).removeClass('toggle-close').addClass('toggle-open').parent().next('.toggle-content').slideToggle(300);
			return false;
		} 
		
		else {
			$(this).removeClass('toggle-open').addClass('toggle-close').parent().next('.toggle-content').slideToggle(300);
			return false;
		}
	});

    var bburl
    bburl = "https://api.bitbucket.org/1.0/repositories/yt_analysis/yt/events/";
    $.getJSON(bburl + "?limit=10&callback=?", populate_events('yt'));
    bburl = "https://api.bitbucket.org/1.0/repositories/yt_analysis/yt/issues/";
    $.getJSON(bburl + "?limit=5&callback=?", populate_issues('yt'));
    /*populate_forks("yt")( [ {username:'sskory'},
                            {username:'MatthewTurk'},
                            {username:'BrittonSmith'},
                            {username:'samskillman'},
                            {username:'atmyers'},
                            {username:'jwise77'},
                            {username:'sklemer'},
                            {username:'caseywstark'},
                            {username:'gsiisg'},
                            {username:'chummels', reponame:'yt-chummels'},
                          ]);*/

   $('#notification').delay(10).slideDown('slow');
   $('#notification').delay(30000).slideUp('slow');
   $("a[rel]").overlay({
        mask: { color: "#555",
           loadSpeed: 200,
           opacity: 0.9
        },
        onBeforeLoad: function() {
            $("#slider-cycle").cycle("pause");
            var wrap = this.getOverlay().find(".content_wrap");
            wrap.html("<object type=\"application/x-shockwave-flash\" width=\"640\" height=\"320\" data=\"http://vimeo.com/hubnut/?user_id=user3192834&amp;color=4a8f43&amp;background=000000&amp;fullscreen=1&amp;slideshow=0&amp;stream=channel&amp;id=243779&amp;server=vimeo.com\"> <param name=\"quality\" value=\"best\" />       <param name=\"allowfullscreen\" value=\"true\" />     <param name=\"allowscriptaccess\" value=\"always\" />   <param name=\"scale\" value=\"showAll\" /> <param name=\"movie\" value=\"http://vimeo.com/hubnut/?user_id=user3192834&amp;color=4a8f43&amp;background=000000&amp;fullscreen=1&amp;slideshow=0&amp;stream=channel&amp;id=243779&amp;server=vimeo.com\" /></object>");
        },
        onBeforeClose: function() {
            $("#slider-cycle").cycle("resume");
            var wrap = this.getOverlay().find(".content_wrap");
            wrap.html("");
        }
        }); 
});	//END of jQuery





