from django.db import models
import datetime
import os

def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('portfolio/', filename)


class Portfolio(models.Model):
    portfolio = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_file_path)
    published_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.portfolio


class Contact(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.CharField(max_length=255)
    msg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fullname

# 