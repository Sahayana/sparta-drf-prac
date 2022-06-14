from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from user.forms import CustomUserChangeForm, CustomUserCreationForm
from user.models import User, UserProfile
# Register your models here.


# class CustomUserAdmin(UserAdmin):
#     form = CustomUserChangeForm
#     add_form = CustomUserCreationForm

#     list_display        = ("username", "email", "date_joined", "is_admin")
#     search_fields       = ("username", "email")
#     readonly_fields     = ("id", "date_joined", "last_login")
#     ordering            = ("username", )

#     fieldsets           = (
#         (None, {"fields" : ("id", "username", "password",)}),
#         ("Personal info", {"fields" : ("email", )}),
#         ("Permission", {"fields" : ("is_active", "is_admin", "is_staff", "is_superuser", "is_public")}),
#         ("Date", {"fields" : ("date_joined", "last_login")}),
#     )

# admin.site.register(User, CustomUserAdmin)

admin.site.register(User)

# class CustomUserProfileAdmin(admin.ModelAdmin):

#     list_display        = ("user", )
#     search_fields       = ("user", )    
#     ordering            = ("user", )

#     fieldsets           = (
#         (None, {"fields" : ("id", "user")}),
#         ("Personal info", {"fields" : ("bio", "birthday")}),        
#     )

# admin.site.register(UserProfile, CustomUserProfileAdmin)

admin.site.register(UserProfile)
admin.site.unregister(Group)
