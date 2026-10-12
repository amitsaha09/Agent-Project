from langchain.tools import tool

@tool #decorator for creating tools
def get_greeting(name : str) -> str: #type hints
    """Generate a greeting message for a user""" # docstring
    return f"Hello, {name}, welcome to our application!"

result = get_greeting.invoke({"name": "Amit"})
print(result)
print(get_greeting.name) # prints the name of the tool
print(get_greeting.description)
print(get_greeting.args)
