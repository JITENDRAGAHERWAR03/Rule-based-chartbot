#Rule based Chatbot Implementation in Python

print("Namaste! Welcome to your chatbot")
print("You can ask me basic question ,type 'bye' to exit")

# chatbot Memory Creation [ dictionary of responses]
responses = {
    "hello": "Hello there!",
    "how are you": "I'm doing well, thank you!",
    "what is your name": "I'm a chatbot created by you.",
    "bye": "Goodbye! Have a great day!"
}

# method to get response from chatbot
def get_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, "I'm sorry, I don't understand that.")

# take user input
while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("Chatbot: " + response)
    if user_input.lower() == "bye":
        break