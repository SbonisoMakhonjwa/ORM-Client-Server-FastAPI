
**Pre-requisites**
1. Python installed
2. Docker installed

**Project structure**
This project consists of 2 servers:
1. OSRM server
2. Calculation server

Both these servers are deployed in docker containers.

**OSRM Server (not broken)**
The Open Source Routing Machine is a server which calculates the distance between two points. It takes in a longitude and latitude of two points and calculates the distance between the two.

The image is **BIG**. It will build into 4.5gb. Make sure you have enough space.

**Calculation server**
This server, is a "client" for the OSRM server. In other words, you will see a GET method which ultimately calls the OSRM server. 
This server is built with fastapi.