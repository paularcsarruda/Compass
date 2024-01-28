# Docker

## O que é Docker?

O Docker é uma plataforma de software livre que permite aos desenvolvedores desenvolver, implementar, executar, atualizar e gerenciar componentes de *contêineres* executáveis e padronizados que combinam o código-fonte de aplicativos com as bibliotecas e estruturas do sistema operacional (S.O.) necessárias para executar o código em qualquer ambiente.

## Por quê utilizar o Docker?

- O **Docker proporciona mais velocidade na configuração do ambiente** de um desenvolvedor.
- Pouco tempo gasto em manutenção, containers são executados como configurados
- Performance para executar aplicação, mais performático que uma vm
- NOs livra da **Matrix from Hell**

## Primeiro Teste - Containers

`docker run` docker/whalesay `cowsay` Hello_world

# Containers

### **Como os contêineres funcionam**

A **tecnologia de contêineres oferece todas as funcionalidades e os benefícios das máquinas virtuais, incluindo isolamento de aplicativos, ajuste de escala com custo reduzido e descartabilidade**, além de outras vantagens importantes:

- **Mais leve:** ao contrário das VMs, os contêineres não hospedam a carga útil de uma instância inteira de sistemas operacionais e hypervisors. Estes incluem apenas os processos e as dependências do sistema operacional que são necessários para executar o código. Seu tamanho é medido em megabytes (em vez de em gigabytes, como em algumas VMs), fazem melhor uso da capacidade de hardware e oferecem tempos de inicialização mais rápidos.
- **Melhor produtividade do desenvolvedor:** aplicativos em contêineres podem ser gravados uma vez e executados em qualquer lugar. E, comparados às VMs, a implementação, o provisionamento e a reinicialização dos contêineres ocorre de maneira mais simples e rápida. Isso os torna ideais para uso em pipelines de [integração contínua](https://www.ibm.com/br-pt/topics/continuous-integration) e [entrega contínua](https://www.ibm.com/br-pt/topics/continuous-delivery) (CI/CD) e mais adequados para equipes de desenvolvimento que adotam práticas de [DevOps](https://www.ibm.com/br-pt/topics/devops) e Agile.
- **Maior eficiência de recursos:** os contêineres permitem aos desenvolvedores executar várias vezes no mesmo hardware o mesmo número de cópias de um aplicativo que as VMs. Isso pode reduzir seus gastos com a cloud.

## Definindo o nome do Container

- podemos definir o nome usando a flag `--name`
- se não colocarmos o nome, receberemos um nome aleatório
- a flag é inserida junto do comando run: `docker run -- name <NAME>`

# Comandos Básicos

`docker version` → verifica a versão

`docker --help`

`docker run` → roda Containers, sempre inicia um novo Container

**`docker run -it ubuntu` -> roda o terminal do Ubuntu**

`exit` → para a execução

`docker ps` ou `docker container ls` → exibe quais **Containers** estão sendo executados no momento;

`flag -a` -> temos também todos os **Containers** já executados na máquina e.g.: `docker ps -a`

`Flag -it` → rodar **Container** e deixá-lo executando no terminal

`docker stop <id ou nome>` → parar o Container

`docker start <id>` → inicia o Container

## Verificando Logs

- podemos verificar o que aconteceu em um Container, utilizando: `docker logs <id>`
- assim, as últimas ações realizadas no Container serão exibidas no terminal

## Removendo Containers

- podemos remover um Container da máquina, utilizando: `docker -rm <id>`
- se o Container ainda estiver rodando podemos utilizar a `flag -f`(force)

# Imagens

## O que são Imagens?

Uma imagem do Docker, ou imagem de contêiner, é um arquivo executável independente usado para criar um contêiner. Essa imagem de contêiner contém todas as bibliotecas, dependências e arquivos de que o contêiner precisa para ser executado. Uma imagem do Docker é compartilhável e portátil, então você pode implantar a mesma imagem em vários locais ao mesmo tempo, da mesma forma que um arquivo binário de software.

## Como escolher uma boa Imagem

- podemos fazer o download das imagens em https://hub.docker.com

## Criando uma Imagem

- para criar uma imagem vamos precisar de um arquivo Dockerfile em uma pasta que ficará o projeto
- esse arquivo vai precisar de algumas instruções para ser executado
- **FROM:** imagem base
- **WORKDIR:** diretório da aplicação
- **EXPOSE:** porta da aplicação
- **COPY:** quais arquivos precisam ser copiados

# Docker Swarn

# YAML

O YAML é uma linguagem legível de serialização de dados muito usada na escrita de arquivos de configuração. Dependendo, a sigla YAML pode significar em inglês yet another markup language (mais uma linguagem de marcação) ou YAML ain’t markup language (YAML não é linguagem de marcação) [acrônimo recorrente]. Ambos destacam que o YAML é voltado para os dados, e não documentos.

```
# Para comentários basta usar o caractere (#).
# Yaml não permite
# multiplas linhas em comentário.
```

Podemos ter **strings, null, integers, floats e booleanos.** As strings podem ser com ou sem aspas duplas (“ ”) ou únicas (‘ ’), geralmente use elas quando se tem caracteres especiais.

```
#Doc 1
---# Start
tipo: "Teste"# ou 'Teste' ou teste
teste: true
numero: 1
nulo: null
...# End
```

Para data é seguido o padrão ISO 8601. (yyyy-mm- ddThh:mm:ss.ffffff)

Note que é importante indentar o código com espaços.

```
#Doc 2
---
pessoa:
nome: &nome Fulano
sobrenome: Cicrano
idade: 45
data_nascimento: 1974-05-13 09:25:55
"estado civil": null
masculino: true

hobbies:
-'andar de bicicleta'
- patinar
-nadar
```

As listas podem conter *colchetes* ([]), e caso precisar pode usar uma estrutura parecida com dicionário em python ({}) com *chaves* para o item *‘chave:valor’* os membros da lista são indicados por (-) *hífen.*

```
nadar: ["Praia", "Piscina", "Lago"]
amigos:
- nome: "João"
idade: 25
- {nome: "Eduardo",idade: 24}                           -
-
nome: "Frederico"
    idade: 26
```

Caso queira que o YAML leia mais de uma linha em uma chave pode ser usado o caractere *maior* (>), no retorno ele junta tudo e retorna uma linha somente. Quando se usa o *pipe* (|) ele retorna com varias linhas de acordo com a estrutura que foi criada. [Aqui](https://rollout.io/blog/yaml-tutorial-everything-you-need-get-started/) tem uns exemplos bons.

```
descricao:>
  Aqui tem algumas caracteristicas do fulano,
  ele possui 45 anos e tem alguns amigos.
  Ele adora esportes.

assinatura:|
  Fulano
  Cicrano Org
  email - cicrano.fulano@gmail.comid:*nome
...
```

# Kubernetes ‘K8S’

## O que são Kubernetes?

Originates from Ancient Greek, meaning 'helmsman' or 'pilot’

- uma **ferramenta de orquestração de containers**
- permite a criação de múltiplos containers em diferentes máquinas (nodes)
- escalando projetos, **formando um cluster**
- gerencia serviços, garantindo que as aplicações sejam executadas sempre da mesma forma
- criada pelo **google**

## Conceitos Fundamentais

- **Control Plane:** onde é gerenciado o controle dos processos dos **Nodes**
- **Nodes:** máquinas que são gerenciadas pelo control plane
- **Deployment:** a execução de uma imagem/projeto de um Pod
- **Pod:** um ou mais containers que estão em um Node
- **Services:** serviços que expõe os Pods ao mundo externo
- **Kubectl:** cliente de linha de comando para Kubernetes

## Dependências Necessárias

- o Kubernetes pode ser executado de uma maneira simples em nossa máquina
- vamos precisar do client Kubectl, que é uma maneira de executar o Kubernetes
- e também o Minikube, **uma espécie de simulador** de Kubernetes, para não precisarmos de vários computadores/servidores

## Iniciando o Minikube

- para inicializar o Minikube vao=mos utilizar o comando `minikube start --drive=<DRIVE>`
- onde o driver vai depender de como foi a sua instalação das dependÊncias e por qualquer um deles atingiremos os mesmos resultados
- pode ser utilizado o docker ou VM's
- podemos testar o minikube com: `minikube status`

## Comandos

- `minikube start --driver=docker` → inicializa o minikube
- `minikube status`
- `minikube stop`
- para **iniciar novamente repete o comando start**

# Acessando a Dashboard do Kubernetes

- o minikube nos disponibiliza uma dashboard
- onde podemos ver todo o detalhamento do nosso projeto: serviços, pods, etc.
- comando: `minikube dashboard`
- ou para apenas obter a URL: `minikube dashboard --url`

## Deployment teoria

- o **Deployment** é uma parte fundamental do **Kubernetes**
- como ele criamos nosso serviço que vai rodar nos **pods**
- definimos uma **imagem e um nome**, para posteriormente ser replicado entre os servidores
- a partir da criação dos Deployment teremos containers rodando
- vamos precisar de uma imagem no Hub do Docker, para gerar um Deployment

## Criar Deployment

- para rodar o projeto no Kubernetes é necessário um Deployment, que é onde rodamos os containers das aplicações no Pods
- o comando é: `kubectl create deployment <NOME> --image=<IMAGEM>`
- desta forma, o projeto de Flask estará sendo orquestrado pelo Kubernetes

## Checando Deployments

- para verificar o Deployment: `kubectl get deployments`
- para verificar detalhes: `kubectl describe deployments`
- desta forma conseguimos saber se o projeto está de fato rodando e também o que está rodando neles

## Checando Pods

- os Pods também são componentes muito importantes, é o local onde os Containers são executados
- para verificar os Pods utilizamos: `kubectl get pods`
- para verificar detalhes: `kubectl describe pods`
- desta forma recebemos o status dos Pods que estão ligados e também informações importantes sobre eles

## Configurações do Kubernetes

- podemos verificar como o Kubernetes está configurado utilizando:
- `kubectl config view`
- desta forma receberemos informações importantes baseadas no Minikube, que é por onde o Kubernetes está sendo executado

## Service Teoria

- as apps de Kubernetes não tem conexão com o mundo externo
- por isso é necessário a criação de um Service, que é o que possibilita expor os Pods
- o Service é uma entidade separada dos Pods, que expões eles a uma rede

## Criando um Service

- para criar um serviço e expor nossos Pods: `kubectl expose deployment <NOME> --type=<TIPO> --port=<PORT>`
- colocaremos o nome do Deployment já criado
- o tipo de Service, há vários para utilizarmos, porém o LoadBalancer é o mais comum, onde todos os Pods são expostos
- e uma porta para o serviço ser consumido

## Verificando nossos Services

- podemos obter detalhes dos Services já criados, utilizando: `kubectl get services`
- e obter informações de um Service específico com: `kubectl descrive services/<NOME>`

## Replicando a Aplicação

- podemos utilizar outros Pods e replicar nossa aplicação
- o comando é: `kubectl scale deployment/<NOME> --replicas=<NUMERO>`
- podemos agora verificar no Dashboard o aumento de Pods
- e também com o comando de: `kubectl get pods`

## Verificando o número de Réplicas

- `kubectl get rs`
- desta maneira temos os status das réplicas dos projetos

## Diminuindo a Escala

- podemos facilmente diminuir o número de Pods
- esta técnica é chamada de scale down
- `kubectl scale deployment/<NOME> --replicas=<NUMERO_MENOR>`

## Atualização da Imagem

- para atualizar a imagem vamos precisar do nome do Container, isso é dado na Dashboard dentro do Pod
- e também a nova imagem deve ser uma outra versão da atual, precisamos subir uma nova tag no Hub
- depois utilizar o comando: `kubectl set image deployment/<NOME> <NOME_CONTAINER>=<NOVA_IMAGEM>`

## Desfazer alteração

- para desfazer uma alteração utilizamos uma ação conhecida como rollback
- o comando para verificar a alteração é: `kubectl rollout status deployment/<NOME>`
- com ele e com o `kubectl get pods`, podemos identificar problemas
- para voltar a alteração utilizamos: `kubectl rollout undo deployment/<NOME>`

## Deletar um Service

- para deletar um Service, utilizamos o comando: `kubectl delete service <NOME>`

## Deletando um deployment

- para deletar um deployment, utilizamos o comando: `kubectl delete deployment <NOME>`

## Modo Declarativo

- o modo declarativo é guiado por um arquivo, semelhante ao Docker Compose
- dessa forma tornamos nossas configurações mais simples e centralizamos tudo em um comando
- também escrevemos em YAML o arquivo de Kubernetes

## Chaves mais utilizadas

- **apiVersion:** versão utilizada da ferramenta
- **kind:** tipo de arquivo (Deployment, Service)
- **metadata:** descrever algum objeto, inserindo chaves como name
- **replicas:** número de réplicas de Nodes/Pods
- **containers:** definir as especificações de containers como: nome e imagem

## Criando o arquivo

- para transformar o projeto em declarativo, vamos criar um arquivo para realizar o Deployment
- Desta maneira vamos aprender a criar os arquivos declarativos e utilizar as chaves e valores

## Executando arquivo de Deployment

- o comando para executar o arquivo é: `kubectl apply -f<ARQUIVO>`
- desta maneira o Deployment será criado conforme configurado no arquivo YAML

## Parando o Deployment

- para parar de executar o deployment baseado em arquivo, o declarativo, utilizamos também o delete
- o comando é `kubectl delete -f<ARQUIVO>`
- desta maneira, teremos os Pods sendo excluídos e o serviço finalizado

## Criando o Serviço

- para criar o Serviço declarativo temos que criar um arquivo para realizar o Service(kind)

## Executando o Serviço

- o comando é `kubectl apply -f <ARQUIVO>`
- Obs.: precisamos gerar o IP de acesso com `minikube service <NOME>`

## Parando o Serviço

- o comando é o `kubectl delete -f <ARQUIVO>`
- desta maneira o serviço não estará mais disponível, e perderemos acesso ao projeto

## Atualizando o Projeto no Declarativo

- primeiro temos que criar uma nova versão da imagem
- e fazer o `push` para o Hub
- depois é só alterar no arquivo de Deployment a `tag`
- e reaplicar o comando de `apply`

## Unindo Arquivos do Projeto

- vamos precisar unior o deployment e o service em um único arquivo
- a separação de objetos para o YAML é com: `---`
- desta forma, cada um deles será executado
- uma boa prática é colocar o service antes do deployment