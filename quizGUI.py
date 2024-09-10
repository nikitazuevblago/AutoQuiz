import streamlit as st
from QAG import *

st.title("Quiz Chat Bot")

def main():
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
        welcome_prompt = """Hi! I'm a bot that will help you learn the material you read. 
                        Just enter the text and take the quiz to check your knowledge :)"""
        st.session_state.messages.append({"role":"assistant","content":welcome_prompt})
        st.session_state.stage = "text"
        st.session_state.correct_answer = None

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if st.session_state.stage == "text":
        message_placeholder = "Enter the text"
    elif st.session_state.stage == "TF":
        message_placeholder = 'Enter "true" or "false"'

    # Get user input
    user_prompt = st.chat_input(message_placeholder)

    if user_prompt:

        # User message
        with st.chat_message("user"):
            st.markdown(user_prompt)
        st.session_state.messages.append({"role":"user","content":user_prompt})


        # Check if answer is correct
        if st.session_state.correct_answer!=None:
            correct_answer = str(st.session_state.correct_answer).lower().strip()
            user_prompt = str(user_prompt).lower().strip()
            if correct_answer==user_prompt:
                assistant_prompt = "Correct!"
            else:
                assistant_prompt = f'Wrong. Correct answer is "{correct_answer}"'
            with st.chat_message("assistant"):
                st.markdown(assistant_prompt)
            st.session_state.messages.append({"role":"assistant",
                                              "content":assistant_prompt})
            st.session_state.correct_answer = None

        # Assistant message
        if st.session_state.stage == "text":
            TF_QAG_list = TF_QAG(user_prompt)
            st.session_state.QAG_list = TF_QAG_list
            st.session_state.stage = "TF"

        if st.session_state.stage == "TF":
            print(st.session_state.QAG_list)
            print(len(st.session_state.QAG_list))
            if len(st.session_state.QAG_list)>0:
                QA_dict = st.session_state.QAG_list[0]
                assistant_prompt = f"Is this statement correct? {QA_dict['statement']}"
                with st.chat_message("assistant"):
                    st.markdown(assistant_prompt)
                st.session_state.messages.append({"role":"assistant",
                                                    "content":assistant_prompt})
                st.session_state.correct_answer = QA_dict['answer']
                st.session_state.QAG_list = st.session_state.QAG_list[1:]
                st.rerun()
            else:
                assistant_prompt = f"Good job, this is the end of the quiz. Enter a new text to solve another quiz!"
                st.session_state.messages.append({"role":"assistant",
                                              "content":assistant_prompt})
                st.session_state.stage = "text"
                st.rerun()
        

if __name__ == '__main__':
    main()