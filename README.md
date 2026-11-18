# Bairro em Dia — Inteligência Artificial e Machine Learning

## 1. Descrição do projeto

O **Bairro em Dia** é uma solução CitizenTech voltada ao registro e acompanhamento de problemas urbanos, como iluminação pública danificada, descarte irregular de lixo, buracos nas vias e problemas em calçadas.

Este repositório contém exclusivamente o desenvolvimento da parte de Inteligência Artificial e Machine Learning do projeto.

A proposta é estudar dados públicos de solicitações urbanas e desenvolver um modelo capaz de estimar o risco de uma solicitação ultrapassar um prazo de referência para resolução.

## 2. Problema escolhido

A demora na resolução de problemas urbanos pode prejudicar a qualidade de vida da população.

A utilização de Machine Learning pode ajudar a identificar padrões presentes nas solicitações e estimar quais registros apresentam maior risco de demora.

### Pergunta de Machine Learning

**É possível estimar a probabilidade de uma solicitação de serviço urbano ultrapassar um prazo de referência para resolução utilizando apenas informações disponíveis no momento de sua abertura?**

## 3. Fonte de dados

A fonte de dados planejada é o conjunto público de solicitações de serviços da Prefeitura de São Paulo, relacionado ao SP156.

Portal de referência:

https://www.prefeitura.sp.gov.br/web/gestao/w/acesso_a_informacao/310875

A base deverá ser obtida em fonte oficial, acompanhada da identificação do conjunto de dados, período analisado, data de download e licença ou condições de uso.

As informações exatas da base utilizada, como quantidade de registros, período e colunas disponíveis, devem ser preenchidas após o download e a inspeção do arquivo real.

**Importante:** não utilizar dados sintéticos como se fossem dados reais.

## 4. Objetivo do modelo

O objetivo é desenvolver um modelo de classificação utilizando Random Forest.

O modelo deverá estimar se uma solicitação apresenta risco de ultrapassar o prazo de referência definido para sua resolução.

A variável-alvo será construída a partir das datas de abertura e finalização, quando essas informações estiverem disponíveis na base.

Somente informações conhecidas no momento da abertura poderão ser utilizadas como variáveis preditoras.

Informações posteriores à abertura, como resultado da solicitação ou data de finalização, não devem ser utilizadas como variáveis de entrada do modelo.

## 5. Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python 3.11 | Linguagem de programação |
| Pandas | Manipulação de dados |
| Scikit-learn | Treinamento e avaliação do modelo |
| NumPy | Operações numéricas |
| Matplotlib | Visualização de dados |
| Seaborn | Gráficos estatísticos |
| Joblib | Persistência do modelo treinado |
| Jupyter Notebook | Desenvolvimento e experimentação |
| FastAPI | Disponibilização opcional de previsões |

## 6. Etapas do desenvolvimento

### 6.1 Coleta dos dados

Obter a base pública de solicitações urbanas do SP156.

Registrar a origem, o endereço de acesso, o período dos dados e a data de download.

### 6.2 Análise exploratória

Realizar uma análise inicial para identificar:

- Quantidade de registros.
- Colunas disponíveis.
- Tipos de dados.
- Valores ausentes.
- Registros duplicados.
- Distribuição das categorias.
- Distribuição dos tempos de resolução.

### 6.3 Preparação dos dados

Realizar o tratamento necessário para preparar a base para o treinamento:

- Limpeza de registros inválidos.
- Tratamento de valores ausentes.
- Conversão de tipos de dados.
- Codificação de variáveis categóricas.
- Construção da variável-alvo.
- Separação entre variáveis preditoras e variável-alvo.

### 6.4 Separação dos dados

Separar os dados em conjuntos de treinamento e teste.

A validação cruzada e a seleção de hiperparâmetros devem utilizar exclusivamente o conjunto de treinamento.

O conjunto de teste deve ser reservado para a avaliação final.

### 6.5 Treinamento do modelo

O algoritmo selecionado é o Random Forest Classifier.

O desenvolvimento deverá testar pelo menos 10 combinações de hiperparâmetros, considerando no mínimo três parâmetros, como:

- `n_estimators`
- `max_depth`
- `min_samples_leaf`

A seleção da melhor configuração deverá considerar os resultados obtidos na validação cruzada.

## 7. Avaliação do modelo

A avaliação deverá apresentar métricas de treinamento e teste lado a lado.

As métricas previstas são:

- Accuracy.
- Precision.
- Recall.
- F1-score.
- ROC-AUC.
- Matriz de confusão.

Também deverão ser apresentados gráficos que ajudem a interpretar os resultados, como:

- Comparação das métricas de treinamento e teste.
- Matriz de confusão.
- Curva ROC.
- Importância das variáveis.

A análise deverá discutir possíveis sinais de overfitting e a capacidade de generalização do modelo.

**Os resultados numéricos devem ser preenchidos somente após a execução real do notebook com a base selecionada.**

## 8. Estrutura do projeto

```text
bairro-em-dia-ia-ml/
├── ml/
│   ├── app.py
│   ├── Dockerfile
│   ├── notebook.ipynb
│   ├── README.md
│   └── requirements.txt
├── dados/
│   └── README.md
├── RELATORIO_ML.md
└── README.md
```

## 9. Como executar o projeto

### Pré-requisitos

- Python 3.11.
- Pip.
- Jupyter Lab ou Jupyter Notebook.

### Criar ambiente virtual

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Instalar dependências

```bash
pip install -r ml/requirements.txt
```

### Preparar a base de dados

Coloque o CSV obtido na fonte oficial dentro da pasta `dados`, utilizando o nome:

```text
dados/solicitacoes_sp156.csv
```

Consulte `dados/README.md` para as orientações de obtenção e documentação da base.

### Executar o notebook

```bash
jupyter lab ml/notebook.ipynb
```

Execute as células na ordem apresentada e verifique se os nomes das colunas correspondem aos dados reais.

## 10. Serviço opcional de previsão

O projeto também prevê a possibilidade de disponibilizar o modelo treinado por meio de uma API Python com FastAPI.

O arquivo `ml/app.py` contém a implementação desse serviço.

A API de previsão depende da existência de um modelo treinado e salvo corretamente.

Enquanto o artefato do modelo não estiver disponível, o serviço poderá retornar HTTP 503 para solicitações de previsão.

A documentação da API FastAPI, quando o serviço estiver disponível, poderá ser acessada em:

`http://localhost:8000/docs`

## 11. Relatório acadêmico

O arquivo `RELATORIO_ML.md` reúne a documentação do desenvolvimento, incluindo:

- Problema selecionado.
- Pergunta de Machine Learning.
- Fonte e período dos dados.
- Preparação da base.
- Algoritmo escolhido.
- Combinações de hiperparâmetros.
- Métricas de treinamento e teste.
- Gráficos e análise de resultados.
- Discussão sobre overfitting.
- Conclusão voltada ao cidadão.

O relatório deverá ser atualizado com os resultados reais obtidos durante a execução do notebook.

## 12. Integrantes

- Vinicius Henrique — RM556908
- Gustavo Pierre — RM558928
- Gabriel Belo — RM551669
- Laura Souza — RM556320

## 13. Considerações finais

A proposta de Machine Learning busca utilizar dados públicos para estudar padrões de solicitações urbanas e estimar riscos de demora na resolução de problemas.

O resultado poderá contribuir para uma melhor compreensão das demandas da população e apoiar a identificação de solicitações que merecem maior atenção.

As previsões devem ser interpretadas como estimativas estatísticas, e não como garantias de prazo de atendimento.

Este repositório corresponde exclusivamente à disciplina de **Inteligência Artificial e Machine Learning**. A implementação do backend Java e do banco de dados da aplicação pertence a outro repositório.