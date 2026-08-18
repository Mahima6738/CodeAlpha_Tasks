def chatbot_responce(user_choice):
    user_choice  = user_choice.lower()

    if user_choice == 'hello' or user_choice == "hii":
        return "hello! How I can help you today. "

    elif user_choice == 'how are you':
        return "I am doing great! Thanks for asking."   

    elif 'your name' in user_choice:
        return "I'm a simple python chatbox. "

    elif 'bye' in user_choice:
        return 'Good bye! have a great day. '

    else:
        return 'Sorry! I can not understand that.'

    print("Welcome to our chatbot.")
    print("Chatbot: Hello! type something (type bye to exit): ")

while True:
    user = input("You : ")
    responce = chatbot_responce(user)

    print("chatbot: ", responce)

    if "bye" in user.lower():
        break


