import re
import random
from collections.abc import Sequence


class Email(Sequence):
    def __init__(self, cpf = None):
        if cpf is None:
            self._emails = {}
            self._index = 0
        else:
            try:
                request = self.validate(cpf)
            except:
                raise ValueError("Formato inválido")
            self._emails = {0: request[1]}
            self._index = 1
        self._next_index = 0
        
        
    @property
    def emails(self):
        return self._emails
    
    @emails.setter
    def emails(self, args):
        try:
            email = self.validate(args)[1]
        except ValueError:
            raise ValueError("Formato inválido")
        else:
            self._emails[self._index] = email
            self._index += 1
    
    def __repr__(self):
        if len(self._emails) > 1:
            return f"Emails: {list(map(lambda x: f'{x}', self.emails.values()))}"
        if len(self.emails) == 1:
            return f"Email: {self._emails[0]}"
        return f"Emails: {self._emails}"
    
    def __len__(self):
        return len(self._emails)
    
    def __getitem__(self, index):
        if index >= len(self._emails):
            raise IndexError
        return self._emails[index]
    
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration
        self._next_index += 1
        return self._emails[self._next_index - 1]
        
    def add(self, email):
        try:
            self.emails = email
        except ValueError:
            raise ValueError("Formato inválido")
    
    def generate(self, first_name, last_name):
        """
        Função que gera um email aleatório e retorna o mesmo.
                Parâmetros:
                        first_name (str): Nome do usuário.
                        last_name (str): Sobrenome do usuário.
                Retorno:
                        str: Email aleatório.
        """

        numeros_aleatorios = "".join([str(random.randint(0, 9)) for _ in range(4)])
        email = first_name.lower() + "." + last_name.lower() + numeros_aleatorios + "@gmail.com"
        self.add(email)
        return email
        
    def validate(self, email):
        # Verificação básica
        if '@' not in email or '.' not in email.split('@')[1]:
            raise ValueError("Formato inválido")
        
        # Verificação de sintaxe
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise ValueError("Formato inválido")
                
        return True, email


def read(email : str) -> Email:
    try:
        obj = Email(email)  
        return obj
    except ValueError:
        raise ValueError("Formato inválido")



    