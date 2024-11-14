from django.db import models

# Create your models here.

TAGS = [
    ('TC','Technology'),
    ('HE','Health'),
    ('TR','Travel'),
    ('FO','Food'),
    ('LI','Lifestyle'),

]

class Blog(models.Model):
    id = models.IntegerField(primary_key=True,max_length=2)
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.CharField(choices=TAGS, max_length=10)

    class Meta:
        verbose_name_plural = "Blog"

    def __str__(self):
        return self.title
    
class Blog_1(models.Model):
    id = models.IntegerField(primary_key=True,max_length=2)
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.CharField(choices=TAGS, max_length=10)
   
    class Meta:
        verbose_name_plural = "Blog_1"

    def __str__(self):
        return self.title