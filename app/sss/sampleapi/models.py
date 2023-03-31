from django.db import models

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=300) 
    age = models.IntegerField(default=0)
    place = models.TextField()
    email = models.EmailField()
    mobileNumber = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
