import os
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
import openai

# Set your OpenAI API key
openai.api_key = st.secrets["API_KEY"]

st.title("Stumpbox")

#setup
topicList = "start"

st.write("Start by configuring the context with the options below then generate a list of topics or the full posts.")

col1, col2, col3 = st.columns(3)
with col1:
    topic = st.selectbox("Select a topic:", ('Disinformation', 'Reproductive Rights'))
    voice = st.selectbox("Select a style:", ('John Stewart', 'Sean Hannity', 'Barack Obama'))

with col2:
    voteFor = st.text_input("Who should people vote for?", "Joe Biden")
    position = st.text_input("What position?", "President")



with col3:
    postCount = st.slider("How many social media posts do you want in the series?", 2, 10, 6)


st.write("")
st.write("Start by configuring the context with the options above then generate a list of topics or the full posts.")



st.write("")
topicListPrompt = "You are a social media consultant. The client has asked you for a plain text list of " + str(postCount) + "social media posts about " + str(topic) + ". Generate a list of " + str(postCount) + " post titles about " + str(topic)+ ". Titles need to be witten in the voice of " + str(voice) +" but do not mention" + str(voice) + ". Return a topic name, topic number and topic description in a JSON format."
if st.button('Generate topics'):
    with st.spinner("thinking..."):
        result = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a political analyst doing marketing."},
                {"role": "user", "content": topicListPrompt}
            ],
            max_tokens=4096,
            temperature=0.2)
        response = result.choices[0].message.content
        st.markdown(response)


st.write("")



postListPrompt = "You are a social media consultant. The client has approved the topic list that is found here: " + topicList + ". Write the content for each post. Write in a narrative style with the voice of " + str(voice) + "Ensure everyone votes for " + str(voteFor) + "running for the position of " + str(position) + "."
if st.button('Generate posts'):
        result = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a political analyst doing marketing."},
                {"role": "user", "content": postListPrompt}
            ],
            max_tokens=4096,
            temperature=0.2)
        response = result.choices[0].message.content
        st.markdown(response)

