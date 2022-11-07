# django_rest_api

Basic functionalty 

Django rest api app that has 2 enpoints

/processFile - takes a csv file that gets validated and sent to db (currently using sqqlite)
    - Format of the csv file is as follows 
        Date,Purchase/Sale,Country,Currency,Net,VAT
        2020/1/19,Sale,Poland,AED,511.92,112.62
    - It will return the a json object with 2 arrays with keys successf and keys failed to indicate whether a key was inserted into the db

Running repo Locally

Everything gets built in a docker container to run you need docker and docker-compose[Example of how to install on Ubuntu] (https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/How-to-install-Docker-and-docker-compose-on-Ubuntu)

in The root of the repository run 

```
    docker-compose up
```
This will expose expose the service on port 8000


/retrieveRows gets values from db
    - Expects a country code and date 
    - Returns all values from db that have the matching date and country
    
  There is an exmaple postman (in the postman folder) collection one for each route.
  
  Code explantion can be found at Code.md
  
  and 
  
  Scaling docs can be found at Scale.md



