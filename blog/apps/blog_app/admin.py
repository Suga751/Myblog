from django.contrib import admin
from.models import Post
from.models import Comment

admin.site.register(Post)
admin.site.register(Comment)

# Register your models here. This is where we register out models so they can show up on our admin page.
