# Django Powered Blog Platform

This Django-powered blog offers a seamless user experience for both article authors and readers. Key features include:

## Key Features

### 1. User Authentication
- Secure registration, login, and account management.
- Users can log in with either username or email against their password or entirely passwordless using their Google account
- Customized account dashboard with option to add or manage bio data such as profile picture, name, email, phone, bio, website, gender
- Any additions or updates on account section are sent with jquery ajax and sweetalert 2 js is used to show response 
### 2 Social authentication
-Users can log in or sign up with their Google account instead of using password
### 3. Blog Post Management
- Modernized creation, editing, and publishing experience.
- Ckeditor WYSIWYG editor for blog content field
- Users can create account or log in to add posts, this posts can only be published by site admins to be publicly accessible and crawlable by social media and search engine bots.
### 4. Search Engine Optimization Features(SEO)
- Descent page urls using slug generated from the post title
- Dynamic sitemap.xml file
- Robots.txt file
- Dynamic meta tags eg title, keyword and meta description tags
- Social media open graph (og) tags for social media bots
- Dynamic Alt text for images
### 5. Home Page Hero Section  Slider
- A slider showing the latest five approved posts.

### 6. Dedicated Pages
- Single Blog Page, authors page, single author page, categories page, search page and single category page.

### 7. Contact page
- Contact page with ajax submission and sweetalert for responses
### 8. Sticky Sidebar On Single Blog Page
- Ensures easy navigation during scrolling.

### 9. Responsive Design
- Optimized for various devices.
- This is automatically handled by bootstrap css

### 10. Dark mode toggle
- The web app has a dark mode toggle button on the menu to switch from light to dark mode, to enhance user experience and accesibility. 
- It's also an emerging trend on most websites today.
- It also has a feature to check browser/client device mode preference and set it
- The choice between light or dark mode whether pecked from device preference or adjusted by user is remembered and applied throughout the app even if page is reloaded


### **Project Structure**

The following is the structure of django my web app project:

```
django-blog/
├── blog/                      # Main application folder
│   ├── migrations/            # Database migration files
│   ├── templates/             # HTML templates for the blog
│   ├── static/                # Static files (CSS, JS, Images)
│   │   ├── css/               # Stylesheets
│   │   ├── js/                # JavaScript files
│   │   └── images/            # Images used in the blog
│   ├── admin.py               # Django admin configurations
│   ├── apps.py                # Application-specific configurations
│   ├── models.py              # Database models for the blog
│   ├── views.py               # Views handling HTTP requests
│   ├── urls.py                # URL routing for the blog
│   └── tests.py               # Unit tests for the blog
│
├── django_blog/               # Project configuration folder
│   ├── __init__.py            # Project initialization file
│   ├── asgi.py                # ASGI configuration for async requests
│   ├── settings.py            # Project settings (database, installed apps, etc.)
│   ├── urls.py                # Project-wide URL routing
│   └── wsgi.py                # WSGI configuration for deployment
│
├── media/                     # Uploaded media files (e.g., user images)
├── manage.py                  # Django management script
├── requirements.txt           # List of project dependencies
├── db.sqlite3                 # SQLite database file (default)
├── .gitignore                 # Git ignore file
└── README.md                  # Project documentation (this file)
```

---


## Technical Implementation

### Backend
- **Django:** backend for database interactions, user authentication, and application logic.

### Frontend
- **HTML, CSS, and Bootstrap:** Front-end that is visually appealing and responsive design.
- **jQuery:** Enhances user interactions and dynamic elements.
- **Sweetalert  2 js:** for interactive responses and messages
- **Toastrjs :** for global messages feedback using reactjs style toasters


### Search Functionality
- **Reusable Search Bar:** Embeddable on other page or section.
- **AJAX Integration:** Uses jQuery AJAX for dynamic search results.

### Author Page
- **Sticky Sidebar:** Displays author’s image, bio, and website link for easy navigation.

### Category Page
- **Dynamic Listing:** Lists all categories with at least one published post, showing category image, name, description, and post count.

### Blog Posts
- **Responsive Grid:** Displays blog posts in a visually appealing grid layout.
- **Professional Design:** Uses Bootstrap to ensure a modern and user-friendly interface.

## Libraries Used
### 1. django-ckeditor 
### 2.  django-phonenumber-field 
### 3.  django-allauth
### 4.   PyJWT
### 5.  django-unfold 
### 6.   pillow 
### 7.  cryptography==43.0.3
### 8.  django-autocomplete-light==3.11.0
### 9.  django-environ==0.11.2

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [jQuery](https://jquery.com/)
- [Sweetalert 2 js](https://sweetalert2.github.io/)
- [EMOBILIS](https://www.emobilis.ac.ke)

[//]: # (Grazie Professional plugin)