from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Message(models.Model):

    sender = models.ForeignKey(User, related_name='sent_messages')
    receiver = models.ForeignKey(User, related_name='received_messages')
    text = models.TextField()
    read = models.BooleanField(default=True)
    ts_created = models.DateTimeField(auto_now_add=True)
    ts_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-ts_created']

    def __str__(self):
        return 'Message ' + str(self.id)

    def get_absolute_url(self):
        return reverse('message', kwargs={'pk': self.id})
