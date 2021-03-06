# DevOps_Assignment
The complete DevOps Assignment which includes problems of Automated Data Pipelines using Python with CLI, System Architecture, and Docker Deployment.

**--------------------------------------------------------------------------------------------------------------**     

### Que3. Automated Data Pipeline using Python with Command Line Interface (argparse module)
**Ans**:
- **Description of the tasks for which I built a automated data pipeline**,
  - Created 4 python scripts (First.py, Second.py, Third.py, Fourth.py) to run inside another main python program (sample.py) for wchich built an automated data pipeline.
  - Created main python program file called "sample.py" which will perform below tasks according to the requirements as follows 
    - **a**.	Navigated to the folder and ran other python scripts which contains some kind of data ingestion/tranformation.
    - **b**.	To get the inputs from the user via command line arguments I have used command line interface with "argparse" module in main python program and parsed it to run other 4 python scripts according to the requirement in asceding/desceding order.
    - **c**.	Printed the output as per the requirement,
      - Folder Path (/Users/akshay/Desktop/Python/script)
      - Files/ File it is executed (First.py, Second.py, Third.py, Fourth.py)
      - Outputs of files 
      - Log File (Log1.txt)
  
#### New things I learned:
       - Usage of Python with Command Line Interface with argparse module
       - Extensive Usage of Linux
       - Usage of Python as a programming
       - Automation of tasks by building automated data pipeline using Python with CLI
       
### Various ways to execute main python program "sample.py" using command line arguments,

  - **Execution of sample.py to execute a single python script**
      - python sample.py --folder /Users/akshay/Desktop/Python/script --file First.py --output log1.txt

  - **Execution of sample.py to execute a multiple python script in ascending order**
      - python sample.py --folder /Users/akshay/Desktop/Python/script --sort ascending --output log1.txt

  - **Execution of sample.py to execute a multiple python script in descending order**
      - python sample.py --folder /Users/akshay/Desktop/Python/script --sort descending --output log1.txt

       
**-------------------------------------------------------------------------------------------------------------**     

### Que2. System Architecture 
**Ans**: 

![alt tag](https://github.com/akshayjadhav21/DevOps_Assignment/blob/master/System%20Architecture.png "System Architecture")
 
## Given architecture explanation:
-	**DNS name**: - The Domain Name Server will provide access to web server to all users who want to access the application at foo.com.
- **Content Delivery Networks (CDN)**: - CDN will shorten the time required for a client to communicate with a server by reducing the geographical distance between the server and the client.
-	**Load Balancer**: - There are two load balancers which distribute the network traffic across a cluster of target servers to increase the availability of the application.
-	**Service**: - There are two service servers that are provided to the users to maintain the application uptime.

## Benefit:
- The application which is running on foo.com will never go down and the website will be accessible without any delay.
- When user sends a web request on web server, the request will get redirected to the nearest server according to the geographical location of the user and the server.
- Following the CDN, two load balancers will redirect the traffic of requests across target service servers depending on the volume of the traffic.
- Moreover, two load balancers are used to maximize application uptime and data distribution.
- It provides additional benefits such as data availability and application uptime consistency.

## We could roll out an update to the service without any downtime impact to application foo.com by using below architecture,
- Multiple Application Servers
- Load Balancers
- All HTTP request should be stateless to achieve zero downtime deployment

## We could deploy the above application using AWS Cloud services with the following architecture,
- **Two EC2 instances**: - EC2 instances will provide the service to the application which is running using URL e.g foo.com
- **Elastic Load Balancer**: - Elastic Load Balancer will redirect the web requests made by the users/ traffic across multiple target EC2 servers to increase fault-tolerance in the application

#### New things I learned:
     - How to understand and acknowledge the implemeted system architecture
     - How to leverage the infrastructure of the implemented architecture with new and updated changes
     - How to maitain the application consistency at the time of deployments with zero downtime deployment
     - How to implement and deploy the application architecture using AWS cloud services (I have a introductory knowledge of AWS Cloud Services) 
     
**-------------------------------------------------------------------------------------------------------------**  

### Que1. Docker
**Ans**:

- Firstly, as per the requirement I have pulled the Docker Image for SQL Server Developer Edition and checked whether image got pulled. (docker images)
- I have created the container by using the pulled image named as "sqlserver”. (docker run \ -e 'ACCEPT_EULA=Y' \ -e 'SA_PASSWORD=Password1!' \ -e 'MSSQL_PID=Express' \ --name sqlserver \ -p 1433:1433 -d mcr.microsoft.com/mssql/server:latest)
- After container creation, I have checked whether the docker container has created properly or not. (docker container ls)
- I have entered inside the newly created docker container. (docker exec -it sqlserver "bash")
- From the container I have connected to SQL command using sqlcmd with the required credentials. (/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "Password1!")
- Moreover, I have created the database named “testDB”, table “Test” and inserted a record into the table as per the requirement. (Given Scripts)

**The things I tried to implement a lot are as below**,
- I have tried to create DBScripts folder and tried to keep all my sql files into it to run, but I got confused about the directories while dealing with overall docker concept.
-	I have tried to implement the Dockerfile to process all things at a time such as pulling an SQL image, create a container using an image, expose SQL port outside the host image, but I was confused about how to fetch DBScripts folder and from which folder path.

#### New things I learned:
     - Extensive usage of docker to the developers
     - How to increase the efficiency of Testing environment with minimum memory requirement with docker
     - Unlike VMs, easy implementation of infrastructure and less memory consumed

