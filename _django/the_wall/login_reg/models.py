from django.db import models
from datetime import date
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your models here.
class UserManager(models.Manager):
  def validator(self, postData):
    errors = {}
    first_name = postData.get('first_name', '').strip()
    last_name = postData.get('last_name', '').strip()
    email = postData.get('email', '').strip()
    password = postData.get('password', '').strip()
    confirm_password = postData.get('confirm_password', '').strip()

    if len(first_name) < 2:
      errors['first_name'] = 'Your first name should be at least 2 characters long.'
    if len(last_name) < 2:
      errors['last_name'] = 'Your last name should be at least 2 characters long.'
    if len(password) < 8:
      errors['password'] = 'Password must be at least 8 characters long.'
    try:
      validate_email(email)
    except ValidationError:
      errors['email'] = 'Please enter a valid email address.'
    if password != confirm_password:
      errors['confirm_password'] = 'Passwords do not match.'
    return errors


class User(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.EmailField()
  password = models.CharField(max_length=255)
  objects = UserManager()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)