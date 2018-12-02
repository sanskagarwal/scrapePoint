# SCRAPEPOINT

ScrapePoint is a python script to convert [javatpoint](http://www.javatpoint.com) webpage to pdf. Currently it's not highly customizable but still does the job.


## Installation

First of all, clone or download the above project using,
```sh
$ git clone https://github.com/skbro/scrapePoint
```
Open scrapePoint directory.

#### Before Running app.py install following dependencies first:

=> For Windows Users
```sh
> pip install BeautifulSoup4
> pip install pdfkit
```
Also, 
Step 1: Install "wkhtmltopdf" package from [here](http://wkhtmltopdf.org/) accordingly to your machine.
Step 2: Add PATH to environment variables or in line no. 75 in app.py add whole PATH to wkhtmltopdf.exe.
        
=> For Linux Users
```sh
$ pip install BeautifulSoup4
$ pip install pdfkit
$ sudo apt-get install wkhtmltopdf
```

After Installation of all packages run the following command
```sh
$ python app.py
```

# Working

 - After running app.py, first of all it will request the webpage and get HTML of each module, it may take 2-4 mins
 - Then, it will convert each module to PDFs by the help of pdfkit and wkhtmltopdf packages in 30-40 seconds.
 - Project already consists of javatpoint.css to get better PDFs.


## License

MIT
