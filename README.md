# Eventex

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/luizolimpio/wttd.svg?branch=master)](https://travis-ci.org/luizolimpio/wttd)

## Como desenvolver?

1. Clone o repositório
2. Crie um virtualenv.
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

os-Win7
```console
git clone git@github.com:luizolimpio/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd\Scripts\Activate.bat
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test

```
## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku

```console
heroku create minhainstancia 
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBUG=False
#configuro o email
git push heroku master --force
```



 