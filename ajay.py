quiz_data = [
    {
        "question": "What is the capital of india?",
        "options": ["A. delhi", "B. paris", "C. Rome", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    }
]

# Main quiz function
def run_quiz():
    score = 0
    total_questions = len(quiz_data)
    
    for item in quiz_data:

        print(item["question"])
        for option in item["options"]:
            print(option)
        
        
        answer = input("Enter your answer (e.g., A, B, C, D): ").upper()
        while answer not in ['A', 'B', 'C', 'D']:
            print("Invalid option. Please choose A, B, C, or D.")
            answer = input("Enter your answer (e.g., A, B, C, D): ").upper()
        
    
        if answer == item["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {item['answer']}.")
        
        print()  
    print(f"Quiz Over! Your final score is {score} out of {total_questions}.")

if __name__ == "__main__":
    run_quiz()
