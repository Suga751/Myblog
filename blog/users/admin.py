from django.contrib import admin
from accounts.models import UserProfile



class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'city', 'facebook')

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-city', 'user')
        return queryset

    user_info.short_description = 'Info'

admin.site.register(UserProfile, UserProfileAdmin

# admin.site.register(UserProfile, UserProfileAdmin)