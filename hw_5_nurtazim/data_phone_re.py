
import  re
file1=open("src/data_phone.json", "r")
file=file1.read()
file1.close()

reg = re.compile ("(\d{13})")

found = re.findall(reg,file)
total_phone=len(found)



reg1= re.findall("[(][0-6][0-9][0-9][)][ ]?[\d]{3}-[\d]{4}", file)




(print(f"Total amount of phone numbers with 13 digits: {total_phone}"))

print(reg1)



import  re
file1=open("src/data_phone.json", "r")
file=file1.read()
file1.close()

reg = re.compile ("(\d{13})")

found = re.findall(reg,file)
total_phone=len(found)



reg1= re.findall("[(][0-6][0-9][0-9][)][ ]?[\d]{3}-[\d]{4}", file)



(print(f"Total amount of phone numbers with 13 digits: {total_phone}"))

print(reg1)


