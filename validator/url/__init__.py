import re
import random
import string
from collections.abc import Sequence


class URL(Sequence):
    def __init__(self, url = None):
        if url is None:
            self._urls = {}
            self._index = 0
        else:
            try:
                request = self.validate(url)
            except:
                raise ValueError("Formato inválido")
            self._urls = {0: request[1]}
            self._index = 1
        self._next_index = 0
        
        
    @property
    def urls(self):
        return self._urls
    
    @urls.setter
    def urls(self, args):
        try:
            url = self.validate(args)[1]
        except ValueError:
            raise ValueError("Formato inválido")
        else:
            self._urls[self._index] = url
            self._index += 1
    
    def __repr__(self):
        if len(self.urls) > 1:
            return f"URLs: {list(map(lambda x: f'{x}', self.urls.values()))}"
        if len(self.urls) == 1:
            return f"URL: {self.urls[0]}"
        return f"URLs: {self.urls}"
    
    def __len__(self):
        return len(self.urls)
    
    def __getitem__(self, index):
        if index >= len(self.urls):
            raise IndexError
        return self.urls[index]
    
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration
        self._next_index += 1
        return self.urls[self._next_index - 1]
        
    def add(self, url):
        try:
            self.urls = url
        except ValueError:
            raise ValueError("Formato inválido")
    
    def generate(self, name, random_lenght=0):
        """
        Função que gera uma URL aleatória e retorna a mesma.
                Parâmetros:
                        name (str): Nome do site.
                        random_lenght (int): Comprimento da parte aleatória da URL.
                
                Retorno:
                        str: URL aleatória.
        """

        caracteres = string.ascii_lowercase + string.digits
        parte_aleatoria = ''.join(random.choice(caracteres) for i in range(random_lenght))
        self.add(f"http://www.{name}.com/{parte_aleatoria}")
        return f"http://www.{name}.com/{parte_aleatoria}"
        
    def validate(self, url):
        """
        Função que valida uma URL e retorna True ou False.
                Parâmetros:
                        url (str): URL a ser validada.
                Retorno:
                        tuple: (True, url)
        """
        padrao = re.compile(r"^https?://(www\.)?\w+\.\w{2,3}(/\S*)?$")
        if padrao.match(url):
            return True, url
        else:
            raise ValueError("Formato inválido")

def read(url : str) -> URL:
    try:
        obj = URL(url)  
        return obj
    except ValueError:
        raise ValueError("Formato inválido")
