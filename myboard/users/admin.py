from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "profile"

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

    # list_display에 커스텀 필드 추가
    list_display = ('custom_user_display', 'email', 'first_name', 'last_name', 'is_staff')

    # 커스텀 메서드로 pk와 username 출력
    def custom_user_display(self, obj):
        return f'[{obj.pk}] {obj.username}'

    custom_user_display.short_description = 'User'  # 어드민에서의 컬럼 이름

admin.site.unregister(User)
admin.site.register(User, UserAdmin)