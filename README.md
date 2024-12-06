# Trabalho de Visão Computacional - IA
Projeto criado para disciplina Fundamentos de Inteligência Artificial (FIA) - Graduação. Prof. Pablo De Chiaro
Este projeto configura um ambiente virtual Python e instala as bibliotecas necessárias para um projeto de Visão Computacional.

## Integrantes: 
| Nome    |
|---------|
| Bruno   |
| Lucas   |
| Murilo  |



## O que é o projeto?

- A ideia inicial era um detector de libras, porém, o treinamento do modelo começou a ficar muito longo,
e por isso decidimos fazer somente um Detector de Mãos.

## Como rodar?

1. Criar o ambiente virtual

```python
    python -m venv env-visao
```

2. Ativar o ambiente virtual

```python
    .\env-visao\Scripts\activate
```
3. Ativar o ambiente virtual
    ### Windows
    ```python
        .\env-visao\Scripts\activate
    ```
    ### Linux / MacOS
    ```python
        source env-visao/bin/activate
    ```    

4. Instalar as Dependencias

```python
    pip install -r requirements.txt
```

5. Rodar o Projeto

```python
    python hands_detector.py
```
