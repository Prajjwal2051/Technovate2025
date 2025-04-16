# this is the chat-bot programm for the technovate event

class TechnovateChatbot:
    def __init__(self):
        self.theme_2025="the theme will be inserted here"
        self.commands={
            "what is technovate": self.about_technovate,
            "theme for 2025": self.theme,
            "team required": self.team_requirement,
            "technical events": self.tech_events,
            "cultural events": self.cultural_events,
            "talent show": self.open_stage,
            "external participants": self.external_participation,
            "how to register": self.registration_info,
            "register for events": self.event_registration,
            "accommodation": self.accommodation_info,
            "food": self.food_info,
            "contact": self.contact_info,
            "last year theme": self.previous_theme,
            "celebrity guests": self.celeb_guests,
            "sponsors": self.past_sponsors,
            "help": self.help_info
        }

def chat(self):
    print("Hey, I am the Technovate Bot. Ask me anything about our college fest")
    while True:
        query=input("\nYou: ").lower().strip()
        if query in ["exit","quit","bye"]:
            print("Bot: Bye! See you at the Technovate")
            break;  
        found = False
        for key in self.commands:
            if key in query:
                self.commands[key]()
                found=True
                break
        if not found:
            print("Bot: Sorry, I didn't understand that. Type 'help' to see what i can answer")





if __name__=="__main__":
    bot=TechnovateChatbot()
    bot.chat()