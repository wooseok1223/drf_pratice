from django.conf import settings
from django.db import models


class Basic(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(Basic):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    is_public = models.BooleanField(default=False, db_index=True)
    ip = models.GenericIPAddressField(null=True, editable=False)

    # def dispatch(self, request, *args, **kwargs):
    #     print("request body : ", request.body) # print 비추 logger 추천
    #     print("request post : ", request.POST)
    #     return super().dispatch(request, *args, **kwargs)

