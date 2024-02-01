Sim, é possível reutilizar containers no Docker. 
Para reiniciar um container que está parado, pode ser utilizado o comando:

```
docker start <NOME_DO_CONTAINER> 
```
No caso:
```
docker start carguru
```
ou

O comando ```docker restart <NOME_DO_CONTAINER>```, que é usado para reiniciar um ou mais containers que estão em execução no ambiente Docker. Ele difere do comando docker start porque não apenas inicia um container parado, mas também reinicia containers que já estão em execução.
