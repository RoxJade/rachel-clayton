from django.db import models


class Signup(models.Model):

    class Meta:
        verbose_name_plural = 'Subscribers'

    email = models.EmailField(max_length=254, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.email
