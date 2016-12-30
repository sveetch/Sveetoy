;(function($) {
    'use strict';

    /*
    * Find current media query to display it in a container
    *
    * - The last matched media query is the current one;
    * - Require debounce event from jquery-smartresize library;
    * - Should be ready to use in your template and app.js;
    * - Can be hided/displayed again using "SHIFT+M";
    */
    // Init key shortcut (SHIFT+M) to show/hide container
    $.fn.initCurrentMediaQuery = function(options) {
        return this.each(function() {
            var $container = $(this);
            $(document).keydown(function( event ) {
                if ( event.which == 13 ) {
                    event.preventDefault();
                } else if ( event.which == 77 && event.shiftKey == true && event.ctrlKey != true && event.metaKey != true ){
                    $container.toggle();
                }
            });
        });
    };
    // Fill/Update current mquery value
    $.fn.watchForCurrentMediaQuery = function(options) {
        return this.each(function() {
            var current,
                $container = $(this),
                matched = [];
            if (matchMedia(Foundation.media_queries['small']).matches){
                matched.push('small');
            };
            if (matchMedia(Foundation.media_queries['medium']).matches){
                matched.push('medium');
            };
            if (matchMedia(Foundation.media_queries['large']).matches){
                matched.push('large');
            };
            if (matchMedia(Foundation.media_queries['xlarge']).matches){
                matched.push('xlarge');
            };
            if (matchMedia(Foundation.media_queries['xxlarge']).matches){
                matched.push('xxlarge');
            };
            matched.reverse();
            current = matched.shift();
            $('.value', $container).html(current);
        });
    };
}( jQuery ));
