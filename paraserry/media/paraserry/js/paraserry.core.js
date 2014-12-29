
$( document ).ready(function() {
	console.log("READY")

    $( "#cv" ).on( "click", function() {
        event.preventDefault();
        $('#resume-list').animatescroll({scrollSpeed:2000,easing:'easeInOutBack'});
    });

    $( "#work" ).on( "click", function() {
        event.preventDefault();
        $('#project-list').animatescroll({scrollSpeed:2000,easing:'easeInOutBack'});
    });

    $( "#contact" ).on( "click", function() {
        event.preventDefault();
        $('#contact-me').animatescroll({scrollSpeed:2000,easing:'easeInOutBack'});
    });

    $( "#about" ).on( "click", function() {
        event.preventDefault();
        $('#about-me').animatescroll({scrollSpeed:2000,easing:'easeInOutBack'});
    });
	
})