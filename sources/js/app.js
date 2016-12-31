/*
 **
 ** Main frontend Javascript
 **
 */
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
