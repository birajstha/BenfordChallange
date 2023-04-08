## How to Run this Flask App with Docker Compose

To run the Flask App with Docker Compose, follow the instructions below.

### Prerequisites

Docker and Docker Compose should be installed on your machine.

### Steps

1. Clone the repository and navigate to the root directory of the project.

2. Starting the database container:
    `docker-compose up -d benford_db`

3. Building the images
    `docker-compose build`

4. Once database is running, start the flask_app container
    `docker-compose up benford_app`

The webpage should be accessible at port 5000

docker run -p 5000:5000 birajstha/benford_app