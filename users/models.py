from django.db import models
from django.contrib.auth.models import AbstractUser

# In Django, each class is a database model where attributes are the fields/columns of the database

class CustomUser(AbstractUser):

    # Customize User Model Here (Using age and job as sample)
    age = models.PositiveSmallIntegerField(null = True, blank = True, unique = False)

    # Be careful with string-based field types. Setting both null and blank will result in two possible values
    # for "no data" which will cause errors
    job = models.CharField(max_length = 100, blank = True)

    