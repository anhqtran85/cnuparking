# CNU Parking Application


## Directories
- /cnuapp
  - /cnuapp
  - /main
    - /templates
    - /migrations
  - /tests
  
The `/cnuapp` directory contains all files used for the web application

The `/main` directory contains files to create the structure of the database (`models.py`), the url paths for 
connectivity between all html pages within the application (`urls.py`), a file that handles all the user requests 
and validates users (`views.py`), and a file that creates forms that are used in the html files (`forms.py`). 

Inside the `/main` directory is the `/migrations` directory that records all the changes made to the structure 
of the database and the `/templates` directory is also in the `/main` directory.  This directory holds all the html 
files used in the web application.

The `/tests` directory contains three different python files that test if the web application works correctly.

### Build locally
  1) Create Virtual Environment
     1) `cd` to desired directory
     2) run `python3 -m venv venv`
     3) run `source venv/bin/activate`
     4) run `sudo apt install python`
     5) run `sudo apt install django`
  2) Create Django Project
     1) `cd` to desired directory
     2) Copy the Clone with HTTPS address 
     3) Run `git clone [address]`

### Run application locally:

  1) `cd` to the directory that contains `manage.py` file
  2) run `python manage.py runserver`
  3) go to your web browser and paste `http://127.0.0.1:0000/`

This will save the generated pdf as "results.pdf"

### Kill:

To kill it, simply do `Ctrl+c`.
