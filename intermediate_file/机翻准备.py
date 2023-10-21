import  re
with open('jp_chs2.json','w+',encoding='utf8') as f:
    with open('jp_chs.json','r',encoding='utf8') as w:
        w=w.readlines()
        for i in w:
            asd = re.compile(r'\"(.*?)\"')
            ressg = asd.findall(i)
            print(ressg)
            if ressg ==[] :
                f.write(i)
            else:
                a=i.replace('\"\"','\"{}\"'.format(ressg[0]))
                f.write(a)
pause
