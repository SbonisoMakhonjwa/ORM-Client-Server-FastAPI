# Fix the errors

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

To run this server, you need to run the following commands from the dockerfile directory:
1. docker build -t <your image name> .
2. docker run -p 5000:5000 <your image name>
The -p flag has the following pattern <host machine port>:<docker container port>. I.e. applications would be able to send traffic to port 5000 on your host machine which will be mapped to your container port.

The image is **BIG**. It will build into 4.5gb. Make sure you have enough space.

**Calculation server**
This server, is a "client" for the OSRM server. In other words, you will see a GET method which ultimately calls the OSRM server. 
This server is built with fastapi, which is a python server. You will need to Google the fastapi commands etc to see how this is started up.

Your job here is to fix the docker file and maybe some other code issues once the dockerfile is fixed. You will see that the docker file is missing a bunch of things (if you compare it to the OSRM server dockerfile). You need to add them and ensure that the fastapi server is started. Use the OSRM server dockerfile as a reference to see how things work.

HINT: docker uses a "build context" and that is typically the directory where your dockerfile is contained. Docker will need to copy items from the buildcontext to be able to run the application. It will need to use the files that you see in the build context.

**Required result**
Once both the servers are up and running, you should be able to call the calculation server on the relevant port and submit a longitude/latitude set to calculate the distance.
