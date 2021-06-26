<<<<<<< HEAD
import  re
file1=open("src\data_corey.txt ","r")
file=file1.read()
file1.close()
reg = re.compile ("(\d{3}\D{0,3}\d{3}\D{0,3}\d{4})")
found = re.findall(reg,file)

"""ПОИСК ЗНАЧЕНИИ НА ОКОНЧАНИЕ 7  """


num_end=re.findall("(\d{3}\D{0,3}\d{3}\D{0,3}[0-9][0-9][0-9][7])", file)
num_end_7=len(num_end)
total_num=len(found)



"""КОНКРЕТНО ДЛЯ ЭТОЙ ЗАДАЧИ"""
reg1=re.compile("([a-zA-Z]+@[a-zA-Z]+.(com|net))")

mail_com_net=re.findall(reg1,file)


"""КОЛИЧЕСТВО COM И MAIL"""

total_mail_com=len(mail_com_net)


"""УНИВЕРСАЛЬНЫЙ ШАБЛОН"""
univers=re.compile("\w+@\w+.\w{3}")
univers_mail=re.findall(univers,file)




print(f"Total amount of phone numbers: {total_num}")

print(f"Total amount of phone numbers with ending 7: {num_end_7}")






def give_mail():
    giv=input("Нажмите Y что бы вывести net и сом адреса, нажмите N что бы вывести все адреса>>")
    if giv=="Y":
        print(mail_com_net)
    if giv=="N":
        print(univers_mail)


=======
import  re
file1=open("src\data_corey.txt ","r")
file=file1.read()
file1.close()
reg = re.compile ("(\d{3}\D{0,3}\d{3}\D{0,3}\d{4})")
found = re.findall(reg,file)




"""ПОИСК ЗНАЧЕНИИ НА ОКОНЧАНИЕ 7  """


num_end=re.findall("(\d{3}\D{0,3}\d{3}\D{0,3}[0-9][0-9][0-9][7])", file)
num_end_7=len(num_end)
total_num=len(found)



"""КОНКРЕТНО ДЛЯ ЭТОЙ ЗАДАЧИ"""
reg1=re.compile("([a-zA-Z]+@[a-zA-Z]+.(com|net))")

mail_com_net=re.findall(reg1,file)


"""КОЛИЧЕСТВО COM И MAIL"""

total_mail_com=len(mail_com_net)


"""УНИВЕРСАЛЬНЫЙ ШАБЛОН"""
univers=re.compile("\w+@\w+.\w{3}")
univers_mail=re.findall(univers,file)




print(f"Total amount of phone numbers: {total_num}")

print(f"Total amount of phone numbers with ending 7: {num_end_7}")






def give_mail():
    giv=input("Нажмите Y что бы вывести net и сом адреса, нажмите N что бы вывести все адреса>>")
    if giv=="Y":
        print(mail_com_net)
    if giv=="N":
        print(univers_mail)


>>>>>>> 1594e7a785b138a7ca803f3c3ecd0ddf8091fb62
give_mail()