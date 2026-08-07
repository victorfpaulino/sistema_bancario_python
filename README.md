# Sistema Bancário em Python

Projeto de estudo com foco em **Programação Orientada a Objetos (POO)** em Python. A ideia é simular as operações básicas de um sistema bancário — criação de contas, depósitos, saques e extrato.

## 💡 Sobre o projeto

Este é um projeto em evolução. O objetivo principal aqui não é reinventar um sistema bancário real, mas sim praticar POO de forma consistente: modelar entidades do mundo real (conta, conta corrente, conta poupança) como classes, entender relações de herança entre elas e organizar a lógica de negócio de forma clara.

## 🏗️ Estrutura atual

- `conta.py` — classe base de conta, com os atributos e métodos comuns (saldo, depósito, saque, extrato).
- `conta_corrente.py` — conta corrente, herda de `Conta` e adiciona regras específicas (ex: limite de saque).
- `conta_poupanca.py` — conta poupança, herda de `Conta` com suas próprias regras (ex: rendimento).
- `main.py` — ponto de entrada / execução do sistema.

## 🚀 Próximos passos

Este projeto vai continuar evoluindo. Os próximos passos planejados são:

- [ ] Criar uma camada simples de "banco de dados" usando arquivo `.txt`, para persistir usuários e contas entre execuções (ao invés de perder tudo ao fechar o programa).
- [ ] Adicionar cadastro de usuários vinculado às contas.
- [ ] Melhorar a validação de operações (saldo insuficiente, valores inválidos, etc).
- [ ] Cobrir o projeto com testes.

## ▶️ Como rodar

```bash
git clone https://github.com/victorfpaulino/sistema_bancario_python.git
cd sistema_bancario_python
python main.py
```

Não há dependências externas — usa apenas Python puro.

## 🎯 O que este projeto demonstra

- Aplicação prática de herança e polimorfismo em Python.
- Organização de um projeto pequeno em múltiplos módulos/classes.
- Evolução incremental de um projeto de estudo (do script simples até, futuramente, persistência de dados).

---

Projeto de estudo, feito por [Victor Paulino](https://github.com/victorfpaulino).
