# helloworld

This is helloworld program written using Python Web Framework, Flask. 

# Instructions
- Pre-requisites and assumptions:
   
    - Linux/Mac OS operating system
    - Python 3.x installed
 
To make sure your Python installation is functional, you can open a terminal window and type python3, or if that does not work, just python. Here is what you should expect to see:

      $ python3
      Python 3.7.7 (default, Mar 10 2020, 15:43:33)
      [Clang 11.0.0 (clang-1100.0.33.17)] on darwin
      Type "help", "copyright", "credits" or "license" for more information.
      >>>

- To avoid mixing up with system python packages or other projects, create a virtualenv
      
      $pip3 install virtualenv
      
- Clone/download this git project to a temp location
- Extract the files to a location ex: /tmp/helloworld

      $cd helloworld
      $virtualenv venv
      $source venv/bin/activate

You should see a (venv) appear at the beginning of your terminal prompt indicating that you are working inside the virtualenv. Now when you install the dependent packages from requirements.txt file in project folder using pip3:

     $pip3 install -r requirements.txt

# Testing and validation
- Run unit tests 

      $pytest -v --cov
     
  Known Issues here:
    -- Need to enter "Ctl + C" to get out of some loop and show the results.
    -- Its also showing all system packages in code coverage. 
    
  ==================================== test session starts =============================================================
platform darwin -- Python 3.7.7, pytest-5.4.3, py-1.8.2, pluggy-0.13.1 -- /Users/rerigindindla/Downloads/helloworld-master/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/rerigindindla/Downloads/helloworld-master
plugins: cov-2.10.0
collected 4 items                                                                                                                                                     

test_helloworld.py::test_get_noheader PASSED                                                                                                                    [ 25%]
test_helloworld.py::test_post_noheader PASSED                                                                                                                   [ 50%]
test_helloworld.py::test_post_header PASSED                                                                                                                     [ 75%]
test_helloworld.py::test_get_header PASSED                                                                                                                      [100%]

# Running command line with curl
  - Open two terminal sessions 
  - On terminal 1: Start the webapp by going to helloworld folder (you should see helloworld.py)
         
         $python3 helloworld.py
    This will start a webapp and listening on 5000 on localhost
    
  - On terminal 2: Run the following curl commands:
    ** GET command with no Accept Header **
    
         curl -X GET http://127.0.0.1:5000/
    
    ** GET command with Accept Header **
    
         curl -H "Accept: application/json" -X GET http://127.0.0.1:5000/

    ** Repeat the above commands with POST (replace GET)
    
# Running in Debug mode
  Cancel the app on Terminal1, export the following variable and re-run the above comands. Notice the debug the statements printed on the web server.
         
         export FLASK_ENV=development
         $python3 helloworld.py
