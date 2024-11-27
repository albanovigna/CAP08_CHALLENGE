import os
import openai
from dotenv import load_dotenv
from chat_memory import ChatMemory
from search_engine import SearchEngine

load_dotenv()

class Chatbot:
    def __init__(self):
        self.memory = ChatMemory()
        self.search_engine = SearchEngine()
        openai.api_key = os.getenv('OPENAI_API_KEY')
    
    def detect_language(self, text):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a language detector. Respond only with the language name."},
                {"role": "user", "content": f"What language is this text in: {text}"}
            ]
        )
        return response.choices[0].message['content'].strip().lower()
    
    def generate_response(self, user_input):
        # Detect language first
        language = self.detect_language(user_input)
        
        # Realizar búsqueda
        print("\nBuscando información relevante...")
        search_results = self.search_engine.search(user_input)
        
        # Recopilar contexto
        context = ""
        sources = []
        for result in search_results:
            content = self.search_engine.get_page_content(result['link'])
            context += f"\nContenido de {result['title']}: {content[:500]}"
            sources.append(f"- [{result['title']}]({result['link']})")
        
        # Preparar mensajes
        self.memory.add_message("user", user_input)
        messages = self.memory.get_history()
        messages.append({
            "role": "system",
            "content": f"You must respond ONLY in {language}. Use this information: {context}"
        })
        
        # Generar respuesta
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            stream=True
        )
        
        # Mostrar respuesta en streaming
        full_response = ""
        print("\nRespuesta:", end=" ", flush=True)
        for chunk in response:
            if hasattr(chunk.choices[0].delta, 'content'):
                content = chunk.choices[0].delta.content
                print(content, end="", flush=True)
                full_response += content
        
        # Agregar fuentes
        print("\n\nFuentes:")
        for source in sources:
            print(source)
        
        self.memory.add_message("assistant", full_response)

    def start(self):
        print("Hello! I'm your AI assistant. Type 'exit' to end.\nHola! Soy tu asistente IA. Escribe 'salir' para terminar.")
        
        while True:
            user_input = input("\nTú: ").strip()
            
            if user_input.lower() in ['salir', 'exit']:
                print("¡Hasta luego! / Goodbye!")
                break
            
            self.generate_response(user_input)

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.start()
