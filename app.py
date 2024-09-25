from chat_history import chat_history_manager
from agent import Agent
from prompts import PROMPTS_VERSION_ONE, PROMPTS_VERSION_TWO
from css.custom_css import inject_custom_css
from dotenv import load_dotenv
import streamlit as st
import uuid

load_dotenv()

# Inject custom CSS
inject_custom_css()

selected_prompt = PROMPTS_VERSION_ONE

# Fetch the temperature if not already fetched
if 'temperature' not in st.session_state:
    st.session_state.temperature = 0.7

# Fetch the model name if not already fetched
if 'llm_model' not in st.session_state:
    st.session_state.llm_model = "gpt-4o"

# Initialize the Agent if not already initialized
if 'agent' not in st.session_state:
    st.session_state.agent = Agent(prompt_text=selected_prompt, agent_type="strategist", Temperature=st.session_state.temperature, llm_model=st.session_state.llm_model)
    st.session_state.selected_prompt = selected_prompt  

# Sidebar for agent selection and displaying configuration
st.sidebar.title("🌿 Seedbot Settings")

# Add brief description and links in the sidebar
st.sidebar.markdown("Seedworld: Immersive AAA metaverse where UGC gaming meets web3 and real-world economies, built by Seedify")
st.sidebar.markdown("[X (Twitter)](https://x.com/SeedworldMeta)")
st.sidebar.markdown("[Whitepaper](https://seedworld.gitbook.io/seedworld-wp)")

# Display agent configuration in sidebar
st.sidebar.subheader("🤖 Assistant Configuration")
#first_sentence = ' '.join(st.session_state.selected_prompt.split('. ')[:1])
first_sentence = f"""I am Seedbot, your unofficial Seedworld support assistant. I can answer any questions you have about Seedworld’s economy, gameplay, NFTs, nodes, tokens, land ownership, staking, and more, using detailed information from the Seedworld whitepaper."""
st.sidebar.write(f"📝 About me: {first_sentence}")
st.sidebar.write(f"🌡️ Temperature: {st.session_state.temperature}")
st.sidebar.write(f"🧠 Model: {st.session_state.llm_model}")
st.sidebar.write("⚠️ Disclaimer: Responses may not be 100% accurate.")


# Initialize agent_with_chat_history in session state if not already present
if 'agent_with_chat_history' not in st.session_state:
    st.session_state.agent_with_chat_history = st.session_state.agent.get_agent_with_history()

# Initialize conversation history in session state if not already present
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Welcome, gamer! Curious about Seedworld? Ask me anything!"}]

st.title("🎮 Seedbot")
st.markdown("🌐 unofficial Seedworld support assistant built on the top of Seedworld's whitepaper, may not be 100% accurate. Explore Seedworld, one question at a time 🌱")

# Display each message in the chat
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input area for user to type their message
prompt = st.chat_input("Plant your idea here...")

# Determine the agent descriptor
agent_descriptor = "🌱 Seedbot"
#st.markdown(f"<div class='agent-descriptor'>Chatting with {agent_descriptor}</div>", unsafe_allow_html=True)

if prompt:
    # Ensure session_id is initialized in session state
    if "session_id" not in st.session_state:
        st.session_state["session_id"] = str(uuid.uuid4())

    # Append user message to the conversation history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = st.session_state.agent_with_chat_history.invoke(
        {"input": prompt},
        config={"configurable": {"session_id": st.session_state["session_id"]}}
    )
    agent_name = "🌱 Seedbot"

    response_text = response.get('output')

    print(chat_history_manager.chat_histories)

    # Append agent's response to the conversation history
    st.session_state.messages.append({"role": "assistant", "content": response_text})
    with st.chat_message("assistant"):
        st.markdown(f"🌱 Seedbot: {response_text}")

# Add a footer
st.markdown("---")
#st.markdown("🌐 Exploring the Seedworld metaverse, one question at a time.")
#st.markdown("⚠️ Disclaimer: This is an unofficial Seedworld assistant built on Seedworld GitBook content. Responses may not always be accurate.")

