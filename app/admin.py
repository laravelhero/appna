from django.contrib import admin
from app.models import Donation, Member
from import_export import resources


from import_export.admin import ImportExportModelAdmin

# Register your models here.

class DonationResource(resources.ModelResource):
    class Meta:
        model = Donation

class DonationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "purpose", "amount",)

admin.site.register(Donation, DonationAdmin)



class MemberResource(resources.ModelResource):
    class Meta:
        model = Member

class MemberAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "location", "medical", "year_of_graduation", "membership_type",)

admin.site.register(Member, MemberAdmin)