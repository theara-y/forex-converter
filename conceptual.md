### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  - Python is a strictly typed language. JS is not strictly typed.
  - Python does not have keywords for declaring variables. JS uses the keywords ***var***, ***let*** and ***const*** to declare variables.
  - The convention for naming variables in Python is *snake_case*. The convention for naming variables in JS is *camelCase*.
  - Constant variables in Python rely on the naming convention *ALL_CAP_SNAKE_CASE*. In JS, const variable are declared using the *const* keyword.
  - Python has 3 numerical types: *int*, *float* and *complex*. JS only has 2 numerical types *Number* and *BigInt*. 
  - Python uses indentation to define code blocks. JS defines code blocks within curly braces.
  - ***None*** is a special value in Python used to indicate the absence of a value. ***null*** is used in JS.
  - In Python, a variable must be initialized with a value. In JS, variables do not need to be initialized and are assigned with ***undefined*** by default.
  - Python has four primitive data types: *int*, *float*, *bool* and *str*. JS has seven primitive data types: *undefined*, *Boolean*, *String*, *Number*, *BigInt*, *Symbol* and *null*.
  - There are only single line comments in Python which starts with ***#***. In JS, single line comments start with ***//*** and multi-line comments are enclosed in ***/\**** and ***\*/***.
  - Python has built-in data structures such as tuple, list and dict. There are similar ways to create these data structures in JS, but they are known as arrays and objects or map.
  - Python uses // for floor divisions. JS uses the floor method from the Math object.
  - The '==' operator in Python is used to compare value and data type. JS uses '==' for value comparison and '===' for value and type comparison.
  - Python uses **and**, **or** and **not** as logical operators. JS uses **&&**, **||** and **!** as logical operators.
  - Python uses **type()** to check an instance's type, and JS uses **typeof**.
  - Python uses **print()** for output, and JS uses **console.log()**.
  - Python uses **elif** and JS uses **else if**.
  - Python uses **for...in** to loop through an iterable. JS uses **for...of**. **for...in** in JS is used to loop through an object's keys.
  - Python uses **def** to declare functions and JS uses the keyword **function**.
  - Python functions have to be called with the required number of arguments. In JS, any missing or additional arguments are treated as *optional*.
  - Constructors for Python classes override the **__init__** function and pass **self** to refer to a class' instance. Constructors in JS are declared as **constructor** and **this** is used instead.
  - Instances in Python do not use the *new* keyword, but JS does.
  - Python is mostly used for backend applications and requires a compiler and interpreter to run Python applications. JS is mostly used for frontend development and can be run in a browser. JS can also be run on the backend using a server like Node.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  1. Use the **get()** method on a **dict**. It will return **None** if the key is missing.
  2. Use **try** and **catch** when accessing the **dict**. A **KeyError** is thrown if the key is missing.

- What is a unit test?

A unit test involves testing one isolated piece of functionality such as *pure* functions where the same output is produced everytime for a given input.

- What is an integration test?

An integration test involves testing the behavior when two or more components interact with each other.

- What is the role of web application framework, like Flask?

A web application framework allows developers to build web applications quicker than if they were building from scratch. Flask for example provides a development server, debugging tools, and a library of helpful functionalities such as routes and template rendering.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

Using parameters are more appropriate when the data is an object used in the application or database. A URL query parameter is more appropriate for additional options or attributes. The HTTP methods GET, POST, DELETE signify fetching, creating, updating, and deleting data and parameters should indicate what type of data is being handled. In addition, URL query parameters are visible to users within in URL address, so sensitive information should not be stored there.

- How do you collect data from a URL placeholder parameter using Flask?

Declare the parameter in the route definition enclosed within angled brackets. Pass the parameter in the function being decorated. A type can be defined within the angled brackets before the parameter name.

    @app.route('/user/<int:id>')
    def getUser(id):
        # code...

- How do you collect data from the query string using Flask?

Import the **request** object from flask and then access **request.args** with the name of the query parameter.

    from flask import request
    ...
    request.args['foo'] or request.args.get('foo')

- How do you collect data from the body of the request using Flask?

The body of the request can be fetched through the **request** object. **request.data** will return the body as a string. **request.json** will return the body as a JSON if the content type of the request is set as **application/json** or use **request.get_json(force = True)** to ignore the content type.

    request.data # returns data string
    request.json # returns json data
    request.get_json(force = True) # returns json data

- What is a cookie and what kinds of things are they commonly used for?

A cookie is data structured as a key/value pair where the key and value are both strings. They are given to the client by the server to store on the client's browser. When the client visits the server again, the cookie is passed to the server in the client's request. The client can have multiple cookies from a single server and cookies from other servers. Cookies have an expiration time where it will no longer be valid. They are used to store user data generated from interacting with the website to save preferences or provide a personal experience. They are also used to automatically authenticate a user once they have logged in.

- What is the session object in Flask?

Session objects in flasks are cookies that are serialized, compressed and encoded using base64 encoding and signed to prevent users from modifying the session data.

- What does Flask's `jsonify()` do?

**jsonify()** returns a JSON string given a valid a JSON object.
