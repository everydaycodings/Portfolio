# Django Porfolio Web App

Porfolio is a Django web application built with Python 3.12.0.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Azure Configuration](#azure-configuration)
- [.env File Configuration](#env-file-configuration)
- [Local Environment Setup](#local-environment-setup)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is configured to use Azure for its default database and file storage solutions. However, you can also set it up in a local environment for development and testing purposes.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-repository.git
    cd your-repository
    ```

2. **Create a virtual environment:**

    ```sh
    python3.12 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Run the server:**

    ```sh
    python manage.py runserver
    ```

## Usage

To use this project, follow the installation steps and then navigate to `http://127.0.0.1:8000/` in your web browser.



For a full list of models and their definitions, refer to the `models.py` file.

## Azure Configuration

This project uses Azure for its default database and file storage configurations. To configure Azure:

1. **Set up an Azure SQL Database.**
2. **Set up Azure Blob Storage** for file storage.
3. **Configure environment variables** by creating a `.env` file in the root of your project.

## .env File Configuration

The `.env` file should contain the following environment variables:

```env
# .env

# Database configuration
# Django Credentials
SECRET_KEY=''
DEBUG=True

# Azure Dtabase
DB_NAME=''
DB_USER=''
DB_PASSWORD=''
DB_HOST = ''
DB_PORT = ''


# Azure File Storage Settings
DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
STATICFILES_STORAGE_BACKEND = 'storages.backends.azure_storage.AzureStorage'
MEDIA_URL = ''
AZURE_ACCOUNT_NAME = ''
AZURE_ACCOUNT_KEY = ''
AZURE_MEDIA_CONTAINER = ''
AZURE_STATIC_CONTAINER = ''
AZURE_CONNECTION_STRING = ''


# Email Credentials
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = ''
ADMIN_EMAIL1 = ''
ADMIN_EMAIL2 = ''


# Cache Settings

# Cache time in minutes
CACHE_TIME = 15
```

You can adapt the values to match your Azure account and storage settings.

3. **Update your `settings.py` with the following configurations:**

    ```python
    # settings.py

    import os
    from dotenv import load_dotenv

    load_dotenv()

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sql_server',
            'NAME': os.getenv('DATABASE_NAME'),
            'USER': os.getenv('DATABASE_USER'),
            'PASSWORD': os.getenv('DATABASE_PASSWORD'),
            'HOST': os.getenv('DATABASE_HOST'),
            'PORT': os.getenv('DATABASE_PORT'),
        }
    }

    STORAGES = {
        "default": {
            "BACKEND": os.getenv('DEFAULT_STORAGE_BACKEND'),
            "OPTIONS": {
                "connection_string": os.getenv('AZURE_CONNECTION_STRING'),
                "azure_container": os.getenv('AZURE_MEDIA_CONTAINER'),
            },
        },
        "staticfiles": {
            "BACKEND": os.getenv('STATICFILES_STORAGE_BACKEND'),
            "OPTIONS": {
                "connection_string": os.getenv('AZURE_CONNECTION_STRING'),
                "azure_container": os.getenv('AZURE_STATIC_CONTAINER'),
            },
        },
    }
    ```

## Local Environment Setup

To set up and run the project in a local environment:

1. **Database Configuration:**

    Update the `settings.py` to use SQLite or any other local database of your choice:

    ```python
    # settings.py

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / "db.sqlite3",
        }
    }
    ```

2. **File Storage Configuration:**

    For local file storage, you can use the default file system storage:

    ```python
    # settings.py

    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
    ```

3. **Apply Migrations & Run Server:**

    Apply migrations and run the development server:

    ```sh
    python manage.py migrate
    python manage.py runserver
    ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Create a new Pull Request

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.