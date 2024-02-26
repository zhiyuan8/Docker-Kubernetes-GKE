# docker-compose

This guide provides instructions for setting up and managing Docker containers using Docker Compose, including a sample project setup that integrates a Python FastAPI container with a Selenium Chrome container for web scraping.

## Getting Started with Docker Compose

### Installing Docker Compose on Linux

To install `docker-compose`, execute the following commands in your terminal:

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```

**Note:** Ensure that your `docker-compose.yml` or `docker-compose.yaml` file is located in the root directory of your project.

### Basic Docker Compose Commands

- **Starting Containers:** To start your Docker containers in detached mode, similar to the `docker run` command, use:
    ```bash
    docker-compose up -d
    ```
- **Building and Starting Containers:** To build your Docker containers and then start them in detached mode, akin to running `docker build` followed by `docker run`, use:
    ```bash
    docker-compose up --build -d
    ```
- **Following Logs in Real-Time:** To follow the container logs in real-time, execute:
    ```bash
    docker-compose logs -f
    ```
- **Stopping Containers:** To stop and remove all containers, networks, and volumes associated with your Docker Compose setup, use:
    ```bash
    docker-compose down
    ```

### Restart Policies

Specify the restart behavior of your containers in the `docker-compose.yml` file using the following options:

- `no`: Never restart.
- `always`: Always restart.
- `on-failure`: Restart only when the container exits with an error.
- `unless-stopped`: Restart unless the container is stopped manually.

## Example Project: `1-docker-compose`

This project demonstrates integrating a Python Docker container running FastAPI with a Selenium Chrome container for web scraping purposes.

### Architecture Overview

```
[Client] ---> [FastAPI Container] ---> [Selenium Chrome Container]
   |                |                             |
   |                |-----------------------------|
   |----------------|
        Docker Network
```

- The **Client** sends a request to the **FastAPI Container** (e.g., to perform web scraping on a specific URL).
- The **FastAPI Container** processes the request and forwards it to the **Selenium Chrome Container** over the Docker network using the Selenium WebDriver.
- The **Selenium Chrome Container** performs the web scraping and sends the results back to the FastAPI Container.
- Finally, the **FastAPI Container** sends the response back to the Client.

### Running the Project

1. Start the Docker containers with:
    ```bash
    docker-compose up -d
    ```
2. To test the health of the application, visit `http://localhost:8000` in your browser.
3. To test the web scraping functionality, use Postman to send a POST request:
    ```json
    POST http://localhost:8000/scrawl
    {
        "url": "https://pebblely.com/"
    }
    ```

# Docker Network

*TODO*

# Docker Swarm

*TODO*

# References

- [Working with Multiple Containers Using Docker Compose](https://www.digitalocean.com/community/tutorials/workflow-multiple-containers-docker-compose)

---

This structure uses Markdown elements like headings, code blocks, and lists to organize the content, making it more accessible and easier to follow for readers.