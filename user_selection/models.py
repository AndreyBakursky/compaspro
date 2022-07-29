from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User


class UserNew(User, AbstractBaseUser):
    ROOT = 'RT'
    MANAGER = 'MR'
    CRM_ADMINISTRATOR = 'CA'
    ROLE_CHOICES = [
        (ROOT, 'Root'),
        (MANAGER, 'Manager'),
        (CRM_ADMINISTRATOR, 'CRM-administrator')
    ]

    IMAGES = [
        'media/photos/root.jpg',
        'media/photos/manager.jpg',
        'media/photos/admin.jpg'
    ]

    role = models.CharField(
        max_length=2,
        choices=ROLE_CHOICES,
        default=ROOT
    )
    offer = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='photos/', blank=True, default='media/photos/root.jpg')

    def __str__(self):
        return self.username
