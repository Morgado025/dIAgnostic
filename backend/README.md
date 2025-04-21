# dIAgnostic API

Uma API REST construída com FastAPI para diagnóstico médico, incluindo **detecção de pneumonia** a partir de imagens de raio-X e **predição de diabetes** a partir de dados clínicos. 

## 🧠 Visão Geral

Esta API permite:

- Enviar uma imagem de raio-X do tórax e obter um diagnóstico de **pneumonia** ou **normal**.
- Enviar dados clínicos para obter um diagnóstico de **diabetes positivo** ou **negativo**.

## 🚀 Funcionalidades

- 📷 Detecção de Pneumonia via imagem de raio-X
- 💉 Predição de Diabetes via dados clínicos
- ✅ Verificação de saúde da API e dos modelos carregados
- 🌐 Documentação interativa automática com Swagger e ReDoc

## 🧰 Tecnologias e Requisitos

- Python 3.8+
- [FastAPI](https://fastapi.tiangolo.com/)
- Uvicorn
- TensorFlow
- OpenCV
- NumPy
- Scikit-learn (para modelo de diabetes)

## 📦 Instalação

1. Clone este repositório:

```bash
git clone https://github.com/mariafernandarsantos/dIAgnostic.git
cd dIAgnostic/backend
```

2. (Opcional) Crie e ative um ambiente virtual:
```bash
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

3. Instale as dependências do projeto
```bash
pip install -r requirements.txt
```

4. Certifique-se de ter os arquivos de modelo:

`pneumonia_detection_model.h5`

`diabetes_model.sav`

`diabetes_scaler.sav`

Esses arquivos devem estar no diretório raiz do backend. Se desejar treinar os modelos, consulte os notebooks de treinamento disponíveis no repositório.


## Uso

### Iniciando a API

Execute o seguinte comando no diretório do projeto:

```bash
uvicorn main:app --reload
# ou
python main.py
```

A API estará disponível em `http://localhost:8000`

### Endpoints da API

`GET | /`: Mensagem de boas-vindas e descrição da API
`GET | /health`: Verifica se a API e os modelos estão ativos
`POST | /predict/pneumonia`: Envia uma imagem para diagnóstico
`POST | /predict/diabetes`: Envia dados clínicos para diagnóstico

### Predição de Pneumonia

Você pode usar cURL para testar a API:

```bash
curl -X POST -F "file=@caminho/para/sua/imagem.jpg" http://localhost:8000/predict/pneumonia
```

Ou usar qualquer cliente HTTP como Postman, ou o seguinte código Python:

```python
import requests

url = "http://localhost:8000/predict/pneumonia"
imagem = "caminho/para/sua/imagem.jpg"

with open(imagem, "rb") as f:
    response = requests.post(url, files={"file": f})

print(response.json())
```

### Formato da Resposta

A API retorna uma resposta JSON com a seguinte estrutura:

```json
{
  "filename": "exemplo.jpg",
  "diagnosis": "PNEUMONIA",
  "confidence": 0.9527,
  "raw_prediction": 0.9527
}
```

- `filename`: O nome do arquivo enviado
- `diagnosis`: "PNEUMONIA" ou "NORMAL"
- `confidence`: O nível de confiança (0-1) para a predição
- `raw_prediction`: A saída bruta do modelo

### Predição de Diabetes

Corpo da requisição (JSON):
```json
{
  "pregnancies": 2,
  "glucose": 130,
  "blood_pressure": 80,
  "skin_thickness": 25,
  "insulin": 100,
  "bmi": 28.5,
  "diabetes_pedigree": 0.3,
  "age": 40
}
```
cURL:
```bash
curl -X POST http://localhost:8000/predict/diabetes \
     -H "Content-Type: application/json" \
     -d @dados.json
```

Python:
```python
import requests

url = "http://localhost:8000/predict/diabetes"
data = {
    "pregnancies": 2,
    "glucose": 130,
    "blood_pressure": 80,
    "skin_thickness": 25,
    "insulin": 100,
    "bmi": 28.5,
    "diabetes_pedigree": 0.3,
    "age": 40
}
response = requests.post(url, json=data)
print(response.json())
```

Resposta esperada:
```json
{
  "diagnosis": "NEGATIVE",
  "probability": 0.1562,
  "message": "No diabetes detected"
}
```


## Documentação da API

O FastAPI gera automaticamente documentação interativa da API:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## TODO produção
1. Ajuste nas configurações CORS na seção `app.add_middleware`
2. Configure autenticação adequada
3. Use um servidor ASGI de nível de produção como Gunicorn com workers Uvicorn
4. Implante atrás de um proxy reverso como Nginx
5. Use variáveis de ambiente para configuração
