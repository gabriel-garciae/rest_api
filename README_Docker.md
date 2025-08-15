# Configuração do PostgreSQL com Docker

Este projeto inclui configuração para rodar PostgreSQL em um container Docker, permitindo conexão via DBeaver ou qualquer outro cliente PostgreSQL.

## Pré-requisitos

- Docker instalado
- Docker Compose instalado
- DBeaver ou outro cliente PostgreSQL

## Configuração Rápida

### 1. Iniciar o Container PostgreSQL

```bash
# Na raiz do projeto
docker-compose up -d
```

### 2. Verificar Status

```bash
docker-compose ps
```

### 3. Parar o Container

```bash
docker-compose down
```

## Configurações do Banco

- **Host**: localhost
- **Porta**: 5432
- **Database**: rest_api_db
- **Usuário**: postgres
- **Senha**: postgres123

## Conexão via DBeaver

1. Abra o DBeaver
2. Clique em "New Database Connection"
3. Selecione "PostgreSQL"
4. Configure:
   - **Host**: localhost
   - **Port**: 5432
   - **Database**: rest_api_db
   - **Username**: postgres
   - **Password**: postgres123
5. Clique em "Test Connection" para verificar
6. Clique em "Finish"

## Estrutura do Banco

O script `init.sql` cria automaticamente:
- Tabela `users` com campos básicos
- Índices para performance
- Trigger para atualizar timestamp automaticamente
- Usuário de exemplo

## Comandos Úteis

```bash
# Ver logs do container
docker-compose logs postgres

# Acessar o container
docker exec -it rest_api_postgres psql -U postgres -d rest_api_db

# Parar e remover volumes (cuidado: apaga todos os dados)
docker-compose down -v

# Reconstruir o container
docker-compose up -d --build
```

## Solução de Problemas

### Porta 5432 já em uso
Se a porta 5432 estiver ocupada, edite o `docker-compose.yml`:
```yaml
ports:
  - "5433:5432"  # Mude para 5433 ou outra porta livre
```

### Erro de conexão
1. Verifique se o container está rodando: `docker-compose ps`
2. Verifique os logs: `docker-compose logs postgres`
3. Aguarde o healthcheck passar (pode levar alguns segundos na primeira execução)

### Reset completo
```bash
docker-compose down -v
docker-compose up -d
```

## Variáveis de Ambiente

Copie `config.env.example` para `config.env` e ajuste as configurações conforme necessário. 