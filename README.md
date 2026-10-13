# Sistema de Testes e Qualidade de Software

Projeto desenvolvido em Python com foco em testes automatizados, validação de funcionalidades e qualidade de software, utilizando a biblioteca pytest.

## Objetivo

Praticar conceitos de Quality Assurance (QA), desenvolver testes automatizados e verificar o comportamento de funções em situações comuns e excepcionais.

## Funcionalidades

- Soma, subtração, multiplicação e divisão
- Tratamento de divisão por zero
- Testes com números negativos e decimais
- Validação de resultados esperados
- Teste de entrada inválida: texto no lugar de número
- Verificação de exceções com pytest

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

### 2. Executar os testes automatizados

```bash
py -m pytest -v
```

## Resultado dos testes

Os 11 testes automatizados foram executados com sucesso.

```text
11 passed
```

## Aprendizados

- Criação e execução de testes automatizados
- Uso de `assert` para validar resultados
- Validação de exceções com `pytest.raises`
- Testes com entradas válidas e inválidas
- Identificação de comportamentos inesperados
- Organização de um projeto Python
- Controle de versão com Git e publicação no GitHub

## Autora

Estudante do último ano de Análise e Desenvolvimento de Sistemas.

**GitHub:** https://github.com/Josiani1111
