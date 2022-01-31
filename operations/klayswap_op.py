import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
application = get_wsgi_application()

from api.klayswap.restapi import KlayswapAPI
from db.models import (
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


class KlayswapOperator:

    def __init__(self):
        self.api = KlayswapAPI()

    def daily_save_symbols(self):
        pass

    def hourly_save_tokens(self):
        pass

    def hourly_save_pools(self):
        pass

    def minute_save_data(self):
        pass


if __name__ == '__main__':
    pass