﻿# Passwordless Authentication System

## Official Description
A Django-based authentication system that provides flexible user authentication methods including both traditional password-based and passwordless options. The system features secure user registration with encrypted data storage, multiple authentication backends, and device fingerprinting capabilities. Built with Django 5.0+, this solution offers:

- Dual authentication methods (password-based and passwordless)
- Secure data encryption for sensitive user information
- Device fingerprinting for enhanced security
- MAC address tracking for trusted devices
- User-friendly registration process
- Customizable country selection
- Session management
- Modern responsive UI with clean CSS styling

Perfect for applications requiring flexible and secure authentication methods while maintaining user privacy through encrypted data storage.   
Check the Project Report for detailed documentation.  [Report](https://github.com/MBA-01/PasswordlessAuthentication/blob/b770deb00a4b80deb58e421bcac9d33cf0d4751d/Passwordless%20Authentication%20Report.pdf)


## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Security](#security)
- [Contributing](#contributing)
- [License](#license)

## Features
### Core Features
- **Dual Authentication Methods**
  - Traditional password-based authentication
  - Passwordless authentication via email/phone
- **Security Features**
  - AES-256 encryption for sensitive data
  - Device fingerprinting
  - MAC address tracking
  - Session management
  - CSRF protection
- **User Management**
  - Custom user model
  - Profile management
  - Device history tracking
- **UI/UX**
  - Responsive design
  - Clean, modern interface
  - Mobile-friendly layouts

## Project Structure
  
passwordless/  
├── accounts/  
│ ├── migrations/  
│ ├── management/  
│ ├── templates/  
│ │ └── accounts/  
│ ├── init.py  
│ ├── admin.py  
│ ├── apps.py  
│ ├── forms.py  
│ ├── models.py  
│ ├── urls.py  
│ └── views.py  
├── passwordless/  
│ ├── init.py  
│ ├── asgi.py  
│ ├── settings.py  
│ ├── urls.py  
│ └── wsgi.py  
├── static/  
│ ├── css/  
│ ├── js/  
│ └── images/  
├── templates/  
│ ├── base.html  
│ └── components/  
├── manage.py  
├── requirements.txt  
└── README.md  
  

## Requirements
- Python 3.8+
- Django 5.0+
- PostgreSQL 12+
- Additional dependencies in requirements.txt

## Installation
1. Clone the repository:     
    bash : '''  
            git clone https://github.com/yourusername/passwordless.git   
           '''   
2. Create and activate virtual environment:   
    bash : """     
            python -m venv venv  
            source venv/bin/activate # Linux/Mac   
            or     
            venv\Scripts\activate # Windows   
           """

3. Install dependencies:
    bash : """     
            pip install -r requirements.txt   
           """  
 
4. Configure environment variables:    
    bash : """     
        cp .env.example .env  
           """   

5. Run migrations:   
    bash : """     
python manage.py migrate   
           """   

6. Create superuser:   
    bash : """     
        python manage.py createsuperuser  
           """   

7. Run the development server:  
    bash : """      
        python manage.py runserver  
           """   
## Configuration
### Environment Variables.


#### env 

DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
EMAIL_HOST=smtp.your-email-provider.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@domain.com
EMAIL_HOST_PASSWORD=your-email-password


### Key Settings
- `AUTHENTICATION_BACKENDS`: Configure authentication methods
- `ENCRYPTION_KEY`: Set your encryption key for sensitive data
- `SESSION_COOKIE_AGE`: Configure session duration
- `ALLOWED_HOSTS`: Set allowed hosts for production

## Usage
### Password-based Authentication

python
"""from accounts.auth import PasswordAuthBackend"""

#### Example usage in views:

"""auth_backend = PasswordAuthBackend()
user = auth_backend.authenticate(request, username=username, password=password)
"""

### Passwordless Authentication

"""from accounts.auth import PasswordlessAuthBackend"""


## Security
- All sensitive data is encrypted using AES-256
- Passwords are hashed using Django's default PBKDF2 algorithm
- CSRF protection enabled for all POST requests
- Session cookies are secure and httponly
- Rate limiting implemented for authentication attempts
- Regular security updates and dependency monitoring

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

