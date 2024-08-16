from django.contrib import admin
from .models import Profile, Comment, Subscriber
from .models import Post, Category

admin.site.register(Post)
admin.site.register(Category)
# admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Subscriber)
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Profile, ProfileAdmin)