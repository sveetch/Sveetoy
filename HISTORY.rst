.. _PyCssStyleguide: https://github.com/sveetch/py-css-styleguide

=========
Changelog
=========

Version 0.9.1 - Unreleased
--------------------------

`Download ZIP package for version 0.9.1 <http://sveetch.github.io/Sveetoy/dist/Sveetoy-sass-0.9.1.zip>`_

* Add ``$include-hover`` option to ``sv-button-colors()`` mixin to automatically append button properties prefixed with ``hover`` in pseudo event "hover";
* Fix invalid parent selector ``&`` on top level in some components which has become an error since ``libsass==3.6.2``. It should be a backward change for your previous sources;

Version 0.9.0 - 2018/05/12
--------------------------

`Download ZIP package for version 0.9.0 <http://sveetch.github.io/Sveetoy/dist/Sveetoy-sass-0.9.0.zip>`_

* Patch ``$sv-hr-colors`` usage in styleguide to avoid an error when it is empty, close #48;
* Fix horizontal rule distance so it does not touch anymore horizontal margin, close #47;
* Add ``sv-flex()`` mixin, related to #30;
* Add typography mixins for headers, related to #30;
* Upgraded demo to be built on Foundation 6.4.3;
* Don't load anymore modernizr from demo since it is not used;

Version 0.8.4 - 2018/04/22
--------------------------

`Download ZIP package for version 0.8.4 <http://sveetch.github.io/Sveetoy/dist/Sveetoy-sass-0.8.4.zip>`_

* Fix flexbox component where some rules was allways created even if ``$include-sv-flex`` was disabled;
* Implement usage of `PyCssStyleguide`_ to fully build demonstration from styleguide. You can find the CSS manifest in ``styleguide_manifest.scss``;
* Common color backgrounds classes (aka ``.bg-NAME``) are now builded from ``$sv-color-background-palette`` which by default is a copy of ``$sv-colors-schemes``;
* Dropped ``styleguide`` component since now styleguide is achieved through `PyCssStyleguide`_;

Version 0.8.3 - 2018/03/13
--------------------------

`Download ZIP package for version 0.8.3 <http://sveetch.github.io/Sveetoy/dist/Sveetoy-sass-0.8.3.zip>`_

* ``$sv-hr-default-color`` miss ``!default`` mark, close #43;
* Don't use anymore shortand ``flex`` property to avoid a `bug from IE11 <https://github.com/philipwalton/flexbugs#flexbug-8>`_, close #45;

Version 0.8.2 - 2018/02/12
--------------------------

A dummy version to fix an error in release. Forgot it.

Version 0.8.1 - 2018/02/12
--------------------------

`Download ZIP package for version 0.8.1 <http://sveetch.github.io/Sveetoy/dist/Sveetoy-sass-0.8.1.zip>`_

* Add some lines about 'hover' support for color scheme model usage in box and button, close #40;
* Add component ``styleguide`` with helper classes ``styleguide-schemes-background-COLORNAME``, close #41;
* Add ``!important`` mark to all helper classes values, close #42;
* Fix wrong mquery in sample settings, close #39;

Version 0.8.0 - 2017/12/11
--------------------------

`Download ZIP package for version 0.8.0 <http://sveetch.github.io/Sveetoy/dist/Sveetoy-sass-0.8.0.zip>`_

* Bunch of renaming and tidying up, close #31 :

  * Rename every ``sveetoy`` to ``sv`` in variables, mixins and classes, did the same for ``flexbox`` to ``flex``;
  * Rename every breakpoint suffix like ``foo-medium`` to ``medium-foo`` for consistent naming;
  * Removed useless patch for Foundation5;
  * Removed useless ``topbar`` component;
  * Removed deprecated mixin ``sveetoy-simulate-grid-columns``;
  * Moved ``components/_global.scss`` to ``_global.scss``;
  * Moved every variables from mixins to ``_global.scss`` file;

* Add behavior to color schemes for button and boxes to support ``hover-`` prefix properties to define rules for ``:hover`` event, close #32;
* Add ``.bg-***`` classes for every color scheme with ``background`` property, ``hover-background`` is supported also for these classes, close #36;
* Add transparent feature for block and box, close #37;
* Change default ``.flex-grid`` cell size to ``100%``, close #25;
* Change border properties support in color schemes so we can use ``border`` shortand, ``border-style``, ``border-width`` and ``border-color``.
* Change border properties support in color schemes so font color is not used anymore as a default value;
* Change ``font-color``  behavior so it is not defined anymore automatically with inverted color from ``background`` since it may not contain correct color, close #35;
* Rename ``background-color`` property from color scheme to ``background`` so now we can define more complex background;

Version 0.7.2 - 2017/11/13
--------------------------

`Download ZIP package for version 0.7.2 <http://sveetch.github.io/Sveetoy/dist/Sveetoy-sass-0.7.2.zip>`_

* Add `Stylelint <https://stylelint.io/>`_ rules configuration from `Sass syntax guide with Stylelint <https://github.com/emencia/stylelint-guide>`_;
* Fix every syntax warnings from Stylelint;


Version 0.7.1 - 2017/11/04
--------------------------

`Download ZIP package for version 0.7.1 <http://sveetch.github.io/Sveetoy/dist/Sveetoy-sass-0.7.1.zip>`_

* Usage of `sassdoc <http://sassdoc.com>`_ to build API documentation for variables and mixins;
* [Backward incompatible] Default distance word has changed from ``normal`` to ``default``, it affects underline and horizontal rule features, close #24;
* Button color scheme should override ``disabled`` feature default behavior, close #22;
* Move ``global`` to ``globals``, remove unused ``.position-relative``, added ``medias`` component, close #33;


Version 0.7.0 - 2017/10/23
--------------------------

`Download ZIP package for version 0.7.0 <http://sveetch.github.io/Sveetoy/dist/Sveetoy-sass-0.7.0.zip>`_

* Add older package version links in changelog;
* Dropp Foundation5 support, close #28;
* Fix headers missing font family, close #27;
* Fix invalid sample settings, close #26
* To enforce naming cohesion with Foundation:

  * ``$font-weight-normal`` have been removed;
  * ``$font-weight-bold`` have been removed;
  * ``$font-weight-thin`` have been renamed to ``$global-weight-thin``;
  * ``$font-weight-strong`` have been renamed to ``$global-weight-strong``;


Version 0.6.1 - 2017/03/05
--------------------------

`Download ZIP package for version 0.6.1 <http://sveetch.github.io/Sveetoy/dist/Sveetoy-sass-0.6.1.zip>`_

* Add missing ``$sveetoy-row-larger-width`` in default settings;
* Dropped Modernizr condition on flexbox class in Flexbox component, close #17;
* Fix inconvenient parent selector on spaces features so it should build with Compass again, close #19;
* Rename flexbox vertical alignments from ``.align-[ALIGNMENT]`` to ``.v-align-[ALIGNMENT]`` and moved them out of ``.flex-grid`` so they can be used everywhere, close #20;
* ``.inner`` blocks feature only work as direct child of a ``.block.delegate``, close #21;


Version 0.6.0 - 2017/03/05
--------------------------

`Download ZIP package for version 0.6.0 <http://sveetch.github.io/Sveetoy/dist/Sveetoy-sass-0.6.0.zip>`_

* Foundation6 support, close #14:
* Include makefile action to install Foundation6 sources using Foundation 6.3.1;
* Default demonstration page is built with Foundation6, Foundation5 demo is still available;
* Add Foundation6 assets;
* Fix components grid, flex and typography to build CSS with Foundation6;


Version 0.5.2 - 2017/02/28
--------------------------

`Download ZIP package for version 0.5.2 <http://sveetch.github.io/Sveetoy/dist/Sveetoy-sass-0.5.2.zip>`_

* Add flexbox direction classes, close #2;
* Use ``$sveetoy-breakpoints`` to build every flexbox media query classnames;
* Add ``boxes`` component that combine spaces and color schemes, close #3;
* Build ``<hr>`` features from schemes, close #4;
* Build ``<small>`` element size features from ``$sveetoy-smalls``, close #5;
* Build ``.underline`` features from schemes, close #6;
* Dropped button feature ``f-dropdown.overflow``, close #7;
* Build button color features from variable ``$sveetoy-button-colors-schemes``, close #8;
* Build button ``.modest`` features from variable ``$sveetoy-button-modests``, close #9;
* Rename text thickness features for better consistency, close #12 :

  * ``.text-strong`` becomes ``.text-bold``;
  * ``.text-stronger`` becomes ``.text-strong``;
  * ``$font-weight-stronger`` becomes ``$font-weight-strong``;

* Rename ``.section`` to ``.block``, close #15;
* Add vocabulary references and accorded ``spaces`` component features to width terms, close #16;
* Rename button feature ``.strong`` to ``.important``;
* Add ``sveetoy/_settings.scss`` to include some default settings and keep components only with ``!default`` values, close #13;
* Fix ``buttons`` and ``type`` components to work nice with empty default values;
* Add "Install" part in demo;


Version 0.5.1 - 2017/02/06
--------------------------

`Download ZIP package for version 0.5.1 <http://sveetch.github.io/Sveetoy/dist/Sveetoy-sass-0.5.1.zip>`_

* Continue to improve demo;
* Some cleaning in sources;
* Move every TODO in a github issue;
* Add a script to correctly release with correct version and create an archive;
* Publish the first sources archive in ``dist/``;


Version 0.5.0 - 2017/02/04
--------------------------

`Download ZIP package for version 0.5.0 <http://sveetch.github.io/Sveetoy/dist/Sveetoy-sass-0.5.0.zip>`_

First release but without an archive yet.
