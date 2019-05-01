# SCRAPEPOINT

ScrapePoint is a python script to convert [javatpoint](http://www.javatpoint.com) webpages to pdf. Finally it's highly customizable and does the job.


## Installation

First of all, clone or download the above project using,
```sh
$ git clone https://github.com/skbro/scrapePoint
```
Open scrapePoint directory.

#### Before Running app.py install following dependencies first:


```sh
$ pip install BeautifulSoup4
$ pip install pdfkit
```
Also, 
Step 1: Install "wkhtmltopdf" package from [here](http://wkhtmltopdf.org/) accordingly to your machine. Linux Users needs to download static binary as some of the features are missing in package provided by linux repos.
Step 2: For Windows => Add PATH to environment variables in line no. 155-156 in app.py add whole PATH to wkhtmltopdf.exe.

After Installation of all packages run the following command
```sh
$ python app.py
```

# Working

 - After running app.py, first of all it will ask the user about the topic and modules, he/she wants to download.
 - After this, it will request the webpage and get HTML of each module, it may take 2-4 mins depending upon length of whole topic
 - Then, it will convert each module to PDFs by the help of pdfkit and wkhtmltopdf packages in 1-2 mins, again according to length of whole topic. Note: pdfkit ignores some files mainly images when a certain request timeout is achieved.
 - Project already consists of javatpoint.css to get better PDFs.

## License

MIT
