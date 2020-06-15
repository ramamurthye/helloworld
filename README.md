# helloworld

This is helloworld program written using Python Web Framework, Flask. 

# Instructions
- Pre-requisites and assumptions:
    Linux/Mac OS operating system
    Python 3.x installed
 
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



