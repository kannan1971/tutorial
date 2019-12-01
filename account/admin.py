from django.contrib import admin
from account.models import UserProfile



class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'website', 'user_phone' ,'user_info')

# using Method to return column data
    def user_info(self,obj):
        return obj.description

    def user_phone(self,obj):
        return obj.Phone

#  To sort the column asc or desc

    def get_queryset(self, request):
        queryset=super(UserProfileAdmin,self).get_queryset(request)
        queryset=queryset.order_by('-Phone','user')
        return queryset

# column heading change
    user_info.short_description='Info'

# Register your models here.
admin.site.register(UserProfile,UserProfileAdmin)

#  to change the header (Django Administration) in the Admin module Method 1
# admin.site.site_header ='Admin Panel'

# method to - overide the html template_name
# create template base_site.html in template/admin/folder.
