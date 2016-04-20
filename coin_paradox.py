# -*- coding: utf-8 -*-

def printt(*args, **kwargs):
    prespace = ' '.join([' '] * kwargs.get('tab', 0))
    print prespace,
    for item in args:
        print item,
    print ''

hh_first = 0
ht_first = 0

records = []
import random
for i in range(500000):
    last_coin = -1
    while True:
        coin = random.randint(1, 2)
        records.append(coin)
        if coin is 1 and last_coin is 1:
            hh_first += 1
            break
        elif coin is 2 and last_coin is 1:
            ht_first += 1
            break
        last_coin = coin

printt("records lens:", len(records))
printt("hh_first:", hh_first)
printt("ht_first:", ht_first)

records = records
r_h = 0
r_t = 0
r_hh = 0
r_ht = 0
r_th = 0
r_tt = 0
for i in range(len(records)-1):
    if records[i] == 1:
        r_h += 1
        if records[i+1] == 1:
            r_hh += 1
        else:
            r_ht += 1
    else:
        r_t += 1
        if records[i+1] == 1:
            r_th += 1
        else:
            r_tt += 1
        
printt("r_h:", r_h)
printt("r_t:", r_t)
printt("r_hh:", r_hh)
printt("r_ht:", r_ht)
printt("r_th:", r_th)
printt("r_tt:", r_tt)
