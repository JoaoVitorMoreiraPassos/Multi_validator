import validator.cpf as cpf
import validator.cnpj as cnpj
import validator.cep as cep
import validator.bank_card as bank_card
import validator.date as date
import validator.email as email
import validator.fone_number as fone_number
import validator.passport as passport
import validator.password as password
import validator.url as url
from collections.abc import Sequence

class FakeData(Sequence):
    def __init__(self, quantity = 1):
        self._quantity = quantity
        self._cpf = cpf.CPF()
        self._cnpj = cnpj.CNPJ()
        self._cep = cep.CEP()
        self._bank_card = bank_card.CreditCard()
        self._date = date.Date()
        self._email = email.Email()
        self._fone_number = fone_number.TelPhone()
        self._passport = passport.PassPort()
        self._password = password.PassWord()
        self._url = url.URL()
        self._datas = {}
        self._index = 0
        for i in range(quantity):
            self._datas[self._index] = {
                "cpf": self._cpf.generate(),
                "cnpj": self._cnpj.generate(),
                "bank_card": self._bank_card.generate(),
                # "email": self._email.generate(),
                "passport": self._passport.generate(),
                "password": self._password.generate(3),
                # "url": self._url.generate(),
            }
            self._index += 1
        self._next_index = 0
    
    @property
    def datas(self):
        return self._datas
    
    def __repr__(self):
        if len(self.datas) > 1:
            buffer = ""
            for i in self.datas.values():
                buffer += "\t" + str(i) + "\n"
            return f"""Fakes: {buffer}"""
        if len(self.datas) == 1:
            return f"Fake:\n{self.datas}"
        return f"Fakes: {self.datas}"
    
    def __len__(self):
        return len(self.datas)
    
    def __getitem__(self, index):
        if index >= len(self.datas):
            raise IndexError
        return self.datas[index]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration
        self._next_index += 1
        return self.datas[self._next_index - 1]
    
    def add(self, quantity=1):
        for i in range(quantity):
            self._datas[self._index] = {
                "cpf": self._cpf.generate(),
                "cnpj": self._cnpj.generate(),
                "bank_card": self._bank_card.generate(),
                # "email": self._email.generate(),
                "passport": self._passport.generate(),
                "password": self._password.generate(3),
                # "url": self._url.generate(),
            }
            self._index += 1