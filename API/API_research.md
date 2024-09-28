# What are APIs? How are they used and why are they so popular?
APIs (Application Programming Interfaces) are sets of rules and protocols that allow different 
software applications to communicate with each other. They act as intermediaries, providing a 
structured way for applications to exchange data and functionality.

# Create a diagram to showcase the data transfer process in API communication.
![img.png](img.png)
![img_1.png](img_1.png)


# What is a REST API? 

REST (Representational State Transfer) is an architectural style for designing networked applications,
primarily used for web services. It defines a set of constraints that, when applied, create a simple,
scalable, and maintainable API.

# What makes an API RESTful?
A RESTful API adheres to the following constraints:

- **Statelessness**: Each request is treated independently, without relying on previous requests. 
This makes the API scalable and easier to maintain.
- **Client-Server Architecture**: The API separates concerns between the client (the application making
the request) and the server (the application providing the service).
- **Cacheable**: Responses can be cached to improve performance and reduce load on the server.
- **Layered System**: The API can be layered to support modularity and scalability.
- **Uniform Interface**: The API uses a uniform interface, typically HTTP methods 
- (GET, POST, PUT, DELETE, etc.) and URIs to represent resources.
- 
# REST Guidelines:
1. Use HTTP methods appropriately.(GET,POST,PUT,DELETE,PATCH)
2. Use URIs to represent resources: URIs should be descriptive and consistent.
3. Leverage HTTP status codes: Use appropriate HTTP status codes to indicate the success or failure of 
a request.
4. Support caching: Implement caching mechanisms to improve performance and reduce load on the server.
5. Use HATEOAS (Hypertext As The Engine Of Application State): Allow clients to discover available 
actions and resources through the API responses.

# Benefits of RESTful APIs:
- Scalability: RESTful APIs are designed to be scalable, handling increasing loads efficiently.
- Flexibility: They are flexible and can support various use cases.
- Maintainability: RESTful APIs are easier to maintain and evolve over time.
- Interoperability: between different systems.


By following these guidelines, you can create robust, scalable, and maintainable RESTful APIs that are 
easy to use and understand.

# What is HTTP? (what does it stand for and what is it used for? What is HTTPS?)

# Explain HTTP request structure using the diagrams provided, or your own.

# Explain HTTP response structure using the diagram provided, or your own.

# What are the 5 HTTP verbs and what do they do?

GET → ?Retrieve a resource.
POST → Create a new resource.
PUT → Update an existing resource.
PATCH → Delete a resource.
DELETE → Apply partial updates to a resource.


# What is statelessness? Show examples of “stateless” and stateful http requests.

# What is caching?