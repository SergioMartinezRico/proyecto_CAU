Sistema de Asistencia Inteligente para Ingeniería (CAU)
Este proyecto implementa un Chatbot de Asistencia Técnica basado en Inteligencia Artificial Generativa, diseñado específicamente para resolver incidencias en un departamento de ingeniería. El sistema gestiona consultas sobre software CAD (Catia/SolidWorks), normativas (ISO/ANSI) y gestión de licencias.

📋 Descripción del Proyecto
El sistema integra un modelo de lenguaje grande (LLM) para ofrecer respuestas contextuales y, simultáneamente, clasificar y estructurar la información de los tickets (categoría, sentimiento y urgencia) en una base de datos relacional.

Características principales:

Asistencia Especializada: Entrenado mediante System Prompts para actuar como soporte técnico de ingeniería.

Memoria Conversacional: Uso de LangChain para mantener el contexto de la sesión.

Salida Estructurada: El LLM responde estrictamente en JSON, permitiendo extraer metadatos analíticos.

Arquitectura Híbrida: Desarrollo local en contenedores y despliegue escalable en AWS.

🛠️ Stack Tecnológico
Backend & AI
Lenguaje: Python 3.x

Framework: Flask (API RESTful)

Orquestación IA: LangChain

Modelo LLM: LLaMA-3.3-70b (vía Groq API)

Frontend
Tecnologías: HTML5, CSS3, JavaScript (Vanilla)

Servidor Web: Nginx (Alpine Linux)

Datos & Infraestructura
Base de Datos: PostgreSQL 16.x

DevOps (Local): Docker & Docker Compose

DevOps (Cloud): AWS RDS (PostgreSQL) & AWS EC2 (Ubuntu)

Herramientas: pgAdmin 4, Git

🏗️ Arquitectura del Sistema
La solución sigue una arquitectura desacoplada cliente-servidor:

API Gateway (Flask):

Gestiona el flujo de mensajes y valida sesiones.

Implementa CORS para comunicación segura.

Robustez: Mecanismo de limpieza (extraer_json_seguro) para asegurar el parseo de respuestas del LLM.

Interfaz de Usuario (SPA):

Detección dinámica de entorno (Localhost vs AWS IP) para configuración automática de endpoints.

Renderizado visual de estado ("Typing...") y tablas de historial con etiquetas de urgencia.

Base de Datos (Modelo Normalizado):

Diseño optimizado con tablas maestras (roles, departments, categories, sentiments, urgencies) para evitar redundancia.

Tabla transaccional interactions que referencia IDs en lugar de texto repetitivo.

🚀 Instalación y Despliegue (Local)
El proyecto está contenerizado para facilitar el despliegue local.

Prerrequisitos
Docker Desktop instalado.

API Key de Groq.

Pasos
Clonar el repositorio:

Bash

git clone <url-del-repositorio>
cd <nombre-carpeta>
Configurar variables de entorno: Crea un archivo .env basado en el ejemplo y añade tu API Key:

Fragmento de código

GROQ_API_KEY=tu_api_key_aqui
DB_HOST=db
DB_NAME=cau_engineering
...
Iniciar con Docker Compose:

Bash

docker-compose up --build
Frontend disponible en: http://localhost:80

Backend disponible en: http://localhost:5000

pgAdmin disponible en: http://localhost:5050

☁️ Despliegue en AWS
El entorno de producción utiliza servicios gestionados para alta disponibilidad.

Database: Amazon RDS (PostgreSQL). Copias de seguridad automáticas y Security Groups estrictos.

App Server: Amazon EC2 (Ubuntu) ejecutando los contenedores de la aplicación.

Nota sobre Migración de Datos
Para migrar los datos desde el entorno local (Docker) a RDS, se recomienda usar pg_dump y pgAdmin. Importante: Al restaurar en RDS, utilizar la opción "Do not save owner" para evitar conflictos de permisos entre el usuario root local y el usuario maestro de AWS.

Autor: Sergio Martínez Rico
