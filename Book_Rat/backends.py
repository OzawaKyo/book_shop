from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import Group

class AdminBackend(ModelBackend):
    def user_can_access_admin_site(self, user):
        return user.is_active and user.is_superuser or user.groups.filter(name='Admin').exists()

    def has_perm(self, user, perm, obj=None):
        return self.user_can_access_admin_site(user)
