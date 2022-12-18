from django.db import models

class Contact(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.CharField(max_length=255)
    msg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fullname

# 