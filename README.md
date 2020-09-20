# DevOps_Assignment
The complete DevOps Assignment which includes problems related to Docker, System Architecture, and Automated Data Pipelines using Python

Que2. 
Ans: 
 
1.	Given architecture explanation:
-	DNS name
 - The Domain Name Server will provide access to web server to all users to access the website.
-	Content Delivery Networks (CDN)
o	CDN will shorten the time required for a server to communicate with a client by reducing the geographical distance between the server and the client.
-	Load Balancer
o	There are 2 Load Balancers which can distribute the network traffic across a cluster of particular servers to increase the availability of the website.
-	Service
o	There are 2 service servers that are provided to the users to maintain the application uptime.
•	Benefit:
o	The application which is running on foo.com will never go down and the website will be accessible without any delay.
o	When user sends a web request on web server, the request will get redirected to the nearest server according to the geographical location of the user and the server.
o	After the CDN, two load balancers will redirect the traffic of requests to the appropriate service servers depending on the traffic volume.
o	Two load balancers are used to maximize application uptime and data distribution.
o	It provides additional benefits such as data availability and application uptime consistency.

•	We could roll out an update to the service without any downtime impact to app foo.com by using below architecture,
o	Multiple Application Servers
o	Load Balancers
o	All HTTP request should be stateless to achieve zero downtime

•	We could deploy the above application using AWS Cloud services with the following architecture,
o	Two EC2 instances
	EC2 instance provides the service to the application which is running at example e.g foo.com
o	Elastic Load Balancer
	Elastic Load Balancer will redirect the web requests made by the users/ traffic across multiple target EC2 server to increase fault-tolerance in the application

