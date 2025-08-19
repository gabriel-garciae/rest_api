-- create table users

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    empresa VARCHAR(100),
    cargo VARCHAR(100), 
    anos_experiencia INT CHECK (anos_experiencia >= 0),
    salario NUMERIC(12,2) CHECK (salario >= 0),
    is_ativo BOOLEAN DEFAULT true,
    qualidade_servico VARCHAR(50)
);


INSERT INTO users
    (id, nome, empresa, cargo, anos_experiencia, salario, is_ativo, qualidade_servico)
VALUES
    (1, 'Fabio', 'Tech', 'Software Eng', 3, 12345.67, true, 'good');
