from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import RegexValidator

class Post(models.Model):
    title  = models.CharField(validators=[RegexValidator(regex='.{5,}',
                              message='Title should contain at least 5 Charcters',
                              code='nomatch')], max_length=60)
    content = models.TextField(validators=[RegexValidator(regex='.{30,}',
                               message='Text should contain at least 30 Charcters',
                               code='nomatch')], max_length=5000)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    up_votes = models.ManyToManyField(User, related_name="up_votes", blank=True)
    down_votes = models.ManyToManyField(User, related_name="down_votes", blank=True)
    rates = models.IntegerField(default=0)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('user-posts', kwargs={'username':self.author.username})
