#web.py skeleton

This is a sample skeleton for a web.py application.

The structure is:

	 |-doc
	 |-licenses
	 |-requirements
	 |-www
	 |---app
	 |-----controllers
	 |-----models
	 |-----tools
	 |-----views
	 |---lib
	 |---log
	 |---static
	 |-----css
	 |-----img
	 |-----js
	 |---test
	 |---tmp

- doc: Documentation of the project.
- licenses: Project license or any other licenses used by 3rd party libraries go here.
- requirements: Mandatory Python libraries to install with pip.
- www: Project's www folder.
- www/app: The application itself.
- www/app/controllers: Handlers of the application. Each `{name}_handler` is a module.
- www/app/models: SQLAlchemy classes.
- www/app/tools: These are libraries which are dependent to application.
- www/app/views: Contains the HTML files (using Mako template engine). UI of the application.
- www/lib: 3rd party libraries which cannot be installed with pip or easy_install. These are application independent.
- www/log: Logging.
- www/static: Static files of the application, which contains javascript, images and css files.
- www/test: Unit testing.
- www/tmp: Contains the `mako_modules` and other unnecessary garbage files.
- www/main.py: The only file executed directly.
- www/settings.py: Default settings (constant variables etc.) of the application.
- www/urls.py: URL definitions which are mapped to their handler classes.