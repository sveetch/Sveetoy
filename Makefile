.PHONY: help install install-venv install-foundation5 clean delpyc demo-build demo-server

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  install              -- to proceed to a new install of this project. Will require 'git' client. Use clean command before if you want to reset a current install."
	@echo "  install-venv         -- to install the Python virtual environment. Will require 'virtualenv'."
	@echo "  install-foundation5  -- to install last Foundation5 sources. Will require 'wget' and 'bower'."
	@echo
	@echo "  demo-build           -- to build demonstration site in development mode."
	@echo "  demo-server          -- to start demonstration site server with CherryPie."
	@echo
	@echo "  clean                -- to clean your local repository from all installed stuff."
	@echo "  delpyc               -- to remove all *.pyc files, this is recursive from the current directory."
	@echo

delpyc:
	find . -name "*\.pyc"|xargs rm -f

clean-foundation5:
	rm -Rf foundation-sites-5.5.3
	rm -Rf sources/js/foundation5/foundation
	rm -Rf sources/js/foundation5/vendor/*.js

clean: delpyc clean-foundation5
	rm -Rf bin include lib local pip-selfcheck.json
	rm -Rf project/_build project/.webassets-cache

install: install-venv install-foundation5

install-venv:
	virtualenv --no-site-packages --setuptools .
	bin/pip install -r requirements/dev.txt
	@echo "Install done. You should execute 'bin/activate' to start environment."

install-foundation5:
	@echo "* Download Foundation 5.5.3 archive;"
	wget https://github.com/zurb/foundation-sites/archive/v5.5.3.tar.gz
	@echo "* Open archive;"
	tar xvzf v5.5.3.tar.gz
	@echo "* Delete archive;"
	rm -Rf v5.5.3.tar.gz
	@echo "* Use 'bower' to get Foundation dependencies"
	cd requirements && bower install
	@echo "* Link Foundation Javascript files into project sources"
	cd sources/js/foundation5 && ln -s ../../../foundation-sites-5.5.3/js/foundation
	cd sources/js/foundation5/vendor && ln -s ../../../../foundation-sites-5.5.3/vendor/jquery/dist/jquery.js
	cd sources/js/foundation5/vendor && ln -s ../../../../foundation-sites-5.5.3/vendor/modernizr/modernizr.js
	cd sources/js/foundation5/vendor && ln -s ../../../../foundation-sites-5.5.3/vendor/jquery.cookie/jquery.cookie.js

demo-build:
	cd project && ../bin/optimus-cli build

demo-server:
	cd project && ../bin/optimus-cli runserver 0.0.0.0:8001
