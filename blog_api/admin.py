from django.contrib import admin
from blog_api import models

# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.Category)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title','author','category','verified')
admin.site.register(models.Story,StoryAdmin)
admin.site.register(models.Comment)
