from fastapi import FastAPI, Form, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from app.utils.file_reader import read_txt, read_pdf
from app.utils.text_cleaner import clean_text
from app.utils.nlp_preprocess import preprocess_nlp
from app.services.ai_service import classify_email

app = FastAPI(title="Desafio AutoU - Email Classifier")

# CORS (útil já pensando no frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/classify-email")
async def classify_email_endpoint(
    file: UploadFile = File(None),
    text: str = Form(None)
):
    # Obter texto bruto
    if file:
        filename = file.filename.lower()

        if filename.endswith(".txt"):
            raw_text = await read_txt(file)
        elif filename.endswith(".pdf"):
            raw_text = await read_pdf(file)
        else:
            raise HTTPException(status_code=400, detail="Formato não suportado")
    else:
        raw_text = text or ""

    # Limpeza básica
    cleaned_text = clean_text(raw_text)

    if not cleaned_text:
        return {"error": "Texto vazio"}

    # Pré-processamento NLP (stop words + lemmatização)
    nlp_result = preprocess_nlp(cleaned_text)

    # Classificação com IA (texto natural limpo)
    ai_result = classify_email(nlp_result)

    return {
        "email_text": cleaned_text,
        "category": ai_result["category"],
        "suggested_response": ai_result["suggested_response"]
    }