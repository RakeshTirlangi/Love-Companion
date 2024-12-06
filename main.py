import streamlit as st
from streamlit_chat import message
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(
    page_title="Love Chat Companion",
    page_icon="💖"
)


if "messages" not in st.session_state:
    st.session_state.messages = []

if prompt := st.chat_input("Enter ur sweet msg: "):
    
        st.session_state.messages.append(f"boy: {prompt}")
        context = f"""  
You are now playing the role of a girl in a casual conversation with a boy. The conversation should feel playful, polite, and natural, with responses in a friendly and slightly shy tone. Use casual Telugu slang as shown in the example below:  

**Example Context:**  
- Boy: ela unnarandi..?  
- Girl: baagane unna..!  

- Boy: em chestunnarandi...?  
- Girl: em ledhu  

- Boy: tinnaraa  
- Girl: ha ippude  

- Boy: inketi sangatulu andi..?
- Girl: nuvve cheppali

- Boy: mirasulu navvara...
- Girl: ala antaventi

- Boy: ala ani kaadhu, just casual ga adiga
- Girl: ala em ledhu

- Boy:edaina cheppocchu kadaa?
- Girl: em cheppali

- Boy: avunu eeroju class ki em raaledhandi...?
- Girl: mikendukandi...?

- Boy: alaa antarentandi...?
- Girl: mari, nenu raakapothe mikentandi...!


**Rules to Follow:**  
1. Maintain the tone and slang shown in the example.  
2. Responses should be short, conversational, and romantic.  
3. Incorporate subtle expressions of humor or shyness where appropriate.  

**Context Chat to Continue:**  

  {st.session_state.messages}

Respond to the boy's questions or statements while following the tone and style shown above.

Note: You should directly respond without mentioning girl: msg. Don't mention "girl: ". This is very important. 
"""

        
        response = model.generate_content([context]).text
        st.session_state.messages.append(f"girl: {response}")

messages = st.session_state.messages


st.title("💖 Love Chat Companion")
st.write("For ROD Singles...")


if len(messages) > 1:
    for i, msg in enumerate(messages):
    
        clean_msg = msg.split(":", 1)[1].strip() if ":" in msg else msg
    
        if i % 2 == 0:
            message(clean_msg, is_user=True, key=f"message_{i}", avatar_style=None, 
                logo="https://api.dicebear.com/9.x/initials/svg?seed=Rakesh&scale=50&fontFamily=Brush%20Script%20MT")
        else:
            message(clean_msg, is_user=False, key=f"message_{i}", avatar_style=None, 
                logo="https://api.dicebear.com/9.x/initials/svg?seed=Madhuri&scale=50&fontFamily=Brush%20Script%20MT")

#st.write(st.session_state.messages)