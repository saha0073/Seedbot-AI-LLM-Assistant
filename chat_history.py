from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import BaseMessage
from typing import Dict
from pydantic import BaseModel, Field
from typing import Dict, List

class InMemoryHistory(BaseChatMessageHistory, BaseModel):
    #\"\"\"In memory implementation of chat message history.\"\"\"
    messages: List[BaseMessage] = Field(default_factory=list)

    def add_message(self, message: BaseMessage) -> None:
        #\"\"\"Add a self-created message to the store\"\"\"
        self.messages.append(message)

    def clear(self) -> None:
        self.messages = []

class ChatHistoryManager:
    def __init__(self):
        self.chat_histories: Dict[str, InMemoryHistory] = {}

    def get_history_by_session_id(self, session_id: str) -> BaseChatMessageHistory:
        if session_id not in self.chat_histories:
            self.chat_histories[session_id] = InMemoryHistory()
        return self.chat_histories[session_id]

# Create a global instance of ChatHistoryManager
chat_history_manager = ChatHistoryManager()