from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class SignUp(models.Model):
    username = models.CharField(max_length=150, unique=True)  # Ensure unique usernames
    password = models.CharField(max_length=255)  # Store hashed passwords for security
    email = models.EmailField(unique=True)  # Email field with unique constraint
    date_joined = models.DateTimeField(auto_now_add=True)  # Automatically store the signup date
    
    def save(self, *args, **kwargs):
        # Automatically hash the password before saving
        if not self.pk or not check_password(self.password, self.get_password()):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    def get_password(self):
        """Returns the hashed password"""
        return self.password
