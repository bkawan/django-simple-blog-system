$(document).on('ready',function(){
    $('.clients-autoplay').slick({
        slidesToShow: 6,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 2000,
        prevArrow: '<div class="slick-prev" style="background-color:black;"><i class="fa fa-angle-left" aria-hidden="true"></i> previus</div>',
        nextArrow: '<div class="slick-next" style="background-color:black;"><i class="fa fa-angle-right" aria-hidden="true"></i>next</div>'
    });
    
});