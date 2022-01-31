import os
import requests
import datetime
from dotenv import load_dotenv

load_dotenv(override=True)

KLAYSWAP_URL = os.getenv('KLAYSWAP_URL')


class KlayswapAPI:
    """
    예상 수익률 (APR):

    (dailyMining * KSP Price) / poolVolume * 365 * 100
    """

    def __init__(self):
        self.url = KLAYSWAP_URL
        self._data = None

    def call_api(self):
        res = requests.get(self.url)
        self._data = res.json()

    def check_data(self):
        if self._data is None:
            self.call_api()

    @property
    def klayswap_common(self):
        self.check_data()
        return {
            'date': datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
            'cur_vol': self._data['common']['curVol'],
            'cur_tvl': self._data['common']['curTvl'],
            'staking_vol': self._data['common']['stakingVol'],
        }

    @property
    def klayswap_token(self):
        self.check_data()
        tokens = []
        for token in self._data['tokenInfo']:
            data = {
                'address': token['address'],
                'symbol': token['symbol'],
                'name': token['name'],
                'chain': token['chain'],
                'decimal': token['decimal'],
                'image': token['img'],
                'grade': token['grade'],
                'contract_grade': token['contractGrade'],
                'is_drops': token['isDrops'],
                'is_stable': token['isStable'],
            }
            tokens.append(data)
        return tokens

    @property
    def klayswap_token_info(self):
        self.check_data()
        info = []
        date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        for token in self._data['tokenInfo']:
            data = {
                'address': token['address'],
                'date': date,
                'amount': token['amount'],
                'volume': token['volume'],
                'oracle_price': token['oraclePrice'],
            }
            info.append(data)
        return info

    @property
    def klayswap_pool(self):
        self.check_data()
        pools = []
        for pool in self._data['recentPoolInfo']:
            data = {
                'exchange_address': pool['exchange_address'],
                'token_a': pool['tokenA'],
                'token_b': pool['tokenB'],
                'is_ksp_pool': pool['isKSPPool'],
                'is_xrp_pool': pool['isXRPPool'],
                'is_eth_pool': pool['isETHPool'],
                'is_klay_pool': pool['isKLAYPool'],
                'is_stable_pool': pool['isStablePool'],
                'is_drops_pool': pool['isDropsPool'],
                'is_drops_tag': pool['isDropsTag'],
            }
            pools.append(data)
        return pools

    @property
    def klayswap_pool_info(self):
        self.check_data()
        info = []
        date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        for pool in self._data['recentPoolInfo']:
            data = {
                'exchange_address': pool['exchange_address'],
                'date': date,
                'amount_a': pool['amountA'],
                'amount_b': pool['amountB'],
                'lp_price': pool['lpPrice'],
                'supply': pool['supply'],
                'pool_volume': pool['poolVolume'],
                'last_hour_trade_a': pool['lastHourTradeA'],
                'last_hour_trade_b': pool['lastHourTradeB'],
                'last_hour_trade_volume': pool['lastHourTradeTotalVolume'],
                'decimals': pool['decimals'],
                'fee': pool['fee'],
                'last_mined': pool['lastMined'],
                'mining_index': pool['miningIndex'],
                'daily_mining': pool['dailyMining'],
                'mining_rate': pool['miningRate'],
            }
            info.append(data)
        return info

    def _fmt_date(self, date: str):
        return date.replace('-', '') \
                   .replace('T', '') \
                   .replace('Z', '') \
                   .replace(':', '') \
                   .replace('.', '')

    @property
    def klayswap_day_volume(self):
        self.check_data()
        volumes = []
        for volume in self._data['dayVolume']:
            data = {
                'date': self._fmt_date(volume['dateId']),
                'amount': volume['amount'],
            }
            volumes.append(data)
        return volumes

    @property
    def klayswap_day_tvl(self):
        self.check_data()
        tvls = []
        for tvl in self._data['dayTvl']:
            data = {
                'date': self._fmt_date(tvl['dateId']),
                'amount': tvl['amount'],
            }
            tvls.append(data)
        return tvls

    @property
    def klayswap_single_leverage_pool_info(self):
        self.check_data()
        info = []
        date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        for pool in self._data['leveragePoolInfo']['single']:
            data = {
                'date': date,
                'address': pool['address'],
                'token': pool['token'],
                'amount': pool['amount'],
                'total_deposit': pool['totalDeposit'],
                'total_deposit_vol': pool['totalDepositVol'],
                'total_supply': pool['totalSupply'],
                'mining_rate': pool['miningRate'],
                'daily_mining': pool['dailyMining'],
                'mining_index': pool['miningIndex'],
                'last_mined': pool['lastMined'],
                'total_borrow': pool['totalBorrow'],
                'total_reserve': pool['totalReserve'],
                'total_reserve_vol': pool['totalReserveVol'],
                'burn_ksp': pool['burnKSP'],
                'burn_ksp_vol': pool['burnKSPVol'],
                'is_deposit': pool['isDeposit'],
                'is_withdraw': pool['isWithdraw'],
                'reserve_factor': pool['reserveFactor'],
            }
            info.append(data)
        return info

    @property
    def klayswap_plus_leverage_pool_info(self):
        self.check_data()
        info = []
        date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        for pool in self._data['leveragePoolInfo']['plus']:
            data = {
                'date': date,
                'address': pool['address'],
                'pool': pool['pool'],
                'borrow_factor': pool['borrowFactor'],
                'liquidation_factor': pool['liquidationFactor'],
                'is_borrowable_a': pool['isBorrowableA'],
                'is_borrowable_b': pool['isBorrowableB'],
                'is_deposit': pool['isDeposit'],
                'is_withdraw': pool['isWithdraw'],
                'oracle_price': pool['oraclePrice'],
            }
            info.append(data)
        return info


if __name__ == '__main__':
    api = KlayswapAPI()
    print(api.klayswap_token)