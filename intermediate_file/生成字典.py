import os
with open('jp_all.txt','r',encoding='utf-8') as f:
    with open('jp_chs.json','w+',encoding='utf-8') as ff:
        f=f.readlines()
        for i in f:
            k='    "{}": "",\n'.format(i[:-1])
            ff.write(k)
