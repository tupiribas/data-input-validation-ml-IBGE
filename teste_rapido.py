from src.data.validador import MunicipioIBGE
from pydantic import ValidationError

# Exemplo com o dado valido
try:
    municipio = MunicipioIBGE(
        codigo_municipio=2927408,
        nome_municipio='Salvador',
        populacao=259000000
    )
    print('Dados validados com Sucesso!!')
except ValidationError as err:
    print('Erro na validação dos dados: ERROR VALIDAÇÃO DADOS 001:', err)

# Exemplo com o dado INVALIDO (população)
try:
    municipio = MunicipioIBGE(
        codigo_municipio=2927408,
        nome_municipio='Salvador',
        populacao=-259000000
    )
except ValidationError as err:
    print('Erro na validação dos dados: ERROR VALIDAÇÃO DADOS 002:', err)
