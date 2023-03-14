
# Multivalidator

Um validador e gerador para os seguintes parâmetros:

- Bank Card
- CNPJ
- CPF
- Date
- Email
- Fone Number
- Passaport
- Password
- Url


## Instalação


```bash
  pip install multivalidator
```
2. Ativando o ambiente virtual:
```bash
  . venv/bin/activate  
```
## Exemplos

1. Gera 10 dados
```python
  import validator as vlt

  # Retorna um dicionário com o parametro escolhido e validado
  cpf = vlt.cpf.CPF("06906496301")
  cnpj = vlt.cnpj.CNPJ()
  date = vlt.date.Date("08-04-2021")
  email = vlt.email.Email("moreirapassosj@gmail.com")
  fone = vlt.fone_number.TelPhone("11999999999")
  passport = vlt.passport.PassPort("AB1234567")
  password = vlt.password.PassWord("123456789")


  # As funções validade e generate funcionam para todos os parâmetros
  cpf.generate()
  cpf.validade('40028922')
```
