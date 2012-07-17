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
	 |-----bridge
	 |-----views
	 |---lib
	 |---log
	 |---public
	 |-----css
	 |-----img
	 |-----js
	 |---static
	 |-----css
	 |-----cs
	 |-----img
	 |-----js
	 |---test
	 |---tmp


- **doc**: Documentation of the project.
- **licenses**: Project license or any other licenses used by 3rd party libraries go here.
- **requirements**: Mandatory Python libraries to install with pip.
- **sh**: Bash script files of the project.
- **www**: Project's www folder.
	- **app**: The application itself.
		- **controllers**: Handlers of the application. Each `{name}_handler` is a module.
		- **models**: Models of the application.
		- **bridge**: Here goes the services that connects with another services (such as a socket server running on Java).
		- **tools**: These are libraries which are dependent to application.
		- **views**: Contains the HTML files (using Mako template engine). UI of the application.
	- **lib**: 3rd party libraries which cannot be installed with pip or easy_install. These are application independent.
	- **log**: Logging.
	- **public**: Static files of the application, which contains javascript, images and css files.
	- **static**: Static files of the application, which contains javascript, coffeescript, images and css files.
	- **test**: Unit testing.
	- **tmp**: Contains the `mako_modules` and other unnecessary garbage files.
	- **main.py**: The only file executed directly.
	- **settings.py**: Default settings (constant variables etc.) of the application.
	- **urls.py**: URL definitions which are mapped to their handler classes.

# High Level Diagrams

![](https://github.com/faruken/web.py-skeleton/raw/master/wpk2.png)

## Package Diagrams

### Sub-modules
![](https://github.com/faruken/web.py-skeleton/raw/master/wpk0.png)

### High-level modules

![](https://github.com/faruken/web.py-skeleton/raw/master/wpk1.png)


