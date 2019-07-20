## Criando uma api usando flask manualmente.

### Endpoint /user/<id> 
Retorna informações sobre um usuario especifico

```json
    {
        "id" : "user_id",
        "name" : "Name of the user",
        "email" : "email@domain"
    }
```
### Endpoint /users
Retorna uma lista com todos os ususarios

```json
    [
        {
            "id" : "user_id",
            "name" : "Name of the user",
            "email" : "email@domain"
        },       
        {
            "id" : "user_id",
            "name" : "Name of the user",
            "email" : "email@domain"
        }
    ]
```

### Endpoint /addUser 
Utiliza o metodo post e insere um usuario retornando a nova lista com o novo usuario inserido
Json do request
```json
{
    "name" : "Name of the new user",
    "email" : "email@domain"
}
```
Json da resposta

```json
    [
        {
            "id" : "user_id",
            "name" : "Name of the user",
            "email" : "email@domain"
        },
        {
            "id" : "user_id",
            "name" : "Name of the user",
            "email" : "email@domain"
        },
        {
            "id" : "user_id",
            "name" : "Name of the new user",
            "email" : "email@domain"
        }
    ]
```
