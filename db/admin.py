from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from db.models import (
    User,
    Symbol,
    KlayswapCommon,
    KlayswapToken,
    KlayswapTokenInfo,
    KlayswapTokenInfoHour,
    KlayswapPool,
    KlayswapPoolInfo,
    KlayswapPoolInfoHour,
    KlayswapHourOHLCV,
    KlayswapDayVolume,
    KlayswapDayTVL,
    KlayswapSingleLeveragePoolInfo,
    KlayswapSingleLeveragePoolInfoHour,
    KlayswapPlusLeveragePoolInfo,
    KlayswapPlusLeveragePoolInfoHour,
)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(Symbol)
admin.site.register(KlayswapCommon)
admin.site.register(KlayswapToken)
admin.site.register(KlayswapTokenInfo)
admin.site.register(KlayswapTokenInfoHour)
admin.site.register(KlayswapPool)
admin.site.register(KlayswapPoolInfo)
admin.site.register(KlayswapPoolInfoHour)
admin.site.register(KlayswapHourOHLCV)
admin.site.register(KlayswapDayVolume)
admin.site.register(KlayswapDayTVL)
admin.site.register(KlayswapSingleLeveragePoolInfo)
admin.site.register(KlayswapSingleLeveragePoolInfoHour)
admin.site.register(KlayswapPlusLeveragePoolInfo)
admin.site.register(KlayswapPlusLeveragePoolInfoHour)