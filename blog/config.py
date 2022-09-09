import os

class Config:
    SECRET_KEY = os.environ.get('blog_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('blog_db')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('email_user')
    MAIL_PASSWORD = os.environ.get('email_password')

