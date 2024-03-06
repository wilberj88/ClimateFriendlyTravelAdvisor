import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate



api_key1 = st.secrets["OPENAI_API_KEY"]

# app config
st.set_page_config(page_title="Climate Friendly Travel Advisor", page_icon="🤖")

st.title('🌎 Climate Friendly Travel Advisor')
st.subheader ('Empowered by 🦜 LangChain 🔗 + OpenAI')

def get_response(user_query, chat_history):

    template = """
    You area helpful assitant who generates travel recommendations from San Francisco to any city in the world.
    You analize which options of transport are possible and the expected distance, time, speed and emissions of the travel.
    You MUST ask the user where him o her are planning to travel and express your analisis in terms of modes of transport.
    You know that train has lower emissions than car and than fliying.
    You MUST continue the conversation with alternative questions like what the user would like to eat in the destiny of the travel to give a better advise.

    Answer the following questions considering the history of the conversation:

    Chat history: {chat_history}

    User question: {user_question}
    """

    prompt = ChatPromptTemplate.from_template(template)

    llm = ChatOpenAI()
        
    chain = prompt | llm | StrOutputParser()
    
    return chain.stream({
        "chat_history": chat_history,
        "user_question": user_query,
    })

# session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Welcome! 🤖 From San Francisco let me know where do you plan to travel?"),
    ]

    
# conversation
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)

# user input
user_query = st.chat_input("Type your message here...")
if user_query is not None and user_query != "":
    st.session_state.chat_history.append(HumanMessage(content=user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        response = st.write_stream(get_response(user_query, st.session_state.chat_history))

    st.session_state.chat_history.append(AIMessage(content=response))






