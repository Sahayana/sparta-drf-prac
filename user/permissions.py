from email import message
from rest_framework import permissions
import datetime


class IsPublicPermission(permissions.BasePermission):
    message = "Only public user can post an article. (New users will be set public automatically 3 hours after sign up.)"

    # global permissions that accepts all incoming http requests.
    def has_permission(self, request, view):
        user =  request.user
        is_3hours = datetime.datetime.now() >= user.date_joined + datetime.timedelta(seconds=60*60*3)
        return (user.is_authenticated and is_3hours)