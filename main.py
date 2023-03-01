import validator as vlt


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

credit_card = vlt.bank_card.read("5502099573557190")
print(credit_card)
credit_card.generate()
credit_card.generate()
credit_card.generate()
for i in credit_card:
    print(i)