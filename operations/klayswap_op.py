import os
import datetime
from django.db import close_old_connections
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

    @property
    def symbol_dict(self):
        symbols = list(Symbol.objects.all().values('id', 'address'))
        return {d['address']: d['id'] for d in symbols}

    @property
    def pool_dict(self):
        pools = list(KlayswapPool.objects.all().values('id', 'exchange_address'))
        return {d['exchange_address']: d['id'] for d in pools}

    def daily_save_symbols_and_pools(self):
        self.api.call_api()

        existing_symbols = list(Symbol.objects.all().values_list('address', flat=True))
        existing_pools = list(KlayswapPool.objects.all().values_list('exchange_address', flat=True))

        data = self.api.klayswap_token
        inst_list = []
        for token in data:
            if token['address'] not in existing_symbols:
                inst = Symbol(exchange='klayswap',
                              asset_type='defi',
                              symbol=token['symbol'],
                              symbol_id=f'klayswap_defi_{token["symbol"]}',
                              address=token['address'],
                              active=True)
                inst_list.append(inst)
        Symbol.objects.bulk_create(inst_list)
        print(f'Saved {len(inst_list)} symbols to DB')

        data = self.api.klayswap_pool
        inst_list = []
        for pool in data:
            if pool['exchange_address'] not in existing_pools:
                inst = KlayswapPool(**pool)
                inst_list.append(inst)
        KlayswapPool.objects.bulk_create(inst_list)
        print(f'Saved {len(inst_list)} pools to DB')

    def daily_save_tokens(self):
        self.api.call_api()

        date = datetime.datetime.now().strftime('%Y%m%d')
        data = self.api.klayswap_token
        inst_list = []
        for token in data:
            token['date'] = date
            inst = KlayswapToken(**token)
            inst_list.append(inst)
        KlayswapToken.objects.bulk_create(inst_list)
        print(f'Saved {len(inst_list)} tokens to DB')

    def minute_save_data(self):
        close_old_connections()

        self.api.call_api()

        symbol_dict = self.symbol_dict
        pool_dict = self.pool_dict

        data = self.api.klayswap_common
        inst = KlayswapCommon(**data)
        inst.save()

        data = self.api.klayswap_token_info
        inst_list = []
        for info in data:
            try:
                info['id'] = f'{symbol_dict[info["address"]]}{info["date"]}'
                _ = info.pop('address')
                inst = KlayswapTokenInfo(**info)
                inst_list.append(inst)
            except:
                print(f'Error with: {info}')
        KlayswapTokenInfo.objects.bulk_create(inst_list)
        print(f'Saved {len(inst_list)} token info to DB')

        data = self.api.klayswap_pool_info
        inst_list = []
        for info in data:
            try:
                info['id'] = f'{pool_dict[info["exchange_address"]]}{info["date"]}'
                _ = info.pop('exchange_address')
                inst = KlayswapPoolInfo(**info)
                inst_list.append(inst)
            except:
                print(f'Error with: {info}')
        KlayswapPoolInfo.objects.bulk_create(inst_list)
        print(f'Saved {len(inst_list)} pool info to DB')


if __name__ == '__main__':
    op = KlayswapOperator()
    op.daily_save_symbols_and_pools()