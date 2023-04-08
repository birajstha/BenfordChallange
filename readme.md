## How to Run this Flask App with Docker Compose

To run the Flask App with Docker Compose, follow the instructions below.

### Prerequisites

Docker and Docker Compose should be installed on your machine.

### Steps
1. Clone the repository and navigate to the root directory of the project.

2. Run the following command to build the images:
    
    docker-compose up -d flask_db

`docker-compose build`

`docker-compose up flask_app`

`docker stop $(docker ps -a -q)`

`docker rm $(docker ps -a -q)`