from django.contrib import admin

from db.models import (
    Symbol,
    KlayswapCommon,
    KlayswapToken,
    KlayswapTokenInfo,
    KlayswapTokenInfoHour,
    KlayswapPool,
    KlayswapPoolInfo,
    KlayswapPoolInfoHour,
    KlayswapDayVolume,
    KlayswapDayTVL,
    KlayswapSingleLeveragePoolInfo,
    KlayswapSingleLeveragePoolInfoHour,
    KlayswapPlusLeveragePoolInfo,
    KlayswapPlusLeveragePoolInfoHour,
)

admin.site.register(Symbol)
admin.site.register(KlayswapCommon)
admin.site.register(KlayswapToken)
admin.site.register(KlayswapTokenInfo)
admin.site.register(KlayswapTokenInfoHour)
admin.site.register(KlayswapPool)
admin.site.register(KlayswapPoolInfo)
admin.site.register(KlayswapPoolInfoHour)
admin.site.register(KlayswapDayVolume)
admin.site.register(KlayswapDayTVL)
admin.site.register(KlayswapSingleLeveragePoolInfo)
admin.site.register(KlayswapSingleLeveragePoolInfoHour)
admin.site.register(KlayswapPlusLeveragePoolInfo)
admin.site.register(KlayswapPlusLeveragePoolInfoHour)