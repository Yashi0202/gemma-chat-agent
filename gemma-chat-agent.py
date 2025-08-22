# Importing necessary modules from LangChain and Gradio
from langchain.agents import initialize_agent, Tool
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents.agent_types import AgentType
from langchain_core.messages import HumanMessage, AIMessage
from langchain_community.llms import Ollama
import gradio as gr

# 1. Setup LLM (Gemma via Ollama)
llm = Ollama(model="gemma")

# 2. Define tools that the agent can use
search = DuckDuckGoSearchRun()  # Web search using DuckDuckGo
wiki = WikipediaAPIWrapper()     # Wikipedia lookup

# List of tools that the agent will have access to
tools = [
    Tool(name="duck_search", func=search.run, description="Useful for web search queries"),
    Tool(name="wikipedia", func=wiki.run, description="Useful for looking up things on Wikipedia"),
    Tool(name="calculator", func=lambda x: str(eval(x)), description="Useful for basic math like 2+2 or 5*3")
]

# 3. Agent setup
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,  # Best for tool use
    verbose=True,
)

# 4. Memory to store chat history
chat_history = []

# Core function to handle one chat turn
def chat_fn(message, history):
    chat_history.append(HumanMessage(content=message))

    try:
        response = agent.run(message)
    except Exception as e:
        response = f"❌ Error: {str(e)}"

    chat_history.append(AIMessage(content=response))
    return response

# 5. Gradio UI section using ChatInterface (simplified UI component)
with gr.Blocks(theme=gr.themes.Base(), title="Gemma Agent") as demo:
    gr.Markdown("💬 **Chat with Calc + Wiki Agent (Gemma via Ollama)**")
    chatbot = gr.ChatInterface(fn=chat_fn)

# Entry point to launch the Gradio app when run as a script
if __name__ == "__main__":
    demo.launch(share=False, inbrowser=True)

