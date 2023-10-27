import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    openai_api_key = os.getenv("OPENAI_API_KEY")
    openai_model = os.getenv("OPENAI_MODEL")
    output_max_length = int(os.getenv("OUTPUT_MAX_LENGTH"))
    request_timeout = int(os.getenv("REQUEST_TIMEOUT"))
    temperature = int(os.getenv("TEMPERATURE"))
    seed = int(os.getenv("SEED"))
    max_consecutive_auto_reply = int(os.getenv("MAX_CONSECUTIVE_AUTO_REPLY"))
    code_dir = os.getenv("CODE_DIR")
    assert openai_api_key is not None, "Open AI key not found"


cfg = Config()

if __name__ == "__main__":
    from websocket_server.log_init import logger

    logger.info("model: %s", cfg.openai_model)
