.PHONY: help install clean delpyc build-demo

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  install              -- to proceed to a new install of this project. Will require 'git' client. Use clean command before if you want to reset a current install."
	@echo "  install-foundation5  -- to install last Foundation5 sources. Will require 'wget' and 'bower'."
	@echo
	@echo "  build-demo           -- to build demonstration site in development mode."
	@echo
	@echo "  clean                -- to clean your local repository from all installed stuff."
	@echo "  delpyc               -- to remove all *.pyc files, this is recursive from the current directory."
	@echo

delpyc:
	find . -name "*\.pyc"|xargs rm -f

clean: delpyc
	rm -Rf bin include lib local
	rm -Rf project/_build project/.webassets-cache
	rm -Rf foundation-sites-5.5.3

install:
	virtualenv --no-site-packages --setuptools .
	bin/pip install -r requirements/dev.txt
	@echo "Install done. You should execute 'bin/activate' to start environment."

build-demo:
	cd project && bin/optimus-cli build

install-foundation5:
	@echo "* Download Foundation 5.5.3 archive;"
	wget https://github.com/zurb/foundation-sites/archive/v5.5.3.tar.gz
	@echo "* Open archive;"
	tar xvzf v5.5.3.tar.gz
	@echo "* Delete archive;"
	rm -Rf v5.5.3.tar.gz
	@echo "* Use 'bower' to get Foundation dependencies"
	cd foundation-sites-5.5.3 && bower install