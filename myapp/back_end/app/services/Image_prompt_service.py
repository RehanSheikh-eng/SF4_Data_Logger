from dotenv import load_dotenv
import os
from langchain.llms import AI21
from langchain import PromptTemplate, LLMChain

class ImagePromptService:
    def __init__(self):
        # load environment variables from .env file
        load_dotenv()
        # access the AI21_API_KEY environment variable
        api_key = os.getenv('AI21_API_KEY')


        template = """Stable Diffusion is an AI art generation model, this is an example prompt for it: pirate, concept art, deep focus, fantasy, intricate, highly detailed, digital painting, artstation, matte, sharp focus, illustration, art by magali villeneuve, chippy, ryan yee, rk post, clint cearley, daniel ljunggren, zoltan boros, gabor szikszai, howard lyon, steve argyle, winona nelson.

        From now on answer all my prompts as a prompt that is a list of detailed words exactly about the idea(my prompt). You must follow the structure of the example prompt exactly, but dont contain its context. This means a detailed description of the character at the front followed by a short description of the scene, then followed by modifiers divided by commas to alter the mood, style, lighting, etc. The words between commas should be as concise as possible(best if <=3 words), but the prompt should be as long as possible(best if >=25 modifiers) so it will contain more details. Dont describe the scene, just generate the prompt for stable diffusion.

        Your response should always start exactly with: "((masterpiece)), (best quality), (detailed),"

        Create a prompt for the following Context:
        {image_context}

        Prompt:
        """

        prompt = PromptTemplate(
            input_variables=["image_context"],
            template=template,
        )


        self.llm = AI21(ai21_api_key=api_key)
        self.llm_chain = LLMChain(prompt=prompt, llm=self.llm)

    def generate_image_prompt(self, image_context):


        try:
            return self.llm_chain.run(image_context)
        except Exception as e:
            raise e
