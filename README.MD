# Django Powered Blog Platform

A robust, feature-rich, and visually appealing blog platform built with Django. This platform provides a seamless
experience for both authors and readers, featuring secure authentication (including Google Social Login), SEO
optimization, responsive design with dark mode, and an intuitive content management interface.

---

## 🌟 Key Features

### 👤 User Management & Authentication

- **Secure Authentication:** Standard registration and login using email/username.
- **Social Login:** Integrated Google OAuth for passwordless sign-in via `django-allauth`.
- **Custom User Profiles:** Personalized dashboards where users can manage their bio, profile picture, phone number, and
  social links.
- **AJAX-Powered Updates:** Profile updates are handled asynchronously with jQuery AJAX and SweetAlert2 for a modern UX.

### 📝 Content Management

- **Modern Post Editor:** Integrated CKEditor 5 for a rich-text editing experience.
- **Post Approval Workflow:** Users can submit posts, which remain unpublished until reviewed and approved by site
  administrators.
- **Image Handling:** Dynamic Alt text and automated profile picture uploads using Pillow.
- **Category Management:** Organizable blog posts with dedicated category pages.

### 🔍 Search Engine Optimization (SEO)

- **SEO-Friendly URLs:** Slugs generated automatically from post titles.
- **Sitemaps & Robots:** Dynamic `sitemap.xml` and `robots.txt` generation.
- **Meta Tags:** Automated generation of meta titles, keywords, and descriptions.
- **Open Graph (OG) Tags:** Rich previews when sharing posts on social media platforms.

### 🎨 Design & UI/UX

- **Responsive Design:** Built with Bootstrap to ensure compatibility across all devices (mobile, tablet, desktop).
- **Dark Mode Toggle:** User-switchable light/dark mode that respects system preferences and persists across sessions.
- **Hero Slider:** Featured section on the homepage showcasing the latest five approved posts.
- **Sticky Sidebar:** Persistent navigation on single blog pages for improved readability.
- **Interactive Feedback:** Global message feedback using Toastr.js and SweetAlert2.

---

## 🛠️ Tech Stack

- **Backend:** [Django 5.2](https://www.djangoproject.com/)
- **Frontend:** HTML5, CSS3, [Bootstrap 5](https://getbootstrap.com/), [jQuery](https://jquery.com/)
- **Database:** SQLite (default), supports PostgreSQL/MySQL
- **Rich Text Editor:** [CKEditor 5](https://ckeditor.com/ckeditor-5/)
- **Auth:** [Django-allauth](https://django-allauth.readthedocs.io/)
- **Utilities:** Pillow (Images), SweetAlert2, Toastr.js, django-phonenumber-field

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- **Python 3.12+**
- **pip** (or [uv](https://github.com/astral-sh/uv) for faster dependency management)
- **Git**

### 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/paulmbui20/django-blog.git
   cd django-blog
   ```

2. **Set up a virtual environment:**
   ```bash
   # Using venv
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

   # OR using uv (recommended)
   uv venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   # Using pip
   pip install -r requirements.txt

   # OR using uv
   uv sync
   ```

4. **Configure Environment Variables:**
   Copy the example environment file and update the values:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and provide your `SECRET_KEY`, `DEBUG` status, and other necessary credentials.

### 🔧 Database Setup

1. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

2. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

### 🏃 Running the Project

1. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

2. **Access the application:**
    - Website: `http://127.0.0.1:8000/`
    - Admin Panel: `http://127.0.0.1:8000/admin/`

---

## 📁 Project Structure

```text
django-blog-prod/
├── accounts/           # User authentication and profile management
├── blog/               # Core blog logic, posts, and comments
├── djangoBlog/         # Project configuration (settings, urls, asgi/wsgi)
├── media/              # User-uploaded files (profile pics, post images)
├── static/             # Global static files (CSS, JS, Images)
├── templates/          # Global HTML templates
├── manage.py           # Django management script
├── pyproject.toml      # Project metadata and dependencies
└── requirements.txt    # Dependency list
```

---

## 🧪 Testing

Run the test suite to ensure everything is working correctly:

```bash
python manage.py test
```

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- [Django Framework](https://www.djangoproject.com/)
- [Bootstrap Team](https://getbootstrap.com/)
- [EMOBILIS](https://www.emobilis.ac.ke) for the inspiration and guidance.
- [SweetAlert2](https://sweetalert2.github.io/) and [Toastr.js](https://codeseven.github.io/toastr.js/) for the awesome
  UI components.
