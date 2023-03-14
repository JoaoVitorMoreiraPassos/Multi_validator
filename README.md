
# Multivalidator

Um validador e gerador para os seguintes parâmetros:

- Bank Card
- CNPJ
- CPF
- Date
- Email
- FoneNumber
- PassPort
- PassWord
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

1. Importanto biblioteca
```python
  import validator as vlt
```
**read**
```python
  # read: Retorna um objeto iterável que contém o parâmetro escolhido
  # Exemplo:
  cpf = vlt.cpf.read("06906496301")
  cnpj = vlt.cnpj.read("92.639.324/0001-92")
  date = vlt.date.read("08-04-2021")
  email = vlt.email.read("moreirapassosj@gmail.com")
  fone = vlt.fone_number.read("11999999999")
  passport = vlt.passport.read("AB1234567")
  password = vlt.password.read("123456789")
```
**generate**
```python
  # Gera um cpf válido e adiciona-o no objeto iterável
  cpf.generate()
  # Saida: ['069.064.963-01', '262.848.575-35']
  # Aviso: Alguns geradores necessitam de parâmetros na sua chamada(Consulte a documentação)
```

**validate**
```python
  # Retorna uma tupla com um valor booleano indicando se é valido, e o cpf formatado
  cpf.validate('06906496301')
  #Saída: (True, '069.064.963-01')
```

**add**
```python
  # Adiciona um cpf no objeto iterável existente.
  cpf.add('06906496301')
  #Saída: ['069.064.963-01', '262.848.575-35', '171.414.230-28']
```