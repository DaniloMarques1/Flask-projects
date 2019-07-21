## Usando JSON WEB TOKEN com o flask_jwt_extended

### Para conseguir um token enviar os dados (email, password) para o endpoint /login
Resposta do endpoint em caso de um login válido, http code 200
```json
   {
       "access_token" : "token"
   }
```
Resposta caso não tenha conseguido logar, http code 400
```json
    {
        "message" : "Invalid credentials"
    }
```

### Para retornar informações sobre o usuario atualmente logado (com base no token passado) fazer uma requisição ao endpoint /user
Retorno do endpoint caso o token passado no header seja valido, httpcode 200
```json
    {
        "id" : "id do usuario",
        "name" : "Nome do usuario",
        "email" : "email@dousuario"
    }
```
Resposta caso o token não seja válido, httpcode 401
```json
    {
        "message" : "Invalid token access"
    }
```

A lib do jwt tem um comportamento padrão para caso o token seja inválido ou tenha expirado, mas podemos (e vamos) modificar esse comportamento.  
Retorno padrão caso o token nao seja válido, httpcode 401 ou 422
```json
    {
        "msg" : "Why the token is not valid"
    }
```
