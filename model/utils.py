import pandas as pd

def sample_questions():
    # Quiz data
    data = {
        "Question": [
            "What is the capital of Germany?",
            "How many planets are in our solar system?",
            "Who developed the theory of relativity?",
            "How many continents are there?",
            "Which chemical element has the symbol 'O'?"
        ],
        "Answer": [
            "Berlin",
            "8",
            "Albert Einstein",
            "7",
            "Oxygen"
        ],
        "Category": [
            "Geography",
            "Astronomy",
            "Science",
            "Geography",
            "Chemistry"
        ],
        "Difficulty": [
            "Easy",
            "Medium",
            "Hard",
            "Easy",
            "Medium"
        ]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Save as CSV
    sample_csv = df.to_csv("quiz_template.csv", index=False)

    return sample_csv
