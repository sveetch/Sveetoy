# -*- coding: utf-8 -*-
"""
Assets bundles
"""
from webassets import Bundle

# Register custom webasset filter for RCssMin minifier
from webassets.filter import register_filter
from rcssmin_webassets_filter import RCSSMin
register_filter(RCSSMin)

"""
BASE BUNDLES, contains common app/components bundles, do not register your
main bundles here. However you can comment/uncomment some app files for your
needs.
"""
AVALAIBLE_BUNDLES = {
    # App bundle for Modernizr
    'modernizr_f6_js': Bundle(
        "js/foundation6/vendor/modernizr.js",
        filters='closure_js',
        output='js/modernizr_f6.min.js'
    ),

    # Bundle for Foundation JAVASCRIPT stuff
    'foundation6_js': Bundle(
        "js/foundation6/vendor/jquery.js",
        #"js/foundation6/vendor/motion-ui.js",
        "js/foundation6/vendor/what-input.js",
        'js/foundation6/foundation/plugins/foundation.core.js',
        'js/foundation6/foundation/plugins/foundation.util.box.js',
        'js/foundation6/foundation/plugins/foundation.util.keyboard.js',
        'js/foundation6/foundation/plugins/foundation.util.mediaQuery.js',
        'js/foundation6/foundation/plugins/foundation.util.motion.js',
        'js/foundation6/foundation/plugins/foundation.util.nest.js',
        'js/foundation6/foundation/plugins/foundation.util.timerAndImageLoader.js',
        'js/foundation6/foundation/plugins/foundation.util.touch.js',
        'js/foundation6/foundation/plugins/foundation.util.triggers.js',
        #'js/foundation6/foundation/plugins/foundation.abide.js',
        #'js/foundation6/foundation/plugins/foundation.accordion.js',
        #'js/foundation6/foundation/plugins/foundation.accordionMenu.js',
        'js/foundation6/foundation/plugins/foundation.drilldown.js',
        'js/foundation6/foundation/plugins/foundation.dropdown.js',
        'js/foundation6/foundation/plugins/foundation.dropdownMenu.js',
        #'js/foundation6/foundation/plugins/foundation.equalizer.js',
        #'js/foundation6/foundation/plugins/foundation.interchange.js',
        'js/foundation6/foundation/plugins/foundation.magellan.js',
        #'js/foundation6/foundation/plugins/foundation.offcanvas.js',
        #'js/foundation6/foundation/plugins/foundation.orbit.js',
        'js/foundation6/foundation/plugins/foundation.responsiveMenu.js',
        'js/foundation6/foundation/plugins/foundation.responsiveToggle.js',
        #'js/foundation6/foundation/plugins/foundation.reveal.js',
        #'js/foundation6/foundation/plugins/foundation.slider.js',
        'js/foundation6/foundation/plugins/foundation.sticky.js',
        'js/foundation6/foundation/plugins/foundation.tabs.js',
        'js/foundation6/foundation/plugins/foundation.toggler.js',
        'js/foundation6/foundation/plugins/foundation.tooltip.js',
        'js/foundation6/foundation/plugins/foundation.zf.responsiveAccordionTabs.js',
        filters='closure_js',
        output='js/foundation6.min.js'
    ),
}

"""
MAIN AVAILABLE BUNDLES, this is where you will register your main Asset bundles
"""
AVALAIBLE_BUNDLES.update({
    # Main CSS bundle
    'main_f6_css': Bundle(
        'css/app.foundation6.css',
        filters='rcssmin',
        output='css/app.foundation6.min.css'
    ),

    # JAVASCRIPT bundle common main frontend script
    'main_f6_js': Bundle(
        # Foundation bundle
        AVALAIBLE_BUNDLES['foundation6_js'],

        # Main frontend script
        "js/app.js",

        filters='closure_js',
        output='js/app.foundation6.min.js'
    ),
})


"""
ENABLE NEEDED BUNDLE HERE, only these bundles will be used
"""
ENABLED_BUNDLES = [
    'main_f6_css',
    'modernizr_f6_js',
    'main_f6_js',
]
# Build a new dict of enabled bundles
PUBLISHED_BUNDLES = {k:AVALAIBLE_BUNDLES[k] for k in ENABLED_BUNDLES}