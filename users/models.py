from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.PositiveIntegerField()
    registration_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    points = models.IntegerField(default=0)
    level = models.IntegerField(default=1)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    objectives = models.TextField()
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    
    assistance_days = models.DateField(auto_now=False, auto_now_add=False)
    membership_start_date = models.DateField(null=True, blank=True, help_text='Date when the client started their gym membership')
    membership_expiry_date = models.DateField(null=True, blank=True, help_text="Date when the client's membership will expire")

    def __str__(self):
        return f"{self.user.name} Client Profile"