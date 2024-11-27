class ChatMemory:
    def __init__(self):
        self.conversation_history = []
    
    def add_message(self, role, content):
        self.conversation_history.append({"role": role, "content": content})
    
    def get_history(self):
        return self.conversation_history
    
    def clear(self):
        self.conversation_history = []
