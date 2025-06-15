from openai import OpenAI

class ClarifaiHelper:
    def __init__(self, api_key):
        self.client = OpenAI(
            base_url="https://api.clarifai.com/v2/ext/openai/v1",
            api_key=api_key
        )
        
        self.models = {
            "ChatGPT": "https://clarifai.com/openai/chat-completion/models/o4-mini",
            "DeepSeek": "https://clarifai.com/deepseek-ai/deepseek-chat/models/DeepSeek-R1-0528-Qwen3-8B",
            "Gemini": "https://clarifai.com/gcp/generate/models/gemini-2_5-flash"
        }

    def get_response(self, model_name, question, temperature=0.7):
        try:
            response = self.client.chat.completions.create(
                model=self.models[model_name],
                messages=[
                    {"role": "user", "content": question}
                ],
                temperature=temperature,
                stream=False
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"