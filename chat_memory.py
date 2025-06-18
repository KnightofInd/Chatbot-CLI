from collections import deque

class ChatMemory:
    def __init__(self, max_turns=5):
       
        self.max_turns = max_turns
        self.memory = deque(maxlen=max_turns)

    def add_turn(self, user_input, bot_response):
        
        self.memory.append((user_input, bot_response))

    def get_context(self):
       
        context = ""
        for user, bot in self.memory:
            context += f"User: {user}\nBot: {bot}\n"
        return context
