from django.contrib import admin
from .models import Students, Encrypted_Data, Encryption_Keys
# Register your models here.
# class AccountsAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'subject', 'date']

# class AccountsAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'subject', 'date']

# class AccountsAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'subject', 'date']

admin.site.register(Students)
admin.site.register(Encrypted_Data)
admin.site.register(Encryption_Keys)
