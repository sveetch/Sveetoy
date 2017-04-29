=========
Changelog
=========

Version 0.6.1 - Unreleased
--------------------------

* Fixed inconvenient parent selector on spaces features so it should build with Compass again, close #19;
* ``.inner`` blocks feature only work as direct child of a ``.block.delegate``, close #21;
* Added missing ``$sveetoy-row-larger-width`` in default settings;

Version 0.6.0 - 2017/03/05
--------------------------

Foundation6 support, close #14:

* Include makefile action to install Foundation6 sources using Foundation 6.3.1;
* Default demonstration page is built with Foundation6, Foundation5 demo is still available;
* Added Foundation6 assets;
* Fixed components grid, flex and typography to build CSS with Foundation6;

Version 0.5.2 - 2017/02/28
--------------------------

* Added flexbox direction classes, close #2;
* Use ``$sveetoy-breakpoints`` to build every flexbox media query classnames;
* Added ``boxes`` component that combine spaces and color schemes, close #3;
* Build ``<hr>`` features from schemes, close #4;
* Build ``<small>`` element size features from ``$sveetoy-smalls``, close #5;
* Build ``.underline`` features from schemes, close #6;
* Dropped button feature ``f-dropdown.overflow``, close #7;
* Build button color features from variable ``$sveetoy-button-colors-schemes``, close #8;
* Build button ``.modest`` features from variable ``$sveetoy-button-modests``, close #9;
* Renamed text thickness features for better consistency, close #12 :

  * ``.text-strong`` becomes ``.text-bold``;
  * ``.text-stronger`` becomes ``.text-strong``;
  * ``$font-weight-stronger`` becomes ``$font-weight-strong``;

* Renamed ``.section`` to ``.block``, close #15;
* Added vocabulary references and accorded ``spaces`` component features to width terms, close #16;
* Renamed button feature ``.strong`` to ``.important``;
* Added ``sveetoy/_settings.scss`` to include some default settings and keep components only with ``!default`` values, close #13;
* Fixed ``buttons`` and ``type`` components to work nice with empty default values;
* Added "Install" part in demo;

Version 0.5.1 - 2017/02/06
--------------------------

* Continued to improve demo;
* Some cleaning in sources;
* Moved every TODO in a github issue;
* Add a script to correctly release with correct version and create an archive;
* Publish the first sources archive in ``dist/``;

Version 0.5.0 - 2017/02/04
--------------------------

First release but without an archive yet.