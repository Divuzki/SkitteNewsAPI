from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.urls import reverse

# Third Party
from rest_framework.reverse import reverse as api_reverse

User = settings.AUTH_USER_MODEL

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=150, default='Admin')
    author = models.CharField(max_length=150)
    title = models.CharField(max_length=240)
    description = models.CharField(max_length=400, blank=True, null=True)
    content = models.TextField()
    urlToImage = models.CharField(max_length=2038, null=True, blank=True)
    urlToPost = models.CharField(max_length=3000, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

    @property
    def owner(self):
        return self.user

    def get_api_url(self, request=None):
        return api_reverse("api-post:post-rud", kwargs={'pk': self.pk}, request=request)

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)