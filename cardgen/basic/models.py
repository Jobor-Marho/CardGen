from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NewUserModel(User):
    businessname = models.CharField(max_length=264)
    is_verified = models.BooleanField(default=False)
    authkey = models.IntegerField(default=0)
