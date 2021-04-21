from django.contrib import admin
from blogone.models import *
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(User)