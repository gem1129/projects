from django.contrib import admin

from .models import Post

# Django admin 사이트에 Post모델을 등록한다
admin.site.register(Post)

# Register your models here.
