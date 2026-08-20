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
    "c#": "C#",
    "c": "C",
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
    Normalize the input text.
    """

    text = text.lower()

    # Keep letters, numbers, spaces and programming symbols
    text = re.sub(r"[^\w\s\+\#\.-]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


# ---------------------------------------------------------
# KEYWORD MATCHING
# ---------------------------------------------------------

def contains_keyword(text, keyword):
    """
    Check whether a keyword appears as a COMPLETE word/phrase.

    Examples:

        'c'       -> matches 'I know c'
        'c'       -> does NOT match 'come'
        'c'       -> does NOT match 'cnn'
        'java'    -> does NOT match 'javascript'
        'python'  -> matches 'python programming'
    """

    # For single-letter C, require it to be surrounded
    # by non-letter/non-number characters.
    if keyword == "c":
        return re.search(r"(?<![a-zA-Z0-9])c(?![a-zA-Z0-9])", text) is not None

    # Normal matching for everything else
    pattern = r"(?<!\w)" + re.escape(keyword) + r"(?!\w)"

    return re.search(pattern, text) is not None


# ---------------------------------------------------------
# EXTRACTION FUNCTION
# ---------------------------------------------------------

def extract_information(text):

    cleaned_text = clean_text(text)

    result = {
        "skills": [],
        "technologies": [],
        "languages": []
    }

    # -----------------------------------------------------
    # SKILLS
    # -----------------------------------------------------

    for keyword, value in SKILLS.items():

        if contains_keyword(cleaned_text, keyword):

            if value not in result["skills"]:
                result["skills"].append(value)

    # -----------------------------------------------------
    # TECHNOLOGIES
    # -----------------------------------------------------

    for keyword, value in TECHNOLOGIES.items():

        if contains_keyword(cleaned_text, keyword):

            if value not in result["technologies"]:
                result["technologies"].append(value)

    # -----------------------------------------------------
    # PROGRAMMING LANGUAGES
    # -----------------------------------------------------

    for keyword, value in LANGUAGES.items():

        if contains_keyword(cleaned_text, keyword):

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

    if user_input.lower().strip() == "exit":
        print("Program ended.")
        break

    if not user_input.strip():
        print("Please enter some text.\n")
        continue

    extracted_data = extract_information(user_input)

    print("\nExtracted Information:")

    print(json.dumps(extracted_data, indent=4))

    print()