API - Application Programming Interface

A set of rules that allows different software or systems to communicate with each other.
An API usually lives on a type of server and is used to manipulate the data from a database.
API's handle different types of requests.

As the USER we make REQUESTS to the API and the API returns us a RESPONSE, this RESPONSE containing data/message for our needs.
The API defines the format and structure of these messages/data.

Think of a restaurant. You (THE CLIENT) chooses what you want to eat (DATA), the KITCHEN (API) prepares you order and sends it to you.

We mentioned that an API defines the format and structure, but what does this look like?
There are many different types of formats but the most popular being JSON.

<hr>

JSON - JavaScript Object Notation:

    This consists of key-value pairs and arrays. Think of JSON containing objects of dictionaries and arrays to denote our data.
    Continuing with our kitchen example, this is a visual of what JSON data looks like:


    {
        "crust": "original",
        "toppings": ["cheese", "pepperoni", "garlic"],
        "status": "cooking"
    }

    When we make requests to our API to retrieve data, we typically receieve this, and our job as developers is to parse this
    data to our liking in a format that will help us do our task.

<hr>

HTTP REQUESTS: We can make different types of requests to our API to either receieve data or manipulate data to our database associated with
our API. Here are the common requests:

    GET: Retrieve data (like reading a menu)
    POST: Add new data (placing an order)
    PUT: Replace existing data (updating an order)
    DELETE: deleting existing data (canceling order)
    CUSTOM: You can create your own request types

Now that we've covered requests, we will make a circle and summarize:

    GET:
        Purpose: Used for retrieving data from an API.
        Scenario: Imagine you’re reading a menu in a restaurant. You’re not altering anything; you’re just checking what’s available.
        API Action: The client (you) sends a GET request to the server (kitchen), asking for specific information (like menu items).
    POST:
        Purpose: Used for adding new data to an API.
        Scenario: When you place an order at a restaurant, you’re adding a new item to their system.
        API Action: The client (you) sends a POST request to the server (kitchen), providing details (like your order).
    PUT:
        Purpose: Used for updating existing data in an API.
        Scenario: Imagine you ordered a pizza with extra cheese, but you change your mind and want less cheese now.
        API Action: The client (you) sends a PUT request to the server (kitchen), modifying the existing order.
    DELETE:
        Purpose: Used for removing data from an API.
        Scenario: If you decide to cancel your pizza order altogether, you’re removing it from the system.
        API Action: The client (you) sends a DELETE request to the server (kitchen), asking to discard the order.

<hr>

GET: assoicated with reading/retrieving data from our API
POST, PUT, and DELETE: associated with manipulating/removing data from our API

<hr>

Of course this is a very basic overview of API's but this is an amazing start. Keep going!
