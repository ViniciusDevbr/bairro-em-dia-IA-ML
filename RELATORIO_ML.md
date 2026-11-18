# Relatório de Inteligência Artificial & Machine Learning — Bairro em Dia

## 1. Problema e pergunta de ML
O Bairro em Dia permite que moradores registrem e acompanhem problemas em espaços públicos. O módulo de ML investiga: **com base nas características disponíveis no momento do registro, é possível estimar a probabilidade de uma solicitação urbana ultrapassar um prazo de referência para resolução?**

A previsão pode ajudar a comunicar risco e apoiar a priorização, mas não substitui a decisão do órgão público e não garante prazo.

## 2. Dados e preparação
Fonte planejada: conjunto público Dados do SP156, da Prefeitura de São Paulo (SMIT). Portal: https://dados.prefeitura.sp.gov.br/dataset/dados-do-sp156. API documentada: https://apilib.prefeitura.sp.gov.br/store/apis/info?name=SP156&provider=admin&version=v1.

**Preencher após baixar e inspecionar o arquivo:** nome exato do recurso, período, data de extração, quantidade de registros, colunas e licença/termos. A presença e a qualidade das datas de abertura/encerramento devem ser verificadas antes de criar o alvo.

Foram consideradas como variáveis candidatas categoria/assunto, região, mês, dia da semana e canal. Campos disponíveis apenas após o encerramento não devem entrar como preditores, para evitar vazamento de informação. Registros sem datas necessárias e duplicados são tratados conforme documentado no notebook.

O alvo binário é `atrasou`: diferença entre encerramento e abertura superior ao prazo de referência escolhido após análise exploratória. O valor do prazo deve ser justificado com a distribuição e/ou referência operacional, não escolhido para forçar resultado. A base é dividida em treino e teste estratificado. Codificação categórica ocorre dentro de Pipeline/ColumnTransformer para evitar vazamento na validação cruzada.

## 3. Modelo e treinamento
Foi escolhido Random Forest por lidar bem com dados tabulares e relações não lineares, sem exigir padronização das variáveis numéricas. O treinamento compara combinações de `n_estimators`, `max_depth` e `min_samples_leaf`, com GridSearchCV e validação cruzada aplicada somente ao conjunto de treino. Um baseline deve ser comparado ao modelo.

## 4. Resultados
**Preencher somente após executar o notebook com os dados reais.**

| Métrica | Treino | Teste |
|---|---:|---:|
| Accuracy | — | — |
| Precision | — | — |
| Recall | — | — |
| F1 | — | — |
| ROC-AUC | — | — |

Inserir matriz de confusão, curva ROC, importância de variáveis e comparação de desempenho de treino/validação. Discutir diferença entre treino e teste. Diferença muito grande sugere overfitting; resultados próximos, em conjunto com validação cruzada, indicam melhor generalização, mas não garantem desempenho em outros bairros/períodos.

## 5. Conclusão para o cidadão
Quando validado, o modelo poderá informar se uma ocorrência apresenta maior ou menor risco histórico de ultrapassar o prazo de referência. Isso pode melhorar a transparência e ajudar a equipe a identificar padrões. A previsão depende da representatividade dos dados históricos, pode reproduzir desigualdades de registro/atendimento e deve ser apresentada como estimativa, não como promessa. Se os dados não tiverem datas confiáveis de encerramento, a pergunta de ML deverá ser reformulada antes de reportar métricas.
