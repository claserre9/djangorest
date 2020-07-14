from django.contrib import admin
from apiempl import models

admin.site.register(models.User)
admin.site.register(models.UserForumPost)
admin.site.register(models.UserComment)

