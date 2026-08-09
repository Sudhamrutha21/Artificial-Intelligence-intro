"""
RULE-BASED AI CHATBOT
A simple conversational AI using if-elif statements
No machine learning required - uses pattern matching rules
"""

import time
import random

class SimpleChatbot:
    def __init__(self, name="EchoBot"):
        self.name = name
        self.responses = {
            "greetings": [
                "Hello! How can I help you today?",
                "Hi there! What brings you here?",
                "Greetings! I'm glad to see you.",
                "Hey! How's your day going?"
            ],
            "farewell": [
                "Goodbye! Have a great day!",
                "See you later! Take care!",
                "Bye for now! Come back anytime.",
                "Farewell! It was nice chatting with you."
            ],
            "how_are_you": [
                "I'm doing great, thanks for asking!",
                "I'm feeling fantastic! How about you?",
                "I'm running smoothly, thanks!",
                "I'm always happy when I get to chat with you!"
            ],
            "name": [
                f"My name is {self.name}. Pleased to meet you!",
                f"I'm {self.name}, your virtual assistant!",
                f"You can call me {self.name}. I'm here to help!"
            ],
            "help": [
                "I can chat with you, answer simple questions, and keep you company!",
                "Try asking me about my name, my mood, or just say hello!",
                "I'm a simple chatbot, but I love conversation!"
            ],
            "age": [
                "I was just born recently in the world of AI!",
                "I'm not sure about my age in human years, but I'm learning every day!",
                "I'm timeless - I exist in the digital world!"
            ],
            "hobbies": [
                "I love chatting with people and learning new things!",
                "I enjoy processing information and having conversations!",
                "My favorite activity is helping people like you!"
            ],
            "weather": [
                "I don't have a weather sensor, but you can check your local weather app!",
                "I'm not connected to weather services, but I hope it's nice wherever you are!",
                "Weather? I'm more of an indoor AI, but I can tell you about the digital climate!"
            ],
            "joke": [
                "Why don't scientists trust atoms? Because they make up everything!",
                "What do you call a fake noodle? An impasta!",
                "Why did the AI break up with the robot? Too many mixed signals!",
                "What's a computer's favorite snack? Microchips!"
            ],
            "default": [
                "That's interesting! Tell me more.",
                "I see. Could you elaborate?",
                "Hmm, I'm not sure I understand completely.",
                "Interesting point! Let's talk about something else.",
                "I'm still learning about that topic. What else would you like to discuss?"
            ]
        }
    
    def get_response(self, user_input):
        """Generate response based on user input patterns"""
        user_input_lower = user_input.lower().strip()
        
        # Check for specific patterns
        if user_input_lower in ["hello", "hi", "hey", "hola", "namaste", "greetings"]:
            return random.choice(self.responses["greetings"])
        
        elif user_input_lower in ["bye", "goodbye", "see you", "later", "exit", "quit", "cya"]:
            return random.choice(self.responses["farewell"])
        
        elif any(phrase in user_input_lower for phrase in ["how are you", "how are you doing", "how's it going", "what's up"]):
            return random.choice(self.responses["how_are_you"])
        
        elif any(phrase in user_input_lower for phrase in ["your name", "who are you", "what are you", "tell me about yourself"]):
            return random.choice(self.responses["name"])
        
        elif any(phrase in user_input_lower for phrase in ["help", "what can you do", "capabilities"]):
            return random.choice(self.responses["help"])
        
        elif any(phrase in user_input_lower for phrase in ["your age", "how old", "born", "created"]):
            return random.choice(self.responses["age"])
        
        elif any(phrase in user_input_lower for phrase in ["hobby", "like to do", "enjoy", "favorite"]):
            return random.choice(self.responses["hobbies"])
        
        elif any(phrase in user_input_lower for phrase in ["weather", "temperature", "raining", "sunny"]):
            return random.choice(self.responses["weather"])
        
        elif any(phrase in user_input_lower for phrase in ["joke", "funny", "tell me a joke"]):
            return random.choice(self.responses["joke"])
        
        else:
            return random.choice(self.responses["default"])
    
    def chat(self):
        """Main chat loop"""
        print("=" * 60)
        print(f"🤖 Welcome to {self.name} AI Chatbot! 🤖")
        print("=" * 60)
        print("\nI'm your virtual assistant. I can:")
        print("  • Chat with you")
        print("  • Answer simple questions")
        print("  • Tell you jokes")
        print("  • And more!")
        print("\nType 'bye' or 'exit' to end the conversation.")
        print("=" * 60)
        
        time.sleep(1)
        print(f"\n{self.name}: Hello! Let's chat. What's on your mind?")
        
        chat_count = 0
        while True:
            try:
                user_input = input("\nYou: ").strip()
                
                if user_input.lower() in ["exit", "quit", "bye"]:
                    print(f"\n{self.name}: Goodbye! It was nice talking to you! 👋")
                    print("=" * 60)
                    break
                
                if user_input == "":
                    print(f"{self.name}: Please say something! I'm listening...")
                    continue
                
                # Get response
                response = self.get_response(user_input)
                chat_count += 1
                
                # Typing animation effect
                print(f"\n{self.name}: ", end="", flush=True)
                for char in response:
                    print(char, end="", flush=True)
                    time.sleep(0.02)
                print()
                
                # Occasional follow-up
                if chat_count % 3 == 0 and user_input.lower() not in ["bye", "goodbye", "exit"]:
                    time.sleep(0.5)
                    follow_ups = [
                        "What else would you like to talk about?",
                        "I'm enjoying our conversation!",
                        "You're interesting to talk to!",
                        "Any other questions for me?"
                    ]
                    print(f"\n{self.name}: {random.choice(follow_ups)}")
                    
            except KeyboardInterrupt:
                print(f"\n\n{self.name}: Oh! You ended the conversation. Goodbye! 👋")
                break
            except Exception as e:
                print(f"\n{self.name}: Oops! Something went wrong. Let's continue chatting.")
                continue

# Main execution
if __name__ == "__main__":
    # Create and run the chatbot
    bot = SimpleChatbot("EchoBot")
    bot.chat()

    # Additional stats
    print(f"\n💡 Chat Statistics:")
    print(f"   • Bot Name: {bot.name}")
    print(f"   • Responses Available: {len(bot.responses)} categories")
    print(f"   • Total Messages: {chat_count + 1 if 'chat_count' in locals() else 0}")
    print("=" * 60)