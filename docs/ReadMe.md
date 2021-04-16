# Read Me
## What's done
- The intention of the code is to meet the requirements outlined in docs/coding-challenge.pdf
- The code is developed using Python 3.9 using Virtual environment for package isolation
- The application is build using Flask (Other dependencies are in Requirements.txt)

## Pre-requisites  
- The application has a pre-requisite of MongoDB Daemon
- The mongodb uri is set as env var named AUDIO_FILE_SERVER_DATABASE_URI (else defaults to mongodb://localhost:27017/)

## Running
- The application's entry point is startup.py
- The command is `python startup.py`
  
## Unit tests
- The application is unit tested using the default framework `unittest`
- The command to run unit test is python -m unittest
- The unit test coverage is measured by `coverage`
- Command to run test coverage is "coverage run --omit=venv/*,ut/* -m unittest"
- Command to get coverage report is "coverage html"
- The coverage report is available at htmlcov/index.html
- **The unit test code coverage is 100%**

## Integration Tests
- The integration tests are available as a post man collection (2.1 version)
- The collection can be found at docs/AudioService.postman_collection.json  
