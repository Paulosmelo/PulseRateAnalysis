# Resume
This project was created to help me to learn how to use python and javascript for data visualization. It is a web page that shows data from analysis about pulse rates and exercises.  

# Data
I get the data from a list of data sources made to help students who are learning about data science. If you want to know about it, follow the link below. 

https://vincentarelbundock.github.io/Rdatasets/doc/Stat2Data/Pulse.html  

# Data Retrieving
It is going to be use python to reads the data and insert it in a SQLite database. The python file is going to fill the database and after that, another python file is gonna read it and creates a js file with objects.

# Data visualization
It going to use a js library (chart.js) to get the js file and create a bubble chart.

# Required
Python 3 and SQLite.

# Tutorial
Step 1: Download the code and unzip it.  
Step 2: Run file "src/model.py" to create a database and insert data into it.  
Step 3: Run file "src/controller.py" to create a js file with the objects.  
Step 4: Open "view/index.html" in your browser.
