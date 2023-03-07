# Babrigo Media
- Full stack photography portfolio and booking website

# Technologies
Django, Python, HTML, CSS, JS

# User Story
- User should be able to see an index page that contains a collection of photos
- User should be able to GET a collection of photos
- User should be able to GET their collection of photos * if applicable client
- SuperUser should be able to able to POST new photos into collection
- SuperUser should be able to DELETE collections, and single photos
- SuperUser should be able to UPDATE errors to collections or photos
- User should be able to CREATE and submit a contact form

# Wireframes
![Landing Page](Imgs/LandingPage.png)
![Collections Page](Imgs/Collections.png)
![Contact Page](Imgs/ContactPage.png)

# Route Tables

Main       
| **URL**          | **HTTP Verb**|**Action**|
|------------------|--------------|----------|
| /                | GET          | home  
| /collections     | GET          | index   
| /my_collections  | GET          | show  
| /contact         | POST         | post  
| /edit            | PUT & POST   | destroy

Users       
| **URL**                        | **HTTP Verb**|**Action**|
|--------------------------------|--------------|----------|
| /users/accounts/signup         | POST         | create   
| /users/accounts/login          | GET          | login  
| /users/accounts/login          | POST         | create  
| /users/accounts/logout         | DELETE       | destroy
