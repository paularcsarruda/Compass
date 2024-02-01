# Big Data Fundamentos 3.0 - DSA

## O que é Big Data?

O **Big Data** refere-se ao *conjunto de dados em grande volume, alta velocidade e com variedade de formatos*. Esses dados são analisados para obter insights e tomar decisões estratégicas. O Big Data é caracterizado pelo uso de tecnologias e ferramentas específicas para lidar com o volume e a complexidade dos dados.

## 4 V's do Big Data

- Volume de dados (tamanho dos dados)
- Variedade (formato dos sados): arquivos de audio, vídeo, txt…
- Velocidade (como os dados são gerados): post, vídeos…
- Veracidade (confiabilidade dos dados)

## Big Data e Ciência de Dados são a mesma coisa?

Não. Big Data é a matéria prima, os dados per se, gerados em alto volume, variedade, velocidade, e veracidade. Ciência de Dados é um conjunto de técnicas para análise de dados.

Entretanto eles podem ser relacionados, sendo chamado de Big Data Analytics.

## Sistemas de Armazenamento de Dados

### Volume

O primeiro dos v's (volume) é critico em Big Data, existe um custo para manter o armazenamento dos dados.

### Como Armazenamos os Dados

- Warehouse: quando os dados são estruturados ou podem ser estruturados antes do armazenamento;
- Data Lake ou Data Store: quando os dados NÃO são estruturados ou NÃO podem ser estruturados antes do armazenamento.

Dependendo do volume de dados a empresa não consegue estruturar antes do armazenamento, podendo usar ambos os armazenamentos.

### Bancos Relacionais e Não Relacionais

- BD Relacionais: são estruturados e com schema (bem definido e criado antes do armazenamento) bem definidos. São muito utilizados em portais de compra, de sistema RP ou CRM.
- BD NoSQL: dados semi ou não estruturados e outros tipos de relacionamentos entre os dados. BD NoSQL podem ser utilizados para construir Data Lakes e Data Store.

### O que é uma Warehouse?

- sistema de armazenamento que conecta e harmoniza grandes quantidades de dados de muitas fontes diferentes. Seu objetivo é alimentar a inteligência de negócios, relatórios e analises e oferecer suporte aos requisitos de negócio.
- armazena dados antigos e atuais em um único local e são adaptados para dados estruturados e não estruturados (e.g.: vídeos, imagens e sensores).

### Beneficios do DW

- Melhor Análise de Negócios
- Consultas mais rápido (pouco ou nenhum suporte de TI)
- Melhoria de Qualidade dos Dados

### O que é um Data Lake?

- é um repositório centralizado que permite armazenar todos os dados estruturados e não estruturados em qualquer escala.
- O principal desafio de uma arquitetura Data Lake é que os dados brutos são armazenados sem a supervisão de conteúdo. É necessário definir mecanismos para tornar os dados utilizaveis.

### Benefícios do DL

- Armazenamento em formato bruto, apesar que é possível armazenar os dados após uma limpeza ou transformação prévia
- Importação de qualquer quantidade de dados em Tempo real
- Repositório Central para todos os dados da empresa

### O que é um Data Store?

- é um repositório para armazenar e gerenciar de forma persistente coleções de dados que incluem não apenas dados estruturados, mas também tipos de armazenamento variado, como documentos, dados no formato de chave-valor, filas de mensagens e outros formatos de arquivo.

### Tipos mais comuns de DS

- Armazenamento de chave-valor
- Motor de Pequisa de texto completo
- Fila de mansagens
- Sistema de arquivos distribuídos

### Beneficios do DS

- Armazenamento de variados tipos de dados
- Flexibilidade
- Suporte a dados semi-estruturados
- Custo menor

## Sistema Híbrido de Armazenamento

Com o avanço do **Big Data** veremos cada vez mais sistemas híbridos de armazenamento, com dados armazenados em diferentes tipos de repositórios, local ou na nuvem.

## Armazenamento e Processamento Paralelo

## O que é um Servidor?

Um **servidor**(e.g.: portal da DSA) é um computador geralmente com alta capacidade computacional, que serve serviços de armazenamento, aplicações ou banco de dados.

o **servidor** possui *escalabilidade vertical*, ou seja, há um limite de espaço.

## O que é um Cluster?

Um **cluster** é um conjunto de servidores com o mesmo propósito, visando fornecer um tipo de serviço, como armazenamento ou processamento de dados. O **cluster** possui escalabilidade horizontal. Com ele aumentamos de forma considerável a capacidade computacional.

## O Armazenamento Paralelo

Consiste em *distribuir o armazenamento de dados através de diversos servidores* , o que permite aumentar de forma considerável a capacidade de armazenamento usando hardware de baixo custo.

## Software para o AP - Apache Hadoop

- Para que o hardware possa fazer o seu trabalho temos que ter uma **camada de software**, responsável por gerenciar o armazenamento.
- Sistema de arquivos distribuídos (e.g.: NTFS, ext3, …)

## Processamento Paralelo de Big Data

No processamento paralelo o objetivo é dividir uma tarefa em várias sub-tarefas e executá-las em paralelo.

Ao usar um framework de processamento paralelo, as sub-tarefas são levadas para o processador da máquina do **cluster** onde os dados estão armazenados, aumentando assim a velocidade de processamento de grandes volumes de dados.

## Cloud Computing

### O que é Cloud Computing?

A computação em nuvem **é a disponibilidade sob demanda dos recursos de computação como serviços na Internet**. Ela elimina a necessidade de as empresas adquirirem, configurarem ou gerenciarem a infraestrutura, assim elas pagarão apenas pelo que usarem.

### Principais Provedores em Nuvem

- AWS
- Azure
- Oracle
- Google Cloud

# Machine Learning

### O que é Machine Learning?

é uma sub-área da IA da Ciência da Computação que se concentra no uso de dados e algoritmos para imitar a forma como os humanos aprendem, melhorando gradativamente sua precisão.

- Artificial Intelligence
- Machine Learning
- Deep Learning

### Pipeline de Machine Learning

um pipeline de machine learning é **dividir uma tarefa completa de machine learning em um fluxo de trabalho de várias etapas**.

Cada etapa é um componente gerenciável que pode ser desenvolvido, otimizado, configurado e automatizado individualmente. As etapas são conectadas por meio de interfaces bem definidas.

### O que é MLOps?

Machine Learning Ops (ML + DEV + OPS) é um conjunto de práticas que **visa implantar e manter modelos de aprendizado de máquina em produção de forma confiável e eficaz**. 

### **Quais Problemas Podem Ser Resolvidos com MLOps?**

Com MLOps as empresas podem resolver, ou pelo menos amenizar, os problemas acima citados, ao mesmo tempo que exploram todas as vantagens do uso de Big Data em sistemas de Machine Learning. A seguir estão os principais desafios que as equipes enfrentam:

- Há uma escassez de Cientistas de Dados que sejam bons em análise de dados e que tenham conhecimento em desenvolvimento e implantação de aplicações web.
- Mudança dos objetivos de negócios no modelo -existem muitas dependências com os dados mudando continuamente, sendo difícil manter os padrões de desempenho do modelo e garantira governança de IA.
- Lacunas de comunicação entre as equipes técnicas e de negócios que não possuem uma linguagem comum.
- Avaliação de risco - há muito debate em torno da natureza da caixa preta de sistemas de Machine Learning.

## Data as a Service (DaaS)

DaaS é uma estratégia de gerenciamento de dados, que visa alavancar os dados como um ativo de negócios para maior agilidade no processo de análise. **Hoje os dados são um ativo de negócios, permitindo criar modelos preditivos, extrair padrões e anomalias.**

O DaaS fornece uma maneira de gerenciar as grandes quantidades de dados que as organizações geram todos os dias e fornecer essas informações para a tomada de decisões baseada em dados.

### Arquitetura DaaS

A **arquitetura DaaS** se concentra no provisionamento de dados de uma variedade de fontes sob demanda por meio do uso de APIs. Foi projetada para *simplificar o acesso aos dados, podendo incluir uma variedade de tecnologias de gerenciamento de dados*:

- virtualização de dados
- serviço de dados
- análise de autoatendimento
- catalogação de dados

### Principais Benefícios de DaaS

- monetização de dados
- redução de custos
- caminho mais rápido para inovação
- agilidade no processo de decisão
- menor risco no uso de dados
- criação de uma cultura de Data-Driven (as decisões da empresa são todas orientadas a dados)

## ETL - Extração, Transformação e Carga de Dados

**ETL**, do inglês *Extract, Transform, Load* (Extrair, Transformar, Carregar), é uma sigla para designar **processos de preparação e tratamento de dados** em diferentes contextos. Tudo começa na captação de informações em diversos sistemas, a transformação desses dados conforme regras estabelecidas de negócio, até o carregamento para uma ferramenta de análise ou BI.

## ETL vs ELT

### **Processo ETL**

O ETL tem três etapas:

1. Você extrai dados brutos de várias fontes
2. Você usa um servidor de processamento secundário para transformar esses dados.
3. Você carrega esses dados em um banco de dados de destino

### **Processo ELT**

Estas são as três etapas do ELT:

1. Você extrai dados brutos de várias fontes
2. Você o carrega em seu estado natural em um data warehouse ou data lake
3. Você o transforma conforme necessário enquanto está no sistema de destino

A abordagem **ETL usa um conjunto de regras de negócios para processar dados de várias fontes antes da integração centralizada**. A abordagem **ELT carrega os dados como estão e os transforma em um estágio posterior**, dependendo do caso de uso e dos requisitos de análise.
