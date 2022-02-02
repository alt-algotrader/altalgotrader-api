from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email


class Symbol(models.Model):
    exchange = models.CharField(max_length=20, blank=True, null=True)
    asset_type = models.CharField(max_length=20, blank=True, null=True)
    symbol = models.CharField(max_length=50, blank=True, null=True)
    symbol_id = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField(default=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.symbol_id


class KlayswapCommon(models.Model):
    date = models.CharField(primary_key=True, max_length=30)
    cur_vol = models.CharField(max_length=50, blank=True, null=True)
    cur_tvl = models.CharField(max_length=50, blank=True, null=True)
    staking_vol = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.date} {self.cur_tvl}'


class KlayswapToken(models.Model):
    date = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    symbol = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    chain = models.CharField(max_length=50, blank=True, null=True)
    decimal = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    grade = models.CharField(max_length=20, blank=True, null=True)
    contract_grade = models.CharField(max_length=20, blank=True, null=True)
    is_drops = models.BooleanField(blank=True, null=True)
    is_stable = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.address


class KlayswapTokenInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    date = models.CharField(max_length=30, blank=True, null=True)
    amount = models.CharField(max_length=100, blank=True, null=True)
    volume = models.CharField(max_length=100, blank=True, null=True)
    oracle_price = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.id} {self.volume} {self.oracle_price}'


class KlayswapTokenInfoHour(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    date = models.CharField(max_length=30, blank=True, null=True)
    amount = models.CharField(max_length=100, blank=True, null=True)
    volume = models.CharField(max_length=100, blank=True, null=True)
    oracle_price = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.id} {self.volume} {self.oracle_price}'


class KlayswapPool(models.Model):
    exchange_address = models.CharField(max_length=100, blank=True, null=True)
    token_a = models.CharField(max_length=100, blank=True, null=True)
    token_b = models.CharField(max_length=100, blank=True, null=True)
    is_ksp_pool = models.BooleanField(blank=True, null=True)
    is_xrp_pool = models.BooleanField(blank=True, null=True)
    is_eth_pool = models.BooleanField(blank=True, null=True)
    is_klay_pool = models.BooleanField(blank=True, null=True)
    is_stable_pool = models.BooleanField(blank=True, null=True)
    is_drops_pool = models.BooleanField(blank=True, null=True)
    is_drops_tag = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.exchange_address


class KlayswapPoolInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    date = models.CharField(max_length=30, blank=True, null=True)
    amount_a = models.CharField(max_length=100, blank=True, null=True)
    amount_b = models.CharField(max_length=100, blank=True, null=True)
    lp_price = models.CharField(max_length=50, blank=True, null=True)
    supply = models.CharField(max_length=100, blank=True, null=True)
    pool_volume = models.CharField(max_length=100, blank=True, null=True)
    last_hour_trade_a = models.CharField(max_length=100, blank=True, null=True)
    last_hour_trade_b = models.CharField(max_length=100, blank=True, null=True)
    last_hour_trade_volume = models.CharField(max_length=50, blank=True, null=True)
    decimals = models.CharField(max_length=10, blank=True, null=True)
    fee = models.CharField(max_length=10, blank=True, null=True)
    last_mined = models.CharField(max_length=50, blank=True, null=True)
    mining_index = models.CharField(max_length=50, blank=True, null=True)
    daily_mining = models.CharField(max_length=50, blank=True, null=True)
    mining_rate = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.id


class KlayswapPoolInfoHour(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    date = models.CharField(max_length=30, blank=True, null=True)
    amount_a = models.CharField(max_length=100, blank=True, null=True)
    amount_b = models.CharField(max_length=100, blank=True, null=True)
    lp_price = models.CharField(max_length=50, blank=True, null=True)
    supply = models.CharField(max_length=100, blank=True, null=True)
    pool_volume = models.CharField(max_length=100, blank=True, null=True)
    last_hour_trade_a = models.CharField(max_length=100, blank=True, null=True)
    last_hour_trade_b = models.CharField(max_length=100, blank=True, null=True)
    last_hour_trade_volume = models.CharField(max_length=50, blank=True, null=True)
    decimals = models.CharField(max_length=10, blank=True, null=True)
    fee = models.CharField(max_length=10, blank=True, null=True)
    last_mined = models.CharField(max_length=50, blank=True, null=True)
    mining_index = models.CharField(max_length=50, blank=True, null=True)
    daily_mining = models.CharField(max_length=50, blank=True, null=True)
    mining_rate = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.id


class KlayswapHourOHLCV(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    symbol = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=30, blank=True, null=True)
    open_prc = models.FloatField(blank=True, null=True)
    high_prc = models.FloatField(blank=True, null=True)
    low_prc = models.FloatField(blank=True, null=True)
    close_prc = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.symbol} {self.date} {self.close_prc}'


class KlayswapDayVolume(models.Model):
    date = models.CharField(primary_key=True, max_length=30)
    amount = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.date} {self.amount}'


class KlayswapDayTVL(models.Model):
    date = models.CharField(primary_key=True, max_length=30)
    amount = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.date} {self.amount}'


class KlayswapSingleLeveragePoolInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    date = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    token = models.CharField(max_length=100, blank=True, null=True)
    amount = models.CharField(max_length=100, blank=True, null=True)
    total_deposit = models.CharField(max_length=100, blank=True, null=True)
    total_deposit_vol = models.CharField(max_length=100, blank=True, null=True)
    total_supply = models.CharField(max_length=100, blank=True, null=True)
    mining_rate = models.CharField(max_length=10, blank=True, null=True)
    daily_mining = models.CharField(max_length=50, blank=True, null=True)
    mining_index = models.CharField(max_length=50, blank=True, null=True)
    last_mined = models.CharField(max_length=50, blank=True, null=True)
    total_borrow = models.CharField(max_length=50, blank=True, null=True)
    total_reserve = models.CharField(max_length=50, blank=True, null=True)
    total_reserve_vol = models.CharField(max_length=20, blank=True, null=True)
    burn_ksp = models.CharField(max_length=50, blank=True, null=True)
    burn_ksp_vol = models.CharField(max_length=20, blank=True, null=True)
    is_deposit = models.BooleanField(blank=True, null=True)
    is_withdraw = models.BooleanField(blank=True, null=True)
    reserve_factor = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'{self.date} {self.token}'


class KlayswapSingleLeveragePoolInfoHour(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    date = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    token = models.CharField(max_length=100, blank=True, null=True)
    amount = models.CharField(max_length=100, blank=True, null=True)
    total_deposit = models.CharField(max_length=100, blank=True, null=True)
    total_deposit_vol = models.CharField(max_length=100, blank=True, null=True)
    total_supply = models.CharField(max_length=100, blank=True, null=True)
    mining_rate = models.CharField(max_length=10, blank=True, null=True)
    daily_mining = models.CharField(max_length=50, blank=True, null=True)
    mining_index = models.CharField(max_length=50, blank=True, null=True)
    last_mined = models.CharField(max_length=50, blank=True, null=True)
    total_borrow = models.CharField(max_length=50, blank=True, null=True)
    total_reserve = models.CharField(max_length=50, blank=True, null=True)
    total_reserve_vol = models.CharField(max_length=20, blank=True, null=True)
    burn_ksp = models.CharField(max_length=50, blank=True, null=True)
    burn_ksp_vol = models.CharField(max_length=20, blank=True, null=True)
    is_deposit = models.BooleanField(blank=True, null=True)
    is_withdraw = models.BooleanField(blank=True, null=True)
    reserve_factor = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'{self.date} {self.token}'


class KlayswapPlusLeveragePoolInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    date = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    pool = models.CharField(max_length=100, blank=True, null=True)
    borrow_factor = models.CharField(max_length=20, blank=True, null=True)
    liquidation_factor = models.CharField(max_length=20, blank=True, null=True)
    is_borrowable_a = models.BooleanField(blank=True, null=True)
    is_borrowable_b = models.BooleanField(blank=True, null=True)
    is_deposit = models.BooleanField(blank=True, null=True)
    is_withdraw = models.BooleanField(blank=True, null=True)
    oracle_price = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.date} {self.pool}'


class KlayswapPlusLeveragePoolInfoHour(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    date = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    pool = models.CharField(max_length=100, blank=True, null=True)
    borrow_factor = models.CharField(max_length=20, blank=True, null=True)
    liquidation_factor = models.CharField(max_length=20, blank=True, null=True)
    is_borrowable_a = models.BooleanField(blank=True, null=True)
    is_borrowable_b = models.BooleanField(blank=True, null=True)
    is_deposit = models.BooleanField(blank=True, null=True)
    is_withdraw = models.BooleanField(blank=True, null=True)
    oracle_price = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.date} {self.pool}'
