from openai import OpenAI
import json
import os

class AITestGenerator:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY")
        )

    def generate(self, endpoint, method, description, num_cases=5):
        prompt = f"""
        You are an expert QA engineer. Generate {num_cases} test cases for:
        Endpoint: {method} {endpoint}
        Description: {description}

        Return ONLY a JSON array with objects containing:
        - name: string (descriptive test name)
        - description: string
        - input_data: dict (request body or params)
        - expected_status: int (HTTP status code)
        - expected_response: dict (expected fields)

        Cover: happy path, validation errors, edge cases, boundary values.
        Return ONLY the JSON array, nothing else.
        """

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert QA engineer who generates precise test cases in JSON format only."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=2048,
            temperature=0.7
        )

        response_text = response.choices[0].message.content
        start = response_text.find("[")
        end = response_text.rfind("]") + 1
        return json.loads(response_text[start:end])
