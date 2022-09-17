from urllib import request, response
import requests
import json
from datetime import datetime
import sqlite3
import psycopg2

# sqlite3 connection & cursor
sqlite3 = sqlite3.connect('crypto_db.db')
sqlite3_cursor = sqlite3.cursor()

# postgres connection & cursor
postgres = psycopg2.connect(
    host = 'localhost',
    database = 'crypto_rates',
    user = 'postgres',
    password = 'postgres',
    port = '5432'
)
postgres_cursor = postgres.cursor()

# Coinlayer api key
api_key = 'b700c579f1fcbffce7764cea59eb731e'

# Live data pull
# live_data = requests.get("http://api.coinlayer.com/api/live?access_key=b700c579f1fcbffce7764cea59eb731e")
# live_json = live_data.json()

# Historical data pull
# historical_data = requests.get("http://api.coinlayer.com/api/2021-11-10?access_key=b700c579f1fcbffce7764cea59eb731e")
# historical_json = historical_data.json()

# Raw data dump from the 'live' and 'historical' www.coinlayer.com API feed.
raw_live_data = {
    'success': True, 
    'terms': 'https://coinlayer.com/terms', 
    'privacy': 'https://coinlayer.com/privacy', 
    'timestamp': 1663286165, 
    'target': 'USD', 
    'rates': {
        'ABC': 59.99, 'ACP': 0.014931, 'ACT': 0.00107, 'ACT*': 0.017178, 'ADA': 0.465592, 'ADCN': 0.00013, 'ADL': 0.01515, 'ADX': 0.15985, 'ADZ': 0.0023, 'AE': 0.08719, 'AGI': 0, 'AIB': 0.005626, 'AIDOC': 5.109867e-05, 'AION': 0.04966, 'AIR': 0.0118, 'ALT': 0.565615, 'AMB': 0.026, 'AMM': 0.006502, 'ANT': 1.82025, 'APC': 0.0017, 'APPC': 0.0014, 'ARC': 0.0169, 'ARCT': 0.00061, 'ARDR': 0.103969, 'ARK': 1.1, 'ARN': 0.001194, 'ASAFE2': 0.4, 'AST': 0.1238, 'ATB': 0.017, 'ATM': 5.2366, 'AURS': 0.352867, 'AVT': 1.41, 'BAR': 5.69, 'BASH': 0.0056, 'BAT': 0.315445, 'BAY': 0.0644, 'BBP': 0.0005, 'BCD': 0.165219, 'BCH': 117.747333, 'BCN': 3.3953e-05, 'BCPT': 0.002681, 'BEE': 1e-06, 'BIO': 0.0008, 'BLC': 0.072132, 'BLOCK': 0.18, 'BLU': 0.00054, 'BLZ': 0.08276, 'BMC': 0.00178, 'BNB': 269.639248, 'BNT': 0.579, 'BOST': 0.048, 'BQ': 7.775e-05, 'BQX': 2.720931, 'BRD': 
        0.005784, 'BRIT': 0.03, 'BT1': 0, 'BT2': 0, 'BTC': 19691.385574, 'BTCA': 0.00036, 'BTCS': 0.01201, 'BTCZ': 19684.29, 'BTG': 23.10912, 'BTLC': 9, 'BTM': 0.078282, 'BTM*': 0.122609, 'BTQ': 0.01, 'BTS': 0.01194, 'BTX': 0.132437, 'BURST': 0.017348, 'CALC': 0.0006, 'CAS': 0.007, 'CAT': 0.16981, 'CCRB': 0.08888, 'CDT': 0.021401, 'CESC': 0.0037, 'CHAT': 0.0008, 'CJ': 0.000898, 'CL': 0.028, 'CLD': 0.02, 'CLOAK': 10, 'CMT*': 0.03954, 'CND': 0.00056, 'CNX': 1.996594, 'CPC': 0.0005, 'CRAVE': 0.4, 'CRC': 0.08475, 'CRE': 1.316485, 'CRW': 0.02202, 'CTO': 0.005, 'CTR': 0.00225, 'CVC': 0.133401, 'DAS': 0.937816, 'DASH': 44.33925, 'DAT': 3.578776e-05, 'DATA': 0, 'DBC': 0.000807, 'DBET': 0.027656, 'DCN': 1.3975e-06, 'DCR': 27.741546, 'DCT': 0.00039, 'DEEP': 0.001, 'DENT': 0.00094, 'DGB': 0.009626, 'DGD': 208.447035, 'DIM': 9.4957e-05, 'DIME': 3e-05, 'DMD': 0.58782, 'DNT': 0.0449, 'DOGE': 0.058818, 'DRGN': 0.01932, 'DRZ': 3, 'DSH': 252.13175, 'DTA': 3.569e-05, 'EC': 50, 'EDG': 0.026377, 'EDO': 0.23772, 'EDR': 0.00023, 'EKO': 6.710205e-05, 'ELA': 1.509, 'ELF': 0.118383, 'EMC': 0.019907, 'EMGO': 0.43382, 'ENG': 0.010054, 'ENJ': 0.504163, 'EOS': 1.378038, 'ERT': 0.2054, 'ETC': 35.560446, 'ETH': 1472.220875, 'ETN': 0.003, 'ETP': 0.034676, 'ETT': 2.9, 'EVR': 0.104931, 'EVX': 0.01377, 'FCT': 0.35922, 'FLP': 0.007, 'FOTA': 0.000134, 'FRST': 0.78001, 'FUEL': 22.41, 'FUN': 0.007627, 'FUNC': 0.00061, 'FUTC': 0.004, 'GAME': 0.16611, 'GAS': 3.289973, 'GBYTE': 17.549423, 'GMX': 6.467e-05, 'GNO': 139.39, 'GNT': 0.33457, 'GNX': 0.003492, 'GRC': 0.0067, 'GRS': 10, 'GRWI': 10000, 'GTC': 1.9672, 'GTO': 0.02191, 'GUP': 0.000619, 'GVT': 0.106421, 'GXS': 0.3932, 'HAC': 0.000484, 'HNC': 0, 'HSR': 9.249418, 'HST': 0.0027, 'HVN': 0.03529, 'ICN': 0.1452, 'ICOS': 17, 'ICX': 0.258093, 'IGNIS': 0.00519, 'ILC': 0.098703, 'INK': 0.00032, 'INS': 0.13808, 'INSN': 0.0473, 'INT': 0.00346, 'IOP': 15.455555, 'IOST': 0.012224, 'ITC': 0.013186, 'KCS': 9.16, 'KICK': 0.000324, 'KIN': 1.1422e-05, 'KLC': 0.000703, 'KMD': 0.132684, 'KNC': 2.001271, 'KRB': 6, 'LA': 0.07438, 'LEND': 0.948652, 'LEO': 4.905145, 'LINDA': 0.000271, 'LINK': 7.55841, 'LOC': 0.76, 'LOG': 0.060174, 'LRC': 0.325443, 'LSK': 0.975612, 'LTC': 56.246225, 'LUN': 0.014315, 'LUX': 2.09e-06, 'MAID': 0.28, 'MANA': 0.720842, 'MCAP': 0.005398, 'MCO': 5.24, 'MDA': 0.05773, 'MDS': 0.000365, 'MIOTA': 0.26194, 'MKR': 677.775, 'MLN': 22.0355, 'MNX': 0.028649, 'MOD': 0.3642, 'MOIN': 0.033073, 'MONA': 0.469205, 'MTL': 1.1315, 
        'MTN*': 0.009575, 'MTX': 0.0044, 'NAS': 0.04282, 'NAV': 0.06, 'NBT': 0.00784, 'NDC': 0.008989, 'NEBL': 1.589265, 'NEO': 9.006128, 'NEU': 0.02831, 'NEWB': 0.002604, 'NGC': 0.057, 'NKC': 0.000858, 'NLC2': 0.599935, 'NMC': 5.867998, 'NMR': 16.7881, 'NULS': 0.2191, 'NVC': 10, 'NXT': 0.002904, 'OAX': 0.125827, 'OBITS': 0.015, 'OC': 0.000443, 'OCN': 9.899e-05, 'ODN': 0.5, 'OK': 0.002908, 'OMG': 1.7316, 'OMNI': 2.1, 'ORE': 0, 'ORME': 1.235715, 'OST': 
        0.000514, 'OTN': 0, 'OTX': 0.023, 'OXY': 0.0509, 'PART': 3.951477, 'PAY': 0.01612, 'PBT': 174.522, 'PCS': 0.019961, 'PIVX': 0.308537, 'PIZZA': 0.001, 'PLBT': 20, 'PLR': 0.004919, 'POE': 2.23431e-05, 'POLY': 0.11675, 'POSW': 
        0.48712, 'POWR': 0.2084, 'PPC': 0.573984, 'PPT': 0.075, 'PPY': 5.45, 'PRC': 3e-05, 'PRES': 0.219998, 'PRG': 0.400001, 'PRL': 0.061361, 'PRO': 0.69, 'PURA': 0.25, 'PUT': 0, 'QASH': 0.012, 'QAU': 0, 'QSP': 0.01731, 'QTUM': 2.988377, 'QUN': 0.008318, 'R': 0.01052, 'RBIES': 1, 'RCN': 0.002064, 'RDD': 0.000381, 'RDN': 0, 'RDN*': 0.324446, 
        'REBL': 0.001849, 'REE': 1e-05, 'REP': 7.452, 'REQ': 0.12365, 'REV': 0.00089, 'RGC': 0.001, 'RHOC': 0.178417, 'RIYA': 0.090025, 'RKC': 5, 'RLC': 1.22665, 'RPX': 0.061017, 'RUFF': 0.00153, 'SALT': 0.768708, 'SAN': 0.085264, 'SBC': 7, 'SC': 0.003763, 'SENT': 0.000598, 'SHIFT': 0, 'SIB': 5.177, 'SMART': 0.000552, 'SMLY': 6e-05, 'SMT*': 0.011226, 'SNC': 0.02234, 'SNGLS': 0.000402, 'SNM': 0.62449, 'SNT': 0.029936, 'SPK': 0.0084, 'SRN': 0.003575, 'STEEM': 0.21546, 'STK': 1.949421, 'STORJ': 0.484106, 'STRAT': 0.027015, 'STU': 0.00019, 'STX': 0.3429, 'SUB': 0.000453, 'SUR': 0.05, 'SWFTC': 0.001564, 'SYS': 0.168, 'TAAS': 10, 'TESLA': 0.019139, 'THC': 0.003579, 'THETA': 1.08379, 'THS': 0.00171, 'TIO': 0.085, 'TKN': 0, 'TKY': 0.000171, 'TNB': 0.006163, 'TNT': 0.004121, 'TOA': 0.002397, 'TRC': 6.2, 'TRIG': 0.442874, 'TRST': 0.04799, 'TRUMP': 0.055, 'TRX': 0.061185, 'UBQ': 0.03534, 'UNO': 13.4, 'UNRC': 6e-05, 'UQC': 8, 'USDT': 1.001667, 'UTK': 0.10874, 'UTT': 0.048, 'VEE': 0.002401, 'VEN': 3.111737, 'VERI': 23.736235, 'VIA': 0.061734, 'VIB': 0.081892, 'VIBE': 0.004915, 'VOISE': 0.00018, 'VOX': 0.778855, 'VRS': 0.1375, 'VTC': 0.199069, 'VUC': 9.9e-05, 'WABI': 0.11632, 'WAVES': 4.369081, 'WAX': 0.1028, 'WC': 0.045, 'WGR': 0.018565, 'WINGS': 0.005144, 'WLK': 0.0058, 'WOP': 0.046453, 'WPR': 0.006033, 'WRC': 0.000298, 'WTC': 0.2952, 'XAUR': 0.10301, 'XBP': 0.0027, 'XBY': 0.2889, 'XCP': 4.47347, 'XCXT': 0.095658, 'XDN': 5.3e-05, 'XEM': 0.041275, 'XGB': 0.0015, 'XHI': 0.001325, 'XID': 0.010924, 'XLM': 0.102325, 'XMR': 145.63974, 'XNC': 0.00018, 'XRB': 22.367692, 'XRP': 0.326477, 'XTO': 0.324858, 'XTZ': 1.579388, 'XUC': 0.00538, 'XVG': 0.003279, 'XZC': 4.96985, 'YEE': 0.000132, 'YOC': 0.00012, 'YOYOW': 0.001813, 'ZBC': 0, 'ZCL': 0.034183, 'ZEC': 58.75432, 'ZEN': 14.46923, 'ZIL': 0.033774, 'ZNY': 0.02, 'ZRX': 0.280915, 'ZSC': 7.9e-05, '611': 0.389165
        }
    }

raw_historical_data = {
    'success': True, 
    'terms': 'https://coinlayer.com/terms', 
    'privacy': 'https://coinlayer.com/privacy', 
    'timestamp': 1636588748, 
    'target': 'USD', 
    'historical': True, 
    'date': '2021-11-10', 
    'rates': {
        'ABC': 59.99, 'ACP': 0.014931, 'ACT': 0.01442, 'ACT*': 0.017178, 'ADA': 2.104418, 'ADCN': 0.00013, 'ADL': 0.01515, 'ADX': 0.744965, 'ADZ': 0.0023, 'AE': 0.148, 'AGI': 0, 'AIB': 0.005626, 'AIDOC': 0.00065, 'AION': 0.1712, 'AIR': 0.001506, 'ALT': 0.565615, 'AMB': 0.042132, 'AMM': 0.01553, 'ANT': 4.817, 'APC': 0.0017, 'APPC': 0.088196, 'ARC': 0.0169, 'ARCT': 0.00061, 'ARDR': 0.318991, 'ARK': 3.469073, 'ARN': 0.05727, 'ASAFE2': 0.4, 'AST': 0.427737, 'ATB': 0.017, 'ATM': 13.6, 'AURS': 0.352867, 'AVT': 0, 'BAR': 14.2225, 'BASH': 0.0056, 'BAT': 1.077421, 'BAY': 0.0644, 'BBP': 0.0005, 'BCD': 2.120736, 'BCH': 666.904267, 'BCN': 0.000409, 'BCPT': 0.00325, 'BEE': 1e-06, 'BIO': 0.0008, 'BLC': 0.072132, 
        'BLOCK': 1.189, 'BLU': 0.00054, 'BLZ': 0.2627, 'BMC': 0.038916, 'BNB': 614.53577, 'BNT': 4.578598, 'BOST': 0.048, 'BQ': 7.775e-05, 'BQX': 2.720931, 'BRD': 0.189431, 'BRIT': 0.03, 'BT1': 0, 'BT2': 0, 'BTC': 65020.576832, 'BTCA': 0.00036, 'BTCS': 0.01201, 'BTCZ': 0.000749, 'BTG': 68.557436, 'BTLC': 9, 'BTM': 0.078282, 'BTM*': 0.122609, 
        'BTQ': 0.01, 'BTS': 0.04833, 'BTX': 0.384985, 'BURST': 0.017348, 'CALC': 0.0006, 'CAS': 0.007, 'CAT': 0.197792, 
        'CCRB': 0.08888, 'CDT': 0.062701, 'CESC': 0.0037, 'CHAT': 0.002625, 'CJ': 0.000898, 'CL': 0.028, 'CLD': 0.02, 'CLOAK': 10, 'CMT*': 0.03954, 'CND': 0.016276, 'CNX': 1.996594, 'CPC': 0.0005, 'CRAVE': 0.4, 'CRC': 0.08475, 'CRE': 1.316485, 'CRW': 0.061, 'CTO': 0.005, 'CTR': 0.017, 'CVC': 0.46093, 'DAS': 0.937816, 'DASH': 217.31191, 'DAT': 0.069333, 'DATA': 0.13811, 'DBC': 0.009103, 'DBET': 0.027656, 'DCN': 2.91793e-05, 'DCR': 102.451963, 'DCT': 0.00059, 'DEEP': 0.001, 'DENT': 0.006352, 'DGB': 0.054793, 'DGD': 883.449465, 'DIM': 9.4957e-05, 'DIME': 3e-05, 'DMD': 0.58782, 'DNT': 0.179, 'DOGE': 0.256028, 'DRGN': 0.168403, 'DRZ': 3, 'DSH': 252.13175, 'DTA': 0.000381, 'EC': 50, 'EDG': 0.02056, 'EDO': 0.82091, 'EDR': 0, 'EKO': 0.001067, 'ELA': 5.1035, 'ELF': 0.52618, 'EMC': 0.105772, 'EMGO': 0.43382, 'ENG': 0.060455, 'ENJ': 2.81444, 'EOS': 4.853373, 'ERT': 0.2054, 'ETC': 56.917306, 'ETH': 4639.409735, 'ETN': 0.01955, 'ETP': 0.311994, 'ETT': 2.9, 'EVR': 0.104931, 'EVX': 0.644884, 'FCT': 1.602751, 'FLP': 
        0.01, 'FOTA': 0.00052, 'FRST': 0.78001, 'FUEL': 0.000809, 'FUN': 0.019396, 'FUNC': 0.00061, 'FUTC': 0.004, 'GAME': 0.205988, 'GAS': 8.622307, 'GBYTE': 38.420519, 'GMX': 6.467e-05, 'GNO': 481.75, 'GNT': 0.517385, 'GNX': 0.02938, 'GRC': 0.0067, 'GRS': 10, 'GRWI': 10000, 'GTC': 9.033986, 'GTO': 0.0478, 'GUP': 0.001482, 'GVT': 0.332049, 'GXS': 0.39381, 'HAC': 0.00153, 'HNC': 0, 'HSR': 1.8723, 'HST': 0.0027, 'HVN': 0.03529, 'ICN': 0.1452, 'ICOS': 17, 'ICX': 1.958243, 'IGNIS': 0.025264, 'ILC': 0.098703, 'INK': 0.001317, 'INS': 0.401735, 'INSN': 0.0473, 'INT': 
        0.01128, 'IOP': 15.455555, 'IOST': 0.048115, 'ITC': 0.1012, 'KCS': 21.471396, 'KICK': 0.000324, 'KIN': 8.7187e-05, 'KLC': 0.000703, 'KMD': 0.976976, 'KNC': 1.849384, 'KRB': 6, 'LA': 0.106801, 'LEND': 3.211739, 'LEO': 3.250192, 'LINDA': 0.000271, 'LINK': 34.319431, 'LOC': 3.730677, 'LOG': 0.060174, 'LRC': 3.031075, 'LSK': 3.385641, 'LTC': 261.276673, 'LUN': 0.102732, 'LUX': 2.09e-06, 'MAID': 0.49806, 'MANA': 2.501196, 'MCAP': 0.005398, 'MCO': 10.36, 'MDA': 0.688565, 'MDS': 0.005005, 'MIOTA': 1.2969, 'MKR': 2948.219213, 'MLN': 129.563389, 'MNX': 0.028649, 
        'MOD': 1.3331, 'MOIN': 0.033073, 'MONA': 1.771827, 'MTL': 3.168, 'MTN*': 0.009575, 'MTX': 0.029801, 'NAS': 0.494022, 'NAV': 0.423792, 'NBT': 211.988786, 'NDC': 0.008989, 'NEBL': 1.37487, 'NEO': 48.303219, 'NEU': 0.175, 'NEWB': 0.002604, 'NGC': 0.265487, 'NKC': 0.002946, 'NLC2': 0.599935, 'NMC': 5.867998, 'NMR': 43.154028, 'NULS': 0.5702, 'NVC': 10, 'NXT': 0.019342, 'OAX': 0.287605, 'OBITS': 0.015, 'OC': 0.001178, 'OCN': 0.000825, 'ODN': 0.5, 'OK': 0.023407, 'OMG': 15.244621, 'OMNI': 3.5397, 'ORE': 0, 'ORME': 1.235715, 'OST': 0.005218, 'OTN': 0, 'OTX': 0.023, 'OXY': 2.206, 'PART': 3.951477, 'PAY': 0.085804, 'PBT': 855.667674, 'PCS': 0.019961, 'PIVX': 0.728033, 'PIZZA': 0.001, 'PLBT': 20, 'PLR': 0.032254, 'POE': 0.00013, 'POLY': 0.656, 'POSW': 0.48712, 'POWR': 0.375067, 'PPC': 1.704996, 'PPT': 0.799536, 'PPY': 5.45, 'PRC': 3e-05, 'PRES': 0.219998, 'PRG': 0.612149, 'PRL': 0.061361, 'PRO': 3.182678, 'PURA': 0.25, 'PUT': 0, 'QASH': 0.08589, 'QAU': 0, 'QSP': 0.057855, 'QTUM': 16.293693, 'QUN': 0.008318, 'R': 1, 'RBIES': 1, 'RCN': 0.021736, 'RDD': 0.002941, 'RDN': 0, 'RDN*': 0.324446, 'REBL': 0.004916, 'REE': 
        1e-05, 'REP': 24.5, 'REQ': 0.2148, 'REV': 0.01576, 'RGC': 0.001, 'RHOC': 0.178417, 'RIYA': 0.090025, 'RKC': 5, 'RLC': 4.496868, 'RPX': 0.145646, 'RUFF': 0.005445, 'SALT': 0.768708, 'SAN': 0.545, 'SBC': 7, 'SC': 0.019592, 'SENT': 0.005, 'SHIFT': 0, 'SIB': 5.177, 'SMART': 0.005042, 'SMLY': 6e-05, 'SMT*': 0.011226, 'SNC': 0.03273, 'SNGLS': 0.000402, 'SNM': 0.68646, 'SNT': 0.095186, 'SPK': 0.0084, 'SRN': 0.011832, 'STEEM': 0.59755, 'STK': 0.0013, 'STORJ': 1.488249, 'STRAT': 0.956873, 'STU': 0.00019, 'STX': 1.057284, 'SUB': 0.004142, 'SUR': 0.3566, 'SWFTC': 0.002149, 'SYS': 0.379069, 'TAAS': 10, 'TESLA': 0.019139, 'THC': 0.011704, 'THETA': 7.327693, 'THS': 0.00171, 'TIO': 0.085, 'TKN': 0, 'TKY': 0.000927, 'TNB': 0.002491, 'TNT': 0.032, 'TOA': 0.002397, 'TRC': 6.2, 'TRIG': 1.287403, 'TRST': 0.04799, 'TRUMP': 0.055, 'TRX': 0.106762, 'UBQ': 0.240467, 'UNO': 95.0001, 'UNRC': 6e-05, 'UQC': 19.3, 'USDT': 1.003313, 'UTK': 0.424568, 'UTT': 0.330676, 'VEE': 0.02594, 'VEN': 9.053607, 'VERI': 23.736235, 'VIA': 0.292592, 'VIB': 0.052078, 'VIBE': 0.027302, 'VOISE': 0.00018, 'VOX': 1845.72102, 'VRS': 0.1375, 'VTC': 0.678812, 'VUC': 9.9e-05, 'WABI': 0.200837, 'WAVES': 23.888445, 'WAX': 0.4976, 'WC': 0.045, 'WGR': 0.053967, 'WINGS': 
        0.033811, 'WLK': 0.0058, 'WOP': 0.046453, 'WPR': 0.011747, 'WRC': 0.00055, 'WTC': 0.9709, 'XAUR': 0.10301, 'XBP': 0.0027, 'XBY': 0.2889, 'XCP': 13.004068, 'XCXT': 0.095658, 'XDN': 0.00126, 'XEM': 0.191695, 'XGB': 0.0015, 'XHI': 0.001325, 'XID': 0.010924, 'XLM': 0.385394, 'XMR': 267.681883, 'XNC': 0.00018, 'XRB': 59.455513, 'XRP': 1.193833, 'XTO': 0.324858, 'XTZ': 5.776283, 'XUC': 0.105843, 'XVG': 0.029104, 'XZC': 4.96985, 'YEE': 0.003445, 'YOC': 0.00012, 'YOYOW': 0.021452, 'ZBC': 0, 'ZCL': 0.152757, 'ZEC': 179.754247, 'ZEN': 92.57386, 'ZIL': 0.102225, 'ZNY': 0.02, 'ZRX': 1.210173, 'ZSC': 0.000454, '611': 0.389165
        }
    }

# Creates a dictionary of json objects
def create_dict(live_data_json, historical_data_json, tickers):
    crypto_dict = {}
    today = datetime.now()
    
    for ticker in tickers:
        crypto_dict[ticker] = {}
        crypto_dict[ticker]['High'] = historical_data_json['rates'][ticker]
        historical_date = historical_data_json['date']
        crypto_dict[ticker]['High Date'] = datetime(int(historical_date[:4]), int(historical_date[5:7]), int(historical_date[8:10]))
        crypto_dict[ticker]['Time Since High'] = crypto_dict[ticker]['High Date'] - today
        crypto_dict[ticker]['Current Price'] = live_data_json['rates'][ticker]
        crypto_dict[ticker]['Delta'] = crypto_dict[ticker]['High'] - crypto_dict[ticker]['Current Price']

    return crypto_dict

# Inserts json dictionary data into sqlite database
def insert_to_sqlite_db(live_data_json, historical_data_json, tickers):

    database_delete = """DELETE FROM rates"""
    sqlite3_cursor.execute(database_delete)

    for t in tickers:
        ticker = t
        price = live_data_json['rates'][t]
        all_time_high = historical_data_json['rates'][t]
        all_time_high_date = historical_data_json['date']
        delta = price - all_time_high

        database_insert = """INSERT INTO rates (ticker, price, all_time_high, all_time_high_date, delta) VALUES (?,?,?,?,?)"""
        sqlite3_cursor.execute(database_insert,[ticker, price, all_time_high, all_time_high_date, delta])
        sqlite3.commit()

    return

def insert_to_postgres_db(live_data_json, historical_data_json, tickers):
    database_delete = "DELETE FROM rates"
    postgres_cursor.execute(database_delete)
    
    for t in tickers:
        ticker = t
        price = live_data_json['rates'][t]
        all_time_high = historical_data_json['rates'][t]
        all_time_high_date = historical_data_json['date']
        delta = price - all_time_high

        database_insert = """INSERT INTO rates (ticker, price, all_time_high_price, all_time_high_date, delta) VALUES (%s,%s,%s,%s,%s)"""
        postgres_cursor.execute(database_insert,[ticker, price, all_time_high, all_time_high_date, delta])
        postgres.commit()

ticker_list = ['BTC']

# sqlite query test
insert_to_sqlite_db(raw_live_data, raw_historical_data, ticker_list)
sqlite_query = sqlite3_cursor.execute("""SELECT * FROM rates""")
print(sqlite_query.fetchall())

# postgres query test
insert_to_postgres_db(raw_live_data, raw_historical_data, ticker_list)
postgres_cursor.execute("""SELECT * FROM rates""")
rows = postgres_cursor.fetchall()
print(rows)

# btc_dict = create_dict(raw_live_data, raw_historical_data, ticker_list)
# print(btc_dict)

sqlite3.close()
postgres_cursor.close()
postgres.close()
