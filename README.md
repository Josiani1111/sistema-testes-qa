# Sistema de Testes e Qualidade de Software

Projeto desenvolvido em Python com foco em testes automatizados e qualidade de software, utilizando a biblioteca pytest.

## Objetivo

Praticar conceitos de Quality Assurance (QA), validação de funcionalidades e identificação de comportamentos incorretos por meio de testes automatizados.

## Funcionalidades

- Soma de números
- Subtração de números
- Multiplicação de números
- Divisão de números
- Tratamento de divisão por zero
- Testes com números negativos
- Testes com números decimais
- Validação de resultados esperados

## Tecnologias utilizadas

- Python 3.14
- pytest 9.1.1
- Git e GitHub

## Estrutura do projeto

```text
sistema-testes-qa/
├── src/
│   └── calculadora.py
├── tests/
│   └── test_calculadora.py
├── requirements.txt
└── README.md
```

## Como executar o projeto

### 1. Instalar as dependências

```bash
py -m pip install -r requirements.txt
```

### 2. Executar os testes

```bash
py -m pytest -v
```

## Resultado dos testes

Os 10 testes automatizados foram executados com sucesso.

```text
10 passed
```

## Aprendizados

- Criação e execução de testes automatizados
- Uso de assert para validar resultados
- Validação de exceções com pytest
- Testes de casos comuns e situações especiais
- Organização básica de um projeto Python

## Autora

Estudante do último ano de Análise e Desenvolvimento de Sistemas.
