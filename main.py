import pdfplumber
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Função para extrair texto de um PDF
def extrair_texto_pdf(caminho_pdf):
    with pdfplumber.open(caminho_pdf) as pdf:
        texto = ''
        for pagina in pdf.pages:
            texto += pagina.extract_text()
    return texto

# Função para processar o texto com o modelo spaCy
def processar_texto(texto):
    nlp = spacy.load('pt_core_news_sm')  # Modelo para Português
    doc = nlp(texto.upper())  # Converte todo o texto para MAIÚSCULO
    return [token.text for token in doc if not token.is_stop and not token.is_punct]

# Função para calcular a similaridade entre currículo e vaga usando TF-IDF
def calcular_similaridade(curriculo, vaga):
    vetorizer = TfidfVectorizer()
    tfidf = vetorizer.fit_transform([curriculo, vaga])
    similaridade = cosine_similarity(tfidf[0:1], tfidf[1:2])
    return similaridade[0][0]

# Função para pontuar o currículo com base na similaridade
def pontuar_curriculo(similaridade):
    if similaridade > 0.8:
        return "Muito adequado"
    elif similaridade > 0.5:
        return "Adequado"
    else:
        return "Não adequado"

# Função para verificar palavras-chave da vaga
def verificar_palavras_chave(curriculo_tokens, palavras_chave):
    presentes = []
    ausentes = []
    tokens_upper = [token.upper() for token in curriculo_tokens]  # Padronização
    for palavra in palavras_chave:
        palavra_upper = palavra.upper()
        if any(palavra_upper in token for token in tokens_upper):
            presentes.append(palavra)
        else:
            ausentes.append(palavra)
    return presentes, ausentes

# Caminho do PDF
caminho_pdf = "./CurriculoLeonardoNovaes.pdf"

# Passo 1: Extrair texto do currículo
curriculo_texto = extrair_texto_pdf(caminho_pdf)

# Passo 2: Processar o texto
curriculo_tokens = processar_texto(curriculo_texto)

# Texto da vaga
vaga_texto = """
• Sólido conhecimento em Python e experiência prática com o framework Django.
• Capacidade de trabalhar de forma autodidata, resolvendo problemas técnicos e aprendendo novas tecnologias quando necessário.
• Experiência com APIs RESTful, integrações de sistemas e banco de dados relacionais.
• Organização e atenção aos detalhes para manter o código limpo e a arquitetura bem planejada.
• Mentalidade orientada para resultados, com proatividade e resiliência para enfrentar desafios técnicos.
"""

# Passo 3: Calcular similaridade
similaridade = calcular_similaridade(" ".join(curriculo_tokens), vaga_texto.upper())  # Vaga também em caixa alta

# Passo 4: Pontuar
pontuacao = pontuar_curriculo(similaridade)

# Palavras-chave da vaga (originais, mas o código compara em MAIÚSCULO)
palavras_chave = [
    "python", "django", "autodidata", "rest", "api", "banco de dados",
    "relacional", "sql", "organização", "detalhes", "resultados", "proatividade", "resiliência"
]

# Verificação das palavras-chave
presentes, ausentes = verificar_palavras_chave(curriculo_tokens, palavras_chave)

# Exibição dos resultados
print(f"📊 Similaridade entre currículo e vaga: {similaridade:.2f}")
print(f"📌 Pontuação do currículo: {pontuacao}\n")

print("🔍 Palavras-chave encontradas no currículo:")
for palavra in presentes:
    print(f"✅ {palavra}")

print("\n🚫 Palavras-chave não encontradas no currículo:")
for palavra in ausentes:
    print(f"❌ {palavra}")
