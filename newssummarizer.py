from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

search_tool = TavilySearchResults(max_results=5)
model = ChatOpenAI(model="gpt-3.5-turbo")
parser = StrOutputParser()

prompt = ChatPromptTemplate.from_template(
    """You are a helpful assistant
    
    summarizes the following news into clear bullet points
    {news}"""
)

chain = prompt | model | parser

news_result = search_tool.run("latest news on AI of 2026 ")
chain.invoke({"news": news_result})

print("News Summary:\n", chain.invoke({"news": news_result}))