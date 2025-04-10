
# 📄 Analisador de Currículo com Similaridade e Palavras-chave

Este projeto em Python tem como objetivo analisar o conteúdo de um currículo em PDF e compará-lo com a descrição de uma vaga de emprego. Ele utiliza técnicas de **Processamento de Linguagem Natural (PLN)** para calcular a **similaridade textual** e verificar a **presença de palavras-chave** importantes no currículo.

---

## 🧰 Tecnologias Utilizadas

- **Python 3**
- [pdfplumber](https://github.com/jsvine/pdfplumber): Para extração de texto de arquivos PDF
- [spaCy](https://spacy.io/): Para processamento de linguagem natural
- [scikit-learn](https://scikit-learn.org/): Para vetorização TF-IDF e cálculo de similaridade

---

## 📦 Instalação

Antes de tudo, instale as dependências com:

```bash
pip install pdfplumber spacy scikit-learn
python -m spacy download pt_core_news_sm
```

---

## 🧠 Como o Programa Funciona

### 1. **Extração de Texto do Currículo**
```python
def extrair_texto_pdf(caminho_pdf):
```
Utiliza `pdfplumber` para abrir o arquivo PDF e extrair o texto de todas as páginas.

---

### 2. **Processamento do Texto com spaCy**
```python
def processar_texto(texto):
```
- Usa o modelo `pt_core_news_sm` da biblioteca spaCy para processar o texto.
- Remove **stopwords** (palavras comuns e irrelevantes) e **pontuações**.
- Converte tudo para **maiúsculo** para facilitar as comparações.

---

### 3. **Cálculo da Similaridade entre Currículo e Vaga**
```python
def calcular_similaridade(curriculo, vaga):
```
- Utiliza o **TF-IDF Vectorizer** do `scikit-learn` para transformar os textos em vetores numéricos.
- Calcula a **similaridade do cosseno** entre o currículo e a vaga.
- Retorna um valor entre `0` e `1`, indicando o quão parecidos os textos são.

---

### 4. **Classificação da Similaridade**
```python
def pontuar_curriculo(similaridade):
```
Baseado no valor da similaridade:
- Acima de 0.8 → **"Muito adequado"**
- Entre 0.5 e 0.8 → **"Adequado"**
- Abaixo de 0.5 → **"Não adequado"**

---

### 5. **Verificação de Palavras-chave**
```python
def verificar_palavras_chave(curriculo_tokens, palavras_chave):
```
- Verifica se as **palavras-chave** da vaga estão presentes no currículo processado.
- Classifica as palavras como **presentes** ou **ausentes**.
- Ignora diferenças de maiúsculas/minúsculas.

---

## 📁 Exemplo de Uso

### PDF do Currículo
```python
caminho_pdf = "./CurriculoLeonardoNovaes.pdf"
```

### Texto da Vaga
```python
vaga_texto = """
• Sólido conhecimento em Python e experiência prática com o framework Django.
...
"""
```

### Palavras-chave Relevantes
```python
palavras_chave = [
    "python", "django", "autodidata", "rest", "api", "banco de dados",
    "relacional", "sql", "organização", "detalhes", "resultados", "proatividade", "resiliência"
]
```

---

## ✅ Saída Esperada

Exemplo de saída no terminal:
```
📊 Similaridade entre currículo e vaga: 0.73
📌 Pontuação do currículo: Adequado

🔍 Palavras-chave encontradas no currículo:
✅ python
✅ django
✅ api
...

🚫 Palavras-chave não encontradas no currículo:
❌ rest
❌ relacional
❌ proatividade
...
```

---

## 🎯 Objetivo

O objetivo é ajudar recrutadores e candidatos a avaliarem de forma rápida e automatizada se um currículo é compatível com uma vaga de emprego, identificando pontos fortes e fracos em relação ao perfil desejado.

---

## 🤖 Melhorias Futuras

- Interface gráfica (GUI) com `tkinter` ou `streamlit`
- Suporte a múltiplos currículos e múltiplas vagas
- Exportação dos resultados em CSV ou PDF
- Detecção de sinônimos com spaCy ou WordNet
