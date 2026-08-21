# AI-Recruiter
 An AI-powered recruitment assistant that analyzes resumes and assists recruiters in hiring decisions.
 
# AI Recruiter – NLP Information Extraction

## 1. Project Overview

AI Recruiter is an NLP-based information extraction system designed to extract professional information from conversational text.

The system accepts a natural-language description of a person's skills and experience and identifies three types of information:

* **Skills**
* **Technologies**
* **Programming Languages**

The extracted information is returned in a structured **JSON format**, making it easier for other applications to process the information.

This project implements **Part 1: NLP Extraction** of the AI Recruiter project.

---

## 2. Problem Statement

Recruitment-related information is often provided in an unstructured and conversational form. A person may describe their experience in a sentence such as:

> "I have experience in machine learning and computer vision, and I developed projects using Python, TensorFlow and OpenCV."

Manually identifying individual skills, technologies, and programming languages from such descriptions can be time-consuming.

The objective of this project is to develop a simple NLP-based system that can process conversational descriptions and automatically extract relevant skills, technologies, and programming languages into a structured JSON format.

---

## 3. Installation Instructions

### Prerequisites

* Python 3.x
* GitHub
* Virtual Studio Code

### Step 1 – Clone the Repository

```bash
git clone https://github.com/Thanishkka/AI-Recruiter
```

### Step 2 – Open the Project Folder

```bash
cd AI-Recruiter-NLP
```

### Step 3 – Run the Program

```bash
python ai_recruiter.py
```

The project uses Python's built-in `json` and `re` modules, so no external Python packages are required.

---

## 4. Dataset Used

This project does **not use an external dataset**.

Instead, it uses a manually created **knowledge base** containing commonly used:

* Skills
* Technologies
* Programming Languages

The knowledge base is stored in the Python program using dictionaries.

For example:

```python
SKILLS = {
    "machine learning": "Machine Learning",
    "computer vision": "Computer Vision",
    "data analysis": "Data Analysis"
}
```

Separate dictionaries are used for technologies and programming languages.

The knowledge base was expanded to include a wider range of areas such as:

* Artificial Intelligence
* Machine Learning
* Data Science
* Web Development
* Cloud Computing
* DevOps
* Cybersecurity
* Databases
* Software Development
* Professional Skills

### Input Data

The system accepts conversational text directly from the user.

Example:

```text
I developed a computer vision project using OpenCV and C++.
```

The system processes this text and extracts the relevant information.

---

## 5. Methodology

The project uses a **rule-based NLP information extraction approach**.

### Step 1 – User Input

The user enters a conversational description of their skills or experience.

Example:

```text
I have experience in machine learning and developed projects using Python and TensorFlow.
```

### Step 2 – Text Preprocessing

The input is normalized before the extraction process.

The preprocessing includes:

* Converting text to lowercase
* Removing unnecessary punctuation
* Removing extra spaces
* Preserving important programming-language symbols such as `+` and `#`

The Python `re` module is used for regular-expression-based text processing.

### Step 3 – Keyword Matching

The processed text is compared against the predefined knowledge base.

The system checks three categories:

```text
Skills
Technologies
Programming Languages
```

Regular expressions are used to perform more accurate keyword matching and prevent partial-word matches.

### Step 4 – Information Classification

When a known term is detected, it is classified into the appropriate category.

For example:

```text
Machine Learning → Skill
TensorFlow → Technology
Python → Programming Language
```

### Step 5 – JSON Output

The extracted information is returned in structured JSON format.

Example:

```json
{
    "skills": [
        "Machine Learning"
    ],
    "technologies": [
        "TensorFlow"
    ],
    "languages": [
        "Python"
    ]
}
```

---

## 6. Technologies Used

### Programming Language

* **Python**

### Python Modules

* **`re`** – Used for regular expressions and text preprocessing.
* **`json`** – Used to generate and display structured JSON output.

### NLP Techniques

* Rule-based NLP
* Text preprocessing
* Keyword matching
* Regular-expression-based matching
* Information extraction
* Entity classification

### Development Tools

* GitHub
* Python development environment

---

## 7. Results

The system successfully extracts relevant skills, technologies, and programming languages from conversational descriptions.

### Example 1 – Machine Learning

**Input:**

```text
I have experience in machine learning and worked with Python and TensorFlow.
```

**Output:**

```json
{
    "skills": [
        "Machine Learning"
    ],
    "technologies": [
        "TensorFlow"
    ],
    "languages": [
        "Python"
    ]
}
```

### Example 2 – Computer Vision and C++

**Input:**

```text
I developed a computer vision project using OpenCV and C++.
```

**Output:**

```json
{
    "skills": [
        "Computer Vision"
    ],
    "technologies": [
        "OpenCV"
    ],
    "languages": [
        "C++"
    ]
}
```

The system correctly identifies **C++ without incorrectly classifying it as C**.

### Example 3 – Generative AI

**Input:**

```text
I worked with Generative AI, Hugging Face, PyTorch and AWS.
```

**Output:**

```json
{
    "skills": [
        "Generative AI"
    ],
    "technologies": [
        "Hugging Face",
        "PyTorch",
        "AWS"
    ],
    "languages": []
}
```

The expanded knowledge base allows the system to recognize a broader range of modern technologies and skills.

---

## 8. Challenges Faced

### 8.1 Incorrect Detection of the Letter "C"

One of the first problems encountered was the incorrect detection of the letter **"C"** as the C programming language.

The initial keyword-matching approach searched for the character `"c"` in the input text. As a result, normal words containing the letter `c` could be incorrectly identified as the programming language C.

For example:

```text
I come from Chennai.
```

The system could incorrectly identify **C** as a programming language simply because the letter `c` appeared in the sentence.

This produced a false positive and showed that simple keyword matching was not sufficient for single-letter programming languages.

### 8.2 Confusion Between C, C++, and C#

Another challenge occurred because **C, C++, and C#** are closely related terms but need to be treated as separate programming languages.

For example:

```text
I developed a project using C++.
```

The initial system could detect both:

```text
C
C++
```

instead of detecting only:

```text
C++
```

Similarly, when processing a term such as:

```text
CNN
```

the letter `C` could incorrectly be identified as the C programming language.

### 8.3 Solution to the C-Related False Positives

To solve these problems, the keyword-matching system was improved using **regular expressions and boundary conditions**.

The system was modified to check whether `C` appears as a complete standalone term rather than simply checking whether the character exists in the sentence.

Separate matching rules were also introduced for:

* `C`
* `C++`
* `C#`

This ensures that:

```text
C       → C
C++     → C++
C#      → C#
CNN     → Not C
come    → Not C
```

This improvement reduced false-positive detections and made the information extraction more reliable.

### 8.4 Dependence on the Knowledge Base

Another challenge is that the system can only recognize terms that are included in its predefined knowledge base.

For example, if a user mentions a new or uncommon technology that is not present in the knowledge base, the system may not identify it.

To improve coverage, the knowledge base was expanded to include a wider range of:

* AI technologies
* Machine learning tools
* Programming languages
* Web frameworks
* Databases
* Cloud platforms
* DevOps tools
* Cybersecurity technologies
* Professional skills

### 8.5 Limited Context Understanding

The current system primarily performs keyword-based extraction rather than understanding the complete meaning of a sentence.

For example:

```text
I have no experience in Python.
```

The system may still identify **Python** because it recognizes the keyword, even though the sentence indicates that the person does not have Python experience.

This is a limitation of the current rule-based approach.

---

## 9. Future Improvements

The project can be improved in several ways:

* Further expand the knowledge base with additional skills, technologies, and programming languages.
* Add synonym and abbreviation handling.
* Improve spelling-error detection.
* Add better context and negation handling.
* Use advanced NLP models for semantic understanding.
* Integrate an LLM for more flexible information extraction.
* Add resume processing as a future feature.
* Add multilingual input support.
* Integrate the extracted information with the matching and RAG components described in later parts of the project.

The current rule-based system provides a simple foundation that can later be extended into a more advanced AI-powered recruitment system.

---

## 10. Screenshots

Screenshots of the running application is added to demonstrate the working system.

### Application Running

Add a screenshot showing the program accepting conversational input.

<img width="1916" height="1021" alt="image" src="https://github.com/user-attachments/assets/03b967d3-1f78-48da-9833-7d5b4dd71906" />


### Extracted JSON Output

Add a screenshot showing the input and the corresponding structured JSON output.

<img width="1917" height="1021" alt="image" src="https://github.com/user-attachments/assets/cf13e444-c25f-4244-8ddb-62380cf6f563" />

---

## 11. Project Structure

```text
AI-Recruiter-NLP/
│
├── ai_recruiter.py
├── requirements.txt
└── README.md
```

### `ai_recruiter.py`

Contains the complete NLP information extraction program.

### `requirements.txt`

Documents the project's Python dependencies.

The project currently uses only Python standard-library modules, so no external packages are required.

### `README.md`

Contains the project overview, problem statement, installation instructions, methodology, results, challenges, and future improvements.

---

## 12. Conclusion

The AI Recruiter NLP project demonstrates how conversational text can be processed and converted into structured professional information.

The current implementation uses a simple and understandable rule-based NLP approach. It preprocesses conversational input, identifies relevant skills, technologies, and programming languages using a categorized knowledge base, and returns the extracted information in JSON format.

The project also demonstrates how testing can reveal false-positive problems, particularly with programming languages such as **C, C++, and C#**, and how regular-expression-based matching can be used to improve extraction accuracy.

This implementation provides the foundation for the **Part 1: NLP Extraction** component of the larger AI Recruiter project and can be extended in the future using more advanced NLP techniques and large language models.
