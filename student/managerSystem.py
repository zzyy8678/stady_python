from student import *

class StudentManager(object):
    def __init__(self):
        # 存储数据所用的列表
        self.student_list = []

    # ⼀一. 程序⼊入⼝口函数，启动程序后执⾏的函数
    def run(self):
        # 1. 加载学员信息
        self.load_student()
        print("====================学员管理系统=============================")
        while True:
            # 2. 显示功能菜单
            self.show_menu()
            # 3. ⽤用户输⼊入功能序号
            while True:
                try:
                    menu_num = int(input('请输⼊入您需要的功能序号：'))
                except ValueError:
                    print("输入不正确，请重新输入：")
                    break
                # 4 根据用户输⼊入的功能序号执⾏不同的功能
                if menu_num == 1:
                    # 添加学员
                    self.add_student()
                elif menu_num == 2:
                    self.del_student()
                elif menu_num == 3:
                    # 修改学员信息
                    self.modify_student()
                elif menu_num == 4:
                    # 查询学员信息
                    self.search_student()
                elif menu_num == 5:
                    # 显示所有学员信息
                    self.show_student()
                elif menu_num == 6:
                    # 保存学员信息
                    self.save_student()
                elif menu_num == 7:
                    # 退出
                    break
        # ⼆二. 定义功能函数
        # 2.1 显示功能菜单

    @staticmethod
    def show_menu():
        print('请选择如下功能-----------------')
        print('1:添加学员')
        print('2:删除学员')
        print('3:修改学员信息')
        print('4:查询学员信息')
        print('5:显示所有学员信息')
        print('6:保存学员信息')
        print('7:退出系统')

    # 2.2 添加学员
    def add_student(self):
        # 1. ⽤用户输⼊入姓名、性别、⼿手机号
        name_list = []
        tel_list = []
        for i in self.student_list:
            name_list.append(i.name)
            print(name_list)
            tel_list.append(i.tel)
            print(tel_list)
        while True:
            name = input('请输⼊入您的姓名：')
            if name not in name_list:
                break
            else:
                print("用户已经存在，请重新输入")
                continue
        while True:
            tel = input('输入一个手机号码：')
            tel = tel.strip()  # 去除两端空格
            if len(tel) != 11:  # 判断手机号是否为11位
                print(f'您输入的手机号码（{tel}）有误，提示：电话长度为11')
            elif tel[0] != '1':  # 判断手机号的第一位是否为1
                print(f'您输入的手机号码（{tel}）有误，提示：电话开头数字应为1')
            elif tel.isdigit() == False:  # 判断手机号是否全为数字组成
                print(f'您输入的手机号码（{tel}）有误，提示：电话是由数字组成')
            elif tel in tel_list:
                print(f'该手机号（{tel}已经存在，请重新输入）')
                continue
            else:
                break
        while True:
            gender = input('请输入性别（nan 或者nv）：')
            if gender == "nan":
                break
            elif gender == "nv":
                break
            else:
                continue
        # 2. 创建学员对象：先导入学员模块，再创建对象
        student = Student(name, gender, tel)
        # 3. 将该学员对象添加到列列表
        self.student_list.append(student)
        # 打印信息
        # print(self.student_list)
        # print(student)

    # 2.3 删除学员
    def del_student(self):
        # 1. ⽤用户输⼊入⽬目标学员姓名
        del_name = input('请输⼊入要删除的学员姓名：')
        # 2. 如果⽤用户输⼊入的⽬目标学员存在则删除，否则提示学员不不存在
        for i in self.student_list:
            if i.name == del_name:
                self.student_list.remove(i)
                break
        else:
            print('查无此⼈人！')
        # 打印学员列列表，验证删除功能
        print(self.student_list)

    # 2.4 修改学员信息
    def modify_student(self):
        name_list = []
        tel_list = []
        # 1. ⽤用户输⼊入⽬目标学员姓名
        modify_name = input('请输入要修改的学员的姓名：')
        # 2. 如果⽤用户输入的目标学员存在则修改姓名、性别、⼿手机号等数据，否则提示学员不存在
        for i in self.student_list:
            name_list.append(i.name)
            tel_list.append(i.tel)
            if i.name == modify_name:
                while True:
                    input_name = input('请输入想修改的名字：')
                    if input_name not in name_list:
                        i.name=input_name
                        break
                    else:
                        print(f'该学员名字重名({input_name})，请重新输入：')
                        continue
                while True:
                    gender=input('请输入性别（nan 或者nv）：')
                    if gender == "nan":
                        i.gender=gender
                        break
                    elif gender == "nv":
                        i.gender=gender
                        break
                    else:
                        print("输入不正确请重新输入，提示，性别为（nan 或者nv）：")
                        continue
                while True:
                    tel = input('输入要修改的手机号码：')
                    tel = tel.strip()  # 去除两端空格
                    if len(tel) != 11:  # 判断手机号是否为11位
                        print(f'您输入的手机号码（{tel}）有误，提示：电话长度为11')
                    elif tel[0] != '1':  # 判断手机号的第一位是否为1
                        print(f'您输入的手机号码（{tel}）有误，提示：电话开头数字应为1')
                    elif tel.isdigit() == False:  # 判断手机号是否全为数字组成
                        print(f'您输入的手机号码（{tel}）有误，提示：电话是由数字组成')
                    elif tel in tel_list:
                        print(f'该手机号（{tel}已经存在，请重新输入）')
                        continue
                    else:
                        i.tel=tel
                        break
                print(f'修改该学员信息成功，姓名{i.name},性别{i.gender}, 手机号{i.tel}')
                break
        else:
            print('查⽆无此⼈人！')

    # 2.5 查询学员信息
    def search_student(self):
        # 1. ⽤用户输⼊入⽬目标学员姓名
        search_name = input('请输入要查询的学员的姓名：')
        # 2. 如果用户输入的目标学员存在，则打印学员信息，否则提示学员不存在
        for i in self.student_list:
            if i.name == search_name:
                print(f'姓名:{i.name},性别:{i.gender}, 手机号:{i.tel}')
                break
        else:
            print('查⽆无此⼈人!')

    # 2.6 显示所有学员信息
    def show_student(self):
        print('姓名\t性别\t⼿手机号')
        print(self.student_list)
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')
            student_result = [i.name, i.gender, i.tel]
            print(student_result)

    # 2.7 保存学员信息
    def save_student(self):
        # 1. 打开⽂文件
        f = open('student.data', 'w')
        # 2. ⽂文件写⼊入学员数据
        # 注意1：文件写入的数据不能是学员对象的内存地址，需要把学员数据转换成列列表字典数据再做存储
        new_list = [i.__dict__ for i in self.student_list]
        # [{'name': 'aa', 'gender': 'nv', 'tel': '111'}]
        print(new_list)
        # 注意2：文件内数据要求为字符串串类型，故需要先转换数据类型为字符串串才能文件写⼊入数据
        f.write(str(new_list))
        # 3. 关闭⽂文件
        f.close()

    # 2.8 加载学员信息
    def load_student(self):
        # 尝试以"r"模式打开数据文件，文件不存在则提示用户；文件存在（没有异常）则读取数据, encoding='utf-8'
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            # 1. 读取数据
            data = f.read()
            # 2. 文件中读取的数据都是字符串,内部为字典数据，故需要转换数据类型再转换字典对象后存储到学员列列表
            new_list = eval(data)
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]
        finally:
            # 3. 关闭文件

            f.close()
