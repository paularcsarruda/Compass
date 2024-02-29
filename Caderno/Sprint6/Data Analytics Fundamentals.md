## Volume de Dados

## Introdução ao Amazon S3 (Simple Storage Service)

>

- é o melhor lugar para armazenar todos os seus dados semiestruturados e não estruturados.
- Amazon S3 armazena dados como **objetos** em **buckets**.
- Em qualquer bucket, você pode adicionar o conteúdo nele de forma ordenada e organizada ou, simplesmente jogar o que quiser de qualquer jeito nele.
- Um **objeto** é composto por um arquivo e quaisquer metadados que descrevam esse arquivo
- **Buckets** são contêineres lógicos para objetos. Você pode ter um ou mais buckets em sua conta e controlar o acesso a cada um individualmente
- ex. sites, data analytics, etc.

>

Question: 

Imagine uma empresa que implementou o Amazon QuickSight como uma ferramenta de visualização de dados. Quando essa ferramenta depende de dados armazenados fisicamente, latência pode ser adicionada ao processamento. Essa latência pode se tornar um problema para os usuários. Outra preocupação comum é a capacidade de um usuário reunir os conjuntos de dados corretos para executar a análise necessária.

R: Amazon S3

Com o Amazon S3, você pode armazenar de modo econômico todos os tipos de dados em seus respectivos formatos nativos. Em seguida, você pode executar quantos servidores virtuais forem necessários usando o Amazon Elastic Compute Cloud (Amazon EC2) e usar as ferramentas analíticas da AWS para processar seus dados. Você pode otimizar suas instâncias do EC2 para fornecer as proporções corretas de CPU, memória e largura de banda para obter melhor desempenho.

Desacoplar seu processamento e armazenamento oferece muitos benefícios, incluindo a capacidade de processar e analisar os mesmos dados com diversas ferramentas.

O Amazon S3 facilita a criação de um ambiente multi-tenant em que muitos usuários podem trazer suas próprias ferramentas de análise de dados para um conjunto comum de dados. Isso melhora o custo e a governança de dados em relação às soluções tradicionais, que exigem que várias cópias de dados sejam distribuídas em múltiplas plataformas de processamento.

Embora isso possa exigir uma etapa adicional para carregar seus dados na ferramenta certa, ter o Amazon S3 como seu datastore central oferecerá ainda mais benefícios em relação às opções de armazenamento tradicionais.

Combine o Amazon S3 com outros serviços AWS para consultar e processar dados. O Amazon S3 também se integra à computação sem servidor do AWS Lambda para executar código sem provisionar ou gerenciar servidores. O Amazon Athena pode consultar o Amazon S3 diretamente usando a linguagem de consulta estruturada (SQL), sem a necessidade de entrada de dados em um banco de dados relacional.

As APIs REST são interfaces de programação comumente usadas para interagir com arquivos no Amazon S3. As APIs RESTful do Amazon S3 são simples, fáceis de usar e compatíveis com a maioria dos principais provedor independente de software (ISV) terceirizados, incluindo o Apache Hadoop e outros fornecedores de ferramentas analíticas líderes do mercado.

# **introdução a data lakes**

Um data lake pode utilizar buckets do Amazon S3 e podemos organizar os dados em categorias dentro dele. Não importa como os dados chegaram lá ou de que tipo eles são. Você pode armazenar dados estruturados e não estruturados de maneira eficaz em um data lake no Amazon S3. A AWS oferece um conjunto de ferramentas para gerenciar todo data lake sem tratar de cada bucket como objetos separados e não associados.

- **Um data lake é um 
repositório centralizado 
que permite armazenar dados 
estruturados
,
 semiestruturados
 e
 não estruturados 
em qualquer escala.**

Muitas empresas acabam agrupando dados em vários locais separados de armazenamento. Chamamos isso de silos. Esses silos raramente são gerenciados e mantidos pela mesma equipe e isso pode ser problemático. As inconsistências na forma como os dados foram escritos, coletados, agregados ou filtrados, podem causar dificuldades quando comparados e combinados na fase de processamento e análise.

Mas quando se usa a data lakes, você pode dividir esses silos de dados e trazê-los para um único repositório central gerenciado por uma única equipe, o que irá fornecer uma única e consistente fonte da verdade. Como os dados podem ser armazenados em seu formato bruto, você não precisa convertê-los, agregá-los ou filtrá-los antes de armazenar. Em vez disso, você pode deixar todo esse pré processamento pro sistema que o processa, em vez do sistema que o armazena.

## benefícios dos data lakes

- fonte única de confiança
- armazena qualquer tipo de dado, independente da estrutura
- pode ser analisado utilizando IA ou ML
- São uma solução **de armazenamento de dados econômica**. Você pode armazenar de forma durável uma quantidade quase ilimitada de dados usando o Amazon S3.
- Implemente a **segurança e a conformidade** líderes do setor. A AWS usa rigorosos mecanismos de segurança, conformidade, privacidade e proteção de dados.
- Permite que você aproveite **muitas ferramentas diferentes de coleta e ingestão** de dados para ingerir dados em seu data lake. Esses serviços incluem o Amazon Kinesis para dados de streaming e dispositivos AWS Snowball para grandes volumes de dados locais.
- Ajudam você a **categorizar e gerenciar seus dados** de forma simples e eficiente. Use o AWS Glue para entender os dados dentro do seu data lake, prepará-los e carregá-los de forma confiável em datastores. Depois que o AWS Glue cataloga seus dados, eles são imediatamente pesquisáveis, podem ser consultados e estão disponíveis para processamento de ETL.
- Ajuda você a transformar dados em **informações significativas**. Utilize o poder dos serviços analíticos criados para finalidades específicas em vários casos de uso, como avaliação interativa, processamento de dados usando o Apache Spark e o Apache Hadoop, data warehousing, análise em tempo real, análise operacional, painéis e visualizações.

# **introdução aos métodos de armazenamento de dados**

### Armazenamento de dados estruturados

- Os Data Warehouses, são usados como um sistema central para armazenar dados analíticos de várias fontes
- Um Data Warehouse é um repositório central de dados estruturados de muitas fontes de dados.
- Os Data Warehouses on-premises exigem um investimento significativo para planejar, configurar e manter. Para muitas pequenas empresas, isso não é uma opção. No entanto, a AWS fornece um serviço de Data Warehousing chamado de Amazon Redshift.
- O Amazon Redshift permite configurar e implantar um novo data warehouse em minutos. Ele foi criado para armazenar e consultar conjuntos de dados que variam de gigabytes a petabytes de tamanho.
- **Um 
data warehouse
 é
 um 
repositório central
 de dados estruturados de muitas origens de dados. Esses dados são 
transformados
, 
agregados
 e 
preparados 
para relatórios e avaliaçãos de negócios.**

# **Apache Hadoop**

O Hadoop usa uma **arquitetura de processamento distribuído**, no qual uma tarefa é mapeada para um cluster de servidores convencionais para processamento. Cada bloco de trabalho distribuído aos servidores do cluster pode ser executado ou re-executado em qualquer um dos servidores. Os servidores do cluster usam frequentemente o **Hadoop Distributed File System (HDFS)** para armazenar dados localmente para processamento. Os resultados da computação realizada pelos servidores são reduzidos a um único conjunto de saída. Um nó, designado como nó principal, controla a distribuição de tarefas e pode lidar automaticamente com falhas dos servidores.

AMAZON EMR

O Amazon EMR é o serviço AWS que implementa frameworks Hadoop. O serviço fará a ingestão dos dados de praticamente qualquer tipo de origem a praticamente qualquer velocidade! O Amazon EMR consegue implementar dois sistemas de arquivos diferentes: HDFS ou Elastic MapReduce File System (EMRFS). Um sistema de arquivos é um conjunto de regras organizacionais que controlam como os arquivos são armazenados.

**HDFS**

Para lidar rapidamente com volumes enormes de dados, o sistema de processamento exigia uma maneira de distribuir a carga de leitura e gravação de arquivos em dezenas ou até centenas de servidores de alta capacidade. O HDFS éum armazenamento distribuído que permite que os arquivos sejam lidos e gravados em clusters de servidores em paralelo. Isso reduz drasticamente a duração total de cada operação.

**Amazon EMRFS**

O Amazon EMR oferece uma alternativa ao HDFS: o EMR File System (EMRFS). O EMRFS pode ajudar a garantir que haja uma “fonte confiável” persistente para dados do HDFS armazenados no Amazon S3. Ao implementar o EMRFS, não é necessário copiar dados para o cluster antes de transformar e analisar os dados como no HDFS. O EMRFS pode catalogar dados em um data lake no Amazon S3. O tempo economizado eliminando a etapa de cópia pode melhorar drasticamente o desempenho do cluster.

## **Velocidade: processamento de dados**

**Quando as empresas precisam de informações rápidas dos dados que estão coletando, mas os sistemas implantados simplesmente não conseguem atender às necessidades, 
há um problema de velocidade.**

# **Definição**

O ***processamento de dados*** significa a coleta e a manipulação de dados para produzir informações significativas. A coleta de dados é dividida em duas partes: coleta de dados e processamento de dados.

# **Tópico 1:**

# **introdução aos métodos de processamento de dados**

O processamento de dados é essencial para qualquer sistema de dados. O processamento de dados define os métodos usados para coletar dados e apresentá-los a mecanismos analíticos ou de armazenamento.

Há dois tipos de processamento: em lote ou batch, e o processamento em streaming.

>

- Lote ou batch 🐢: quando há uma grande quantidade de dados para processar e precisa realizar isso em determinados intervalos. Esse tipo de processamento é executado em datasets como: logs de servidor, dados financeiros, relatórios de fraudes e clickstreams
- Streaming 🐇: significa processar dados em um fluxo contínuo, ou seja, o processamento de dados que são gerados continuamente em pequenos conjuntos de dados, medido em kilobytes. Você usaria o streaming quando precisasse de um feedback em tempo real ou insights contínuos. Esse tipo de processamento é executado em conjuntos de dados como: dados do sensor IoT, compras de comércio eletrônico, atividades de jogadores num jogo, clickstreams ou informações de redes sociais.

Muitas empresas usam os dois tipos de processamento: Streaming e Batch, no mesmo Dataset. O Streaming é usado para obter insights iniciais e feedback em tempo real, enquanto o Batch é usado para obter insights profundos de análises complexas, por exemplo, transações de cartão de crédito.

O streaming também vem em duas formas: em tempo real e próximo do tempo real. Ambos os tipos envolvem dados de streaming que, como você já sabe, são processados rapidamente em pequenos lotes. A diferença vem na velocidade. O processamento em tempo real ocorre em milissegundos, enquanto o processamento próximo do tempo real ocorre em minutos.

**Características da velocidade de processamento de dados**

A capacidade de um sistema processar dados dependerá muito dos requisitos exigidos dele. Escolher o sistema certo é essencial para uma implementação bem-sucedida. Abaixo estão as características das quatro velocidades de coleta e processamento de dados.

# **Tópico 2:**

# **introdução ao processamento de dados em batch**

O processamento em batch deve consumir, de maneira rápida e eficiente, uma enorme quantidade de dados de uma só vez. Isso gera desafios que não existem com o processamento em stream.

O processamento de dados em batch oferece às empresas a capacidade de se aprofundarem nos dados coletados para produzir análise complexa que não pode ser obtida apenas usando a análise de streaming.

- O *processamento em batch* é a execução de uma série de programas ou *trabalhos* em um ou mais computadores sem intervenção manual. Os dados são coletados em batches de maneira assíncrona. O batch é enviado a um sistema de processamento quando condições específicas são atendidas, como um horário específico do dia. Os resultados do trabalho de processamento são enviados a um local de armazenamento que pode ser consultado posteriormente, conforme necessário.

**Processamento de dados em batch com o Amazon EMR e o Apache Hadoop**

As organizações que precisam de soluções de big data estão trabalhando com dados em volume e velocidade tão altos que os ambientes tradicionais não conseguem atender às suas necessidades.

O Amazon EMR é um serviço gerenciado para a implantação de cargas de trabalho do Apache Hadoop. Além de executar o framework Apache Hadoop, você também pode executar outros frameworks distribuídos conhecidos, como Apache Spark, HBase, Presto e Flink no EMR. Você tem a vantagem adicional de poder interagir com dados em outros datastores da AWS, como o Amazon S3 e o Amazon DynamoDB.

# **Tópico 3:**

# **introdução ao processamento de dados de stream**

**O processamento de dados em stream é uma das áreas de processamento que mais cresce. O número de dispositivos coletando informações em tempo real está crescendo rapidamente. Isso impulsiona a necessidade por soluções de processamento que correspondam à velocidade da geração de dados.**

O processamento de dados em stream oferece às empresas a capacidade de obter informações de seus dados em segundos após a coleta dos dados.

**Processamento de big data em stream**

Há vários motivos para usar soluções de dados de streaming. Em um sistema de processamento em batch, o processamento é sempre assíncrono e o sistema de coleta e de processamento costumam ser agrupados. Com soluções de streaming, o sistema de coleta (produtor) e o sistema de processamento (consumidor) são sempre separados. Os dados de streaming usam o que chamamos de *produtores de dados*. Cada um desses produtores pode gravar seus dados no mesmo endpoint, permitindo que vários streams de dados sejam combinados em um único stream para processamento. Outra grande vantagem é a capacidade de preservar a ordem dos dados do cliente e a capacidade de executar o consumo paralelo de dados. Isso permite que múltiplos usuários trabalhem simultaneamente nos mesmos dados.

um serviço para ingerir o stream constante de dados, outro para processar e analisar o stream, e outro para carregar os dados em um datastore analítico, se necessário. O **Amazon Kinesis** atende a cada uma dessas necessidades e você pode usar cada serviço do Kinesis independentemente para criar uma solução de streaming ideal.

- O Amazon Kinesis Data Firehose é a maneira mais fácil de capturar, transformar e carregar streams de dados em datastores da AWS para análises quase em tempo real usando ferramentas existentes de business intelligence.
- O Amazon Kinesis Data Streams permite criar aplicativos personalizados e em tempo real para processar streams de dados usando frameworks comuns de processamento de streams.
- O Amazon Kinesis Video Streams facilita o streaming seguro de vídeos a partir de dispositivos conectados à AWS, onde podem ser usados para análise, machine learning (ML) e outros processamentos.
- O Amazon Kinesis Data Analytics é a maneira mais fácil de processar streams de dados em tempo real com SQL ou Java sem precisar aprender novas linguagens de programação ou frameworks de processamento.

# **Variedade: estruturas e tipos de dados**

Quando sua empresa fica sobrecarregada pelo grande número de origens dos dados  para analisar e você não consegue encontrar sistemas para fazer a análise, sabe que tem um problema de variedade.

# **Tópico 1:**

# **introdução ao armazenamento de dados de origem**

Vamos falar sobre três tipos de dados: estruturados, semiestruturados e não estruturados.

Dados estruturados 

- são dados armazenados em formato tabular, muitas vezes em um sistema gerenciador de banco de dados, o RDBMS.
- Esses dados são organizados com base em um modelo de dados relacional que define e padroniza os elementos de dados e a relação entre si. Isso é chamado de Schema. Por meio do Schema, o RDBMS tem a capacidade de impor a conformidade.
- Dados estruturados são organizados em tabelas, colunas e linhas. Você pode encontrar dados estruturados em um banco de dados transacionais e analíticos. Os bancos de dados transacionais enfrentam operações pesadas de gravação e atualização, enquanto os bancos de dados analíticos enfrentam operações pesadas de leitura.
- Exemplos de aplicativos de dados estruturados incluem Amazon RDS, Amazon Aurora, MySQL, MariaDB, PostgreSQL, Microsoft SQL Server e Oracle.
- Os dados em bancos de dados relacionais são organizados para que os valores em uma tabela possam ser usados para referenciar dados em outra tabela. Em outras palavras, existe uma relação entre duas tabelas.

Dados semiestruturado

- Quando dados semiestruturados são armazenados em um banco de dados não relacional, geralmente chamados de NoSQL, eles não impõem um Schema, nem um conjunto específico de regras e constraints nos dados. Quando dados sempre estruturados são armazenados em arquivos, eles são considerados como tendo uma estrutura auto descritiva, o que significa que o próprio arquivo informará como interpretar os dados dentro dele. A vantagem é que isso permite que cada tabela ou arquivo tenha sua própria estrutura ou Schema.
- os dados semiestruturados são altamente flexíveis. Cada elemento pode conter atributos diferentes, portanto, ele pode escalar pra atender às demandas dinâmicas de uma empresa muito mais rapidamente do que os dados estruturados. Mas a desvantagem dessa flexibilidade é a perda na capacidade de análise.
- Exemplos de datastores semiestruturados são CSV, XML, JSON, Amazon DynamoDB, Amazon Neptune e Amazon ElastiCache.

dado não estruturado

- são dados armazenados em arquivos semelhantes a dados semiestruturados. Esses dados não estão em conformidade com o modelo de dados predefinidos e não estão organizados da maneira predefinida. Os dados não estruturados podem ser muito textuais. Os arquivos PDFs, CSV compõem a maior parte desse tipo de fonte de dados. Os arquivos também podem conter um pouco de texto, no caso de imagens e vídeos.
- Para executar análises significativas em dados não estruturados, você precisa pré-processar os arquivos. Existem algumas maneiras principais de como os arquivos são pré-processados. Você pode usar um serviço para adicionar tags aos dados com base em regras que você define.
- Exemplos de dados não estruturados incluem e-mails, fotos, vídeos, dados de clickstream, Amazon S3 e Amazon Redshift Spectrum.

# **Tópico 2:**

# **introdução a datastores estruturados**

Os dados estruturados são classificados como dados armazenados em um banco de dados ou em um sistema de gerenciamento de banco de dados (DBMS). Um banco de dados é um conjunto estruturado de dados mantido em um computador, que pode ser acessado de várias maneiras. Um DBMS fornece estrutura aos dados, capacidade de manter os dados durante todo o ciclo de vida e capacidade de gerenciar interações com outros processos e sistemas. Diferentes sistemas de gerenciamento de banco de dados gerenciam a organização de dados de diferentes maneiras para atingir metas específicas, como avaliação complexa, navegação rápida de relacionamentos ou recuperação do estado da sessão.

**Dados de arquivos de texto puro**

Em geral, os dados de arquivos de texto puro residem em uma planilha. Pode não parecer um banco de dados, mas ele atende a todos os requisitos básicos. Esse formato fornece uma base sólida para entender algumas das considerações ao escolher um DBMS.

**Bancos de dados relacionais**

O armazenamento de arquivos de texto puro pode não atender às suas necessidades de armazenamento de dados estruturados. A próxima etapa lógica é migrar para uma solução mais robusta: um banco de dados relacional.

**Tipos de sistemas de informação**

Há duas maneiras principais, conhecidas como sistemas de informação, de organizar dados em um banco de dados relacional. Os dados podem ser organizados para se concentrar no armazenamento de transações ou no processo de análise de transações.

Os bancos de dados transacionais são chamados de bancos de dados de processamento de transações on-line (OLTP). Os dados coletados pelos bancos de dados OLTP geralmente alimentam outro tipo de banco de dados que se concentra na análise dos dados transacionais. Os bancos de dados de processamento analítico on-line (OLAP) coletam dados de sistemas OLTP com o objetivo de organizá-los para operações analíticas.

**Indexação de dados colunares e baseada em linha**

Os dados em um banco de dados devem ser indexados para permitir que uma consulta encontre rapidamente os dados necessários para produzir um resultado. Os índices controlam a maneira como os dados são armazenados fisicamente no disco. Eles agrupam fisicamente os registros em uma ordem previsível com base em chaves‑valores dentro da tabela. Isso tem um papel importante na velocidade e na eficiência das consultas.

### OLAP

### OLTP

## Soluções da AMAZON

Na AWS, o Amazon Relational Database Service (Amazon RDS) atende as necessidades de muitos sistemas de gerenciamento de banco de dados relacional diferentes. Ele é compatível com a maioria dos mecanismos de banco de dados mais conhecidos, incluindo Amazon Aurora, MySQL, PostgreSQL, MariaDB, Oracle e SQL Server.

O Amazon RDS facilita a configuração, operaração e scaling de um banco de dados relacional na nuvem. O serviço fornece capacidade econômica e redimensionável enquanto automatiza tarefas administrativas demoradas, como provisionamento de hardware, configuração de banco de dados, aplicação de patches e backups.

O Amazon RDS tem tudo o que você pode precisar para um banco de dados OLTP altamente eficiente. O serviço implementa a indexação baseada em linhas para alcançar o desempenho certo para cargas de trabalho transacionais.

O Amazon Redshift é um data warehouse rápido e dimensionável que permite analisar todos os dados de data warehouses e data lakes de forma simples e econômica. O Amazon Redshift oferece desempenho 10 vezes mais rápido que qualquer outro data warehouse por meio de machine learning, além da execução paralela de consultas em massa e armazenamento colunar em discos de alto desempenho. Você pode configurar e implantar um novo data warehouse em minutos e executar consultas em petabytes de dados no data warehouse do Amazon Redshift e exabytes de dados no data lake criado no Amazon S3.

O Amazon Redshift implementa a indexação colunar para obter o desempenho certo para cargas de trabalho analíticas.

# **Tópico 3:**

# **introdução a datastores semiestruturados e não estruturados**

Os dados semiestruturados e não estruturados geralmente são armazenados em sistemas de banco de dados não relacionais, às vezes chamados de bancos de dados NoSQL. Esse termo pode causar um pouco de confusão. É importante lembrar que o SQL é uma maneira de consultar dados. Isso implica em uma estrutura precisa. Não relacional ou NoSQL *não* significa que os dados armazenados *não podem* ser consultados usando SQL. Uma maneira melhor de pensar nisso: *não é apenas* SQL.

Primeiro é o termo S.Q.L ou SQL na linguagem utilizada para consultar dados. Infelizmente, as pessoas costumam usar esse termo para se referir a bancos de dados relacionais, o que pode ser confuso, em uma discussão como esta. Quando o SQL é usado, você precisa prestar muita atenção para determinar se estamos nos referindo ao SQL como uma linguagem de consulta, ou ao SQL como um tipo de banco de dados.

Dados semiestruturados ou dados não estruturados podem ser armazenados em bancos de dados NoSQL, o que é muito comum para dados semiestruturados. Esses tipos de armazenamentos de dados também podem ser armazenados em servidores de arquivos ou em data lake, ambos comuns para dados não estruturados. Para essa discussão, vamos nos concentrar nos dados armazenados em bancos de dados NoSQL.

Os dados em bancos de dados relacionais são organizados para que os valores em uma tabela possam ser usados para referenciar dados em outra tabela. Em outras palavras, existe uma relação entre duas tabelas.

Já os bancos de dados NoSQL armazenarão todos esses dados em uma única tabela. Portanto, analisando o seu exemplo em um banco de dados NoSQL, todas as informações de cada produto, incluindo os detalhes do fornecedor associado, são armazenados em um único item dentro dessa tabela no banco de dados.

Na AWS, o Amazon DynamoDB é o serviço usado para armazenamento de dados NoSQL. O DynamoDB é um banco de dados de chave-valor e de armazenamento de documentos. Ele oferece performance inferior a 10 milissegundos em qualquer escala e é um banco de dados multi-regional, totalmente gerenciado de vários masters, com opções de segurança, backup e restaurações integradas e armazenamento in cache na memória, para aplicações na escala da Internet.

Os bancos de dados grafos utilizam conexões e relacionamento entre os dados. Se você tem uma aplicação que se concentra principalmente em analisar esses relacionamentos e encontrar padrões neles, como em absolutamente todas as aplicações de mídias sociais, então um banco de dados de Grafo, provavelmente, é uma boa opção.

Os bancos de dados de Grafo são de uso específico para armazenar qualquer tipo de dados, sejam estruturados, semiestruturados ou não estruturados. O objetivo da organização de um banco de dados de Grafos é navegar pelos relacionamentos. Os dados dentro de um banco de dados são consultados utilizando uma linguagem específica associada a um software que você utilizou.

O serviço de banco de dados de Grafos da AWS se chama Amazon Neptune. O Neptune é um serviço de banco de dados rápido, confiável e totalmente gerenciado, que facilita a criação e a execução de aplicações que trabalham com conjuntos de dados altamente conectados.

Os bancos de dados grafos utilizam conexões e relacionamento entre os dados. Se você tem uma aplicação que se concentra principalmente em analisar esses relacionamentos e encontrar padrões neles, como em absolutamente todas as aplicações de mídias sociais, então um banco de dados de Grafo, provavelmente, é uma boa opção.

Os bancos de dados de Grafo são de uso específico para armazenar qualquer tipo de dados, sejam estruturados, semiestruturados ou não estruturados. O objetivo da organização de um banco de dados de Grafos é navegar pelos relacionamentos. Os dados dentro de um banco de dados são consultados utilizando uma linguagem específica associada a um software que você utilizou.

O serviço de banco de dados de Grafos da AWS se chama Amazon Neptune. O Neptune é um serviço de banco de dados rápido, confiável e totalmente gerenciado, que facilita a criação e a execução de aplicações que trabalham com conjuntos de dados altamente conectados.

Como a Erika disse, bancos de dados de grafos, como Neptune, são bancos de dados de propósitos específicos, pra armazenar relacionamentos e navegar por eles. Esses bancos de dados possuem vantagens em relação aos bancos de dados relacionais. Em casos como: redes sociais, mecanismos de recomendação e detecção de fraudes, onde é necessário criar relacionamentos entre os dados e consultar esses relacionamentos de forma muito rápida.

Quando se trata de armazenar dados semiestruturados e não estruturados, a escolha mais indicada geralmente se trata dos bancos de dados NoSQL.

Os bancos de dados de grafo são criados especificamente para armazenar qualquer tipo de dados: estruturados, semiestruturados ou não estruturados. O objetivo da organização em um banco de dados de grafo é navegar pelas relações. Os dados no banco de dados são consultados usando linguagens específicas associadas à ferramenta de software que você implementou.

Logicamente, os dados são armazenados como um nó e as bordas armazenam informações sobre as relações entre os nós. Uma borda tem sempre um nó inicial, um nó final, um tipo e um direcionamento, o que possibilita a descrição de relações entre pais e filhos, ações, propriedades e assim por diante. Não há limite para o número e os tipos de relações que um nó pode ter.

**Vantagens:**

- Permitem a recuperação simples e rápida de estruturas hierárquicas complexas;
- Ótimos para mineração de big data em tempo real;
- Podem identificar rapidamente pontos de dados comuns entre nós;
- Ótimos para fazer recomendações relevantes e permitir a consulta rápida dessas relações.

**Desvantagens:**

- Não é possível armazenar adequadamente dados transacionais;
- Os analistas devem aprender novas linguagens para consultar os dados;
- A análise nos dados pode não ser tão eficiente quanto com outros tipos de bancos de dados.

**Noções básicas sobre relações de grafos**

Imagine que você quisesse examinar um produto ou recomendação social. No gráfico abaixo, observe Bill no canto superior direito. O gráfico mostra que Bill conhece Mary e Amit. Bancos de dados de grafo, como todos os outros, podem armazenar informações sobre várias entidades diferentes. As entidades são chamadas de nós em um banco de dados de grafo. Bill, Mary e Amit representam nós de clientes. Você também pode acompanhar o histórico de compras introduzindo nós de produto. Três clientes compraram esse produto.

Você pode ir além e acompanhar os interesses dos clientes, como o esporte favorito. Esse gráfico dá aos analistas a oportunidade de responder a muitas perguntas úteis. Myra, como cliente, pode estar interessada em quais produtos foram comprados por outros clientes que gostam de esportes. Mary pode estar interessada em saber sobre os outros clientes que seus amigos conhecem.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/5f038bdc-9c8d-4da1-a229-829f0697839f/af2e348c-5a86-457c-b0d9-39ef7fb964a5/Untitled.png)

# Desafio de Negócios

Imagine uma empresa que esteja trabalhando para desenvolver um aplicativo de comércio eletrônico especializado em detecção de fraudes. A empresa precisa de uma solução que possa fornecer detecção quase em tempo real de padrões definidos como suspeitos.

R: 

O Amazon Neptune é um serviço de banco de dados de grafo rápido, confiável e totalmente gerenciado que facilita a criação e a execução de aplicativos que funcionam com conjuntos de dados altamente conectados.

O núcleo do Neptune é um mecanismo de banco de dados de grafo de alto desempenho e criado especificamente para armazenar bilhões de relações e consultar os grafos com latência de milissegundos.

# **Veracidade: limpeza e transformação**

Quando se tem dados que não são controlados, provenientes de vários sistemas diferentes 
e não consegue fazer curadoria dos dados de maneiras significativas, você sabe que tem um problema de veracidade.

# **Definições**

***Curadoria** é a ação ou o processo de selecionar, organizar e cuidar de itens em uma coleção.*

***Integridade dos dados** é a manutenção e a garantia de precisão e consistência dos dados durante todo o seu ciclo de vida.*

***Veracidade dos dados** é o grau em que os dados são exatos, precisos e confiáveis.*

**O problema da veracidade**

Os dados sofrem alterações ao longo do tempo. À medida que são transferidos de um processo para outro, e por um sistema e outro, há oportunidades para que a integridade dos dados seja afetada negativamente. Você deve garantir a manutenção de um alto nível de certeza de que os dados que está analisando são confiáveis.

A veracidade dos dados depende da integridade deles.

# **Tópico 1:**

# **compreensão da integridade dos dados**

- Ter alta integridade de dados, significa que podemos confiar na fonte de dados para planejamento e tomada de decisões e operações.
- integridade de dados é um termo amplo que é aplicado de diferentes maneiras em cada fase do ciclo de vida de dados.
- Esse ciclo de vida inclui a criação, agregação, armazenamento, acesso, compartilhamento e arquivamento.

Na fase de criação, a integridade dos dados significa garantir a precisão dos dados. Isso envolve um certo nível de confiança nos sistemas que coletam os dados. Bancos de dados relacionais, por exemplo, usam o que chamamos de ACID Compliance para impor a integridade dos dados. Para garantir que seus dados são precisos, é necessário auditorias regulares dos seus sistemas de software pra confirmar duas coisas: se eles estão produzindo dados ou arquivos válidos e que as alterações não afetarão negativamente a integridade do sistema.

A próxima fase é Agregação. Os dados nem sempre são agregados, mas é uma fase essencial para muitos sistemas analíticos, nas quais as métricas devem estar bem definidas. A integridade dos dados nessa fase garante que o usuário obtenha 'valor esperado', a partir do 'agregado fornecido. A perda de integridade nessa fase é, muitas vezes, o resultado da má nomenclatura dos valores agregados e do planejamento insatisfatório por parte do desenvolvedor para atender às expectativas dos usuários.

Na fase de Armazenamento, a preocupação é a integridade dos dados. Portanto, é necessário manter os dados em um formato seguro e garantir que todas as alterações sejam precisas. Alguns dados são altamente voláteis, o que significa que estão sujeitos a alterações frequentes, enquanto outros dados são estáveis, portanto, não costumam sofrer alterações. A proteção de dados significa garantir que os dados estáveis não sejam alterados e que os dados voláteis só sejam atualizados por usuários e serviços autorizados.

Na fase de Acesso, os dados se tornam visíveis para os usuários. Nesse estágio, os dados são fornecidos em um formato 'somente leitura. Isso significa que não há alterações permitidas nos dados e a integridade dos dados não pode ser alterada. A integridade dos dados nesse momento é uma prova da integridade de todas as outras fases. É aqui que os analistas de negócios começam a consultar os dados e usá-los para preencher relatórios e dashboards que leva à fase de Compartilhamento. Após a criação de relatórios e dashboards, eles são compartilhados com as empresas por meio de várias ferramentas, da mesma forma que a fase de Acesso. Nessa fase, os dados são somente leitura, portanto, podemos comprovar a integridade de dados nesse estágio.

Chegará um momento em que os dados não têm mais valor e é aqui que entra a fase de Arquivamento. Nesse ponto, a integridade dos dados se trata de garantir o arquivamento adequado. Você até poderia excluir os dados, mas o mais comum é agregá-los de outra forma e descartar o original. Por exemplo, quando um registro de venda individual tiver dez anos, seus dados poderão ser agregados em totais, diários ou mensais, enquanto o registro original seria descartado.

# **Definições**

***Limpeza de dados** é o processo de detecção e correção de corrupções nos dados.*

***Integridade referencial** é o processo para garantir que as restrições das relações da tabela sejam impostas.*

***Integridade do domínio** é o processo para garantir que os dados inseridos em um campo correspondam ao tipo de dados definido para esse campo.*

***Integridade da entidade** é o processo para garantir que os valores armazenados em um campo correspondam às restrições definidas para esse campo.*

**Identificação de problemas de integridade dos dados**

- Saiba qual deve ser a limpeza
- Saiba de onde os erros vêm
- Saiba quais são as alterações aceitáveis
- Saiba se os dados originais têm valor

**Esquemas de banco de dados**

Como discutimos, bancos de dados relacionais dependem de esquemas de banco de dados para organizar o conteúdo dentro do banco de dados e impor a integridade referencial e de domínio. Os programadores também usam esses esquemas ao escrever o software para interagir com o banco de dados.

**Esquema de informações**

Você já imaginou como um DBMS gerencia todos os bancos de dados, tabelas e relações? A resposta está no esquema de informações. Um esquema de informações é um banco de dados de metadados que armazena informações sobre os objetos de dados em um banco de dados.

O Microsoft SQL Server chama seu esquema de informações de banco de dados mestre. A Oracle usa tabelas de dicionário de dados e um registro de metadados. O Apache Hadoop usa um metastore. Cada DBMS pode ter nomes diferentes para a estrutura de dados que armazena os metadados, mas a finalidade é a mesma: definir quais são todos os objetos no banco de dados e registrar informações vitais sobre eles.

# **Tópico 2:**

# **compreensão da consistência do banco de dados**

Para manter a veracidade nos dados armazenados, consistência é essencial. Quando dados são armazenados como arquivos, a consistência é controlada pelo aplicativo que está desenvolvendo os arquivos. Quando os dados são armazenados em um banco de dados, a consistência é responsabilidade do banco de dados que os armazena. Neste tópico, discutiremos os dois métodos implementados pelos bancos de dados: ACID e BASE

# **ACID**

***ACID** é um acrônimo para **A**tomicidade, **C**onsistência, **I**solamento e **D**urabilidade. É um método para manter a consistência e a integridade em um banco de dados estruturado.*

**Conformidade com o ACID**

ACID é o bastião de longa duração da integridade dos dados relacionais. Em um banco de dados como o Amazon RDS, uma sequência de instruções executadas em conjunto é chamada de transação. Milhões de transações podem ser executadas consecutivamente. Os dados e as restrições nesses dados são muito ativos em bancos de dados relacionais.

O ACID é a maneira mais comum de atingir e manter a consistência e disponibilidade dos dados em um banco de dados relacional. Em um banco de dados, como o Amazon RDS, uma sequência de operações é chamada de Transação. Milhões de transações podem ser executadas consecutivamente e as alterações nos dados são muito comuns, assim como as restrições nestes dados. O objetivo de um banco de dados compatível com ACID é retornar à versão consistente e mais recente de todos os dados e garantir que os dados nos sistemas atendam às regras e restrições a todos os momentos. Esse processo introduz latência no sistema, que deve ser considerada.

o acrônimo ACID. O "A" significa Atomicidade. As transações podem conter vários statements ou instruções. A Atomicidade garante que todos os statements sejam bem sucedidos ou falhem juntos. É tudo ou nada! Nenhum statement será bem sucedido se algum outro não for.

O "C" significa Consistência. Para que uma transação seja concluída com êxito, todos os statements dentro dela devem atender a todas as constraints definidas no banco de dados. Se um único statement violar essa verificação, por exemplo, se eu tiver um valor acima de 100 mil em uma coluna que aceita apenas dígitos únicos, toda a transação será revertida. Nós vamos ter um rollback, tá? E o banco de dados voltará ao estado anterior. Isso também garante que as atualizações de dados não estejam disponíveis até que todas as replicações sejam atualizadas também.

O "I" significa Isolamento. O Isolamento garante que uma transação não interfira em outra transação simultânea. Os bancos de dados são espaços movimentados e o isolamento garante que, quando várias transações solicitarem os mesmos dados, os dados não serão corrompidos em consequência do processo. O isolamento significa que há regras vigentes que regem as alterações de dados. Ele funciona como uma catraca. Se duas transações desejarem atualizar o mesmo registro, uma delas deverá aguardar até que a outra seja concluída ou falhe.

O "D" significa Durabilidade. A Durabilidade dos dados tem a ver com a garantia de que, depois que forem realizadas, as alterações realmente sejam mantidas. Quando uma transação é concluída, a durabilidade garante que o resultado da transação seja permanente, mesmo em caso de falha do sistema. Isso significa que todas as transações concluídas resultam em um novo registro ou em uma atualização de um registro existente. Elas são gravadas em disco e não permanecem apenas na memória.

# BASE

Consistência BASE. A Consistência BASE está mais preocupada com a disponibilidade rápida dos dados. A Consistência BASE é geralmente implementada em bancos de dados NoSQL, em grandes sistemas distribuídos e em DataStores não estruturados. Para garantir a disponibilidade, as alterações nos dados são disponibilizadas imediatamente na instância em que a alteração foi feita. No entanto, pode levar algum tempo para que a alteração replicada seja propagada entre todas as instâncias. Eventualmente, a alteração será totalmente consistente em todas as instâncias.

**Conformidade com BASE**

O BASE promove a integridade de dados em bancos de dados não relacionais, às vezes são chamados de bancos de dados NoSQL. Bancos de dados não relacionais, como o Amazon DynamoDB, ainda usam transações para processar solicitações. Esses bancos de dados são hiperativos e a principal preocupação é a disponibilidade dos dados em relação à consistência dos dados. Para garantir que os dados estejam altamente disponíveis, as alterações nos dados são disponibilizadas imediatamente na instância em que a alteração foi feita. No entanto, pode levar algum tempo para que essa alteração seja replicada em toda a frota de instâncias. O objetivo é que a alteração acabe sendo totalmente consistente em toda a frota.

O "BA", em BASE, significa 'Basicamente disponível'. Conforme a Erika havia falado pra gente, isso permite que uma instância do banco de dados receba um novo registro ou até mesmo uma atualização de um registro existente e disponibiliza essa alteração de forma imediata para essa instância. À medida que essa alteração é, por fim, replicada em todas as outras instâncias, essas instâncias se tornam consistentes. Em um sistema ACID, essa alteração não ficaria visível para ninguém, até que todas as instâncias fossem consistentes. Essa é a diferença! Sim, essa é a principal diferença! Em um sistema BASE, a consistência completa é trocada por disponibilidade imediata. Em algum momento, você terá consistentes disponibilidades completas, nos dois modelos de consistência. A diferença é que isso ocorre primeiro em um.

O "S", em BASE, significa Soft State. Quer dizer que o estado é flexível, onde vai ser permitido consistência parcial entre instâncias distribuídas. Por esse motivo, consideramos que os sistemas BASE estão em estado flexível, também chamado de estado mutável. Por outro lado, em um sistema ACID, o banco de dados é considerado como um estado rígido, pois os usuários só podem acessar os dados totalmente consistentes.

O "E", no BASE, significa Consistência Eventual. Como você mencionou, a Consistência Eventual significa que a alteração fica disponível imediatamente em uma instância, e essa alteração será, por fim, feita em todas as cópias. Enquanto isso, os dados estão sempre disponíveis de alguma maneira. A nova ou antiga.

# **Tópico 3:**

# **introdução ao processo de ETL**

Os dados de origem são confusos, estão em vários locais e raramente são desenvolvidos com o mesmo estilo de organização. Tentar entender essa confusão sem transformar os dados de origem é como tentar ouvir com clareza uma única voz em uma multidão. Você pode capturar partes da conversa, mas ela perderá contexto e validade rapidamente.

# **Noções básicas sobre ETL**

Extração, transformação e carregamento (ETL) é o processo de coletar dados de origens brutas e transformá-los em um tipo comum. Esses novos dados são carregados em um local final para serem disponibilizados para avaliação e inspeção analíticas. Em ambientes modernos baseados na nuvem, geralmente nos referimos a esse processo como ELT (extração, transformação e carregamento). As etapas são simplesmente executadas em uma ordem diferente, mas o resultado é o mesmo.

A fase de extração desse processo é provavelmente a mais importante de todas as fases. Os dados necessários para a maioria das transformações de análise de dados provavelmente virão de vários locais e serão de vários tipos, como logs de transações, bancos de dados de produtos, origens de dados públicas ou fluxos de aplicativos.

Há quatro áreas principais para as quais você deve planejar.

1. Você deve identificar **onde** todos os dados de origem residem. Esses dados podem ser armazenados on-premises por sua empresa, mas também podem incluir dados encontrados on-line.
2. Você deve planejar cuidadosamente **quando** a extração ocorrerá devido ao possível impacto do processo de cópia no sistema de origem.
3. Você deve planejar **onde** os dados serão armazenados durante o processamento. Ele geralmente é chamado de local intermediário.
4. Você deve planejar **com quefrequência** a extração deve ser repetida.

Depois de determinar de onde os dados vêm e o que deseja, você extrairá essas informações e as colocará em um local intermediário.

Transformar seus dados em um formato uniforme e consultável é realmente o centro do processo de ETL. Essa fase envolve o uso de uma série de regras e algoritmos para inserir os dados no formato final. A limpeza de dados também ocorre durante essa parte do processo.

As transformações podem ser básicas, como a limpeza de dados para atualizar formatos ou fazer substituições de dados. Pode ser a substituição de valores NULL por zero ou a substituição da palavra feminino pela letra F. Essas alterações aparentemente pequenas podem ter um grande impacto sobre a utilidade desses dados para analistas posteriormente, no processo de visualização.

As transformações também podem ser mais avançadas, incluindo a aplicação de regras empresariais aos dados para calcular novos valores. Filtragem, operações complexas de agrupamento, agregação de linhas, divisão de colunas e validação de dados são tipos muito comuns de transformações aplicadas nessa fase.

Os serviços do Amazon ETL podem até mesmo fazer uma transformação entre diferentes tipos de origens de dados, como transformar dados não relacionais em um formato de dados relacional ou transformar dados relacionais em arquivos JSON a serem armazenados em um data lake do Amazon S3.

Alguns dados já podem estar em seu estado final e podem passar para a próxima fase.

A fase final do processo de ETL é escolher um local para carregar os dados recém-transformados. As etapas de planejamento realizadas na fase de transformação ditam o formato que o datastore final terá. Esse formato pode ser um banco de dados, um data warehouse ou um data lake. Assim que o processo for concluído com êxito, os dados nesse local estarão prontos para serem analisados.

# **Transformação de dados - comparação entre o Amazon EMR e o AWS Glue**

Quando se trata de executar o componente de transformação de dados do ETL, há duas opções na AWS: o Amazon EMR e o AWS Glue. Esses dois serviços fornecem resultados semelhantes, mas exigem diferentes quantidades de conhecimento e investimento de tempo.

O **Amazon EMR** é uma abordagem mais prática para criar seu pipeline de dados. Esse serviço fornece uma plataforma robusta de coleta e processamento de dados. Para usar esse serviço, sua equipe deve ter sólido conhecimento técnico e know‑how. A vantagem dele é que você pode criar um pipeline personalizado para atender às suas necessidades de negócios. Além disso, os custos de infraestrutura podem ser menores do que executar a mesma carga de trabalho no AWS Glue.

O **AWS Glue** é uma ferramenta de ETL gerenciada sem servidor que oferece uma experiência muito mais simplificada do que o Amazon EMR. Isso torna o serviço ideal para tarefas simples de ETL, mas você não terá tanta flexibilidade quanto teria com o Amazon EMR. Você também pode usar o AWS Glue como um metastore para seus dados transformados finais usando o AWS Glue Data Catalog. Esse catálogo é uma substituição de uma metastore do Hive.

# **Valor: relatórios e business intelligence**

**Quando 
há 
grandes volumes
 de 
dados
 usados para corroborar 
algumas informações valiosas
, você pode estar perdendo o 
valor 
dos seus dados.**

# **Tópico 1: introdução à análise de dados**

# **O que é análise de dados?**

Dados sem significado são irrelevantes. Palavras em um idioma que você não compreende são igualmente insignificantes. É somente quando o significado é atribuído que os dados ou as palavras podem ser compreendidos.

A análise de dados tem duas classificações: análise de informações e análise operacional. Análise de informações é o processo de análise de informações para encontrar o valor contido nelas. É uma ampla classificação de análise de dados que pode abranger tópicos que vão desde contabilidade financeira de uma empresa até a análise do número de entradas e saídas em um edifício protegido. A segunda forma de análise é a operacional. Ela é muito semelhante à análise de informações, no entanto, ela se concentra nas operações digitais de uma organização.

## análise de informação e análise operacional

A análise das informações é o processo no qual as informações são analisadas com o intuito de se encontrar o valor que elas contêm. É bem amplo, e pode abranger vários tópicos que vão desde a contabilidade financeira das empresas até a análise do número de entradas e saídas em um prédio.

A segunda forma de análise é a análise operacional e é muito semelhante à análise de informações. No entanto, ela se concentra especificamente nas operações digitais de uma organização. Por exemplo, a maneira como as aplicações de softwares se comportam ou as conexões com os dispositivos e serviços de redes.

## Tipos

Existem cinco tipos de análise: descritiva, diagnóstica, preditiva, prescritiva e cognitiva. Vamos começar com a análise descritiva. Geralmente ela é chamada de mineração de dados. É a forma mais antiga e mais comum. O método envolve agregações ou comparar valores históricos para responder a pergunta: o que aconteceu? O que está acontecendo? Por exemplo: quais foram as vendas de campainhas no mês passado? Ou qual têm sido as marcas mais vendidas de ração para gatos no quarto trimestre até agora? Essa forma de análise fornece insights e exige bastante julgamento humano para transformar esses insights em informações práticas.

A próxima forma de análise, é a diagnóstica. Esse método envolve comparar dados históricos geralmente coletados em análises descritivas com outros conjuntos de dados, datasets. Pra responder a pergunta: por que isso aconteceu? Com essas informações, você pode responder a perguntas como: por que nossas impressões de mídia social caíram no mês passado? Ou qual é a provável causa do aumento das reclamações dos clientes? Assim como a análise descritiva, essa forma de análise provê insights e requer julgamento humano pra transformar esses insights e informações práticas.

Agora, a próxima forma é a análise preditiva. Esse método envolve prever o que vai acontecer no futuro com base no que aconteceu no passado. Por exemplo, quais são as vendas prováveis em 2025, com base na nossa taxa de crescimento atual? Qual o número total das novas assinaturas que podemos esperar com base na trajetória do ano passado? Essa forma de análise fornece insights chamado previsões. Essas previsões também exigem avaliação humana sobre a validade para garantir que sejam realistas.

Próxima forma: análise prescritiva. É aqui que a ação realmente acontece. Esse método envolve analisar dados históricos e previsões pra responder a pergunta: o que deveria ter sido feito? Essa forma de análise se difere das três anteriores, pois exige que as aplicações incorporem regras e constraints pra fazer recomendações inteligentes. A maior vantagem dessa forma de análise é que ela pode ser automatizada. As aplicações que implementam análises prescritivas podem fazer recomendações ou tomar decisões e até mesmo adotar medidas com base nessas recomendações.

A forma final de análise é a cognitiva. Essa forma de análise usa um tipo de inteligência artificial chamado deep learning. O deep learning, juntamente com a análise prescritiva, é usado para tomar decisões e adotar medidas com base em entradas visuais, auditivas ou de linguagem natural. O deep learning imita o julgamento humano, combinando dados e os padrões existentes para tirar novas conclusões. Com cada análise, os resultados são retornados a um banco de dados de conhecimento para informar as futuras decisões. Isso cria um ciclo de feedback de autoaprendizagem. Pensa na Alexa? Quanto mais perguntas você fizer a Alexa, mais o sistema aprenderá.

# **Análise de informações**

# **Definição**

***Análise de informações** é o processo de análise de informações para encontrar o valor contido nelas. Esse termo geralmente é sinônimo de **análise de dados**.*

# **Análise operacional**

As empresas têm milhares de sistemas, aplicativos e clientes que geram dados constantemente. Essa é uma das áreas de coleta de dados que mais cresce. A análise operacional é uma forma de análise usada especificamente para recuperar, analisar e relatar dados para operações de TI. Esses dados incluem logs de sistema, logs de segurança, eventos e processos complexos de infraestrutura de TI, transações de usuários e até mesmo ameaças à segurança.

A [Forrester Research](https://www.forrester.com/report/Turn+Big+Data+Inward+With+IT+Analytics/-/E-RES75501?objectid=RES75501) definiu a análise de TI como “o uso de algoritmos matemáticos e outras inovações para extrair informações significativas do mar de dados brutos coletados por tecnologias de gerenciamento e monitoramento”.

Na AWS, o [Amazon Elasticsearch Service](https://aws.amazon.com/elasticsearch-service/) é comumente usado para implementar análises operacionais.

**Benefícios da análise operacional**

A análise operacional fornece os meios para líderes empresariais coletarem informações desses dados operacionais coletados a partir de dados de streaming e em tempo real.

**Análise preditiva**

A AWS tem o Amazon ML e um conjunto de serviços (incluindo inteligência artificial [IA]) que facilitam para os desenvolvedores a aplicação de análise preditiva aos seus dados e a adição de novos recursos inteligentes de processamento de dados aos seus aplicativos. A Amazon tem uma longa e rica tradição em torno de machine learning (ML) e muito dessa tecnologia acumulada foi organizada em um pacote para o uso do cliente com esse serviço.

A **pilha de machine learning** tem três camadas principais:

1. **Serviços de aplicativos** permitem que os desenvolvedores conectem a funcionalidade de IA pré-criada nos aplicativos sem se preocuparem com os modelos de ML que alimentam esses serviços.
2. **Serviços de plataforma** facilitam para qualquer desenvolvedor começar e se aprofundar em ML.
3. **Frameworks e interfaces** para especialistas em ML.

Na arquitetura a seguir, você vê um exemplo do uso do Amazon ML para produzir previsões em tempo real para usuários de um aplicativo. Nessa arquitetura, há vários serviços trabalhando em conjunto para produzir as previsões.

O Amazon DynamoDB é o local de armazenamento dos dados do aplicativo. O AWS Data Pipeline orquestra o fluxo de dados e a preparação para uso no Amazon SageMaker. Em seguida, você pode treinar um modelo de ML para usar os dados no Amazon SageMaker para fazer previsões em tempo real com base na atividade do usuário.

**Análise cognitiva**

Análise cognitiva é a forma mais recente de análise de dados. Ele oferece uma oportunidade incrível de fornecer recomendações altamente especializadas para empresas sem qualquer envolvimento humano, além da configuração inicial e do treinamento dos modelos de ML.

Alguns exemplos reais de análise cognitiva são:

- Software financeiro que fornece recomendações de investimento precisas, em tempo real e baseadas em fatos;
- Software para a área de saúde que oferece aos clientes acesso a recomendações confiáveis sobre tratamentos e opções atualizadas de saúde;
- Software veterinário que ajuda os veterinários a diagnosticar com rapidez e precisão seus pacientes;
- Software que auxilia ligas de futebol americano e entusiastas a gerenciarem suas equipes.

**Serviços analíticos e velocidade**

Na primeira vez em que você envia dados por um sistema de análise de dados, os dados fluem da ingestão para um local de armazenamento intermediário. Em seguida, os dados são processados a partir do local intermediário e podem resultar na colocação dos dados em um datastore analítico. O processamento dos dados do local intermediário pode ser repetido muitas vezes para produzir muitos resultados analíticos diferentes.

É importante ter uma compreensão sólida da velocidade que você pode esperar dos diferentes tipos de processamento.

# **Tópico 2: introdução à visualização de dados**

**Preparação de dados**

Lembre-se de que há um processo pelo qual os dados devem passar para serem realmente valiosos. Esse processo inclui:

- **Exploração de dados** - essa primeira fase geralmente faz parte do planejamento envolvido na criação de uma operação de ETL.
- **Limpeza de dados** - esse é o processo de normalização dos dados dentro da operação de ETL para garantir que os campos contenham os valores corretos e lidar com o problema de valores ausentes.
- **Transformação de dados** - essa fase envolve a aplicação de funções para manipular dados em novos formatos para fins analíticos.
- **Visualização de dados** - esse é o processo de criação de relatórios e painéis para apresentar o valor contido nos dados.

Já discutimos os três primeiros processos de análise de informações. Esta lição ajudará você a entender o processo final, que é a visualização dos dados.

**O que há em um relatório?**

Os relatórios analíticos são apresentados em vários formatos e tamanhos diferentes. A origem dos dados raramente afeta os relatórios resultantes. Os relatórios são organizados para atender às necessidades dos consumidores dos relatórios.

Há três tipos amplos de relatórios: estáticos, interativos e painéis.

- **Os relatórios estáticos** não desapareceram nesta era digital. Na verdade, ainda são muito utilizados para apresentações e reuniões. São encontrados em formato PDF e slides do PowerPoint e, muitas vezes, podem ser acessados por meio de portais da web e interfaces de software.
- **Os relatórios interativos** estão se tornando cada vez mais comuns. Esses tipos de relatórios geralmente se enquadram como business intelligence de autoatendimento. Esses relatórios costumam ter um estilo de relatório para impressão, mas têm a vantagem de que os consumidores podem aplicar filtros a tabelas e gráficos, alterar as escalas e até mesmo agrupar e classificar os valores nos relatórios. Isso permite que um consumidor conte sua própria história usando a base estabelecida pelo criador do relatório.
- **Painéis** são outra ferramenta de relatórios muito conhecida. A interatividade dos painéis depende do software empregado. Os consumidores encontram o maior benefício em painéis quando se concentram em roll-ups de alto nível dos principais fatores de negócios.

Relatórios e painéis são compostos por vários gráficos e tabelas para responder perguntas. Se as perguntas forem claras, o relatório ou o painel fornecerão as respostas. Relatórios e painéis também podem ser divididos em páginas ou exibições. Essas páginas devem ter um único tema para todos os elementos do relatório nelas. É muito comum dar aos consumidores de relatórios e painéis interativos filtros que podem ser aplicados a toda a página ou a elementos individuais na página.

# Desafio AWS:

Preciso conseguir fazer perguntas de acompanhamento e dividir os dados para descobrir informações sem precisar consultar o tempo todo minha equipe de business intelligence para executar consultas únicas.

R:

O

**Amazon QuickSight**

é um serviço analítico de negócios rápido, fácil de usar e desenvolvido para a nuvem que permite que todos os funcionários de uma empresa criem exibições, executem avaliações únicas e extraiam rapidamente informações empresariais de seus dados, a qualquer momento, em qualquer dispositivo.

Painéis interativos disponibilizam aos consumidores de painéis uma forma de autoatendimento para consumir e separar seus dados para responder perguntas sem precisar depender de uma equipe de business intelligence.

Com o Amazon QuickSight, é possível fazer upload de arquivos CSV e Excel; conectar-se a aplicativos de software como serviço (SaaS), como o Salesforce; acessar bancos de dados on-premises, como o SQL Server, o MySQL e o PostgreSQL; e utilizar de forma contínua suas origens de dados da AWS, como o Amazon Redshift, o Amazon RDS, o Amazon Aurora, o Amazon Athena e o Amazon S3.

O Amazon QuickSight permite que as empresas escalem seus recursos analíticos de negócios para centenas de milhares de usuários e oferece desempenho de consultas rápido e responsivo usando um mecanismo robusto na memória conhecido como SPICE.

**Práticas recomendadas para escrever relatórios**

Elaborar um relatório sólido que fornecerá aos consumidores o que eles precisam para tomar decisões críticas é uma forma de arte. Há algumas etapas para ter sucesso:

1. Coletar dados, fatos, itens de ação e conclusões.
2. Identificar o público, as expectativas dele e o método apropriado de entrega.
3. Identificar os estilos de visualização e o estilo de relatório que melhor atendem às necessidades do público.
4. Criar os relatórios e painéis.
