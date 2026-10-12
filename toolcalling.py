from dotenv import load_dotenv
# from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
from langchain.tools import tool
from rich import print
from langchain_core.messages import HumanMessage

load_dotenv()

#1 creating a tool 
@tool
def get_text_length(text : str) -> int:
    """Return the number of character in a given text"""
    return len(text)

tools = {
    "get_text_length" : get_text_length
}

llm = ChatGoogleGenerativeAI(model="gemini-3.7-flash")

#tool binding 
llm_with_tool = llm.bind_tools([get_text_length])

#messeges with object
message =[]
prompt = input("You: ")
query = HumanMessage (prompt)
message.append(query)

result = llm_with_tool.invoke(message)
message.append(result)

if result.tool_calls:
    tool_name = result.tool_calls[0]["name"]
    tool_message = tools[tool_name].invoke(result.tool_calls[0])

    message.append(tool_message)
    print ( message)
result = llm_with_tool.invoke(message)

print(result.content)