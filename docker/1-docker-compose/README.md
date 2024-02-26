# Introduction
This example combines a Python docker with FastAPI and a Selenium docker for web scraping

```
[Client] ---> [FastAPI Container] ---> [Selenium Chrome Container]
   |                |                             |
   |                |-----------------------------|
   |----------------|
        Docker Network
```
- The Client sends a request to the FastAPI Container (e.g., to perform web scraping on a specific URL).
- The FastAPI Container processes the request and forwards it to the Selenium Chrome Container over the Docker network using the Selenium WebDriver.
- The Selenium Chrome Container performs the web scraping and sends the result back to the FastAPI Container.
- Finally, the FastAPI Container sends the response back to the Client.

# how to run it
To start docker containers, use the following command:
```
docker-compose up -d
```
To test health in the browser, go to `http://localhost:8000`
To test web scraping, in postman
```
POST http://localhost:8000/scrawl
{
    "url": "https://pebblely.com/"
}
```