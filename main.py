# 在这个文件下编写代码，题目具体要求见README.md文件
TempStr = input("请输入带有符号的重量：")
if TempStr[-2:] in ['kg']:
    pd = eval(TempStr[0:-2])*2.2046
    print("转换后的重量为{:.3f}磅".format(pd))
elif TempStr[-2:] in ['pd']:
    kg = eval(TempStr[0:-2])/2.2046    
    print("转换后的重量为{:.3f}公斤".format(kg))
else:
    print("输入格式错误")
