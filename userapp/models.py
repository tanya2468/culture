from django.db import models

# Create your models here.
class Indian(models.Model):
    title = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to='images', null=True)
    image2 = models.ImageField(upload_to='images', null=True)
    category = models.CharField(max_length=200)
    content1 = models.TextField()
    content2 = models.TextField()
    content3 = models.TextField()
    content4 = models.TextField()
    link = models.TextField()



    class Meta:
        db_table = "indian"