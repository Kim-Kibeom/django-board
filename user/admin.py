from django.contrib import admin

from .models import User

admin.site.register(User)

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('user_id', 'email', 'password', 'created_at', 'updated_at')

# admin.site.register(User, UserAdmin)    
