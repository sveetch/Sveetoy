/*
 **
 ** Main frontend Javascript
 **
 */
jQuery(window).load(function () {
    /*
     * Restore "jump to anchor" behavior on page loaded but adding an offset
     */
    if (location.hash) {
        var $header = $('#header-container'),
            offset = 0;

        //console.log("From load(): Location hash detected:"+ location.hash);
        // Compute additional offset from topbar outer height but only in
        // sticky or fixed mode
        if($header.find('.fixed').length>0){
            offset = $header.find('.fixed').outerHeight(true);
        } else if($header.find('.sticky').length>0){
            offset = $header.find('.sticky').outerHeight(true);
        }
        //console.log("offset:"+offset);
        setTimeout(function() {
            // The fasted method is the raw way with 'scrollTo'
            window.scrollTo(0, $(location.hash).offset().top - offset);
            // For more animated and longer scroll, the 'jQuery animate'
            /*$('html, body').animate({
                scrollTop: $(location.hash).offset().top - offset
            }, 100, 'swing', function () {});*/
        },1)
    }
});

jQuery(document).ready(function($) {
    // Init MediaQuery watcher (look into addons.js for more infos)
    $('#watch-for-current-mquery').initCurrentMediaQuery();
    $('#watch-for-current-mquery').watchForCurrentMediaQuery();

    /*
    * Initialize Foundation
    */
    $(document).foundation();

    // Reflow the 'swapImageToBackground' plugin on debounced
    // resize event to recalculate min-height for background image container
    $(window).on("debouncedresize", function( event ) {
        $('#watch-for-current-mquery').watchForCurrentMediaQuery();
    });
});
