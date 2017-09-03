/* ------------------------------------------ */
/*             TABLE OF CONTENTS
/* ------------------------------------------ */

/*   01 - Revolution Slider     */
/*   02 - MENU                  */
/*   03 - Portfolio             */
/*   04 - Sticky Navigation     */
/*   05 - Scroll Div            */
/*   06 - owl Slider            */
/*   07 - Hover Portfolio       */
/*   08 - Hover Shop Content    */
/*   09 - Search                */
/*   10 - Contact form          */
/*   11 - Fancybox              */
/*   12 - Progress-Bar          */
/*   13 - Option-Box            */
/*   14 - Accordions            */
/*   15 - Flickr                */
/*   16 - Tweet                 */
/*   17 - Items Number Shop     */
/*   18 - Shop Checkout         */
/*   19 - Shop images zoom      */
/*   20 - Features us           */
/*   21 - Case Studies          */
/*   22 - Tabs Work Process     */
/*   23 - Back to top button    */
/*   24 - Parallax Mobile       */
/*   25 - Tooltip               */
/*   26 - WOW Animation         */
/*   27 - Date Count down       */

/*-----------------------------------------------------------------------------------*/
/*  Start MENU
/*-----------------------------------------------------------------------------------*/

    $(document).ready(function () {
     parent_list = jQuery('li.parent-list');
            parent_list.on({
                'mouseover': function () {
                    jQuery(this).find('ul:first').addClass('animated fadeInDown');
                },
                'mouseleave': function () {
                    jQuery(this).find('ul:first').removeClass('animated fadeInDown');
                }
            });

    });

/*-----------------------------------------------------------------------------------*/
/*  End MENU
/*-----------------------------------------------------------------------------------*/


/*-----------------------------------------------------------------------------------*/
/*  Start Sticky Navigation
/*-----------------------------------------------------------------------------------*/

//menu header//
jQuery(document).ready(function($){
    //if you change this breakpoint in the style.css file (or _layout.scss if you use SASS), don't forget to update this value as well
    var MQL = 1170;

    //primary navigation slide-in effect
    if($(window).width() > MQL) {
        var headerHeight = $('.Navbar-Header').height();
        $(window).on('scroll',
        {
            previousTop: 0
        },
        function () {
            var currentTop = $(window).scrollTop();
            //check if user is scrolling up
            if (currentTop < this.previousTop ) {
                //if scrolling up...
                if (currentTop > 0 && $('.Navbar-Header').hasClass('is-fixed')) {
                    $('.Navbar-Header').addClass('is-visible');
                } else {
                    $('.Navbar-Header').removeClass('is-visible is-fixed');
                }
            } else {
                //if scrolling down...
                $('.Navbar-Header').removeClass('is-visible');
                if( currentTop > headerHeight && !$('.Navbar-Header').hasClass('is-fixed')) $('.Navbar-Header').addClass('is-fixed');
            }
            this.previousTop = currentTop;
        });
    }


});


$(document).ready(function () {

if($('.Navbar-Header-sticky').attr('data-sticky') == "true"){
    $(window).on("scroll",function(){
        var Scrl = $(window).scrollTop();
        if (Scrl > 1) {
            $('.Navbar-Header-sticky').addClass('sticky animated fadeInDown');
        }else{
            $('.Navbar-Header-sticky').removeClass('sticky animated fadeInDown');
        }
    });
    $('document').ready(function(){
        var Scrl = $(window).scrollTop();
        if (Scrl > 1) {
            $('.Navbar-Header-sticky').addClass('sticky animated fadeInDown');
        }else{
            $('.Navbar-Header-sticky').removeClass('sticky animated fadeInDown');
        }
    });
}

});


/*-----------------------------------------------------------------------------------*/
/*  End Sticky Navigation
/*-----------------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------------*/
/*  Start Scrolling Page
/*-----------------------------------------------------------------------------------*/
            
    jQuery('.scroll').onePgaeNav({
        wrapper : '.scroll-nav'
    });
    
/*-----------------------------------------------------------------------------------*/
/*  End Scrolling Page
/*-----------------------------------------------------------------------------------*/


/*-----------------------------------------------------------------------------------*/
/*  Start Scroll counter
/*-----------------------------------------------------------------------------------*/

jQuery(document).ready(function( $ ) {
    $('.counter').counterUp({
        delay: 10,
        time: 2000
    });
});

/*-----------------------------------------------------------------------------------*/
/*  End Scroll counter
/*-----------------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------------*/
/*  Start SCROLL DIVS
/*-----------------------------------------------------------------------------------*/

$(document).ready(function () {

(function() {

 var current = 1;

 var height = $('.text-scroll').height();

 var numberDivs = $('.text-scroll').children().length;

 var first = $('.text-scroll h1:nth-child(1)');

 setInterval(function() {

    var number = current * -height;

    first.css('margin-top', number + 'px');

    if (current === numberDivs) {

      first.css('margin-top', '0px');

      current = 1;

    } else current++;

 }, 2500);

})();

});

/*-----------------------------------------------------------------------------------*/
/*  End SCROLL DIVS
/*-----------------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------------*/
/*  Start owl Slider
/*-----------------------------------------------------------------------------------*/

$(document).ready(function() {

  $("#owl-portfolio").owlCarousel({
    navigation : true
  });

});


$(document).ready(function() {

  $("#owl-twitter").owlCarousel({

      navigation : true, // Show next and prev buttons
      slideSpeed : 300,
      paginationSpeed : 400,
      singleItem:true,
      navigationText: [
      "<i class='fa fa-angle-left icon-white'></i>",
      "<i class='fa fa-angle-right icon-white'></i>"
      ],
      // "singleItem:true" is a shortcut for:
      // items : 1,
      // itemsDesktop : false,
      // itemsDesktopSmall : false,
      // itemsTablet: false,
      // itemsMobile : false

  });

});

$(document).ready(function() {

  var owl = $("#owl-customer");

  owl.owlCarousel({
      autoPlay: 3000, //Set AutoPlay to 3 seconds
      items : 6,
      itemsDesktop : [1199,3],
      itemsDesktopSmall : [979,3]

      });

  // Custom Navigation Events
  $(".next").click(function(){
    owl.trigger('owl.next');
  })
  $(".prev").click(function(){
    owl.trigger('owl.prev');
  })

});

$(document).ready(function() {

  $("#owl-Testimonials").owlCarousel({

      navigation : true, // Show next and prev buttons
      slideSpeed : 300,
      paginationSpeed : 400,
      singleItem:true,
      navigationText: [
      "<i class='fa fa-angle-left icon-white'></i>",
      "<i class='fa fa-angle-right icon-white'></i>"
      ],
      // "singleItem:true" is a shortcut for:
      // items : 1,
      // itemsDesktop : false,
      // itemsDesktopSmall : false,
      // itemsTablet: false,
      // itemsMobile : false

  });

});


$(document).ready(function() {

  $("#owl-Services-Slider").owlCarousel({

      navigation : true, // Show next and prev buttons
      slideSpeed : 300,
      paginationSpeed : 400,
      singleItem:true,
      navigationText: [
      "<i class='fa fa-angle-left icon-white'></i>",
      "<i class='fa fa-angle-right icon-white'></i>"
      ],
      // "singleItem:true" is a shortcut for:
      // items : 1,
      // itemsDesktop : false,
      // itemsDesktopSmall : false,
      // itemsTablet: false,
      // itemsMobile : false

  });

});


$(document).ready(function() {

  $("#owl-about-img").owlCarousel({
    navigation : true, // Show next and prev buttons
    paginationSpeed : 400,
    singleItem:true,
    autoPlay: 3000, //Set AutoPlay to 3 seconds
      // "singleItem:true" is a shortcut for:
      // items : 1, 
      // itemsDesktop : false,
      // itemsDesktopSmall : false,
      // itemsTablet: false,
      // itemsMobile : false
  });

});

$(document).ready(function() {
 
  var owl = $("#owl-slider-home");
 
  owl.owlCarousel({
      items : 10, //10 items above 1000px browser width
      singleItem:true,
      autoPlay: 5000, //Set AutoPlay to 3 seconds
      itemsDesktop : [1000,5], //5 items between 1000px and 901px
      itemsDesktopSmall : [900,3], // betweem 900px and 601px
      itemsTablet: [600,2], //2 items between 600 and 0
      itemsMobile : false // itemsMobile disabled - inherit from itemsTablet option
  });
 
  // Custom Navigation Events
  $(".next").click(function(){
    owl.trigger('owl.next');
  })
  $(".prev").click(function(){
    owl.trigger('owl.prev');
  })
 
});

$(document).ready(function() {

  $("#owl-Testimonials-Txt").owlCarousel({
    navigation : true,

    items : 1,
    navigationText: [
    "<i class='fa fa-angle-left icon-white'></i>",
    "<i class='fa fa-angle-right icon-white'></i>"
    ],

  });

});


/*-----------------------------------------------------------------------------------*/
/*  End owl Slider
/*-----------------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------------*/
/*  Start Portfolio
/*-----------------------------------------------------------------------------------*/

$(document).ready(function () {

    $('ul#filters li a').click(function(e) {
        e.preventDefault();
        $('ul#filters .active-link').removeClass('active-link');
        $(this).parent().addClass('active-link');
        var filter = $(this).attr('data-filter').toLowerCase();
        $('.portfolio-items > div:visible').each(function(i) {
            $(this).fadeOut(200,function(){show(filter);});
            $('.portfolio-items > div').addClass('portfolio-item-masonry');
        });
        return false;
    });

    function show(filter){
        if(filter == '*') {
            $('.portfolio-items > div').fadeIn(200);
            $('.portfolio-items > div').removeClass('portfolio-item-masonry');
        } else {
            $('.portfolio-items > div').each(function() {
                if($(this).attr('data-filter') == filter) {
                    $(this).fadeIn(200);
                }
            });
        }
    }

});

/*-----------------------------------------------------------------------------------*/
/*  End Portfolio
/*-----------------------------------------------------------------------------------*

/*-----------------------------------------------------------------------------------*/
/*  Start Hover Portfolio
/*-----------------------------------------------------------------------------------*/

$(document).ready(function () {
    $('.portfolio-item').each(function(){
        var $this = $(this),
            $index = $this.index(),
            contents = $this.find('.projectItem-hover');
        $this.hover(function(){
            contents.fadeIn(300).find('.link').removeClass('animated fadeOutUp').addClass('animated fadeInDown');
            contents.find('.zoom').removeClass('animated fadeOutDown').addClass('animated fadeInUp');
            return false;
        },function(){
            contents.fadeOut(30).find('.link').removeClass('animated fadeInDown').addClass('animated fadeOutUp');
            contents.find('.zoom').removeClass('animated fadeInUp').addClass('animated fadeOutDown');
            return false;
        });
    });
});

/*-----------------------------------------------------------------------------------*/
/*  End Hover Portfolio
/*-----------------------------------------------------------------------------------*/


/*-----------------------------------------------------------------------------------*/
/*  Start Contact form
/*-----------------------------------------------------------------------------------*/

var frm = $('#cform');
    frm.submit(function (ev) {
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            success: function (data) {
                $('#cform').append("<div class='alert alert-success'><button type='button' class='close' data-dismiss='alert' aria-hidden='true'>×</button><i class='fa fa-thumbs-o-up'></i><strong>Well done!</strong> Your Message Submitted!</div>")
            }
        });

        ev.preventDefault();
});         

/*-----------------------------------------------------------------------------------*/
/*  End Contact form
/*-----------------------------------------------------------------------------------*/

$(document).ready(function() {  
    $(".SliderText").each(function(){
        var contentHeight = $(this).height();
        contentHeight = (contentHeight * 8) / 21;
        $(this).css("margin-top",contentHeight);
    });
});

/* ---------------------------------------------------------------------- */
/*  Start Fancybox
/* ---------------------------------------------------------------------- */

$(document).ready(function() {
    /*
     *  Simple image gallery. Uses default settings
     */

    $('.fancybox').fancybox();

    /*
     *  Different effects
     */

    // Change title type, overlay closing speed
    $(".fancybox-effects-a").fancybox({
        helpers: {
            title : {
                type : 'outside'
            },
            overlay : {
                speedOut : 0
            }
        }
    });

    // Disable opening and closing animations, change title type
    $(".fancybox-effects-b").fancybox({
        openEffect  : 'none',
        closeEffect : 'none',

        helpers : {
            title : {
                type : 'over'
            }
        }
    });

    // Set custom style, close if clicked, change title type and overlay color
    $(".fancybox-effects-c").fancybox({
        wrapCSS    : 'fancybox-custom',
        closeClick : true,

        openEffect : 'none',

        helpers : {
            title : {
                type : 'inside'
            },
            overlay : {
                css : {
                    'background' : 'rgba(238,238,238,0.85)'
                }
            }
        }
    });

    // Remove padding, set opening and closing animations, close if clicked and disable overlay
    $(".fancybox-effects-d").fancybox({
        padding: 0,

        openEffect : 'elastic',
        openSpeed  : 150,

        closeEffect : 'elastic',
        closeSpeed  : 150,

        closeClick : true,

        helpers : {
            overlay : null
        }
    });

    /*
     *  Button helper. Disable animations, hide close button, change title type and content
     */

    $('.fancybox-buttons').fancybox({
        openEffect  : 'none',
        closeEffect : 'none',

        prevEffect : 'none',
        nextEffect : 'none',

        closeBtn  : false,

        helpers : {
            title : {
                type : 'inside'
            },
            buttons : {}
        },

        afterLoad : function() {
            this.title = 'Image ' + (this.index + 1) + ' of ' + this.group.length + (this.title ? ' - ' + this.title : '');
        }
    });


    /*
     *  Thumbnail helper. Disable animations, hide close button, arrows and slide to next gallery item if clicked
     */

    $('.fancybox-thumbs').fancybox({
        prevEffect : 'none',
        nextEffect : 'none',

        closeBtn  : false,
        arrows    : false,
        nextClick : true,

        helpers : {
            thumbs : {
                width  : 50,
                height : 50
            }
        }
    });

    /*
     *  Media helper. Group items, disable animations, hide arrows, enable media and button helpers.
    */
    $(".video").click(function() {
        $.fancybox({
            'padding'       : 0,
            'autoScale'     : false,
            'transitionIn'  : 'none',
            'transitionOut' : 'none',
            'title'         : this.title,
            'width'         : 640,
            'height'        : 385,
            'href'          : this.href.replace(new RegExp("watch\\?v=", "i"), 'v/'),
            'type'          : 'swf',
            'swf'           : {
            'wmode'             : 'transparent',
            'allowfullscreen'   : 'true'
            }
        });

        return false;
    });


    $('.fancybox-media')
        .attr('rel', 'media-gallery')
        .fancybox({
            openEffect : 'none',
            closeEffect : 'none',
            prevEffect : 'none',
            nextEffect : 'none',

            arrows : false,
            helpers : {
                media : {},
                buttons : {}
            }

        });

    /*
     *  Open manually
     */

    $("#fancybox-manual-a").click(function() {
        $.fancybox.open('1_b.jpg');
    });

    $("#fancybox-manual-b").click(function() {
        $.fancybox.open({
            href : 'iframe.html',
            type : 'iframe',
            padding : 5
        });
    });

    $("#fancybox-manual-c").click(function() {
        $.fancybox.open([
            {
                href : '1_b.jpg',
                title : 'My title'
            }, {
                href : '2_b.jpg',
                title : '2nd title'
            }, {
                href : '3_b.jpg'
            }
        ], {
            helpers : {
                thumbs : {
                    width: 75,
                    height: 50
                }
            }
        });
    });


});

/* ---------------------------------------------------------------------- */
/*  End Fancybox
/* ---------------------------------------------------------------------- */

/*-----------------------------------------------------------------------------------*/
/*  Start Progress-Bar
/*-----------------------------------------------------------------------------------*/

$(document).ready(function () {
    if (jQuery(".progress-bar").length) {
        jQuery(".progress-bar").each(function(){
            var $this = jQuery(this);
            var percent = $this.attr("data-percent");
            $this.bind("inview", function(event, isInView, visiblePartX, visiblePartY) {
                if (isInView) {
                    $this.animate({ "width" : percent + "%"}, percent*20);
                }
            });
        });
    }

});

/*-----------------------------------------------------------------------------------*/
/*  End Progress-Bar
/*-----------------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------------*/
/*  Start Option-Box
/*-----------------------------------------------------------------------------------*/

    $(document).ready(function () {
        $('.show_hide').click(function(){
            $('.option-box').toggleClass('Show');
        });
    });
    /*-----------------------------------------------------------------------------------*/
    /*  Start Change Theme Color On Click
    /*-----------------------------------------------------------------------------------*/

        var Colorop = $(".code_color");
        Colorop.click(function()
        {
            $("link[href*='color']").attr("href",$(this).attr("data-value") );
        });

    /*-----------------------------------------------------------------------------------*/
    /*  End Change Theme Color On Click
    /*-----------------------------------------------------------------------------------*/


    /*-----------------------------------------------------------------------------------*/
    /*  Start Change Theme Background On Click
    /*-----------------------------------------------------------------------------------*/

        var Colorop = $(".code-backg");
        Colorop.click(function()
        {
            $('.Boxed-i').attr("style",$(this).attr("style") );
        });

    /*-----------------------------------------------------------------------------------*/
    /*  Start Change Theme Background On Click
    /*-----------------------------------------------------------------------------------*/


    /*-----------------------------------------------------------------------------------*/
    /*  Strat LOADING OVERLAY
    /*-----------------------------------------------------------------------------------*/

    $(window).load(function()
    {
        $(".loading-overlay .spinner").fadeOut(300);

        $(".loading-overlay").fadeOut(300);
    });

    $(window).load(function() {
      $('body').css({'overflow':'auto', 'height':'auto', 'position':'relative'});
    });

    /*-----------------------------------------------------------------------------------*/
    /*  End LOADING OVERLAY
    /*-----------------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------------*/
/*  End Option-Box
/*-----------------------------------------------------------------------------------*/


/*-----------------------------------------------------------------------------------*/
/*  Start Accordions
/*-----------------------------------------------------------------------------------*/

jQuery(".tap-title").each(function(){
    jQuery(this).click(function() {
        if (jQuery(this).parent().parent().hasClass("toggle-accordion")) {
            jQuery(this).parent().find("li:first .tap-title").addClass("active");
            jQuery(this).parent().find("li:first .tap-title").next(".accordion-inner").addClass("active");
            jQuery(this).toggleClass("active");
            jQuery(this).next(".accordion-inner").slideToggle().toggleClass("active");
            jQuery(this).find("i").toggleClass("fa-plus").toggleClass("fa-minus");
        }else {
            if (jQuery(this).next().is(":hidden")) {
                jQuery(this).parent().parent().find(".tap-title").removeClass("active").next().slideUp(200);
                jQuery(this).parent().parent().find(".tap-title").next().removeClass("active").slideUp(200);
                jQuery(this).toggleClass("active").next().slideDown(200);
                jQuery(this).next(".accordion-inner").toggleClass("active");
                jQuery(this).parent().parent().find("i").removeClass("fa-minus").addClass("fa-plus");
                jQuery(this).find("i").removeClass("fa-plus").addClass("fa-minus");
            }
        }
        return false;
    });
});

jQuery(".tap-title2").each(function(){
    jQuery(this).click(function() {
        if (jQuery(this).parent().parent().hasClass("toggle-accordion")) {
            jQuery(this).parent().find("li:first .tap-title2").addClass("active");
            jQuery(this).parent().find("li:first .tap-title2").next(".accordion-inner").addClass("active");
            jQuery(this).toggleClass("active");
            jQuery(this).next(".accordion-inner").slideToggle().toggleClass("active");
            jQuery(this).find("i").toggleClass("fa-caret-right").toggleClass("fa-caret-down");
        }else {
            if (jQuery(this).next().is(":hidden")) {
                jQuery(this).parent().parent().find(".tap-title2").removeClass("active").next().slideUp(200);
                jQuery(this).parent().parent().find(".tap-title2").next().removeClass("active").slideUp(200);
                jQuery(this).toggleClass("active").next().slideDown(200);
                jQuery(this).next(".accordion-inner").toggleClass("active");
                jQuery(this).parent().parent().find("i").removeClass("fa-caret-down").addClass("fa-caret-right");
                jQuery(this).find("i").removeClass("fa-caret-right").addClass("fa-caret-down");
            }
        }
        return false;
    });
});


/*-----------------------------------------------------------------------------------*/
/*  End Accordions
/*-----------------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------------*/
/*  Start Tweet
/*-----------------------------------------------------------------------------------*/

$('.tweet').twittie({
    username: 'EnvatoStudio',
    hideReplies: true,
    dateFormat: '%b. %d, %Y',
    template: '<i class="fa fa-twitter"></i> {{screen_name}} {{tweet}} <div class="date">{{date}}</div>',
    count: 2,
    loadingText: 'Loading!'
});

$('.tweet-community').twittie({
    username: 'EnvatoStudio',
    hideReplies: true,
    dateFormat: '%b. %d, %Y',
    template: '{{screen_name}} {{tweet}} <div class="date">{{date}}</div>',
    count: 1,
    loadingText: 'Loading!'
});

/*-----------------------------------------------------------------------------------*/
/*  End Tweet
/*-----------------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------------*/
/*  Start Items Number Shop
/*-----------------------------------------------------------------------------------*/

$(document).ready(function () {

    var num = $('#items-num').val();
    $('.add-items i.fa-plus').click(function(e){
        e.preventDefault();
        num ++;
        $('#items-num').attr('value',num);
    });

    $('.add-items i.fa-minus').click(function(e){
        e.preventDefault();
        if (num > 1){
            num --;
            $('#items-num').attr('value',num);
        }
    });
});

$(document).ready(function () {

    var num = $('#items-numb').val();
    $('.add-items-2 i.fa-plus').click(function(e){
        e.preventDefault();
        num ++;
        $('#items-numb').attr('value',num);
    });

    $('.add-items-2 i.fa-minus').click(function(e){
        e.preventDefault();
        if (num > 1){
            num --;
            $('#items-numb').attr('value',num);
        }
    });

});


/*-----------------------------------------------------------------------------------*/
/*  End Items Number Shop
/*-----------------------------------------------------------------------------------*/


/*-----------------------------------------------------------------------------------*/
/*  Start Features us
/*-----------------------------------------------------------------------------------*/

jQuery(document).ready(function($){
    var tabItems = $('.tabs-navigation a'),
        tabContentWrapper = $('.tabs-content');

    tabItems.on('click', function(event){
        event.preventDefault();
        var selectedItem = $(this);
        if( !selectedItem.hasClass('selected') ) {
            var selectedTab = selectedItem.data('content'),
                selectedContent = tabContentWrapper.find('li[data-content="'+selectedTab+'"]'),
                slectedContentHeight = selectedContent.innerHeight();

            tabItems .parent().removeClass('selected');
            selectedItem .parent().addClass('selected');
            selectedContent.addClass('selected').siblings('li').removeClass('selected');
            //animate tabContentWrapper height when content changes
            tabContentWrapper.animate({
                'height': slectedContentHeight
            }, 200);
        }
    });

});

/*-----------------------------------------------------------------------------------*/
/*  End Features us
/*-----------------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------------*/
/*  Start Case Studies
/*-----------------------------------------------------------------------------------*/

jQuery(document).ready(function($){
    var tabItems = $('.Top-Case a'),
        tabContentWrapper = $('.Tap-Case');

    tabItems.on('click', function(event){
        event.preventDefault();
        var selectedItem = $(this);
        if( !selectedItem.hasClass('selected') ) {
            var selectedTab = selectedItem.data('content'),
                selectedContent = tabContentWrapper.find('li[data-content="'+selectedTab+'"]'),
                slectedContentHeight = selectedContent.innerHeight();

            tabItems .parent().removeClass('selected');
            selectedItem .parent().addClass('selected');
            selectedContent.addClass('selected').siblings('li').removeClass('selected');
            //animate tabContentWrapper height when content changes
            tabContentWrapper.animate({
                'height': slectedContentHeight
            }, 200);
        }
    });

});

/*-----------------------------------------------------------------------------------*/
/*  End Case Studies
/*-----------------------------------------------------------------------------------*/


/*-----------------------------------------------------------------------------------*/
/*  Start Tabs Work Process
/*-----------------------------------------------------------------------------------*/


jQuery(document).ready(function($){
    var tabItems = $('.Process-tabs-navigation a'),
        tabContentWrapper = $('.Process-tabs-content');

    tabItems.on('click', function(event){
        event.preventDefault();
        var selectedItem = $(this);
        if( !selectedItem.hasClass('selected') ) {
            var selectedTab = selectedItem.data('content'),
                selectedContent = tabContentWrapper.find('li[data-content="'+selectedTab+'"]'),
                slectedContentHeight = selectedContent.innerHeight();

            tabItems.removeClass('selected');
            selectedItem.addClass('selected');
            selectedContent.addClass('selected').siblings('li').removeClass('selected');
            //animate tabContentWrapper height when content changes
            tabContentWrapper.animate({
                'height': slectedContentHeight
            }, 100);
        }
    });

});

/*-----------------------------------------------------------------------------------*/
/*  End Tabs Work Process
/*-----------------------------------------------------------------------------------*/


/*-----------------------------------------------------------------------------------*/
/*  Start Back to top button
/*-----------------------------------------------------------------------------------*/

var winScroll = $(window).scrollTop();
    if (winScroll > 1) {
        $('#to-top').css({bottom:"10px"});
    } else {
        $('#to-top').css({bottom:"-100px"});
    }
    $(window).on("scroll",function(){
        winScroll = $(window).scrollTop();

        if (winScroll > 1) {
            $('#to-top').css({opacity:1,bottom:"30px"});
        } else {
            $('#to-top').css({opacity:0,bottom:"-100px"});
        }
    });
    $('#to-top').click(function(){
        $('html, body').animate({scrollTop: '0px'}, 800);
        return false;
});

$('.fa-hover').wrapInner('<span />');

/*-----------------------------------------------------------------------------------*/
/*  End Back to top button
/*-----------------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------------*/
/*  Start Parallax Mobile
/*-----------------------------------------------------------------------------------*/

$(document).ready(function () {

    if (navigator.userAgent.match(/Android/i) ||

        navigator.userAgent.match(/webOS/i) ||

        navigator.userAgent.match(/iPhone/i) ||

        navigator.userAgent.match(/iPad/i) ||

        navigator.userAgent.match(/iPod/i) ||

        navigator.userAgent.match(/BlackBerry/i)) {

        $('.parallax').addClass('mobile');

    }

});

/*-----------------------------------------------------------------------------------*/
/*  End Parallax Mobile
/*-----------------------------------------------------------------------------------*/

/* ---------------------------------------------------------------------- */
/*  Start Tooltip
/* ---------------------------------------------------------------------- */


$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

/*-----------------------------------------------------------------------------------*/
/*  End Tooltip
/*-----------------------------------------------------------------------------------*/


/* ---------------------------------------------------------------------- */
/*  Start WOW Animation
/* ---------------------------------------------------------------------- */

$(document).ready(function () {
 new WOW().init();
});

/*-----------------------------------------------------------------------------------*/
/*  End WOW Animation
/*-----------------------------------------------------------------------------------*/



