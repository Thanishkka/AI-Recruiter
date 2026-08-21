import json
import re


# ---------------------------------------------------------
# KNOWLEDGE BASE
# ---------------------------------------------------------

SKILLS = {

    # Artificial Intelligence and Machine Learning
    "artificial intelligence": "AI",
    "ai": "AI",
    "machine learning": "Machine Learning",
    "ml": "Machine Learning",
    "deep learning": "Deep Learning",
    "dl": "Deep Learning",
    "generative ai": "Generative AI",
    "gen ai": "Generative AI",
    "reinforcement learning": "Reinforcement Learning",
    "supervised learning": "Supervised Learning",
    "unsupervised learning": "Unsupervised Learning",
    "natural language processing": "NLP",
    "nlp": "NLP",
    "computer vision": "Computer Vision",
    "predictive modeling": "Predictive Modeling",
    "neural networks": "Neural Networks",
    "model development": "Model Development",

    # Data
    "data analysis": "Data Analysis",
    "data analytics": "Data Analytics",
    "data science": "Data Science",
    "data visualization": "Data Visualization",
    "data mining": "Data Mining",
    "data cleaning": "Data Cleaning",
    "data preprocessing": "Data Preprocessing",
    "data wrangling": "Data Wrangling",
    "exploratory data analysis": "Exploratory Data Analysis",
    "eda": "Exploratory Data Analysis",
    "statistical analysis": "Statistical Analysis",
    "statistics": "Statistics",
    "feature engineering": "Feature Engineering",
    "data modeling": "Data Modeling",

    # Software Development
    "software development": "Software Development",
    "software engineering": "Software Engineering",
    "web development": "Web Development",
    "frontend development": "Frontend Development",
    "front end development": "Frontend Development",
    "backend development": "Backend Development",
    "back end development": "Backend Development",
    "full stack development": "Full Stack Development",
    "mobile development": "Mobile Development",
    "application development": "Application Development",
    "api development": "API Development",
    "testing": "Software Testing",
    "debugging": "Debugging",
    "automation": "Automation",
    "version control": "Version Control",

    # Cloud and DevOps
    "cloud computing": "Cloud Computing",
    "cloud development": "Cloud Development",
    "devops": "DevOps",
    "continuous integration": "Continuous Integration",
    "continuous deployment": "Continuous Deployment",
    "ci/cd": "CI/CD",
    "containerization": "Containerization",

    # Cybersecurity
    "cybersecurity": "Cybersecurity",
    "cyber security": "Cybersecurity",
    "network security": "Network Security",
    "ethical hacking": "Ethical Hacking",
    "penetration testing": "Penetration Testing",
    "information security": "Information Security",

    # Databases
    "database management": "Database Management",
    "database design": "Database Design",
    "sql": "SQL",
    "nosql": "NoSQL",

    # Professional Skills
    "communication": "Communication",
    "leadership": "Leadership",
    "teamwork": "Teamwork",
    "problem solving": "Problem Solving",
    "critical thinking": "Critical Thinking",
    "time management": "Time Management",
    "project management": "Project Management",
    "team management": "Team Management",
    "decision making": "Decision Making",
    "adaptability": "Adaptability",
    "creativity": "Creativity",
    "collaboration": "Collaboration",
    "presentation": "Presentation",
    "research": "Research",
    "technical writing": "Technical Writing"
}


TECHNOLOGIES = {

    # AI / Machine Learning
    "tensorflow": "TensorFlow",
    "pytorch": "PyTorch",
    "keras": "Keras",
    "scikit-learn": "Scikit-learn",
    "sklearn": "Scikit-learn",
    "opencv": "OpenCV",
    "hugging face": "Hugging Face",
    "transformers": "Transformers",
    "langchain": "LangChain",
    "llama": "Llama",
    "ollama": "Ollama",
    "openai": "OpenAI",
    "gemini": "Gemini",
    "chatgpt": "ChatGPT",
    "jupyter": "Jupyter",
    "jupyter notebook": "Jupyter Notebook",

    # Data Science
    "pandas": "Pandas",
    "numpy": "NumPy",
    "matplotlib": "Matplotlib",
    "seaborn": "Seaborn",
    "plotly": "Plotly",
    "scipy": "SciPy",
    "apache spark": "Apache Spark",
    "spark": "Apache Spark",
    "hadoop": "Hadoop",
    "power bi": "Power BI",
    "tableau": "Tableau",
    "excel": "Microsoft Excel",

    # Deep Learning / Neural Networks
    "cnn": "CNN",
    "rnn": "RNN",
    "lstm": "LSTM",
    "gru": "GRU",
    "bert": "BERT",
    "gpt": "GPT",
    "resnet": "ResNet",
    "yolo": "YOLO",

    # Web Development
    "react": "React",
    "angular": "Angular",
    "vue": "Vue.js",
    "vue.js": "Vue.js",
    "node.js": "Node.js",
    "node": "Node.js",
    "express": "Express.js",
    "express.js": "Express.js",
    "django": "Django",
    "flask": "Flask",
    "fastapi": "FastAPI",
    "spring": "Spring",
    "spring boot": "Spring Boot",

    # Databases
    "mysql": "MySQL",
    "postgresql": "PostgreSQL",
    "postgres": "PostgreSQL",
    "mongodb": "MongoDB",
    "sqlite": "SQLite",
    "redis": "Redis",
    "oracle": "Oracle Database",
    "firebase": "Firebase",
    "dynamodb": "DynamoDB",

    # Cloud
    "aws": "AWS",
    "amazon web services": "AWS",
    "azure": "Microsoft Azure",
    "microsoft azure": "Microsoft Azure",
    "google cloud": "Google Cloud",
    "gcp": "Google Cloud",
    "google cloud platform": "Google Cloud",

    # DevOps
    "docker": "Docker",
    "kubernetes": "Kubernetes",
    "jenkins": "Jenkins",
    "terraform": "Terraform",
    "ansible": "Ansible",
    "git": "Git",
    "github": "GitHub",
    "gitlab": "GitLab",
    "bitbucket": "Bitbucket",

    # Mobile Development
    "android studio": "Android Studio",
    "flutter": "Flutter",
    "react native": "React Native",
    "xcode": "Xcode",

    # Operating Systems / Tools
    "linux": "Linux",
    "ubuntu": "Ubuntu",
    "windows": "Windows",
    "visual studio code": "Visual Studio Code",
    "vs code": "Visual Studio Code",
    "postman": "Postman",

    # Cybersecurity
    "wireshark": "Wireshark",
    "metasploit": "Metasploit",
    "burp suite": "Burp Suite"
}


LANGUAGES = {

    # Popular programming languages
    "python": "Python",
    "java": "Java",
    "javascript": "JavaScript",
    "typescript": "TypeScript",
    "c++": "C++",
    "c#": "C#",
    "c": "C",
    "go": "Go",
    "golang": "Go",
    "rust": "Rust",
    "ruby": "Ruby",
    "php": "PHP",
    "swift": "Swift",
    "kotlin": "Kotlin",
    "scala": "Scala",
    "r": "R",
    "dart": "Dart",
    "perl": "Perl",
    "lua": "Lua",
    "matlab": "MATLAB",
    "groovy": "Groovy",
    "shell": "Shell",
    "bash": "Bash",
    "powershell": "PowerShell"
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