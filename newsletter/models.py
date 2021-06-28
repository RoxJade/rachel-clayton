from django.db import models


class Signup(models.Model):

    class Meta:
        verbose_name_plural = 'Subscribers'

    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.email
