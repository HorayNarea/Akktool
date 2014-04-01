from django.contrib import admin
from akkreditierung.models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('MemberID', 'firstname', 'lastname')

admin.site.register(Member, MemberAdmin)
