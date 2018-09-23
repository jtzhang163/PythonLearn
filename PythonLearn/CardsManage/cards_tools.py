#记录所有的名片列表
card_list = []

def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("")
    print("0. 退出系统")
    print("*" * 50) 

def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")

    name = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入QQ：")
    email = input("请输入邮箱：")

    #名片字典
    card_dict = {"name":name,
                 "phone":phone,
                 "qq":qq,
                 "email":email}
    card_list.append(card_dict)
    print("添加 %s 的名片成功" % name)

def show_cards():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")

    #没有记录直接返回
    if len(card_list) == 0:
        print("当前没有任何名片记录！")
        return

    #打印表头
    for name in ["姓名","电话","QQ","邮箱"]:
        print(name,end = "\t\t")
    print("");
    print("=" * 60);
    for card_dic in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dic["name"],card_dic["phone"],card_dic["qq"],card_dic["email"]))
    print("=" * 60);

def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")

    find_name = input("请输入要搜索的姓名：")

    for card_dic in card_list:
        if card_dic["name"] == find_name:
            print("找到了！")
            print("姓名\t\t电话\t\tQQ\t\t邮箱\t\t")
            print("=" * 60);
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dic["name"],card_dic["phone"],card_dic["qq"],card_dic["email"]))

            #执行修改和查询

            break
    else:
        print("没有找到 %s " % find_name)