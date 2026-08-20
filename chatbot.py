import json
import re


# ---------------------------------------------------------
# KNOWLEDGE BASE
# ---------------------------------------------------------

SKILLS = {
    "artificial intelligence": "AI",
    "ai": "AI",
    "machine learning": "Machine Learning",
    "ml": "Machine Learning",
    "deep learning": "Deep Learning",
    "data analysis": "Data Analysis",
    "data science": "Data Science",
    "computer vision": "Computer Vision",
    "natural language processing": "NLP",
    "nlp": "NLP",
    "communication": "Communication",
    "leadership": "Leadership",
    "problem solving": "Problem Solving"
}


TECHNOLOGIES = {
    "tensorflow": "TensorFlow",
    "pytorch": "PyTorch",
    "keras": "Keras",
    "opencv": "OpenCV",
    "cnn": "CNN",
    "rnn": "RNN",
    "lstm": "LSTM",
    "pandas": "Pandas",
    "numpy": "NumPy",
    "scikit-learn": "Scikit-learn",
    "sklearn": "Scikit-learn",
    "django": "Django",
    "flask": "Flask",
    "react": "React",
    "node.js": "Node.js",
    "git": "Git",
    "docker": "Docker",
    "sql": "SQL",
    "mysql": "MySQL",
    "mongodb": "MongoDB"
}


LANGUAGES = {
    "python": "Python",
    "java": "Java",
    "javascript": "JavaScript",
    "c++": "C++",
    "c": "C",
    "c#": "C#",
    "php": "PHP",
    "ruby": "Ruby",
    "go": "Go",
    "kotlin": "Kotlin",
    "swift": "Swift"
}


# ---------------------------------------------------------
# TEXT PREPROCESSING
# ---------------------------------------------------------

def clean_text(text):
    """
    Converts the input into a simple normalized form.
    """

    text = text.lower()

    # Remove unnecessary punctuation
    text = re.sub(r"[^\w\s\+\#\.-]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


# ---------------------------------------------------------
# EXTRACTION FUNCTION
# ---------------------------------------------------------

def extract_information(text):
    """
    Extracts skills, technologies and programming languages
    from conversational text.
    """

    cleaned_text = clean_text(text)

    result = {
        "skills": [],
        "technologies": [],
        "languages": []
    }

    # Search for skills
    for keyword, value in SKILLS.items():
        if keyword in cleaned_text:
            if value not in result["skills"]:
                result["skills"].append(value)

    # Search for technologies
    for keyword, value in TECHNOLOGIES.items():
        if keyword in cleaned_text:
            if value not in result["technologies"]:
                result["technologies"].append(value)

    # Search for programming languages
    for keyword, value in LANGUAGES.items():
        if keyword in cleaned_text:
            if value not in result["languages"]:
                result["languages"].append(value)

    return result


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------

print("======================================")
print("        AI RECRUITER - NLP")
print("======================================")

print("\nEnter a description of your experience.")
print("Type 'exit' to stop.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Program ended.")
        break

    extracted_data = extract_information(user_input)

    print("\nExtracted Information:")

    print(json.dumps(extracted_data, indent=4))
