from django.contrib import admin
from akkreditierung.models import Member


class MemberAdmin(admin.ModelAdmin):
    search_fields = ['MemberID', 'firstname', 'middlename', 'lastname', 'zipcode']
    list_display = ('MemberID', 'firstname', 'middlename', 'lastname', 'haspaid', 'debt', 'akk')
    list_editable = ('haspaid', 'debt', 'akk')
    list_filter = ['akk', 'haspaid']
    list_per_page = 20
    ordering = ['MemberID']

admin.site.register(Member, MemberAdmin)
