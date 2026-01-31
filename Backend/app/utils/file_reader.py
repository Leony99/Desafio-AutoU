from pypdf import PdfReader
from io import BytesIO

async def read_txt(file) -> str:
    content = await file.read()
    return content.decode("utf-8", errors="ignore")

async def read_pdf(file):
    content = await file.read()
    pdf_file = BytesIO(content)
    reader = PdfReader(pdf_file)

    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""

    return text