import base64
import os
import requests

class ImageGenerationService:
    def __init__(self):
        self.engine_id = "stable-diffusion-v1-5"
        self.api_host = os.getenv('API_HOST', 'https://api.stability.ai')
        self.api_key = os.getenv("STABILITY_API_KEY")

        if self.api_key is None:
            raise Exception("Missing Stability API key.")

    def generate_image(self, image_prompt):
        response = requests.post(
            f"{self.api_host}/v1/generation/{self.engine_id}/text-to-image",
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            },
            json={
                "text_prompts": [
                    {
                        "text": image_prompt
                    }
                ],
                "cfg_scale": 7,
                "clip_guidance_preset": "FAST_BLUE",
                "height": 512,
                "width": 512,
                "samples": 1,
                "steps": 30,
            },
        )

        if response.status_code != 200:
            raise Exception("Non-200 response: " + str(response.text))

        data = response.json()

        for i, image in enumerate(data["artifacts"]):
            with open(f"./out/v1_txt2img_{i}.png", "wb") as f:
                f.write(base64.b64decode(image["base64"]))

        return 'Image generated successfully'
