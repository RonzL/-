info_list = []
str_tuple = ("姓名", "电话", "QQ", "邮箱")


def menu_dis():
    # 显示菜单
    print("*" * 50)
    print("欢迎使用【名片管理系统】 V1.0\n")
    print("1.添加名片")
    print("2.显示全部")
    print("3.查询名片\n")
    print("0.退出系统")
    print("*" * 50)


def add_info():
    # 功能1：显示新建名片菜单
    info_dic = {"name": "",
                "phone": "",
                "qq": "",
                "email": ""}
    print("=" * 50)
    print("功能：新建名片")
    # 新增一个字典到列表的元素中
    info_list.append(info_dic)
    print(info_list)
    # 将数据写入列表中新增的字典里
    info_list[-1]["name"] = input("请输入姓名：")
    info_list[-1]["phone"] = input("请输入电话：")
    info_list[-1]["qq"] = input("请输入QQ号码：")
    info_list[-1]["email"] = input("请输入邮箱：")
    print("+" * 50)
    print("成功将 %s 的信息添加！" % info_list[-1]["name"])
    print("+" * 50)


def info_display():
    """
    功能2：显示所有名片
    """

    print("=" * 50)
    print("功能：显示全部")
    print("-" * 60)
    # 打印表头（姓名   电话   QQ    邮箱）
    for i in str_tuple:
        print(i, end='\t\t\t')
    print("")

    # 遍历名片列表输出字典信息
    for str_2 in info_list:
        print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (str_2["name"],
                                              str_2["phone"],
                                              str_2["qq"],
                                              str_2["email"]))
    print("-" * 60)


def del_info():
    """
    功能3: 查询名片
    """
    print("=" * 50)
    print("功能：查询名片")
    find_name = input("请输入要查询的姓名：")

    # 遍历列表中的字典，查找姓名
    for i in info_list:
        if find_name == i["name"]:
            print("-" * 60)
            for j in str_tuple:
                print(j, end='\t\t\t')
            print("")
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (i["name"],
                                                  i["phone"],
                                                  i["qq"],
                                                  i["email"]))
            print("-" * 60)
            print("请输入对名片的操作：1：修改/ 2：删除/ 0：返回上级菜单")
            str_1 = input("请输入您将要进行的操作： ")
            if str_1.isdigit():
                choice_1 = int(str_1)
                if choice_1 == 1:
                    # 修改名片

                    temp_name = i["name"]

                    new_name = input_card_info(i["name"], "请输入修改后的姓名(回车不修改)：")
                    new_phone = input_card_info(i["phone"], "请输入修改后的电话(回车不修改)：")
                    new_qq = input_card_info(i["qq"], "请输入修改后的QQ号码(回车不修改)：")
                    new_email = input_card_info(i["email"], "请输入修改后的邮箱(回车不修改)：")

                    i["name"] = new_name
                    i["phone"] = new_phone
                    i["qq"] = new_qq
                    i["email"] = new_email

                    print("+" * 50)
                    print("%s 的名片修改成功！" % temp_name)
                    print("+" * 50)
                    break

                elif choice_1 == 2:
                    print("+" * 50)
                    print("%s 的名片已经删除成功！" % i["name"])
                    print("+" * 50)
                    del info_list[info_list.index(i)]
                    break

                elif choice_1 == 0:
                    break
            else:
                print("您的输入有误！")
                break
    else:
        print("没有查找到您要找的人！")


def input_card_info(dic_value, message):
    """
    判断是否有输入
    """

    # 输入信息
    str_message = input(message)

    # 如果有输入,返回最新的值
    if len(str_message) > 0:
        return str_message

    # 如果没有输入,返回原来的值
    else:
        return dic_value
