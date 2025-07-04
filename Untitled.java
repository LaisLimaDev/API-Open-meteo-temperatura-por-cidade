O problema está no nome do arquivo de inicialização do pacote de testes:  
Você criou _init_.py, mas o correto é `__init__.py` (com dois underlines antes e depois).

### Como corrigir

1. **Renomeie o arquivo:**
```bash
mv tests/_init_.py tests/__init__.py
```

2. **Garanta que o arquivo `test_core.py` não está vazio.**  
Seu arquivo `test_core.py` está com tamanho 0, ou seja, está vazio.  
Abra o arquivo e coloque o conteúdo dos testes novamente, por exemplo:
````python
from meteo.core import get_lat_lon, get_temperature

def test_get_lat_lon():
    lat, lon = get_lat_lon("Campinas")
    assert lat is not None and lon is not None

def test_get_temperature():
    lat, lon = get_lat_lon("Campinas")
    temp = get_temperature(lat, lon)
    assert temp is not None
````

3. **Execute novamente:**
```bash
pytest
```

Agora o pytest deve encontrar e rodar seus testes normalmente!