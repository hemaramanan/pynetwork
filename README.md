Pynetwork

Pynetwork is a Network Automation tool with WEB GUI

Visit www.pynetwork.net for more information.


Quick Setup Quide

Step: 1

Create the docker-compose.yml file with the below-mentioned properties.


  version: "3.9"
  services:
    pynetwork:
      image: hemaramanan/pynetwork_backend
      volumes:
        - /app/pynetwork/data/
      ports:
        - "5000:5000"
    pynetwork_ui:
      image: hemaramanan/pynetwork_frontend
      ports:
        - "8080:80"
      depends_on:
        - pynetwork

Step: 2

Navigate to the particular folder which contained the docker-compose.yml file and run the docker-compose up command. while you enter that command, you may get some console output mentioned below.


  root@ubs:/home/dev/pynetwork/test# ls
  docker-compose.yml
  root@ubs:/home/dev/pynetwork/test# 
  root@ubs:/home/dev/pynetwork/test# docker-compose up
  Creating network "test_default" with the default driver
  Creating test_pynetwork_1 ... done
  Creating test_pynetwork_ui_1 ... done
  Attaching to test_pynetwork_1, test_pynetwork_ui_1

Congratulations, you have successfully deployed the pynetwork on your local environment. Let's have fun with pynetwork!

Step: 3

Access the pynetwork on your web browser by using the IP address of the host machine with port 8080. In my example, it is http://192.168.100.100:8080/ 