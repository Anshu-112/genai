from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()
llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro"
)
model = ChatHuggingFace(llm=llm)

response = model.invoke("who are you?")

print(response.content)