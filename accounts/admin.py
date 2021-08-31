from django.contrib.auth import get_user_model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
	model = User
	list_display = ("email", "is_staff")
	ordering = ["-id"]
	fieldsets = (
		(None, {"fields": ("email", "password")}),
		("Permissões", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
		("Datas Importantes", {"fields": ("last_login", "date_joined")}))
