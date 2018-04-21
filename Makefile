.PHONY: help install install-venv install-foundation6 install-sassdoc clean delpyc dev-build dev-server dev-clean dev-watcher dev-sassdoc prod-build prod-server prod-clean prod-sassdoc release

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  install              -- to proceed to a new install of this project. Will require 'git' client. Use clean command before if you want to reset a current install."
	@echo "  install-venv         -- to install the Python virtual environment. Will require 'virtualenv'."
	@echo "  install-foundation6  -- to install last Foundation6 sources. Will require 'wget' and 'bower'."
	@echo "  install-sassdoc      -- to install sassdoc tool to build Sass API documentation."
	@echo
	@echo "  dev-build            -- to build demonstration site in development env."
	@echo "  dev-server           -- to start demonstration site server with CherryPie."
	@echo "  dev-watcher          -- to start watchdog on sources in development env."
	@echo "  dev-clean            -- to clean builded HTML and assets from development env."
	@echo "  dev-sassdoc          -- to build Sass doc in development env."
	@echo
	@echo "  prod-build           -- to build demonstration site for Github site."
	@echo "  prod-server          -- to start demonstration site server with CherryPie for Github site."
	@echo "  prod-clean           -- to clean builded HTML and assets from Github site."
	@echo "  prod-sassdoc         -- to build Sass doc for Github site."
	@echo
	@echo "  clean                -- to clean your local repository from all installed stuff."
	@echo "  delpyc               -- to remove all *.pyc files, this is recursive from the current directory."
	@echo
	@echo "  release              -- to build ZIP archive for last library version with everything ready and rebuilt for demonstration on Github."
	@echo

delpyc:
	find . -name "*\.pyc"|xargs rm -f

clean-foundation6:
	rm -Rf foundation-sites-6.3.1
	rm -Rf sources/js/foundation6/foundation
	rm -Rf sources/js/foundation6/vendor/*.js

dev-clean:
	rm -Rf project/_build project/.webassets-cache

clean: delpyc clean-foundation6 dev-clean prod-clean
	rm -Rf bin include lib local pip-selfcheck.json

install: install-venv install-foundation6

install-venv:
	virtualenv --no-site-packages --setuptools .
	bin/pip install -r requirements/dev.txt
	@echo "Install done. You should execute 'bin/activate' to start environment."

install-sassdoc:
	npm install sassdoc

install-foundation6: clean-foundation6
	@echo "* Download Foundation 6.3.1 archive;"
	wget https://github.com/zurb/foundation-sites/archive/6.3.1.tar.gz
	@echo "* Open archive;"
	tar xvzf 6.3.1.tar.gz
	@echo "* Delete archive;"
	rm -Rf 6.3.1.tar.gz
	@echo "* Use 'bower' to get Foundation dependencies"
	cd requirements/foundation6 && bower install
	@echo "* Link Foundation Javascript files into project sources"
	cd sources/js/foundation6 && ln -s ../../../foundation-sites-6.3.1/dist/js foundation
	cd sources/js/foundation6/vendor && ln -s ../../../../foundation-sites-6.3.1/vendor/jquery/dist/jquery.js
	cd sources/js/foundation6/vendor && ln -s ../../../../foundation-sites-6.3.1/vendor/modernizr/modernizr.js
	cd sources/js/foundation6/vendor && ln -s ../../../../foundation-sites-6.3.1/vendor/jquery.cookie/jquery.cookie.js
	cd sources/js/foundation6/vendor && ln -s ../../../../foundation-sites-6.3.1/vendor/what-input/dist/what-input.js

dev-build: dev-clean
	cd project && ../bin/optimus-cli build

dev-server:
	cd project && ../bin/optimus-cli runserver 0.0.0.0:8001

dev-watcher:
	cd project && ../bin/optimus-cli watch

dev-sassdoc:
	./node_modules/sassdoc/bin/sassdoc sources/sass/sveetoy --dest=./project/_build/dev/api

prod-clean:
	rm -Rf docs
	rm -Rf .webassets-cache

prod-build: prod-clean
	cd project && ../bin/optimus-cli build --settings githubpages_settings

prod-server:
	cd project && ../bin/optimus-cli runserver 0.0.0.0:8001 --settings githubpages_settings

prod-sassdoc:
	./node_modules/sassdoc/bin/sassdoc sources/sass/sveetoy

zip-release:
	bin/python release.py -f

release: zip-release prod-build prod-sassdoc

stylelint:
	@stylelint "sources/sass/**/*.scss" --formatter verbose
