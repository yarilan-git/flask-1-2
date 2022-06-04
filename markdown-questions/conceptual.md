### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?  
  >JavaScript is used on the user side, for the development of the front-end. Python is used on the server side, for the development of the back-end.
  

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.  
  >* Use the .get(key) method, with or without having it return a default value. eg.  
    var = ``{"a": 1, "b": 2}``.get('a', 0)
  >* Use an if-in statement to find out if the key exists in the dictionary, prior to attempting to access it.  if "a" in ``{"a": 1, "b": 2}``:

- What is a unit test?  
  >A test that tests a single, atomic block of code that does not call other blocks of code

- What is an integration test?  
  >A test that evaluates how multiple basic units of code 'play togheter', and how they interact with each other.

- What is the role of web application framework, like Flask?  
  >To make the process of developing web applications quicker, by sparing the developer of the need to write extensive and complex layers of code, in the context of managing HTTP requests, and rendeing HTML pages.


- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?  
  >The former is better suited for use cases where the information passed becomes the 'hero' or the main topic of the page. The latter is suited for use cases where the informtion passed only somewhat modifies the behavior or content of the page.

- How do you collect data from a URL placeholder parameter using Flask?  
  >By using the request.args object. The data will be a key/value pair/s in this object.

- How do you collect data from the query string using Flask?  
  >By using the request.args object. The data will be a key/value pair/s in this object.

- How do you collect data from the body of the request using Flask?  
  >By using the request.form object.

- What is a cookie and what kinds of things are they commonly used for?  
  >A key/value pair, stored in the browser, containing informatin needed by the back-end

- What is the session object in Flask?  
  >An object that extends the standard cookie functionality. Supports mutliple data types, as opposed to cookies, which support only strings, and provides for better information security by encripting the content of the cookie.

- What does Flask's `jsonify()` do?  
  >It turns data returned by a route into a json-formatted object.
