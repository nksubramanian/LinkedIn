# Read Me
- The  code runs on Python 3.9 and needs pip
- The project was build using virtual environment   
- The code is tested in Windows 10 using a postman collection
- The code needs a mongod daemon to be running for the persitance layer
- The mongodb uri has to be set in the enviornment variable AUDIO_FILE_SERVER_DATABASE_URI
- else the defaul value of the URI used is mongodb://localhost:27017/
- There is a postman collection to test (integration)
- Command to run test coverage is "coverage run --omit=venv/*,ut/* -m unittest"
- Command to get coverage report is "coverage html"