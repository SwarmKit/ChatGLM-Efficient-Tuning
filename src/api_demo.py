# coding=utf-8
# Implements API for ChatGLM fine-tuned with PEFT in OpenAI's format. (https://platform.openai.com/docs/api-reference/chat)
# Usage: python api_demo.py --model_name_or_path path_to_model --checkpoint_dir path_to_checkpoint
# Visit http://localhost:8000/docs for document.


import uvicorn

from glmtuner import create_app


if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000, workers=1)
