import pandas as pd
from math import log
#from matplotlib import pyplot as plot

def Analitics(path):
    text = open(path, mode='rb').read()

    table = pd.DataFrame({'value': bytearray(text)}).groupby('value').value.count().to_dict()
    table = pd.DataFrame({'char': table.keys(), 'rate': table.values()})
    table['probability'] = table.rate/table.rate.sum()
    table['information_weight'] = table.probability.apply(lambda x: -log(x, 2))

    print('bits count =', len(text)*8)
    print('middle inf weight =', (table.probability * table.information_weight).sum())
    print('summary inf weight or theoretical min =', (table.information_weight * table.rate).sum())
    #print('theoretical min = ', (table.information_weight).sum()*10)

print('source')
Analitics(r"C:\Users\ilya\Desktop\1.txt")
print('\ncoded')
Analitics(r"C:\Users\ilya\Desktop\2.txt")
