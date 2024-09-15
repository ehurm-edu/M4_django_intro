# code from https://tutorial.djangogirls.org/en/django_admin/

from django.contrib import admin
from .models import Post

admin.site.register(Post)