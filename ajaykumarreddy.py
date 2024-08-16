def count_words(text):
    words = text.split()  
    return len(words)     

user_input = input("Enter a sentence or paragraph: ")
if not user_input.strip():
    print("No input provided. Please enter a sentence or paragraph.")
else:
    word_count = count_words(user_input)
    print(f"Word Count: {word_count}")
