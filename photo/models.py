from xml.etree.ElementTree import Comment
from django.db import models
import datetime
# Create your models here.
class Photo(models.Model):
    img=models.ImageField(upload_to="",blank=True, null=True, default="noImg.png")
    title = models.CharField(max_length=200)
    # 최대길이가 200자라는 말
    writer=models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    body=models.TextField()
    password=models.CharField(max_length=10)
    like_count = models.PositiveIntegerField(default=0) #0또는 양수만 받는 필드

    # def __str__(self):
    #     return self.title

    # def summary(self):
    #     return self.body[:50]

class Visitor(models.Model):
    # star=models.CharField(max_length=10)
    visitor=models.CharField(max_length=50)
    date=datetime.date.today()
    # comment=models.TextField()