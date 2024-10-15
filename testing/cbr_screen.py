# -*- coding: utf-8 -*-

def cbr_screener(homedisk):
    sub = 'Макроэкономика и банки/Банк России/Количество офисов банков (M)'
    link = homedisk + sub
    return link
    
def cbr_concat(list_files):
    names = list_files
    for i in trange(len(names), leave = False):
        a = names[i]
        date = a.replace(FORMAT, '')
        b = pd.read_excel(a)
        b['Дата'] = date
        b['Дата'] = pd.to_datetime(b['Дата'])
        if i == 0: 
            result = b
        else: 
            result = pd.concat([result, b], axis=0)
    return result
