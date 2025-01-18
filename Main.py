Penup_servoval = 'S70'
Pendown_servoval = 'S120'
Filelocation = r"C:\Users\Lek\Downloads\CAIS building.gc"

with open(Filelocation,"r+") as File:
    content = File.read()
    newcontent = content.replace('M3', f'M3 {Pendown_servoval}')
    newcontent = newcontent.replace('M5', f'M3 {Penup_servoval}')

with open(Filelocation,"a") as File:
    File.truncate(0)

with open(Filelocation,"w") as File:
    File.write(newcontent)

File.close
print("Rewrite success!")