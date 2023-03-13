import validator as vlt


fake = vlt.FakeData(10)
print(fake)

cpf = vlt.cpf.read("06906496301")
print(cpf)
cpf.generate()
cpf.generate()
cpf.generate()

for i in cpf:
    print(i)
    
print("------------------")
    
cnpj = vlt.cnpj.CNPJ()
print(cnpj)
cnpj.generate()
cnpj.generate()
cnpj.generate()
for i in cnpj:
    print(i)
    
print("------------------")

date = vlt.date.Date("08-04-2021")
print(date)

print("------------------")

email = vlt.email.Email("moreirapassosj@gmail.com")
print(email)
print("------------------")

fone = vlt.fone_number.TelPhone("11999999999")
print(fone)

print("------------------")

passport = vlt.passport.PassPort("AB1234567")
print(passport)

print("------------------")
password = vlt.password.PassWord("123456789")
password.generate(level=3)
print( password )
print("------------------")
url = vlt.url.URL("https://www.google.com")
url.generate("google", 10)
print(url)