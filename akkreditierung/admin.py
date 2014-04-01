from django.contrib import admin
from akkreditierung.models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('MemberID', 'firstname', 'middlename', 'lastname', 'haspaid', 'debt', 'akk')
    search_fields = ['MemberID', 'firstname', 'middlename', 'lastname', 'zipcode']
    list_filter = ['akk']

admin.site.register(Member, MemberAdmin)
