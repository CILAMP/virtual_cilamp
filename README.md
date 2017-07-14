![VL Demo](https://raw.githubusercontent.com/CILamp/vl/master/vl_demo.gif)

Virtual CILAMP
==============

A virtual CILAMP implemented in Python using Tkinter.

Installation
------------

Just clone the repo:

    $ git clone https://github.com/CILAMP/virtual_cilamp.git
    

Dependencies
------------

Make sure you have Python 2.7 or 3.4+ on your system.

Also make sure you have Tkinter on your system.

If on Windows, being able to start IDLE is a good check.

On Linux or Mac, if these give no exceptions, you got Tkinter:

    $ python
    >>import Tkinter  # If on 2.7
    >>import tkinter  # If on 3.x



Running
=======


Linux/Mac
---------

In root of repository:

	$ ./run


Windows bash environment
------------------------

    $ cd src
    $ winpty python winlamp.pyw

'winpty' is for getting Python to run in Windows git-bash properly [1].


Windows cmd.exe or .bat file environment
----------------------------------------
In command prompt, type

    C:\gitrepos\vl\>cd src
    C:\gitrepos\vl\src\>python winlamp.pyw

Skip console window like this, in a .bat file:

	REM pythonw.exe = no console window
	REM -i = specify lamp ID as command line parameter
	start C:\Python27\pythonw.exe D:\github\vl\src\winlamp.pyw -i my_own_lamp

Make a shortcut on your desktop to that .bat file and you can set an icon too :)


[1] http://stackoverflow.com/a/36530750
