"""
chat_agent.py (LangChain version)
--------------------------------
Conversational agent using LangChain + Claude via Bedrock.
- Keeps track of conversation with memory.
- Responds to casual chat.
- Runs the OCR pipeline when the user asks for a comprobante.
"""

from langchain_aws import ChatBedrock
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.memory import ConversationBufferMemory
from . import pipeline
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"


# Initialize Claude model with LangChain
llm = ChatBedrock(
    model_id=MODEL_ID,
    model_kwargs={"max_tokens": 300},
)

# Add memory to keep conversation context
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{input}"),
])

history = ChatMessageHistory()
chain = prompt | llm
conversation = RunnableWithMessageHistory(
    chain,
    lambda session_id: history,
    input_messages_key="input",
    history_messages_key="history",
)


def handle_user_input(user_input: str) -> str:
    """
    Handles user input: 
    - If 'comprobante' is mentioned, run pipeline.
    - Otherwise, let Claude (via LangChain) reply.
    """
    if "comprobante" in user_input.lower():
        for token in user_input.split():
            if token.isdigit():
                file_name = f"comprobante_{token}.jpg"
                try:
                    result = pipeline.run_pipeline(f"samples/{file_name}", backend="mock")
                    return f"Here is the analysis for {file_name}:\n{result}"
                except FileNotFoundError:
                    return f"❌ File {file_name} not found in samples/"
        return "I couldn’t detect the comprobante number."
    else:
        return conversation.invoke({"input": user_input}, config={"configurable": {"session_id": "my-session"}}).content


if __name__ == "__main__":
    print("💬 Conversational OCR Transaction Analyzer (LangChain)")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("👉 You: ")
        if user_input.lower() in ["exit", "quit", "salir"]:
            print("👋 Bye!")
            break

        reply = handle_user_input(user_input)
        print(f"🤖 Claude: {reply}")