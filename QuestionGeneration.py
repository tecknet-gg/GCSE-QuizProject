from gpt4all import GPT4All
import time
import json
import random

def loadModel(model):
    timeStamp = time.time()
    print(f"Loading {model}")
    model = GPT4All(model, n_ctx=4096) #rm -rf ~/.cache/gpt4all/

    timeElapsed = time.time() - timeStamp
    print(f"Model loaded in {round(timeElapsed,2)} seconds")
    return model

def generateQuestions(genre, difficulty):
    modelName = "Meta-Llama-3-8B-Instruct.Q4_0.gguf"
    model = loadModel(modelName)

    usedQuestions = json.load(open("usedQuestions.json"))
    print(len(usedQuestions))
    seed = random.randint(1000000000000, 9999999999999)

    questions = json.load(open("questions.json"))
    usedQuestions.extend([question["question"] for question in questions])
    json.dump(usedQuestions, open("usedQuestions.json", "w"), indent=4)
    json.dump([], open("questions.json", "w"), indent=4)

    if len(usedQuestions) >= 60:
        json.dump([], open("usedQuestions.json", "w"))
        usedQuestions = json.load(open("usedQuestions.json"))


    generatedQuestions = None

    with model.chat_session():
        timeStamp = time.time()
        prompt = f"""
        You are an Quiz master, and you have been tasked with generating exactly 15 challenging general knowledge questions.
        The questions are to be multiple choice, and each question should have 4 options, with one of them being the valid one.
        You are prohibited from generating questions in the following list: 
        {usedQuestions}
        Each question must be unique and ensure that the topic of the questions are diverse in nature.
        You are to return the questions in the following format:
        [
        {{
                "question": "What is the process by which water moves through a plant, from the roots to the leaves?",
                "choices": [
                    "Photosynthesis",
                    "Respiration",
                    "Transpiration",
                    "Evaporation"
                ],
                "answer": "Transpiration"
            }},
            {{
                "question": "Which ancient civilization built the city of Petra in Jordan?",
                "choices": [
                    "Egyptians",
                    "Greeks",
                    "Romans",
                    "Nabataeans"
                ],
                "answer": "Nabataeans"
            }}
            ]
        You are to return the the valid .json questions only, and no other text preceeding or suceeding it.
        """
        print(prompt)
        print("Generating questions...")
        generatedQuestions = model.generate(prompt, max_tokens=1500)
        print(generatedQuestions)

        timeElapsed = time.time() - timeStamp
        print(f"Questions generated in {timeElapsed} seconds")

    if generatedQuestions == "False":
            return(False)
    with open("questions.json", "w") as file:
        json.dump(generatedQuestions, file, indent=4)




generateQuestions(input("Enter a topic: "), "difficult")