# Dockerfile

# Directive instructing base image to build upon
FROM python:3

LABEL maintainer="Olusola Oseni <kenolusola@gmail.com>"

# Set a working directory where all the setup would take place in the image
WORKDIR /flight-booking

# All files in the root directory are copied here
COPY . /flight-booking

# The default user that should be used
USER root

# Install pipev and requirements
RUN apt-get update && apt-get install -y gcc
RUN cd /flight-booking && pip install -r requirements.txt

# ENTRYPOINT ["chmod", "+x"]
CMD [ "/flight-booking/docker/start_api.sh" ]
# ENTRYPOINT exec /flight-booking/docker/start_api.sh
