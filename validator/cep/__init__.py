import re
import pycep_correios
import requests
from collections.abc import Sequence


class CEP(Sequence):
    def __init__(self, cep = None):
        if cep is None:
            self._ceps = {}
            self._index = 0
        else:
            try:
                request = self.validate(cep)
            except Exception as e:
                print(e)
                raise Exception(e)
            else:
                self._ceps = {0: request[1]}
                self._index = 1
        self._next_index = 0
        
        
    @property
    def ceps(self):
        return self._ceps
    
    @ceps.setter
    def ceps(self, args):
        try:
            cep = self.validate(args)[1]
        except Exception as e:
            print(e)
            raise Exception(e)
        else:
            self._ceps[self._index] = cep
            self._index += 1
    
    def __repr__(self):
        if len(self.ceps) > 1:
            return f"{list(map(lambda x: f'CEP: {x}', self.ceps.values()))}"
        if len(self.ceps) == 1:
            return f"CEP: {self.ceps[0]}"
        return f"CEP: {self.ceps}"
    
    def __len__(self):
        return len(self.ceps)
    
    def __getitem__(self, index):
        if index >= len(self.ceps):
            raise IndexError
        return self.ceps[index]
    
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration
        self._next_index += 1
        return self.ceps[self._next_index - 1]
    
    def add(self, cep):
        try:
            self.ceps = cep
        except Exception as e:
            print(e)
            raise Exception(e)
    
    def validate(self, cep):
        # Verifica se o CEP possui 8 dígitos numéricos
        if re.match(r'^\d{8}$', cep):
            # Consulta o serviço dos Correios para verificar se o CEP é válido
            # (substitua a URL pela API dos Correios)
            url = f'https://viacep.com.br/ws/{cep}/json/'
            resposta = requests.get(url)
            if resposta.status_code == 200:
                dados = resposta.json()
                # Verifica se o CEP está dentro do intervalo de CEPs válidos para a cidade ou região
                if 'erro' not in dados:
                    return (True, dados)
        raise Exception('CEP inválido')


def read(cep : str):
    try:
        obj = CEP(cep)  
        return obj
    except Exception as e:
        print(e)
        raise Exception(e)
    
if __name__ == "__main__":
    cep = CEP("64930000")
    all_ceps = pycep_correios