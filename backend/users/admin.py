from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'username']

    def full_name(self, obj: User):
        return obj.get_full_name()
