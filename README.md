# Generic HTTP Web Service Server in Python (GHoWSt)

![Logo](http://www.weburg.com/ghowst/images/ghowstlogo.png)

## An example server providing the Web service and an HTML-only static client

> [!NOTE]
> This is a work in progress to bring a GHoWSt Python server library up to parity with the Java version. Refer to the Java version until this note is removed.

Simple MVC architecture where controllers are defined in app/example.py, views are in templates/, and the model is whatever is needed, kept in app/.

Routing is provided by Flask. Path parameters are not used. Query string and URI parsing are done as needed.

### General setup

We're going to use the cross-platform Waitress WSGI server and rely on Flask to be the static HTML server.

Install Python 3.

### IDE (PyCharm) setup

Add [project_root]/tests to IDE's Include Path list (right click tests folder, then select Mark Directory As -> Test Sources Root)

Enable Flask integration in Settings -> Python -> Flask.

Using pip or your IDE, ensure that the dependencies in requirements.txt are installed to your Python environment.

### Running the application

The application will run with the Waitress WSGI server on port 8081. See further
below for running the Flask development server.

If using the CLI, ensure you are in the project directory. Run:

`python application.py`

If using an IDE, you should only need to run the below file:

`application.py`

Now test the application by going to http://localhost:8081 and make sure everything works.

For development, you can instead ensure you are in app/ and then run:

`python example.py`

Or, run it directly from the IDE.

Now, test the application by going to http://localhost:5000.

### Running the tests

To run unit tests only:

`python -m unittest discover tests/unit`

To run unit and integration tests:

First, ensure the Waitress WSGI server is running, then:

`python -m unittest discover tests`