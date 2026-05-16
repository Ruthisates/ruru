import urllib.parse
import webbrowser
import random

knowledge_base = {
    "hi": "Hi there! What can I help you with today?",
    "hello": "Hello! Nice to meet you.",
    "how are you": "I'm doing great! Ready to help you.",
    "bye": "Goodbye! Take care."
}

def chatbot():
    print("👋 Hello! I'm your helpful chatbot. Ask me anything!")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input == 'bye':
            print("ChatBot: Goodbye! Have a wonderful day!")
            break
        
        answer = knowledge_base.get(user_input)
        
        if answer:
            print(f"ChatBot: {answer}")
        else:
           
            if "what" in user_input:
                responses = [
                    "That seems to be asking about a concept or definition.",
                    "This appears to be a definition-seeking question.",
                    "You're asking about the nature or characteristics of something.",
                    "This question explores what something fundamentally is."
                ]
                print(f"ChatBot: {random.choice(responses)}")
                
            elif "who" in user_input:
                
                responses = [
                    "This question is about a person or group of people.",
                    "You're inquiring about someone's identity or role.",
                    "This seems to ask about a specific individual.",
                    "Questions about people help us understand human stories."
                ]
                print(f"ChatBot: {random.choice(responses)}")
                
            elif "how" in user_input:
                responses = [
                    "This explores a process, method, or way of doing something.",
                    "You're asking about mechanisms or procedures.",
                    "How questions examine the steps or workings of things.",
                    "This investigates the methodology behind something."
                ]
                print(f"ChatBot: {random.choice(responses)}")
                
            elif "why" in user_input:
                responses = [
                    "This seeks reasons, causes, or explanations.",
                    "You're asking about the purpose or rationale behind something.",
                    "Why questions delve into motivations and causes.",
                    "This explores the underlying reasons for phenomena."
                ]
                print(f"ChatBot: {random.choice(responses)}")
                
            elif "when" in user_input:
                responses = [
                    "This focuses on timing, dates, or historical moments.",
                    "You're asking about a specific time period or occurrence.",
                    "When questions locate events in chronological context.",
                    "This examines temporal aspects of situations."
                ]
                print(f"ChatBot: {random.choice(responses)}")
                
            elif "where" in user_input:
                responses = [
                    "This asks about places, positions, or geographical locations.",
                    "You're inquiring about spatial relationships or locations.",
                    "Where questions explore physical placement.",
                    "This investigates geographical or positional aspects."
                ]
                print(f"ChatBot: {random.choice(responses)}")
                
            else:
                responses = [
                    "That's an interesting inquiry worth exploring.",
                    "This question touches on important aspects of knowledge.",
                    "You're asking about something that deserves understanding.",
                    "Questions like this expand our perspective.",
                    "This inquiry helps us learn more about our world.",
                    "Exploring such questions enhances our knowledge.",
                    "Understanding this topic contributes to broader awareness.",
                    "This question addresses meaningful aspects of life."
                ]
                print(f"ChatBot: {random.choice(responses)}")
            
            query = urllib.parse.quote_plus(user_input)
            url = f"https://www.google.com/search?q={query}"
            
            print(f"ChatBot: For detailed information, check this link: {url}")
            
            open_link = input("ChatBot: Open in browser? (yes/no): ").strip().lower()
            if open_link == "yes":
                webbrowser.open(url)
        
        print()     
if __name__ == "__main__":
    chatbot()
