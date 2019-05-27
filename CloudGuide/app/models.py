from django.db import models



class SubTopic(models.Model):
    subName = models.CharField(max_length=200)
    def __str__(self):
        return self.subName

class Topics(models.Model):
    topicsName = models.CharField(max_length=255)
    sub = models.ManyToManyField(SubTopic)
    def __str__(self):
        return self.topicsName

        