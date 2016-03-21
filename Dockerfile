FROM java:8-jre-alpine
MAINTAINER Jens Kat <jenskat@gmail.com>

WORKDIR /lib/coral

ADD target/coral-runtime-0.0.131.jar /lib/coral

# Expose spray and akka tcp
EXPOSE 8000 2555

# main entrypoint, defaults can be overridden on docker run.
ENTRYPOINT ["java", "-cp", "coral-runtime-0.0.131.jar", "io.coral.api.Boot", "start"]

# docker build -t coral/runtime:0.0.131 -t coral/runtime:latest .
# docker run -it --name coral-runtime -p 8000:8000 coral/runtime -cp 32769 -ccp 192.168.99.100 -am "accept-all"
