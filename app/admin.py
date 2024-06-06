from django.contrib import admin
from app.models import Donation, Member
from import_export import resources
from django.utils.safestring import mark_safe


from import_export.admin import ImportExportModelAdmin

# Register your models here.

class DonationResource(resources.ModelResource):
    class Meta:
        model = Donation

class DonationAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ( "full_name", "email", "phone", "purpose", "amount", "created_at",)
    search_fields = ['full_name', 'email']
    list_per_page = 20
    # preserve_filters = True
admin.site.register(Donation, DonationAdmin)



class MemberResource(resources.ModelResource):
    class Meta:
        model = Member

class MemberAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    @admin.display(description=("Member Id"))
    def member_id(self, obj):
        return f"APPN10{obj.id}"

    def image(self, obj):
        return mark_safe(f"<img src={obj.profile_photo.url} width={50}>")

    list_display = ("member_id", 'image', "full_name", "email", "phone", "location", "medical", "year_of_graduation", "is_paid", 'modified_date')
    search_fields = ['full_name', 'email']
    list_filter = ["medical", "year_of_graduation"]
    list_per_page = 20

admin.site.register(Member, MemberAdmin)