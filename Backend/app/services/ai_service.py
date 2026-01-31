import os
import json
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_email(text: str) -> dict:
    prompt = f"""
        Você é um assistente corporativo que classifica emails recebidos por uma empresa.

        Classifique o email abaixo:

        1. Classifique em APENAS UMA categoria:
        - Produtivo: requer ação ou resposta de algum agente, como pedidos, dúvidas, solicitações ou questionamentos...
        - Improdutivo: não requer nenhuma ação.

        2. Se for PRODUTIVO, identifique a intenção principal:
        - status_chamado
        - envio_arquivo
        - duvida_sistema
        - solicitacao_geral
        - outros

        Depois, gere uma resposta automática seguindo estas regras:

        GERAL:
        - A resposta deve ser direcionada ao remetente do email
        - Tom educado, profissional e corporativo
        - Não repetir literalmente o texto do email

        SE PRODUTIVO:
        - Confirmar recebimento
        - Informar que a solicitação será analisada
        - Não prometer prazos ou soluções específicas
        - Basear a resposta neste template por intenção:
        - status_chamado:
        "Recebemos sua mensagem e vamos verificar o status do chamado. Retornaremos assim que houver uma atualização."
        - envio_arquivo:
        "Recebemos o material enviado. Vamos analisá-lo e retornaremos se houver necessidade de mais informações."
        - duvida_sistema:
        "Recebemos sua dúvida e iremos analisá-la. Retornaremos com as orientações necessárias."
        - solicitacao_geral:
        "Recebemos sua solicitação e ela será analisada. Retornaremos assim que possível."
        - outros:
        "Recebemos sua solicitação e ela será analisada. Retornaremos assim que possível."

        SE IMPRODUTIVO:
        - Apenas agradecer ou retribuir a gentileza
        - Basear a resposta neste template:
        "Agradecemos sua mensagem! Desejamos um ótimo dia."

        Responda SOMENTE com um JSON válido.
        NÃO use markdown.
        NÃO escreva nada fora do JSON.

        Formato EXATO:
        {{
            "category": "Produtivo ou Improdutivo",
            "intent": "status_chamado | envio_arquivo | duvida_sistema | solicitacao_geral | outros | null",
            "suggested_response": "resposta final"
        }}

        Email:
        \"\"\"{text}\"\"\"
        """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    raw = response.choices[0].message.content.strip()

    # Remove ```json ``` se vier (fallback)
    raw = re.sub(r"```json|```", "", raw).strip()

    return json.loads(raw)
