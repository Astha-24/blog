from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager):
    """Manager for User Profiles"""

    def create_user(self,email,name,password=None):
        """Create a new user Profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email=self.normalize_email(email)
        user=self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        import pdb;pdb.set_trace()
        """Create and save a new superuser with given details"""
        user=self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email= models.EmailField(max_length=255, unique=True)
    name=models.CharField(max_length=255)
    about=models.CharField(max_length=511)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS =['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name
    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.name

class Category(models.Model):
    category_name=models.CharField(max_length=255)
    category_description=models.CharField(max_length=511)
    def __str__(self):
        return self.category_name

class Story(models.Model):
    """Stories collection"""
    title = models.CharField(max_length=255)
    content = models.TextField(blank = False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    def __str__(self):
        """Return the model as a string"""
        return self.title

class Comment(models.Model):
        comment_message = models.TextField(blank = False)
        comment_time = models.DateTimeField(auto_now_add=True)
        comment_by =  models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE
        )
        story_on = models.ForeignKey(Story,on_delete=models.CASCADE)
        def __str__(self):
            """Return the model as a string"""
            return self.comment_message
