from langchain_community.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()
def generate_pet_name():
    llm = OpenAI(temperature=0.7)
    name = llm("I have a dog pet and I need suggestions for pet names")
    return name

if __name__ == "__main__":
    print(generate_pet_name())    