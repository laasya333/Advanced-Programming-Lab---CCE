#appends to a file containing emails, reads that file,
#validates the emails and writes the validated emails to another new created file
import re

def validate_email(mail):
    pattern=r'^[a-z]{2,}[a-z0-9._]*@[a-z]+\.[a-z]{2,}$'
    if re.match(pattern,mail):
        return True
    else:
        return False
    
f = open("email.txt",'r+',encoding='utf-8')
print("write new emails to file or write end to stop")
con=f.read()
f.seek(len(con))
f.write('\n')
while True:
    mail=input("- ")
    if(mail=="end"):
        print("ended writing!")
        break
    f.write(mail+'\n')    
f.close()
f = open("email.txt",'r',encoding='utf-8')
fvalid=open("validemails.txt",'a', encoding='utf-8')
lines=f.readlines()

for line in lines:
    line.strip()
    if(validate_email(line)):
       fvalid.write(line)
       print("validated and written!")

f.close()
fvalid.close()
