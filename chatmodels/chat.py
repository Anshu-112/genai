from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage , SystemMessage, AIMessage

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)


messages = [
    SystemMessage(content="You are a therapist AI agent")
]
print("Welcome(click 0 to exit)")

while True:
    prompt=input("You: ")
    messages.append(HumanMessage(content=prompt))
    if(prompt=="0"):
        break
    
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))

    print("Bot: " ,response.content)
    
    



