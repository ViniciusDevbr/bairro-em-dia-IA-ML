# IA & Machine Learning

## Objetivo
Classificar se uma solicitação urbana encerrada ultrapassou um prazo de referência. A saída é uma probabilidade de atraso, não uma promessa de data de atendimento.

## Fonte pública
Conjunto Dados do SP156 — Prefeitura de São Paulo:
- Portal: https://dados.prefeitura.sp.gov.br/dataset/dados-do-sp156
- API: https://apilib.prefeitura.sp.gov.br/store/apis/info?name=SP156&provider=admin&version=v1
- Endpoint documentado: `GET /solicitacoes/{ano}/{semestre}`.
Consulte `../dados/README.md` e o dicionário antes de definir o mapeamento das colunas.

## Como executar
1. Baixe os dados públicos e coloque uma amostra CSV em `../dados/solicitacoes_sp156.csv`.
2. Abra `notebook.ipynb`.
3. Inspecione `df.columns` e preencha o dicionário `COLUNAS` com os nomes existentes no arquivo.
4. Ajuste `PRAZO_REFERENCIA_DIAS` de acordo com a distribuição e justifique no relatório.
5. Execute todas as células em ordem.
6. O notebook salva o pipeline em `ml/model/random_forest.joblib`.

O notebook interrompe a execução com mensagem explicativa se o CSV ou as colunas essenciais não estiverem disponíveis. Isso evita publicar métricas inventadas.

## Modelo
RandomForestClassifier em pipeline com OneHotEncoder. GridSearchCV usa 5 folds no treino, com pelo menos 10 combinações de três hiperparâmetros. O teste final é reservado até a avaliação final.

## Integração
Após treinar e gerar `model/random_forest.joblib`, reinicie o serviço ML. `POST /predict` recebe categoria, região, mês, dia da semana e canal.
