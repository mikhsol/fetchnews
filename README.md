# News Fetcher

Cli application for news fetching from different news sources.

# Cli Application Usage

Usage information:
`python -m src.fetchnews -h`

# Environment set up

**Note**: It is required to use Python3!

To run cli application you need to have installed python3, packages form 
requirements.txt and MongoDB with standard configuration.

On a plain Ubuntu (16.04+) based system, do the next steps:
* Update apt packages: `sudo apt update`
* Install pip: `sudo apt install python3-pip`
* Install requirements `pip install requirements.txt`

I recommend you to run MongoDB as Docker container to have your environment 
clean.
* Install docker. Use this [guide](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/) 
for detailed installation information.
* Create directory to store data `mkdir ~/data`
* Run docker container `docker run -p 27017:27017 -v ~/data:/data/db mongo`.  
Use `-d` flag to run container as daemon.  
`-v` flag maps host ~/data directory with /data/db container directory.  
`-p 27017:27017` maps the host 27017 port to container port 27017.
27017 - default port MongoDB use.  
To get more information how to work with MongoDB docker container 
read this [post](https://www.thachmai.info/2015/04/30/running-mongodb-container/).

# Tests Running

* Running unit tests: `./unittests`  
This script will run only unit tests for the project.

* Running unit and integration tests with coverage: `./testcoverage`  
This script will run application with coverage framework and display 
results on standard output. After, it will clean results of coverage framework
work.

# Design

The solution was designed to provide modularity and allow developer
to easily extend application.

Strategy pattern used to implement html processors which encapsulate
the complexity of data fetching from raw html.

Strategy pattern also used in fetcher runners classes. These classes
specify the way application fetch data from particular source and provide
unified way to handle this data.

Repository pattern used to provide API for working with MongoDB.

To extend application and add new source of news, the developer only need 
to implement abstract methods of AbstractFetcherRunner class in the 
source related fetcher runner and provide implementation of specific
html processor for particular source by inheriting a new class from the
AbstractHtmlProcessor.

# License

Application developed under MIT license.