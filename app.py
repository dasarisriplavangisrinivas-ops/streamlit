# # import streamlit as st
# # import ollama
# # st.title("AI chatbot")  
# # st.caption("hii")
# # # st.title("AI chatbot")
# # # st.write("AI CHatbot")
# # # st.button("send")
# # # st.sidebar.button("drop")  its for streamlit
# # # text=st.text_input("Ask me question")
# # if st.button("send"):
# #     response=ollama.chat(
# #         model="llama3.2",
# #         message=[
# #             {
# #             "role":"user",
# #             "content":"prompt"
# #             }
# #         ]

# #     )
# #     st.write(response["message"]
# #     ["prompt"])
# import streamlit as st
# import ollama

# st.title("My AI Chatbot")

# question = st.text_input("Ask something:")

# if question:
#     response = ollama.chat(
#         model="llama3.2",
#         messages=[
#             {
#                 "role": "user",
#                 "content": question
#             }
#         ]
#     )

#     st.write(response["message"]["content"])

import streamlit as st

st.title("AI Chatbot")

st.caption("Welcome to AI Chatbot")

st.write("Enter your prompt:")

question = st.text_input("Ask me anything:")

if st.button("Send"):
    if question:
        st.success("Question sent successfully!")
        st.write("You asked:", question)
    else:
        st.warning("Please enter a question.")

if st.button("Show Error"):
    st.error("Something went wrong!")

if st.sidebar.button("Sidebar Button"):
    st.sidebar.success("Sidebar button clicked!")

st.sidebar.write("AI Chatbot Menu")