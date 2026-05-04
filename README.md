 Emoji Converter (Python)

# Overview
This project converts text-based emoticons like ":)" and ":(" into real emojis.

#Example:
- Input: "Hi Navee :)"
- Output: "Hi Navee 😊"

# How It Works
- Takes a message as input
- Uses a dictionary to map emoticons → emojis
- Replaces all matching patterns in the string
- Prints the updated message

# Tech Used
- Python
- Concepts:
  - Strings
  - Loops
  - Dictionaries
  - String ".replace()" method

#Core Logic
1. Store emoji mappings in a dictionary
2. Loop through each key in the dictionary
3. Replace occurrences in the input string
4. Print final converted message

#Example Run
Enter message: Hi Navee :)
Output: Hi Navee 😊

Enter message: I am sad :(
Output: I am sad 😢

#What I Learned
- Difference between ".split()" and ".replace()"
- Handling real-world messy input
- Using dictionaries for mapping
- Building cleaner logic instead of fragile solutions
