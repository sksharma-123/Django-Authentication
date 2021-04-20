# Django-Authentication

This is a simple django built-in authentication system.

## Follow the following steps carefully : 

### Setup your django project.

### Clone the repository using the given command - 

> **git clone  [https://github.com/sksharma-123/Django-Authentication.git](https://github.com/sksharma-123/Django-Authentication.git)**

### Install the requirements from `requirements.py` file using the given command -

> **pip install -r requirements.txt**

### Move the following files from `files` folder to your main application folder, where `settings.py` file exists.

- `forms.py`
- `urls.py`
- `views.py`

### Modify these settings in your `settings.py` file.

    INSTALLED_APPS = [
	    ...
        'app',
	    'crispy_forms',
	    ...
    ]

---

	TEMPLATES = [
		{
			...
			'DIRS': ['templates'],
			...
		},
	]

### Add these settings at the end of your `settings.py` file.

	LOGIN_REDIRECT_URL = 'home'
	LOGOUT_REDIRECT_URL = '/'
	EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
	
---

### Make sure to run these commands after doing these settings.

	- python manage.py makemigrations
	- python manage.py migrate
