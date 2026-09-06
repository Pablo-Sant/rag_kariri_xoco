from core.chat_engine import get_chat_engine
import streamlit as st


def chat():
    
    st.set_page_config(page_title="Chat LLM", page_icon="💬")
    st.title("Chatbot LLM Kariri Xocó")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
        
        
    if prompt := st.chat_input("Digite sua mensagem aqui..."):
        
            with st.chat_message("user"):
                st.write(prompt)

            st.session_state.messages.append({"role": "user", "content": prompt})
            
            with st.chat_message("assistant"):
                
                try:
                    
                    chat_engine = get_chat_engine() 
                    
                    response = chat_engine.chat(prompt)
                    
                    full_response = str(response.response)
                    
                    st.write(full_response)
                    
                except Exception as e:
                    st.error(f"Erro ao chamar a API: {e}")
                    st.stop()
                    
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                

chat()