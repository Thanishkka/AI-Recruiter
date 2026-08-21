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
    Converts the input into a normalized form.
    """

    # Convert all letters to lowercase
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
    Checks whether a keyword appears as a complete word or phrase.
    """

    # Special handling for C++
    if keyword == "c++":
        pattern = r"(?<![a-zA-Z0-9])c\+\+(?![a-zA-Z0-9])"
        return re.search(pattern, text) is not None

    # Special handling for C#
    if keyword == "c#":
        pattern = r"(?<![a-zA-Z0-9])c\#(?![a-zA-Z0-9])"
        return re.search(pattern, text) is not None

    # Special handling for C
    # This prevents C from being detected inside C++ or C#
    if keyword == "c":
        pattern = r"(?<![a-zA-Z0-9+#])c(?![a-zA-Z0-9+#])"
        return re.search(pattern, text) is not None

    # Normal matching for all other keywords
    pattern = r"(?<!\w)" + re.escape(keyword) + r"(?!\w)"

    return re.search(pattern, text) is not None


# ---------------------------------------------------------
# INFORMATION EXTRACTION
# ---------------------------------------------------------

def extract_information(text):
    """
    Extracts skills, technologies and programming languages
    from the user's conversational input.
    """

    # Clean the input text
    cleaned_text = clean_text(text)

    # Create empty result
    result = {
        "skills": [],
        "technologies": [],
        "languages": []
    }

    # -----------------------------------------------------
    # EXTRACT SKILLS
    # -----------------------------------------------------

    for keyword, value in SKILLS.items():

        if contains_keyword(cleaned_text, keyword):

            if value not in result["skills"]:
                result["skills"].append(value)

    # -----------------------------------------------------
    # EXTRACT TECHNOLOGIES
    # -----------------------------------------------------

    for keyword, value in TECHNOLOGIES.items():

        if contains_keyword(cleaned_text, keyword):

            if value not in result["technologies"]:
                result["technologies"].append(value)

    # -----------------------------------------------------
    # EXTRACT PROGRAMMING LANGUAGES
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
print("          AI RECRUITER - NLP")
print("======================================")

print("\nEnter a description of your experience.")
print("Type 'exit' to stop.\n")


while True:

    user_input = input("You: ")

    # Stop the program
    if user_input.lower().strip() == "exit":
        print("Program ended.")
        break

    # Check for empty input
    if not user_input.strip():
        print("Please enter some text.\n")
        continue

    # Extract information
    extracted_data = extract_information(user_input)

    # Display the result
    print("\nExtracted Information:")

    print(json.dumps(extracted_data, indent=4))

    print()