# Generated by Django 4.0.1 on 2022-02-02 21:47

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='KlayswapCommon',
            fields=[
                ('date', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('cur_vol', models.CharField(blank=True, max_length=50, null=True)),
                ('cur_tvl', models.CharField(blank=True, max_length=50, null=True)),
                ('staking_vol', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KlayswapDayTVL',
            fields=[
                ('date', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('amount', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KlayswapDayVolume',
            fields=[
                ('date', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('amount', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KlayswapHourOHLCV',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('symbol', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.CharField(blank=True, max_length=30, null=True)),
                ('open_prc', models.FloatField(blank=True, null=True)),
                ('high_prc', models.FloatField(blank=True, null=True)),
                ('low_prc', models.FloatField(blank=True, null=True)),
                ('close_prc', models.FloatField(blank=True, null=True)),
                ('volume', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KlayswapPlusLeveragePoolInfo',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('date', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('pool', models.CharField(blank=True, max_length=100, null=True)),
                ('borrow_factor', models.CharField(blank=True, max_length=20, null=True)),
                ('liquidation_factor', models.CharField(blank=True, max_length=20, null=True)),
                ('is_borrowable_a', models.BooleanField(blank=True, null=True)),
                ('is_borrowable_b', models.BooleanField(blank=True, null=True)),
                ('is_deposit', models.BooleanField(blank=True, null=True)),
                ('is_withdraw', models.BooleanField(blank=True, null=True)),
                ('oracle_price', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KlayswapPlusLeveragePoolInfoHour',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('date', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('pool', models.CharField(blank=True, max_length=100, null=True)),
                ('borrow_factor', models.CharField(blank=True, max_length=20, null=True)),
                ('liquidation_factor', models.CharField(blank=True, max_length=20, null=True)),
                ('is_borrowable_a', models.BooleanField(blank=True, null=True)),
                ('is_borrowable_b', models.BooleanField(blank=True, null=True)),
                ('is_deposit', models.BooleanField(blank=True, null=True)),
                ('is_withdraw', models.BooleanField(blank=True, null=True)),
                ('oracle_price', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KlayswapPool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange_address', models.CharField(blank=True, max_length=100, null=True)),
                ('token_a', models.CharField(blank=True, max_length=100, null=True)),
                ('token_b', models.CharField(blank=True, max_length=100, null=True)),
                ('is_ksp_pool', models.BooleanField(blank=True, null=True)),
                ('is_xrp_pool', models.BooleanField(blank=True, null=True)),
                ('is_eth_pool', models.BooleanField(blank=True, null=True)),
                ('is_klay_pool', models.BooleanField(blank=True, null=True)),
                ('is_stable_pool', models.BooleanField(blank=True, null=True)),
                ('is_drops_pool', models.BooleanField(blank=True, null=True)),
                ('is_drops_tag', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KlayswapPoolInfo',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('date', models.CharField(blank=True, max_length=30, null=True)),
                ('amount_a', models.CharField(blank=True, max_length=100, null=True)),
                ('amount_b', models.CharField(blank=True, max_length=100, null=True)),
                ('lp_price', models.CharField(blank=True, max_length=50, null=True)),
                ('supply', models.CharField(blank=True, max_length=100, null=True)),
                ('pool_volume', models.CharField(blank=True, max_length=100, null=True)),
                ('last_hour_trade_a', models.CharField(blank=True, max_length=100, null=True)),
                ('last_hour_trade_b', models.CharField(blank=True, max_length=100, null=True)),
                ('last_hour_trade_volume', models.CharField(blank=True, max_length=50, null=True)),
                ('decimals', models.CharField(blank=True, max_length=10, null=True)),
                ('fee', models.CharField(blank=True, max_length=10, null=True)),
                ('last_mined', models.CharField(blank=True, max_length=50, null=True)),
                ('mining_index', models.CharField(blank=True, max_length=50, null=True)),
                ('daily_mining', models.CharField(blank=True, max_length=50, null=True)),
                ('mining_rate', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KlayswapPoolInfoHour',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('date', models.CharField(blank=True, max_length=30, null=True)),
                ('amount_a', models.CharField(blank=True, max_length=100, null=True)),
                ('amount_b', models.CharField(blank=True, max_length=100, null=True)),
                ('lp_price', models.CharField(blank=True, max_length=50, null=True)),
                ('supply', models.CharField(blank=True, max_length=100, null=True)),
                ('pool_volume', models.CharField(blank=True, max_length=100, null=True)),
                ('last_hour_trade_a', models.CharField(blank=True, max_length=100, null=True)),
                ('last_hour_trade_b', models.CharField(blank=True, max_length=100, null=True)),
                ('last_hour_trade_volume', models.CharField(blank=True, max_length=50, null=True)),
                ('decimals', models.CharField(blank=True, max_length=10, null=True)),
                ('fee', models.CharField(blank=True, max_length=10, null=True)),
                ('last_mined', models.CharField(blank=True, max_length=50, null=True)),
                ('mining_index', models.CharField(blank=True, max_length=50, null=True)),
                ('daily_mining', models.CharField(blank=True, max_length=50, null=True)),
                ('mining_rate', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KlayswapSingleLeveragePoolInfo',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('date', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('token', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.CharField(blank=True, max_length=100, null=True)),
                ('total_deposit', models.CharField(blank=True, max_length=100, null=True)),
                ('total_deposit_vol', models.CharField(blank=True, max_length=100, null=True)),
                ('total_supply', models.CharField(blank=True, max_length=100, null=True)),
                ('mining_rate', models.CharField(blank=True, max_length=10, null=True)),
                ('daily_mining', models.CharField(blank=True, max_length=50, null=True)),
                ('mining_index', models.CharField(blank=True, max_length=50, null=True)),
                ('last_mined', models.CharField(blank=True, max_length=50, null=True)),
                ('total_borrow', models.CharField(blank=True, max_length=50, null=True)),
                ('total_reserve', models.CharField(blank=True, max_length=50, null=True)),
                ('total_reserve_vol', models.CharField(blank=True, max_length=20, null=True)),
                ('burn_ksp', models.CharField(blank=True, max_length=50, null=True)),
                ('burn_ksp_vol', models.CharField(blank=True, max_length=20, null=True)),
                ('is_deposit', models.BooleanField(blank=True, null=True)),
                ('is_withdraw', models.BooleanField(blank=True, null=True)),
                ('reserve_factor', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KlayswapSingleLeveragePoolInfoHour',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('date', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('token', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.CharField(blank=True, max_length=100, null=True)),
                ('total_deposit', models.CharField(blank=True, max_length=100, null=True)),
                ('total_deposit_vol', models.CharField(blank=True, max_length=100, null=True)),
                ('total_supply', models.CharField(blank=True, max_length=100, null=True)),
                ('mining_rate', models.CharField(blank=True, max_length=10, null=True)),
                ('daily_mining', models.CharField(blank=True, max_length=50, null=True)),
                ('mining_index', models.CharField(blank=True, max_length=50, null=True)),
                ('last_mined', models.CharField(blank=True, max_length=50, null=True)),
                ('total_borrow', models.CharField(blank=True, max_length=50, null=True)),
                ('total_reserve', models.CharField(blank=True, max_length=50, null=True)),
                ('total_reserve_vol', models.CharField(blank=True, max_length=20, null=True)),
                ('burn_ksp', models.CharField(blank=True, max_length=50, null=True)),
                ('burn_ksp_vol', models.CharField(blank=True, max_length=20, null=True)),
                ('is_deposit', models.BooleanField(blank=True, null=True)),
                ('is_withdraw', models.BooleanField(blank=True, null=True)),
                ('reserve_factor', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KlayswapToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('symbol', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('chain', models.CharField(blank=True, max_length=50, null=True)),
                ('decimal', models.IntegerField(blank=True, null=True)),
                ('image', models.CharField(blank=True, max_length=100, null=True)),
                ('grade', models.CharField(blank=True, max_length=20, null=True)),
                ('contract_grade', models.CharField(blank=True, max_length=20, null=True)),
                ('is_drops', models.BooleanField(blank=True, null=True)),
                ('is_stable', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KlayswapTokenInfo',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('date', models.CharField(blank=True, max_length=30, null=True)),
                ('amount', models.CharField(blank=True, max_length=100, null=True)),
                ('volume', models.CharField(blank=True, max_length=100, null=True)),
                ('oracle_price', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KlayswapTokenInfoHour',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('date', models.CharField(blank=True, max_length=30, null=True)),
                ('amount', models.CharField(blank=True, max_length=100, null=True)),
                ('volume', models.CharField(blank=True, max_length=100, null=True)),
                ('oracle_price', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Symbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange', models.CharField(blank=True, max_length=20, null=True)),
                ('asset_type', models.CharField(blank=True, max_length=20, null=True)),
                ('symbol', models.CharField(blank=True, max_length=50, null=True)),
                ('symbol_id', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('active', models.BooleanField(blank=True, default=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
