# DevOps_Assignment
The complete DevOps Assignment which includes problems related to Docker, System Architecture, and Automated Data Pipelines using Python

### Que2. System Architecture 
**Ans**: 
 
## Given architecture explanation:
-	**DNS name**: - The Domain Name Server will provide access to web server to all users who want to access the application at foo.com.
- **Content Delivery Networks (CDN)**: - CDN will shorten the time required for a client to communicate with a server by reducing the geographical distance between the server and the client.
-	**Load Balancer**: - There are two load balancers which distribute the network traffic across a cluster of target servers to increase the availability of the application.
-	**Service**: - There are two service servers that are provided to the users to maintain the application uptime.

## Benefit:
- The application which is running on foo.com will never go down and the website will be accessible without any delay.
- When user sends a web request on web server, the request will get redirected to the nearest server according to the geographical location of the user and the server.
- After the CDN, two load balancers will redirect the traffic of requests to the appropriate service servers depending on the volume of the traffic.
- Also, two load balancers are used to maximize application uptime and data distribution.
- It provides additional benefits such as data availability and application uptime consistency.

## We could roll out an update to the service without any downtime impact to application foo.com by using below architecture,
- Multiple Application Servers
- Load Balancers
- All HTTP request should be stateless to achieve zero downtime

## We could deploy the above application using AWS Cloud services with the following architecture,
- **Two EC2 instances**: - EC2 instance provides the service to the application which is running at example e.g foo.com
- **Elastic Load Balancer**: - Elastic Load Balancer will redirect the web requests made by the users/ traffic across multiple target EC2 server to increase fault-tolerance in the application

### Que3. Automated Data Pipeline using Command Line Interface (argparse module)
**Ans**:
- **Description of the tasks for which I need to build automated data pipeline**,
  - There is one News Articles Website where many users usually submit their articles and interested people read the articles and upvotes the articles.
  - I have gathered a dataset of such article submissions and related information such as upvote count, time the article has been updated to the website, etc.
  - Secondly, I have performed two operations on the data for below tasks,
    - To find out the words that appear most often in the headlines of the article
    - To find the timing of article submissions
- **I have built an automated data pipeline using python program according to the requirements given for the problem**,
  - **a**.	I have navigated to the folder using following python code and ran the other python scripts to perform two operations stated above.
  - **b**.	I have taken the input using the argparse module in the python program to get the inputs from the user via command line arguments and parse it to perform operations on it which is quite easy and helpful to work upon for the users.
  - **c**.	I have taken the required arguments as well as optional arguments into the consideration to fulfill the mentioned requirements.
