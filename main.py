import sys
from src.public_function import *
def youxigongne(a):
    if a==1:
        print("请输入执行指令：\n1.解包\n 2.提取文本\n 3.导入文本\n 4.封包\n 5.汉化程序\n")
        b = int(input())
        if b==1:
            MED.unpack('md_scr.med')
        elif b==2:
            MED.extract_med()
        elif b==3:
            MED.output()
        elif b==4:
            MED.repack('output')
        elif b == 5:
            print("请输入需要汉化的程序名字")
            C = input()
            MED.fix_exe(C)
    elif a==2:
        print("请输入执行指令：\n1.提取文本\n 2.封包\n")
        b = int(input())
        if b==1:
            ANIM.extract()
        elif b==2:
            ANIM.output()
    elif a == 3:
        print("请输入执行指令：\n1.提取文本\n 2.Lilim.fix_dict()\n 3.Lilim.output_hook_dict()\n")
        b = int(input())
        if b==1:
            Lilim.extract_for_hook_aos2()
        elif b==2:
            Lilim.fix_dict()
        elif b==3:
            Lilim.output_hook_dict()
    elif a == 4:
        print("请输入执行指令：\n1.解包\n 2.提取文本\n 3.导入文本\n 4.封包\n 5.汉化程序\n" )
        b = int(input())
        if b==1:
            PAC.unpack_pac('srp.pac')
        elif b==2:
            PAC.extract_srp()
        elif b==3:
            PAC.output_srp()
        elif b == 4:
            PAC.repack_pac()
        elif b == 5:
            print("请输入需要汉化的程序名字")
            C = input()
            PAC.fix_exe(C)
    elif a == 5:
        print("请输入执行指令：\n1.解包\n 2.封包\n " )
        b = int(input())
        if b==1:
            RPM.unpack_arc()
        elif b==2:
            RPM.repack_arc()
    elif a == 6:
        print("请输入执行指令：\n 1.解包\n 2.提取文本\n 3.导入文本\n 4.封包\n" )
        b = int(input())
        if b==1:
            NEKOSDK.unpack()
        elif b==2:
            NEKOSDK.extract_pak_txt()
        elif b==3:
            NEKOSDK.output()
        elif b == 4:
            NEKOSDK.repack()
    elif a == 7:
        print("请输入执行指令：\n 1.提取文本\n 2.导入文本\n " )
        b = int(input())
        if b==1:
            SILKY.extract()
        elif b==2:
            SILKY.output()
    elif a == 8:
        print("请输入执行指令：\n 1.解包\n 2.提取文本\n 3.导入文本\n " )
        b = int(input())
        if b==1:
            YU_RIS.decode('data.ypf')
        elif b==2:
            YU_RIS.extract_ybn()
        elif b==3:
            YU_RIS.output_ybn(output_all=True, encrypt=True)
    elif a == 9:
        print("请输入执行指令：\n 1.提取文本\n 2.导入文本\n " )
        b = int(input())
        if b==1:
            XFL.extract()
        elif b==2:
            XFL.output()
    elif a == 10:
        print("请输入执行指令：\n 1.提取文本\n 2.导入文本\n 3.汉化程序\n " )
        b = int(input())
        if b==1:
            LIVEMAKER.extract()
        elif b==2:
            LIVEMAKER.output(True)
        elif b==3:
            LIVEMAKER.extract_exe('game.exe', True)
    elif a == 11:
        print("请输入执行指令：\n 1.提取文本\n 2.导入文本\n " )
        b = int(input())
        if b==1:
            NScript.pt.extract()
        elif b==2:
            NScript.pt.output()
    elif a == 12:
        print("请输入执行指令：\n 1.提取文本\n 2.导入文本\n  " )
        b = int(input())
        if b==1:
            RPGMakerVX.extract()
        elif b==2:
            RPGMakerVX.output()


if True:
#if sys.argv[1] == '1':
    print("请输入游戏引擎编号：\n 1.MED \n 2.ANIM\n 3.Lilim\n 4.PAC\n 5.RPM\n 6.NEKOSDK\n 7.SILKY\n 8.YU_RIS\n 9.XFL\n 10.LIVEMAKER\n "
          "11.Nsrc\n 12.RPGMakerVX\n")
    engineCode=int(input())
    youxigongne(engineCode)
    while 1:
        try:
            youxigongne(engineCode)
        except ValueError as ex:
            break
        except Exception as ex:
            print(ex)
            break
