from typing import List

from haystack.nodes import PromptModel, PromptNode
from websocket_server.config import cfg
from websocket_server.session import Session
from websocket_server.log_init import logger

open_ai_prompt_model = PromptModel(
    model_name_or_path=cfg.openai_model,
    api_key=cfg.openai_api_key,
    max_length=cfg.output_max_length,
)

# Make PromptNode use the model:
pn_open_ai = PromptNode(open_ai_prompt_model)


def simple_query(question: str) -> list:
    return pn_open_ai(question)


def join_simple(res: List[str]) -> str:
    return "\n".join(res)


def run(question: str) -> str:
    return join_simple(simple_query(question))


def memory_run(question: str, session: Session) -> str:
    history = join_simple(session.messages_history)
    message = f"""

=== Previous Messages ===
{history}
=== End Previous Messages ===

Here is the question you need to answer:
{question}
"""
    logger.info(message)
    return run(message)


if __name__ == "__main__":
    from websocket_server.log_init import logger

    logger.info(
        run(
            "Can you write me a poem about the beauty of the English country side in the style of Lord Byron?"
        )
    )
    logger.info(run("Who was Albert Einstein?"))
