import json
import os
from src.infrastructure.gpt.chat_processor_factory import ChatProcessorFactory

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
OPENAI_MODEL = os.environ["OPENAI_MODEL"]


def chat_handler(event, context):
    body = json.loads(event["body"])
    character_description = body["character_description"]
    messages = body["messages"]

    chat_processor = ChatProcessorFactory.create_chat_processor(OPENAI_API_KEY, OPENAI_MODEL)

    response = chat_processor.send_message(character_description, messages)

    return {
        "statusCode": 200,
        "body": json.dumps({"response": response}),
    }
