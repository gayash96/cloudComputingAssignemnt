# crickCenter

To deploy this application in your local system, follow below steps,

1. Clone the repo

2. Rename the application.py file to app.py
```In the Elastic Beanstalk, it looks for the file name application.py, If you are deploying on that, keep the file name as it is. If you are trying to deploy in local environment, then you should rename the file.```

3. Navigate to the code folder

4. Create the virtual environment 
```sh
python3 -m venv .venv
source .venv/bin/activate
```

5. Install the dependencies
 ```sh
pip install -r requirements.txt
```

6. Run the app
```sh
flask run
```


To deploy this application in Elastic Beanstalk, follow below steps,

1. Clone the repo. 

2. Remove the README file from the file list and make a compress from the remaining files to a zip file.

3. Upload the zip file to your Elastic Beanstalk python environemnt.
