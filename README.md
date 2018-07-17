# News-Data
News-Data is a program that applies queries to a database and prints the results in a listed format.

## Requirements
You need Python installed on your OS to execute the program. Any version
after 2.7 will do.

Installation packages can be found here: https://www.python.org/getit/

You will also need to download virtual machine and vagrant, which will provide you the PostgreSQL database as well as an environment to run the project in. These two pieces of software can be downloaded here:
https://www.virtualbox.org/wiki/Download_Old_Builds_5_2
https://www.vagrantup.com/

Additionally, you will need a copy of the news database which can be downloaded here: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

## Deployment
To run the program execute the following from the shell:
'''
vagrant up
'''
followed by '''
vagrant ssh
'''

Then navigate to the vagrant folder in the news database you installed. From there execute the python program including any necessary path.
'''
python logs_analysis.py
'''

## License
This work is public domain.

## Acknowledgements
Thank you again to all my teachers at Udacity for continue to teach me how to make useful programs like this one!
