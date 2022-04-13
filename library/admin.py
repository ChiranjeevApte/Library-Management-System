from click import BadParameter
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AdminAccount, Book


class AccountAdmin(UserAdmin):
	list_display = ('email','username','date_joined', 'last_login', 'is_admin','is_staff')
	search_fields = ('email','username',)
	readonly_fields=('id', 'date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

	

admin.site.register(AdminAccount, AccountAdmin)
admin.site.register(Book)
