from django.db import models

# super username asus
# super username2 sqldb
# super email 2736345T@student.gla.ac.uk
# super pw 1.5HoursLeft

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 128, unique = True)
    views = models.IntegerField(default = 0)
    likes = models.IntegerField(default = 0)

    def __str__(self):
        # return_str = str(self.name) + " " + str(self.views) + " " + str(self.likes)
        return self.name
    
class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title