from django.db import models


class Message(models.Model):
    message_text = models.TextField()
    status = models.BooleanField(default=False)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.message_text
    