# m6-backen-python
# Bank 

Aplicação que interpreta arquivos .txt com informações financeiras (CNAB)

## Tecnologias utilizadas:

<ul>
    <li>Python</li>
    <li>Django</li>
    <li>Django Rest Framework</li>
</ul>

## Instruções para rodar localmente

### Requisito:

<ul>
    <li>Python</li>
</ul>

### Crie o ambiente virtual em seu terminal

```
python -m venv venv
```

### Inicie o ambiente virtual

#### Windows

###### Abra o PowerShell

```
.\venv\Scripts\activate
```

#### Linux

```
source venv/bin/activate
```

### Instale as dependências

```
pip install -r requirements.txt
```

### Execute as migrações

```
python manage.py migrate
```

### Inicie o servidor

```
python manage.py runserver
```

#### Para acessar a API coloque o end point

```
/api/cnab/
```
