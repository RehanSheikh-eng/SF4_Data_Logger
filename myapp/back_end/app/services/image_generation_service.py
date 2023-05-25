from dotenv import load_dotenv
import base64
import os
import requests

class ImageGenerationService:
    def __init__(self):
        load_dotenv()
        self.engine_id = "stable-diffusion-v1-5"
        self.api_host = os.getenv('API_HOST', 'https://api.stability.ai')
        self.api_key = os.getenv("STABLE_DIFFUSION_KEY")

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

        # Save only the first image to a local file
        image = data["artifacts"][0]
        image_content = base64.b64decode(image["base64"])

        # Define the directory and the filename
        dir_path = "./out"
        image_filename = f"{dir_path}/v1_txt2img_0.png"

        # Create the directory if it doesn't exist
        os.makedirs(dir_path, exist_ok=True)

        with open(image_filename, "wb") as f:
            f.write(image_content)

        return image_filename
