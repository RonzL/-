#! /usr/bin/python3      ---> shebang (加上此行命令之后可在shell命令行中执行py文件)

# 名片管理系统
# 实现的功能如下：
#              1. 添加名片：
#              2. 查看名片：
#              3. 查询名片： 3.1.修改名片 3.2删除名片
# 本项目重点在于 循环的使用、元组的使用、列表的使用、for的使用

import cards_tools

info = [{"name": "", "phone": "", "qq": "", "email": ""}]

while True:
    # 显示系统菜单
    cards_tools.menu_dis()
    str_main = input("请输入您将要进行的操作： ")
    if str_main in ["1", "2", "3"]:
	# if str_main.isdigit():
        # choice = int(str_main)
        print("您选择的操作是: %s" % str_main)
        if choice == 1:
            cards_tools.add_info()
        elif choice == 2:
            cards_tools.info_display()
        elif choice == 3:
            cards_tools.del_info()
	elif str_main == "0":
            print("欢迎您下次使用名片管理系统，再见！")
            break
    else:
        print("您的输入有误，请重新输入！(输入的内容只能为数字)")
        continue

