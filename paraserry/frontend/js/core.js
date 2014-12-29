
$( document ).ready(function() {
	console.log("READY")

    $( "#cv" ).on( "click", function() {
        event.preventDefault();
        $('#resume-list').animatescroll({scrollSpeed:1800,easing:'easeOutBounce'});
    });

    $( "#work" ).on( "click", function() {
        event.preventDefault();
        $('#project-list').animatescroll({scrollSpeed:1800,easing:'easeOutBounce'});
    });

    $( "#contact" ).on( "click", function() {
        event.preventDefault();
        $('#contact-me').animatescroll({scrollSpeed:1800,easing:'easeOutBounce'});
    });

    $( "#about" ).on( "click", function() {
        event.preventDefault();
        $('#about-me').animatescroll({scrollSpeed:1800,easing:'easeOutBounce'});
    });
	
})