import webbrowser
from tkinter import *
from tkinter import scrolledtext

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot with Responses Based on Rules")
        self.root.configure(background="yellow")

        title = Label(self.root, text="CHATBOT", font="KinoMT 20 bold", fg="black", bg="yellow")
        title.pack(pady=5)

        self.chat_display = scrolledtext.ScrolledText(self.root, state=DISABLED)
        self.user_input = Text(self.root, height=2, font="timesnewroman 12 ", fg="black", bg="lightgray")
        self.user_input.insert("1.0", "Write a message")
        self.user_input.bind("<FocusIn>", self.clear_placeholder)
        self.user_input.bind("<FocusOut>", self.restore_placeholder)
        self.send_button = Button(self.root, text="Send", command=self.on_send_button_click, bg="green", fg="black", cursor="hand2", font=("timesnewroman 16 "))

        self.chat_display.pack(fill=BOTH, expand=True, pady=4)
        self.user_input.pack(padx=10, pady=2, fill=BOTH, expand=True)
        self.send_button.pack(pady=2)

        self.Tell("Hello! How can I assist you today?")
        self.Tell("Here are a few of my roles:\nYou could say Hello. \nBy beginning your question with 'Google search', you are free to ask me anything. \nBy beginning your search with 'YouTube search', you may look up videos on the website. \nSaying 'play music song-name' at the beginning of your inquiry will start playing music.")

    def take_command(self):
        return self.user_input.get("1.0", END).strip().lower()

    def Tell(self, text, sender="Chatbot"):
        lines = text.split('\n')
        formatted_lines = [f"{sender}: {line.strip()}" for line in lines]
        formatted_text = '\n'.join(formatted_lines)
        self.chat_display.config(state=NORMAL)
        self.chat_display.insert(END, formatted_text + "\n")
        tag_name = "chatbot_tag" if sender == "Chatbot" else "user_tag"
        self.chat_display.tag_configure(tag_name, justify="left", foreground="black" if sender == "Chatbot" else "blue")
        self.chat_display.tag_add(tag_name, "end-2l", "end")
        self.chat_display.see(END)

    def on_enter_pressed(self, event):
        query = self.take_command()
        self.user_input.delete("1.0", END)
        self.user_input.insert(END, query)
        self.Tell("User: " + query)
        self.process_query(query)

    def clear_placeholder(self, event):
        if self.user_input.get("1.0", "end-1c") == "Write a message":
            self.user_input.delete("1.0", END)

    def restore_placeholder(self, event):
        if not self.user_input.get("1.0", "end-1c"):
            self.user_input.insert("1.0", "Write a message")

    def on_send_button_click(self):
        query = self.take_command()
        self.user_input.delete("1.0", END)
        self.Tell(query, sender="User") 
        self.process_query(query)

    def process_query(self, query):
        if "hello" in query:
            self.Tell("Hello Sir, Jarvis here")
            self.Tell("Your personal AI chatbot.")
            self.Tell("How may I help you?")
        elif "how are you" in query:
            self.Tell("I am fine, Sir.")
            self.Tell("What about you?")
        elif "i am fine" in query:
            self.Tell("Good to hear that, Sir.")
            self.Tell("How can I help you?")
        elif "bye" in query:
            self.Tell("Ok sir! Bye. You can call me anytime.")
            self.root.destroy()
        elif "youtube search" in query:
            self.Tell("Ok sir! This is what I found for your search.")
            query = query.replace("jarvis", "").replace("youtube search", "")
            web = "https://www.youtube.com/results?search_query=" + query.lower()
            webbrowser.open(web)
            self.Tell("Done Sir!")
        elif "google search" in query:
            self.Tell("Ok sir! This is what I found for your search.")
            query = query.replace("jarvis", "").replace("google search", "")
            google_url = "https://www.google.com/search?q=" + query.lower()
            webbrowser.open(google_url)
            self.Tell("Done Sir!")
        elif "play music" in query:
            self.Tell("Ok sir! This is what I found for your search.")
            query = query.replace("jarvis", "").replace("play music", "")
            song_url = "https://www.youtube.com/watch?v=kJQP7kiw5Fk?" + query.lower()
            webbrowser.open(song_url)
            self.Tell("Done Sir!")
        elif "who are you?" in query.lower():
            self.Tell("Jarvis")
            self.Tell("A Chatbot with Rule-Based Responses")
        elif "what are your functions?" in query.lower():
            self.Tell("Here are some of my functions:\nYou can say Hello.\nYou can ask me anything by starting your query with 'Google search'.\nYou can search videos on YouTube by starting your query with 'YouTube search'.\nYou can play music by saying 'Play music' at the start of your query. \nAsk 'who created you'. \nAsk 'who are you?'")
        else:
            self.Tell("I'm sorry, I didn't understand that.")

root = Tk()
obj = ChatBot(root)
root.mainloop()
