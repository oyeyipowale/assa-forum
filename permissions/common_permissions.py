from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth.model import Group







# class IsOwnerOrReadOnly(BasePermission):
#     message = "You must be the owner of this thread"
#     my_safe_method = ['GET']

#     def has_permission(self, request, view):
#         if request.method in self.my_safe_method:
#             return True
#         return False

#     def has_object_permission(self, request, view, obj):
        
#         if request.method in SAFE_METHODS:
#             return True
#         return obj.owner == request.user