from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from allauth.account.models import EmailAddress
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model


from covid19_quarantine.users.forms import UserChangeForm, UserCreationForm

## Customize Admin
admin.site.site_header = "COVID-19 Quarantines Management"

## Unregister unnecessary stuff
admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.unregister(EmailAddress)
admin.site.unregister(Token)




User = get_user_model()



@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]
