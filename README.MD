# Django Powered Blog Platform

This Django-powered blog a seamless user experience for both creators and readers. Key features include:

## Key Features

### 1. User Authentication
- Secure registration, login, and account management.
- Customized account dashboard with option to add or manage bio data such as profile picture, name, email, phone, bio, website, gender
- Any addition or updated on account section are sent with jquery ajax and sweetalert 2 js is used to show response 
### 2 Social authentication
-Users can log in or sign up with their google acccount instread of using password
### 3. Blog Post Management
- Modernized creation, editing, and publishing experience.
- Froala WYSIWYG editor for blog content field

### 4. Home Page Hero Section  Slider
- A slider showing the latest five approved posts.

### 5. Dedicated Pages
- Single Blog Page, authors page, single author page, categories page and single category page.

### 6. Contact page
- Contact page with ajax submission and sweetalert for responses
### 7. Sticky Sidebar On Single Blog Page
- Ensures easy navigation during scrolling.

### 8. Responsive Design
- Optimized for various devices.
- This is automatically handled by bootstrap css

### 9. Dark mode toggle
- The web app has a dark mode toggle button on the menu to switch from light to dark mode, to enhance user experience and accesibility. 
- It's also an emerging trend on most websites today.
- It also has a feature to check browser/client device mode preference and set it
- The choice between light or dark mode whether pecked from device preference or adjusted by user is remembered and applied throughout the app even if page is reloaded
## Technical Implementation

### Backend
- **Django:** backend for database interactions, user authentication, and application logic.

### Frontend
- **HTML, CSS, and Bootstrap:** Front-end that is visually appealing and responsive design.
- **jQuery:** Enhances user interactions and dynamic elements.
- **Sweetalert  2 js:** for interactive responses and messages 

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/paulmbui20/django-blog
    cd yourproject
    ```

2. Create a virtual environment:
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

7. Access the application at `http://localhost:8000`.

## Usage

### Search Functionality
- **Reusable Search Bar:** Embeddable on any page with customizable prefixes for unique instances.
- **AJAX Integration:** Uses jQuery AJAX for dynamic search results.

### Author Page
- **Sticky Sidebar:** Displays author’s image, bio, and website link for easy navigation.

### Category Page
- **Dynamic Listing:** Lists all categories with at least one published post, showing category image, name, description, and post count.

### Blog Posts
- **Responsive Grid:** Displays blog posts in a visually appealing grid layout.
- **Professional Design:** Uses Bootstrap to ensure a modern and user-friendly interface.

## Libraries Used
### 1. django-froala-editor 
### 2.  django-phonenumber-field 
### 3.  django-allauth
### 4.   PyJWT
### 5.  django-unfold 
### 6.   pillow 
### 7.  cryptography==43.0.3
### 8.  django-autocomplete-light==3.11.0
### 9.  django-environ==0.11.2






## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [jQuery](https://jquery.com/)
- [Sweetalert 2 js](https://sweetalert2.github.io/)
- [EMOBILIS](https://www.emobilis.ac.ke)
