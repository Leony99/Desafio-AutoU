# Classificador Inteligente de Emails – Desafio AutoU

## Objetivo
Esta aplicação foi desenvolvida como solução para o **Desafio Técnico AutoU**. O objetivo é automatizar a **leitura, classificação e sugestão de respostas para emails corporativos**, reduzindo esforço manual de equipes que lidam com alto volume de mensagens.

A aplicação utiliza **Inteligência Artificial** para classificar emails como **Produtivos** ou **Improdutivos** e sugerir uma resposta adequada para cada caso.

## Funcionalidades

- 📄 Upload de emails nos formatos **.txt** e **.pdf**
- ✍️ Inserção direta de texto do email
- 🤖 Classificação automática:
  - **Produtivo** (requer ação ou resposta)
  - **Improdutivo** (não requer ação)
- 💬 Sugestão de resposta automática baseada no conteúdo
- 📋 Botão para copiar a resposta sugerida
- 🌙 Modo claro / escuro
- ⚡ Interface rápida, simples e responsiva

## Tecnologias Utilizadas

### Backend
- **Python 3.11**
- **FastAPI** – API REST
- **Uvicorn** – servidor ASGI
- **OpenAI API** – classificação e geração de respostas
- **PyPDF2** – leitura de PDFs

### Frontend
- **HTML5/CSS3/JS**
- **Tailwind CSS (CDN)**

## Como rodar o projeto localmente

### 🔹 Pré-requisitos
- Python 3.11+
- Chave de API da OpenAI

### 🔹 Backend

```bash
cd Backend

python -m venv venv

source venv/bin/activate  #Windows: venv\Scripts\activate

pip install -r requirements.txt

python -m spacy download pt_core_news_sm
```

Crie um arquivo `.env`:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxx
```

Inicie o servidor:

```bash
uvicorn app.main:app --reload
```

A API estará disponível em:
```
http://127.0.0.1:8000
```

### 🔹 Frontend

Basta abrir o arquivo:

```
Frontend/index.html
```

Nenhuma instalação adicional é necessária.

## Exemplo de Uso

1. Cole o texto de um email **ou** envie um arquivo `.txt` / `.pdf`
2. Clique em **Classificar email**
3. Veja a categoria atribuída
4. Copie a resposta sugerida com um clique

## Autor

**Leony Costa**  
Desafio Técnico – AutoU
