# GIT & GitHub

**COMANDOS INICIAIS DO GIT**


**PARA CLONAR OU INICIAR UM REPOSITÓRIO GIT**

  - git init -> inicia um novo repositório **git**.
  
  - git status -> verifica o *status* do repositório atual.
  
  - git clone url -> clona o repositório criado no **GITHUB**.


**PARA ATUALIZAR UM REPOSITÓRIO JÁ EXISTENTE**

  - git add . .
  
  - git commit -m mensagem.
  
  - git commit -a -m mensagem -> comando que substitui o **add .** .
  
  - git push.
  
  - git push origin branchname.
  
  - git push origin main.


**PARA INCLUIR A BRANCH NO REPOSITÓRIO MAIN**

  - git merge.
  
  - pull request.


**PARA CRIAR UM STASH**

o **stash** salva um código em outro arquivo, sem alterar a **branch**

- git stash.

- git stash list -> verificar lista de stash.

- git stash apply <0>.

- git stash nome.

- git stash show -p <0>.

- git stash clear -> limpa totalmente as **stash** de uma **branch** .

- git stash drop nome -> deletar uma **stash** específica.


**PARA CRIAR UMA TAG**

 - git tag -a nomedatag -m "msg” -> cria uma _tag_ na **branch** .


**COMANDOS EXTRAS**

  - git branch -> mostra as branchs do repositório.
  
 - git checkout.
  
 - git checkout -b branchname -> cria uma nova **branch** e faz o **checkout** .
  
 - git cherry-pick -> copiar **commits** .
  
 - git squash -> reune **commits** .
  
 - git log -> Historico de **commits** .
  
 - git reset -> voltar uma modificação por vez.
  
 - git reset —hard commit.
  
 - git reset —hard origin/master.
  
 - git ignore -> ignora **files** e **pastas** .

## Fluxo de Trabalho Básico

1. `git init`: inicialize um repositório Git em seu projeto (apenas uma vez).
2. Faça alterações nos arquivos do projeto.
3. `git add [arquivo]`: adicione os arquivos modificados ao staged area.
4. `git commit -m "mensagem"`: crie um commit com uma mensagem descritiva para registrar as alterações.
5. Continue fazendo alterações e criando commits conforme necessário.
6. `git push`: envie seus commits para um repositório remoto para compartilhar com outras pessoas ou fazer backup.
