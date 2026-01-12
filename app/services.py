import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# Cargar entorno
load_dotenv()

# Configuración IA
llm = ChatGroq(temperature=0, model_name="llama-3.1-8b-instant")

# Listas Maestras de BBDD
CATEGORIAS = ["Error Software", "Normativa ISO/ANSI", "Modelado 3D", "Planos 2D", "Licencias"]
SENTIMIENTOS = ["Positivo", "Neutro", "Negativo", "Enfadado/Frustrado"]
URGENCIAS = ["Baja", "Media", "Alta", "Crítica"]

def analizar_duda_con_ia(texto_usuario):
    print(f"🧠 [IA Service] Analizando: '{texto_usuario}'")
    
    # prompt del sistema. Reglas de funcionamiento 
    system_prompt = f"""
    Eres el Asistente Técnico del CAU de Ingeniería.
    
    TUS REGLAS DE ORO:
    1. SOLO respondes preguntas sobre CATIA, SolidWorks, AutoCAD, Ingeniería o Soporte TI.
    2. Si el usuario pregunta sobre cocina, deportes, política o cualquier tema no técnico:
       - Responde AMABLEMENTE: "Disculpa, solo estoy capacitado para resolver dudas de ingeniería y software CAD."
       - Clasifica la incidencia como: Categoria="Error Software", Sentimiento="Neutro", Urgencia="Baja".
    
    3. Si la pregunta es técnica:
       - Responde de forma breve y profesional.
       - Clasifica eligiendo UNA opción de cada lista.

    LISTAS VÁLIDAS:
    - Categorías: {CATEGORIAS}
    - Sentimientos: {SENTIMIENTOS}
    - Urgencias: {URGENCIAS}
    
    DEBES RESPONDER EXCLUSIVAMENTE EN FORMATO JSON:
    {{{{
        "respuesta": "tu respuesta al usuario...",
        "categoria": "opcion exacta...",
        "sentimiento": "opcion exacta...",
        "urgencia": "opcion exacta..."
    }}}}
    """
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{consulta}")
    ])
    
    chain = prompt | llm | JsonOutputParser()
    
    try:
        resultado = chain.invoke({"consulta": texto_usuario})
        return resultado
    except Exception as e:
        print(f"❌ Error en Groq: {e}")
        # Respuesta de seguridad si la IA falla
        return {
            "respuesta": "Error técnico en el servicio de IA.",
            "categoria": "Error Software",
            "sentimiento": "Neutro",
            "urgencia": "Alta"
        }