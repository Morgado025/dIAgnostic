# Treinamento de Modelo para Detecção de Pneumonia e Predição de Diabetes

> **NOTA IMPORTANTE**: O modelo de detecção de pneumonia ainda está em fase experimental e apresenta limitações significativas na detecção precisa. Identificamos falhas que estão sendo analisadas e corrigidas. Atualmente, ele serve como base para estabelecer o fluxo do projeto. Novas versões aprimoradas, com agentes inteligentes e modelos de maior acurácia, serão disponibilizadas em breve.

## Visão Geral

Este repositório contém dois modelos distintos desenvolvidos com foco na área da saúde:

1. **Detecção de Pneumonia**: Classificação de imagens de raio-X em `NORMAL` ou `PNEUMONIA`
2. **Predição de Diabetes**: Classificação de pacientes quanto à presença ou ausência de diabetes, com base em características clínicas

---

## 1. Detecção de Pneumonia

### Dataset

Utiliza o conjunto de dados ["Chest X-Ray Images (Pneumonia)"](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia), contendo imagens divididas em pastas de treino, teste e validação, nas classes `NORMAL` e `PNEUMONIA`.

### Notebook

O notebook `pneumonia.ipynb` abrange:

1. Importação de bibliotecas  
2. Carregamento e pré-processamento das imagens  
3. Visualização de dados  
4. Aumento de dados (Data Augmentation)  
5. Definição da arquitetura da CNN  
6. Treinamento e avaliação  
7. Salvamento do modelo `.h5`  
8. Testes de inferência  

### Arquitetura

- CNN com 5 blocos convolucionais  
- Dropout (0.1–0.2) para regularização  
- Ativação final: sigmoid  
- Otimizador: RMSprop  
- Perda: Binary Crossentropy  

### Resultados e Uso

- Avaliação por acurácia, matriz de confusão, F1-score  
- Pode ser usado para inferência em imagens novas com `pneumonia_detection_model.h5`

---

## 2. Predição de Diabetes

### Dataset

O modelo utiliza o dataset [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database/data), que contém dados clínicos como:

- Número de gestações  
- Glicose  
- Pressão arterial  
- Espessura da pele  
- Insulina  
- Índice de massa corporal (IMC)  
- Função do histórico familiar de diabetes  
- Idade  

### Notebooks e Arquivos

- `diabetes.ipynb`: Notebook com o pipeline completo de treinamento, avaliação e predição.
- `diabetes_model.sav`: Modelo treinado salvo em formato pickle.
- `diabetes_scaler.sav`: Escalador de dados utilizado no pré-processamento, necessário para normalizar os dados antes da predição.

### Etapas

1. Carregamento do dataset e análise exploratória  
2. Limpeza e normalização dos dados  
3. Treinamento de modelos de classificação (ex.: Logistic Regression, Random Forest, etc.)  
4. Avaliação de métricas: acurácia, matriz de confusão, classificação  
5. Exportação do modelo (`diabetes_model.sav`) e do scaler (`diabetes_scaler.sav`)  
6. Testes de predição com novos dados utilizando os arquivos salvos

### Objetivo

Classificar pacientes com base em suas características para prever a probabilidade de terem diabetes.

---

## Requisitos para Execução

- Python 3.6+  
- Jupyter Notebook  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib, Seaborn  
- TensorFlow e Keras (para o modelo de pneumonia)  
- OpenCV (cv2)  

---

## Como Executar

1. Baixe os datasets:
   - Pneumonia: "Chest X-Ray Images (Pneumonia)"
   - Diabetes: "Pima Indians Diabetes Database"
2. Ajuste os caminhos no(s) notebook(s)
3. Execute cada célula do notebook para treinar os modelos
4. Utilize os modelos salvos (`pneumonia_detection_model.h5`, `diabetes_model.sav`, `diabetes_scaler.sav`) para predições

---

## Próximos Passos

- Melhorias no modelo de pneumonia (precisão e interpretabilidade)  
- Combinar o modelo com uma LLM para respostas de recomendações e não de diagnosticos
- Dashboard interativo para entrada de dados e exibição de predições  
- Deploy em app móvel  

---

## Referências

- [Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)  
- [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database/data)