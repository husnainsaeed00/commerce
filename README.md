# commerce
Commerce Project - Harvard Web Programming with Python and JavaScript
This repository contains the solution for the Commerce project from the Harvard Web Programming with Python and JavaScript course. The Commerce project is an e-commerce web application built using Python, Django, and JavaScript.

Project Description
The Commerce project aims to develop a full-stack e-commerce platform that allows users to create listings, place bids on items, and add items to their watchlist. It incorporates essential features of an online marketplace, including user authentication, item listing, bidding, and watchlist management.

The project consists of the following key components:

User Registration and Authentication: Users can register an account, log in, and log out. Authentication is implemented using Django's built-in authentication system.

Listing Creation: Authenticated users can create listings for items they wish to sell. They can provide details such as the title, description, starting bid, and optional image URL for the listing.

Item Bidding: Users can place bids on active listings. The bidding system ensures that bids must be higher than the current highest bid and meet any additional bid requirements set by the seller.

Watchlist Management: Users can add listings to their watchlist to keep track of items they are interested in. They can view and remove items from their watchlist.

Categories and Filtering: Listings can be assigned to different categories, and users can filter listings based on categories.

Setup and Installation
To set up the Commerce project locally, follow these steps:

Clone the repository to your local machine.

Install Python (version 3.x) if you don't have it already.

Set up a virtual environment to isolate project dependencies. Activate the virtual environment.

Install the required Python packages using pip:


pip install -r requirements.txt
Apply database migrations:


python manage.py migrate
(Optional) Load sample data into the database:


python manage.py loaddata sample_data.json
Start the development server:


python manage.py runserver
Open your web browser and visit http://localhost:8000 to access the Commerce project.

Project Structure
The project structure follows the standard Django project layout. Here's a brief overview of the main directories and files:

commerce/: The main Django project directory.

auctions/: The Django app directory containing the core application logic.
models.py: Defines the database models for listings, bids, users, and categories.
views.py: Implements the various views and request handlers.
forms.py: Contains form classes for creating and validating forms.
templates/: Contains the HTML templates for rendering the views.
static/: Stores static files such as CSS stylesheets and JavaScript files.
commerce_project/: Contains project-level configurations and settings.

settings.py: Configures the Django project settings.
urls.py: Defines the project-level URL routing.
sample_data.json: A JSON file containing sample data for testing and demonstration purposes.

Technologies Used
The Commerce project utilizes the following technologies and frameworks:

Python: The programming language used for the server-side logic and scripting.

Django: The web framework for building the e-commerce application using the Model-View-Controller (MVC) architectural pattern.

JavaScript: Used for client-side interactivity and enhancing the user experience.

License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as permitted by the license.

Acknowledgements
The Commerce project is based on the curriculum and project specifications provided by Harvard's Web Programming with Python and JavaScript course. Special thanks to the course instructors and teaching staff for their guidance and support.

