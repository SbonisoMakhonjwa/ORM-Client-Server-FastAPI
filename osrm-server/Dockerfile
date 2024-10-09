#fetch image from docker hub https://hub.docker.com/
FROM osrm/osrm-backend:latest

# Copy the sources.list file to a temporary location (RUN is only for building image)
RUN cp /etc/apt/sources.list /tmp/sources.list

#change to workdirectory /data. if /data doesn't exist, then it will create the directory.
WORKDIR /data


# The OSRM image uses Debian stretch in it's package updates. Stretch is no longer supported.
# Replacing deb.debian with archive.debian then stretch with buster.
RUN sed -i 's/deb\.debian\.org/archive.debian.org/g' /tmp/sources.list && \
    sed -i 's/stretch/buster/g' /tmp/sources.list && \
    mv /tmp/sources.list /etc/apt/sources.list

#We need to install curl to fetch geo files
RUN apt-get update && apt-get install -y curl

#Fetching geo file. The reason for fetching it is that it is large. Cannot save in build context.
RUN curl -O https://download.geofabrik.de/africa/south-africa-latest.osm.pbf

RUN osrm-extract -p /opt/car.lua /data/south-africa-latest.osm.pbf
RUN osrm-partition /data/south-africa-latest.osrm
RUN osrm-customize /data/south-africa-latest.osrm

EXPOSE 5000

# Set the default command to run the shell script. This command is run when the container starts up.
CMD ["/usr/local/bin/osrm-routed", "--threads", "8", "--algorithm", "mld", "/data/south-africa-latest.osrm"]
