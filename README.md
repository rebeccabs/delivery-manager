# Delivery Manager

Sistema web de gerenciamento de entregas desenvolvido com Python, Flask e SQLite, criado para praticar desenvolvimento de software, banco de dados, versionamento com Git/GitHub e deploy em nuvem.

O projeto simula uma operação logística real, permitindo cadastrar, visualizar, atualizar e excluir entregas através de uma interface web moderna e responsiva.

A ideia surgiu a partir da minha experiência profissional com logística e operações de entrega, transformando desafios do dia a dia em um projeto prático para estudo, evolução técnica e construção de portfólio.

## Demonstração Online

Aplicação disponível em:

https://delivery-manager-syqz.onrender.com

## Tecnologias Utilizadas

### Backend

* Python
* Flask
* SQLite

### Frontend

* HTML5
* CSS3
* JavaScript

### Ferramentas

* Git
* GitHub
* VS Code
* Render

## Funcionalidades

### Gestão de Entregas

* Cadastro de entregas
* Listagem de entregas
* Atualização de status
* Exclusão de entregas

### Dashboard

* Total de entregas
* Entregas pendentes
* Entregas em rota
* Entregas concluídas

### Persistência de Dados

* Armazenamento em SQLite
* Integração entre Flask e banco de dados
* Operações CRUD completas

### Interface

* Tema dark personalizado
* Design moderno com efeitos visuais
* Layout responsivo
* Navegação simples e intuitiva

## Estrutura do Projeto

```text
delivery-manager/
│
├── app.py
├── database.py
├── delivery_manager.db
│
├── templates/
│   ├── index.html
│   ├── entregas.html
│   └── cadastro.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── requirements.txt
├── Procfile
└── README.md
```

## Conceitos Praticados

### Desenvolvimento Backend

* Flask
* Rotas
* Templates Jinja2
* Formulários HTML
* Integração com banco de dados

### Banco de Dados

* SQLite
* CRUD
* SELECT
* INSERT
* UPDATE
* DELETE
* WHERE
* COUNT
* GROUP BY

### Frontend

* HTML
* CSS
* JavaScript
* Responsividade
* Manipulação do DOM

### Engenharia de Software

* Organização de código
* Separação de responsabilidades
* Versionamento com Git
* GitHub
* Deploy em nuvem

## Como Executar Localmente

Clone o repositório:

```bash
git clone https://github.com/rebeccabs/delivery-manager.git
```

Entre na pasta:

```bash
cd delivery-manager
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
python app.py
```

Acesse:

```text
http://127.0.0.1:5000
```

## Próximas Melhorias

* Pesquisa de entregas
* Sistema de autenticação
* Entregas vinculadas por usuário
* Dashboard avançado
* Controle de perfis e permissões
* Migração para PostgreSQL

## Objetivo do Projeto

* Desenvolver experiência prática em programação
* Construir um portfólio técnico
* Aprender desenvolvimento backend e full stack
* Aplicar conceitos de banco de dados
* Praticar Git e GitHub
* Realizar deploy de aplicações web
* Simular problemas reais da área logística

## Status

✅ Em desenvolvimento ativo

Versão atual publicada e funcionando online.

## Autora

**Rebecca Bomfim**

Estudante de Engenharia de Software – Universidade Cruzeiro do Sul

GitHub: https://github.com/rebeccabs

LinkedIn: https://www.linkedin.com/in/rebecca-bomfim
