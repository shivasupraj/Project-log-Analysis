# Project-log-Analysis


This is an internal reporting tool that produces answers by printing them out to a text file.

The tool produces answers to the following three questions based on the data in the database:

1. What are the most popular three articles of all time?
2. Who are the most popular articles authors of all time?
3. On which days did more than 1% of requests lead to errors?

## To get started with the project download the following resources.
1. Get python3 from [here](https://www.python.org/downloads/)
2. Get virtual Box 5.1 from [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
3. Get vagrant from here [here](https://www.vagrantup.com/)
4. Download the VM configuration file from [here](https://github.com/udacity/fullstack-nanodegree-vm)
5. Download the sql data from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## Instructions
* Go to the vagrant sub directory from your terminal and type vagrant up, this will cause the vagrant to download and install the Linux Operating System.
* Now run `vagrant ssh` to login to the newly installed Linux virtual machine.
* Now run `cd /vagrant` and go inside the vagrant folder, remember that doing `ls` won't display the vagrant folder.
* Now extract the sql data and put the .sql file inside the vagrant folder so that it can be shared with the Virtual machine.
* Now to load the data into our database, run `psql -d news -f newsdata.sql`.
* Now clone `Project-log-Analysis` into your vagrant folder and run `python log-analysis.py > output.txt` or `python3 log-analysis.py > output.txt` to run the application.
