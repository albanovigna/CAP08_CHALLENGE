# Internet-Enabled Streaming Chatbot

## 1. Información General

### Nombre del proyecto

Chatbot con Capacidad de Búsqueda en Internet y Respuestas en Streaming

### Descripción

Un chatbot de consola inteligente que mantiene memoria de conversación, realiza búsquedas en Internet en tiempo real y proporciona respuestas en streaming con referencias a fuentes.

### Tecnologías principales

- Python 3.9+
- Serper.dev API para búsquedas en Google
- LLM (Large Language Model) para procesamiento de texto
- Bibliotecas de web scraping

### Versión actual

1.0.0

## 2. Requisitos Previos

### Software necesario

- Python 3.9 o superior
- pip (gestor de paquetes de Python)
- API key de Serper.dev
- API key del LLM seleccionado

### Dependencias principales

```python:requirements.txt
requests>=2.28.0
python-dotenv>=0.19.0
beautifulsoup4>=4.9.3
aiohttp>=3.8.0

Copy

Apply

README.md
3. Instalación
Configuración del entorno
git clone <repository-url>

Copy

Execute

cd chatbot-project

Copy

Execute

python -m venv venv

Copy

Execute

pip install -r requirements.txt

Copy

Execute

Variables de entorno
Crear archivo .env:

SERPER_API_KEY=your_serper_api_key
LLM_API_KEY=your_llm_api_key

Ejemplo
OPENAI_API_KEY=your_openai_api_key

Copy

Apply

.env
4. Estructura del Proyecto
chatbot-project/
├── src/
│   ├── search/
│   │   └── serper.py
│   ├── extraction/
│   │   └── text_extractor.py
│   ├── llm/
│   │   └── model.py
│   └── main.py
├── tests/
│   ├── test_search.py
│   ├── test_extraction.py
│   └── test_llm.py
├── requirements.txt
└── .env

Copy

Apply

5. Guía de Uso
Ejecución del chatbot
python src/main.py

Copy

Execute

Ejemplo de interacción
Usuario: ¿Cómo puedo plantar un árbol de manzanas?

Chatbot: ** Búsqueda en internet **

Chatbot: Según un artículo en GardeningKnowHow, el mejor momento para plantar...

Referencias:
- [GardeningKnowHow](https://gardeningknowhow.com/apple-tree)

Copy

Apply

6. Pruebas
Ejecución de pruebas
python -m pytest tests/

Copy

Execute

Tipos de pruebas
Pruebas unitarias para el módulo de búsqueda
Pruebas de integración para la extracción de texto
Pruebas end-to-end para el flujo completo del chatbot
7. Despliegue
El chatbot está diseñado para ejecutarse localmente. No requiere despliegue en servidor.

Consideraciones de seguridad
Mantener las API keys seguras en variables de entorno
No compartir el historial de conversación entre sesiones
Validar y sanitizar las entradas del usuario
8. Contribución
Estándares de código
Seguir PEP 8 para estilo de código Python
Documentar todas las funciones con docstrings
Mantener cobertura de pruebas >80%
Reportar bugs
Crear un issue incluyendo:

Descripción del problema
Pasos para reproducir
Comportamiento esperado vs actual
Logs relevantes
9. Solución de Problemas
Problemas comunes
Error de API key

Verificar que las variables de entorno estén correctamente configuradas
Confirmar que las API keys sean válidas
Problemas de extracción de texto

Verificar la conexión a Internet
Comprobar que los sitios web objetivo estén accesibles
Debugging
Activar logs detallados con nivel DEBUG
Verificar los archivos de log en logs/chatbot.log
10. Changelog
v1.0.0
Implementación inicial del chatbot
Integración con Serper.dev
Sistema de memoria de conversación
Respuestas en streaming
Referencias a fuentes

This documentation provides a comprehensive guide for your chatbot project, following the structure you requested and incorporating all the specifications from the challenge. The documentation is clear, detailed, and includes relevant code examples and commands.
```
