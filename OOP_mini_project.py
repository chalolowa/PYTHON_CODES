import json
from difflib import Suggest

# Download the dictionary file (replace with your download location)
dictionary_file = "path/to/your/dictionary.json"

# Load the JSON data into a Python dictionary
def load_dictionary():
  try:
    with open(dictionary_file, "r") as file:
      data = json.load(file)
      return data
  except FileNotFoundError:
    print(f"Error: Dictionary file '{dictionary_file}' not found.")
    return None

# Function to search for a word definition (case-insensitive)
def get_definition(word):
  dictionary = load_dictionary()
  if dictionary:
    lower_word = word.lower()
    if lower_word in dictionary:
      return dictionary[lower_word]
    else:
      print(f"Word '{word}' not found in the dictionary.")
      # Suggest similar words using difflib
      suggestion = Suggest(dictionary.keys()).suggest(lower_word)[0]
      print(f"Did you perhaps mean '{suggestion}'?")
  else:
    print("Error: Could not load dictionary.")
  return None

# Get user input and handle case-insensitive search
def main():
  while True:
    user_word = input("Enter a word to find its definition (or 'q' to quit): ")
    if user_word.lower() == "q":
      break
    definition = get_definition(user_word)
    if definition:
      print(f"Definition of '{user_word}':\n{definition}")

if __name__ == "__main__":
  main()
