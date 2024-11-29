# Django powered Blog Platform

This Django-powered blog a seamless user experience for both creators and readers. Key features include:

## Key Features

### User Authentication
- Secure registration, login, and account management.

### Blog Post Management
- Intuitive creation, editing, and publishing workflows.

### Home Page Slider
- Showcases the latest five approved posts.

### Dedicated Pages
- Blogs, authors, and categories with detailed post views.

### Sticky Sidebar
- Ensures easy navigation during scrolling.

### Responsive Design
- Optimized for various devices.

## Technical Implementation

### Backend
- **Django:** Robust backend for database interactions, user authentication, and application logic.

### Frontend
- **HTML, CSS, and Bootstrap:** Front-end technologies for a visually appealing and responsive design.
- **jQuery:** Enhances user interactions and dynamic elements.

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
- [EMOBILIS](https://www.emobilis.ac.ke)
