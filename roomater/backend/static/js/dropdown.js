$(document).ready(function() {
	$('dd').hide();
	$("#tell_room").find('h4').click(function() {
                $(this).next().slideToggle();
            });
	$('#create_account').find('h4').click(function() {
                $(this).next().slideToggle();
            });
        $('#tell_yourself').find('h4').click(function() {
                $(this).next().slideToggle();
            });
	$('.dropdown').click(function() {
		$(this).next().slideToggle();
	    });
    });