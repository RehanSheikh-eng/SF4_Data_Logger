from dotenv import load_dotenv
import os
from langchain.llms import AI21
from langchain import PromptTemplate, LLMChain

class StoryGeneratorService:
    def __init__(self):
        # load environment variables from .env file
        load_dotenv()

        # access the AI21_API_KEY environment variable
        api_key = os.getenv('AI21_API_KEY')


        template = """Write a short and engaging story with the following context:
        Context:
        {story_context}

        Story:
        """

        prompt = PromptTemplate(
            input_variables=["story_context"],
            template=template,
        )


        self.llm = AI21(ai21_api_key=api_key)
        self.llm_chain = LLMChain(prompt=prompt, llm=self.llm)

    def generate_story(self, story_context):


        try:
            return self.llm_chain.run(story_context)
        except Exception as e:
            raise e
