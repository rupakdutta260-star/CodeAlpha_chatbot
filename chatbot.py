print("chatbot: hello! type 'bye' to exit.")
while True:
    user = input("you:").lower()
    if user == "hello" or user == "hi" or user =="hey":
        print("chatbot: hello! how are you?")

    elif user == "how are you?":
        print("chatbot: i'm good and thank you asking!")
    elif user == "whats you name?":
        print("chatbot: my name is gigi")
    elif user == "who created you?":
        print("chatbot: i was created by rupak dutta")
    elif user == "bye:":
        print("chatbot: bye! have a nice and enjoyable day!")
        break
    else:
        print("chatbot: sorry! i dont have the khowledge about that ask me some thing else.")
        