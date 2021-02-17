/*

Template:  Theme Name
Author: author name
Version: 1
Design and Developed by: 
NOTE: If you have any note put here. 

*/
/*================================================
[  Table of contents  ]
================================================
	01. jQuery MeanMenu
	02. wow js active
	03. scrollUp jquery active
	04. slick carousel 

 
======================================
[ End table content ]
======================================*/


(function($) {
    "use strict";

/* carousel activator start */
$('.owl-carousel').owlCarousel({
    loop:true,
    margin:0,
    responsiveClass:true,
    responsive:{
        0:{
            items:1,
            nav:true
        },
        600:{
            items:1,
            nav:false
        },
        1000:{
            items:1,
            nav:true,
            loop:true
        }
    }
});
/* carousel activator end */

/*------------------------------------------------
      Top menu stick
     -------------------------------------------------- */
$(window).scroll(function() {
if ($(this).scrollTop() > 112){  
    $('.sticky-header').addClass("sticky");
  }
  else{
    $('.sticky-header').removeClass("sticky");
  }
});



    /*-------------------------------------------
    	01. jQuery MeanMenu
    --------------------------------------------- */
    //jQuery('nav#dropdown').meanmenu();


    /*-------------------------------------------
    	02. wow js active
    --------------------------------------------- */
    new WOW().init();


    /*-------------------------------------------
    	03. scrollUp jquery active
    --------------------------------------------- */
    $.scrollUp({
        scrollText: '<i class="fa fa-angle-up"></i>',
        easingType: 'linear',
        scrollSpeed: 900,
        animation: 'fade'
    });


    /*-------------------------------------------
    	04. slick carousel 
    --------------------------------------------- */
    


    /*************************
          tooltip
    *************************/
    $('[data-toggle="tooltip"]').tooltip();





})(jQuery);





