from django.contrib import admin
from akkreditierung.models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('MemberID', 'firstname', 'middlename', 'lastname', 'haspayed', 'debt')
    search_fields = ['MemberID', 'firstname', 'middlename', 'lastname', 'zipcode']

admin.site.register(Member, MemberAdmin)
