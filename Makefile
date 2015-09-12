_BOWER_COMPONENTS_DIR=./bower_components/
_NODE_MODULES_DIR=./node_modules/

_VENDOR_SCRIPTS=${_BOWER_COMPONENTS_DIR}jquery/dist/jquery.js\
		${_BOWER_COMPONENTS_DIR}bootstrap/dist/js/bootstrap.js\
		${_BOWER_COMPONENTS_DIR}flat-ui/dist/js/flat-ui.js\
		${_BOWER_COMPONENTS_DIR}jquery-flatimeline/assets/js/jquery.flatimeline.js

_VENDOR_STYLESHEETS=${_BOWER_COMPONENTS_DIR}bootstrap/dist/css/bootstrap.css\
		    ${_BOWER_COMPONENTS_DIR}flat-ui/dist/css/flat-ui.css\
		    ${_BOWER_COMPONENTS_DIR}jquery-flatimeline/assets/css/jquery.flatimeline.css

_VENDOR_FONTS=${_BOWER_COMPONENTS_DIR}bootstrap/dist/fonts/*\
	      ${_BOWER_COMPONENTS_DIR}flat-ui/dist/fonts/*

_VENDOR_IMAGES=${_BOWER_COMPONENTS_DIR}flat-ui/dist/img/*

_PROJECT_DIRS=./bencook_info\
	      ./core\
	      ./personal\
	      ./blog


.PHONY: all
all: install lint build
	install
	lint
	build


.PHONY: install
install: package.json bower.json Gemfile
	npm install
	bower install
	bundle install


.PHONY: lint
lint:
	${_NODE_MODULES_DIR}jshint/bin/jshint .
	flake8 .
	pylint ${_PROJECT_DIRS}


.PHONY: build
build: ${_VENDOR_SCRIPTS} ${_VENDOR_STYLESHEETS}
	cat ${_VENDOR_SCRIPTS} > ./core/static/core/scripts/tmp.vendor.js
	${_NODE_MODULES_DIR}.bin/uglifyjs -cm -- ./core/static/core/scripts/tmp.vendor.js > ./core/static/core/scripts/vendor.min.js 2> /dev/null
	rm -f ./core/static/core/scripts/tmp.vendor.js

	${_NODE_MODULES_DIR}.bin/uglifyjs -cm -- ./personal/static/personal/scripts/about.js > ./personal/static/personal/scripts/about.min.js 2> /dev/null

	cat ${_VENDOR_STYLESHEETS} > ./static/styles/tmp.vendor.css
	${_NODE_MODULES_DIR}.bin/minify --output ./static/styles/vendor.min.css ./static/styles/tmp.vendor.css
	rm -f ./static/styles/tmp.vendor.css

	cp -r ${_VENDOR_FONTS} ./static/fonts/
	cp -r ${_VENDOR_IMAGES} ./static/img/

	bundle exec compass compile -e production --force


.PHONY: watch
watch: config.rb
	bundle exec compass watch
