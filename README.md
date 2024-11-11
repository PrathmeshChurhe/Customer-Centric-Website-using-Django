# Customer-Centric Website using Django

This project is a customer-focused website built with Django. It includes essential pages, such as Home, About, Services, Technology, Team, Clients, and Contact, designed to provide users with information about the business and allow them to reach out or subscribe to a newsletter.

---

## Features

- **Home Page**: Allows users to subscribe to a newsletter by submitting their email.
- **Contact Form**: Users can submit inquiries with fields for name, email, subject, and message.
- **Informational Pages**: Includes pages such as About, Services, Technology, Team, and Clients.
- **Success Messages**: Uses Django’s messaging framework to notify users of successful newsletter subscriptions.
- **Admin Management**: Django’s admin interface allows easy management of newsletter subscribers and contact submissions.

---

## Project Structure

- **Models**:
  - `Contact`: Stores user inquiries, including name, email, subject, message, and date of submission.
  - `Newsletter`: Records newsletter subscriptions with email and subscription date.
- **Views**:
  - `home`: Handles newsletter subscriptions from the Home page.
  - `contact`: Processes contact form submissions from the Contact page.
- **Templates**: HTML templates for each page of the website.
- **URLs**:
  - Configured routes for each page, such as Home (`/`), About (`/about`), Services (`/services`), and Contact (`/contact`).

---

## Getting Started

### Prerequisites

- Python 3.x
- Django (install using `requirements.txt`)

### Installation

1. **Clone the Repository**:
    ```bash
    git https://github.com/PrathmeshChurhe/Customer-Centric-Website-using-Django
    cd Customer-Centric-Website-using-Django-master
    ```

2. **Install Dependencies**:
    Install the required packages listed in `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run Database Migrations**:
    Set up the SQLite database:
    ```bash
    python manage.py migrate
    ```

4. **Run the Server**:
    Start the Django development server:
    ```bash
    python manage.py runserver
    ```

    The website will be available at `http://127.0.0.1:8000/`.

---

## Available Pages and Endpoints

- **Home (`/`)**: The main landing page, where users can subscribe to the newsletter.
- **About (`/about`)**: Information about the company and its mission.
- **Services (`/services`)**: Details about the services offered.
- **Technology (`/technology`)**: Information on the technology stack used by the company.
- **Team (`/team`)**: Introduction to the team members.
- **Clients (`/clients`)**: Lists clients or testimonials.
- **Contact (`/contact`)**: Contact form for user inquiries.

---

## Usage

### Subscribing to the Newsletter

- Visit the Home page (`/`).
- Enter your email in the newsletter subscription form.
- On successful subscription, a message will appear confirming your subscription.

### Submitting the Contact Form

- Go to the Contact page (`/contact`).
- Fill in your name, email, subject, and message.
- Submit the form to save your inquiry. You will receive a success message upon completion.

### Admin Interface

To manage contacts and newsletter subscriptions:

1. **Access the Admin Interface**:
    Visit `http://127.0.0.1:8000/admin` and log in using an admin account.

2. **Manage Data**:
    - **Contacts**: View and manage contact inquiries.
    - **Newsletter Subscribers**: View and manage newsletter subscribers.

To create an admin account:
```bash
python manage.py createsuperuser
