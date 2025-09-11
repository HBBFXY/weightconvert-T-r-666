# 在这个文件下编写代码，题目具体要求见README.md文件
TempStr = input()
unit = TempStr[-2:]
value = float(TempStr[:-2])         
if unit == "kg":
    pounds = value * 2.2046
    print(f"对应的英制重量为{pounds:.3f}磅")
elif unit == "pd":
    kilograms = value * 0.4535
    print(f"对应的公制重量为{kilograms:.3f}公斤")
else:
    print("请输入正确的单位")
