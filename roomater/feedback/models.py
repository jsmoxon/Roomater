from django.db import models

class Fdbck(models.Model):
    message = models.CharField(max_length = 10000)
    sender = models.EmailField()    
    def __unicode__(self):
        return self.sender