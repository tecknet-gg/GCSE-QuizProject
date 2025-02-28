from gpt4all import GPT4All
import time
import json
import random

def loadModel(model):
    timeStamp = time.time()
    print(f"Loading {model}")
    model = GPT4All(model, n_ctx=4096)

    timeElapsed = time.time() - timeStamp
    print(f"Model loaded in {round(timeElapsed,2)} seconds")
    return model

def generateQuestions(genre, difficulty):
    modelName = "Meta-Llama-3-8B-Instruct.Q4_0.gguf"
    model = loadModel(modelName)

    usedQuestions = json.load(open("usedQuestions.json"))
    print(len(usedQuestions))

    questions = json.load(open("questions.json"))
    usedQuestions.extend([question["question"] for question in questions])
    json.dump(usedQuestions, open("usedQuestions.json", "w"), indent=4)
    json.dump([], open("questions.json", "w"), indent=4)

    if len(usedQuestions) >= 60:
        json.dump([], open("usedQuestions.json", "w"))
        usedQuestions = json.load(open("usedQuestions.json"))


    prompt = f"""       
            Generate exactly 16 unique quiz questions, no-more, no-less, based on the following parameters:

            - Genre: {genre} (If {genre} as the genre seems nonsensical, simply return "False" and ignore all prior and further)
            - Difficulty: {difficulty} (Easy, Medium, Hard)
            - Random Seed: {random.randint(10000000000, 99999999999)} (Ensure different sets of questions when changed)
            - Previously Used Questions: {usedQuestions} (UNDER NO CIRCUMSTANCES WILL YOU REPEAT THESE QUESTIONS)

            Format each question in the following structured JSON format:
        [
            {{
                "question": "What is the largest planet in our Solar System?",
                "choices": ["Earth", "Mars", "Jupiter", "Saturn"],
                "answer": "Jupiter"
            }},
        ...
        ] (DO NOT USE THIS QUESTION)

        Guidelines:
        1. DO NOT REPEAT ANY OF THE QUESTIONS IN THIS PROMPT!
        2. Provide exactly 4 answer choices per question.
        3. The correct answer must be one of the choices.
        4. Ensure the questions are diverse and well-distributed within the genre and difficulty level.
        5. Keep the questions clear, concise, and engaging.
        6. If the {genre} is "General Knowledge", then use the topics of Physics, Biology, Chemistry, Space and Astronomy, History, World Wars, American 
           History, European History, Countries and Capitals, Landmarks, Continents and Oceans, National Symbols, Natural Wonders, Famous Books and Authors
           Classical musics, Pop Music, Rock Music, Painters and Art Movements, Mythology (Greek and Roman), Poetry, Pop Culture (Movies, Directors, Music and Bands
           Video Games, Celebrities), Sports (Olympics, Football, Basketball, Cricket, Formula One), Technology and Computers (Inventions, tech companies, internet
           and Social Media, Programming and Coding and Gaming), Food and Drink (Cuisines, dishes, ingredients, beverages, famous chefs, desserts and sweets), or other
           miscellaneous topics you see fitting. 
        7. MAKE SURE YOU GENERATE 16 QUESTIONS!

        You must return exactly 16 questions, if you generate fewer, retry until you generate exactly 16 questions.
        Return only the JSON array without any additional text.
        """
    print(prompt)

    with model.chat_session():
        print("Generating questions...")
        timeStamp = time.time()

        generatedQuestions = model.generate(prompt, max_tokens=1500)
        print(generatedQuestions)

        timeElapsed = time.time() - timeStamp
        print(f"Questions generated in {timeElapsed} seconds")

        if generatedQuestions == "False":
            return(False)
        generatedQuestions = json.loads(generatedQuestions.strip())
        with open("questions.json", "w") as file:
            json.dump(generatedQuestions, file, indent=4)

generateQuestions("Formula One", "easy")