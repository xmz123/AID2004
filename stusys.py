import re
import os

# 定义保存学生信息的文件
student_file = 'stundent_txt'


# 显示学生菜单
def menu():
    print('''
          1.录入学生信息
        -------------------
          2.查找学生信息
        -------------------- 
          3.删除学生信息
        --------------------
          4.修改学生信息
        --------------------
          5.排序
        --------------------  
          6.统计学生总人数
        --------------------
          7.显示所有学会信息
        --------------------
          0.退出
        --------------------  
          ''')
def main():
    while True:
        menu()
        option = input('请选择选项：')
        if option == '0':
            print('您已退出学生管理系统！')
            break
        else:
            if option == '1':
                insert()
            elif option == '2':
                search()
            elif option == '3':
                delect()
            elif option == '4':
                pass
            elif option == '5':
                pass
            elif option == '6':
                pass
            elif option == '7':
                pass
def insert():  # 录入学生信息
    mark = True
    while mark:
        studentlist = []
        id = input('请输入学生编号:')
        if len(id) > 8:
            print('编号不符合标准')
            continue
        if not id:
            break
        name = input('请输入学生姓名：')
        if not name:
            break
        try:
            python = input('请输入python成绩:')
            english = input('请输入英语成绩：')
            c = input('请输入c语言成绩：')
        except:
            print('输入无效，请输入一个数值：')
            continue

        student = {'id': id, 'name': name,
                   'python': python,
                   'english': english,
                   'c': c}
        studentlist.append(student)
        save(studentlist)  #这一步很重要
        continue_ = input('是否继续添加？ (y/n)')
        if continue_ == 'y':
            mark = True
        else:
            mark = False

    print('学生信息录入完成!')

def save(student):  # 保存学生信息
    try:
        student_txt = open(student_file, 'a')  # 以追加的方式打开，文件不存在，则创建新文件并打开
    except Exception as e:
        student_txt = open(student_file, "w")
    for info in student:
        student_txt.write(str(info) + "\n")
    student_txt.close()

def search():
    seek_student = []
    mark = True
    while mark:
        id = ''
        name = ''
        if os.path.exists(student_file):
            seek_way = input('1.按照编号查找  2.按照名字查找')
            if seek_way == '1':
                id = input('请输入学生编号：')
            elif seek_way == '2':
                name = input('请输入学生姓名:')
            else:
                print('输入错误，请是重新输入')
                continue
            with open(student_file) as f:
                student = f.readlines()  #读取全部内容
                for list in student:
                    d = dict(eval(list))  #
                    if id is not "":
                        if d['id'] == id:
                            seek_student.append(d)
                    elif name is not "":
                        if d['name'] == name:
                            seek_student.append(d)
                print(seek_student)
                seek_student.clear()
                seek_mark = input('是否继续查询？y:继续 n：退出')
                if seek_mark == 'y':
                    mark = True
                else:
                    mark = False
        else:
            print('暂未存储数据信息')
            return
def delect():
    mark=True
    while mark:
        student_id=input('请输入学生编号：')
        if student_id is not "":
            if os.path.exists(student_file):
                with open(student_file,'r') as rf:
                    old_student=rf.readlines()
            else:
                old_student=[]
            ifdel=False
            if old_student:
                with open(student_file,'w') as wf:
                    d={}
                    for list in old_student:
                        d=dict(eval(list))
                        if d['id']!=student_id:
                            wf.write(str(d) + "\n")
                        else:
                            ifdel=True
                    if ifdel:
                        print(f'编号为{student_id}的学生信息已经删除')
                    else:
                        print(f'没有找到编号为{student_id}的学生')


            else:
                print('无学生信息')
                continue
            inputMark = input("是否继续删除？（y/n）:")
            if inputMark == "y":
                mark = True  # 继续删除
            else:
                mark = False  # 退出删除学生信息功能









if __name__ == '__main__':
    main()
