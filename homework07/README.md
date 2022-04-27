## Homework 07: Creating a Software Diagram for the Midterm Project

The objective of this project was to create a software diagram to illustrate a flow chart of files and related content for the Midterm Project. One script is found in this repository:

* `image.png`: a PNG image that displays the software diagram.

### About the Software Diagram

The software diagram contains three levels: the overarching Midterm Project, the files in the repository, and the methods found in the Python files, `app.py` and `test_app.py`.

In the diagram, an arrow points from `app.py` and `test_app.py` to `Dockerfile` because the Dockerfile contains all of the commands to build the image from the Python files. An arrow also connects `Dockerfile` to `Makefile` because the Makefile shortens the Docker commands `build`, `run`, and `push` to be used on the command line.

A level down, `app.py` is connected to Methods, separated into GET and POST. Each of the nine methods listed in GET uses the `GET` operation in HTTP to retrieve information, while the method in POST uses the `POST` operation to upload information. The file `test_app.py` is connected to a different section of Methods by an arrow, containing the method found in the file, `test_how_to_interact`.

An arrow connects the method `how_to_interact`, found in `app.py`, to `test_how_to_interact`, found in `test_app.py`. At the top of `test_app.py`, the file imports the method `how_to_interact`, and the method `test_how_to_interact` tests runs a "type" test to see if the method returns a string.

Here is a link to the Midterm Project mapped in this software diagram: https://github.com/nikhil-sharma710/o-iss-where-art-thou
