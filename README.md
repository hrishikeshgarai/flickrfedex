# FLICKR FED-EX

flickr. fetches images from NASA's account via the Flickr API.

The homepage contains four navigation tabs. 'About' provides a short summary of the website. 'Contact Us' provides the contact details.

The 'View All Images' page shows all the images fetched from the website. 'Search Images' page allows the user to enter a search query and displays only those images whose descriptions contain the search query. The header 'flickr.' can be used to navigate from various pages to the homepage.

The web application is built using Django in the Backend and JavaScript/HTML/CSS in the Frontend. It is deployed using AWS Elastic BeanStalk.

The backend logic can be found at:
[views.py](https://github.com/hrishikeshgarai/flickrfedex/blob/master/flickrfed/views.py)

Frontend logic for the various pages can be found at:
[Frontend](https://github.com/hrishikeshgarai/flickrfedex/tree/master/flickrfed/templates/flickrfed)

Below is a screenshot of the homepage of web application.

![alt text](https://github.com/hrishikeshgarai/flickrfedex/blob/master/Homepage.PNG)
