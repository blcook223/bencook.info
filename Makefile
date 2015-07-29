_BOWER_COMPONENTS_DIR=./bower_components/
_NODE_MODULES_DIR=./node_modules/

_VIRTUALENV_NAME=bencook.info.dev

_VENDOR_SCRIPTS=${_BOWER_COMPONENTS_DIR}jquery/dist/jquery.js\
		${_BOWER_COMPONENTS_DIR}bootstrap/dist/js/bootstrap.js\
		${_BOWER_COMPONENTS_DIR}flat-ui/dist/js/flat-ui.js\
		./vendor/DanielePetrarolo/flaTimeline.js/assets/js/jquery.flatimeline.js

_VENDOR_STYLESHEETS=${_BOWER_COMPONENTS_DIR}bootstrap/dist/css/bootstrap.css\
		    ${_BOWER_COMPONENTS_DIR}flat-ui/dist/css/flat-ui.css\
		    ./vendor/DanielePetrarolo/flaTimeline.js/assets/css/jquery.flatimeline.css

_PROJECT_DIRS=./bencook_info\
	      ./blog\
	      ./core\
	      ./personal

all: install lint build
	install
	lint
	build


install: package.json bower.json
	npm install
	bower install


lint:
	${_NODE_MODULES_DIR}/jshint/bin/jshint .
	flake8 .
	pylint ${_PROJECT_DIRS}


build: ${_VENDOR_SCRIPTS} ${_VENDOR_STYLESHEETS}
	cat ${_VENDOR_SCRIPTS} > ./core/static/core/scripts/tmp.vendor.js
	${_NODE_MODULES_DIR}.bin/uglifyjs -cm -- ./core/static/core/scripts/tmp.vendor.js > ./core/static/core/scripts/vendor.min.js 2> /dev/null
	rm -f ./core/static/core/scripts/tmp.vendor.js

	${_NODE_MODULES_DIR}.bin/uglifyjs -cm -- ./personal/static/personal/scripts/about.js > ./personal/static/personal/scripts/about.min.js 2> /dev/null
	${_NODE_MODULES_DIR}.bin/uglifyjs -cm -- ./personal/static/personal/scripts/resume.js > ./personal/static/personal/scripts/resume.min.js 2> /dev/null

	cat ${_VENDOR_STYLESHEETS} > ./core/static/core/styles/tmp.vendor.css
	${_NODE_MODULES_DIR}.bin/minify --output ./core/static/core/styles/vendor.min.css ./core/static/core/styles/tmp.vendor.css
	rm -f ./core/static/core/styles/tmp.vendor.css

	${_NODE_MODULES_DIR}.bin/minify --output ./core/static/core/styles/main.min.css ./core/static/core/styles/main.css
	${_NODE_MODULES_DIR}.bin/minify --output ./personal/static/personal/styles/main.min.css ./personal/static/personal/styles/main.css
