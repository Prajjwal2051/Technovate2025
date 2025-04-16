# This is the chat-bot program for the Technovate event

class TechnovateChatbot:
    def __init__(self):
        self.theme_2025 = "the theme will be inserted here"
        self.commands = {
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
        print("Bot: Hey! I am the Technovate Bot 🤖")
        print("Ask me anything about our college fest!")
        while True:
            query = input("\nYou: ").lower().strip()
            if query in ["exit", "quit", "bye"]:
                print("Bot: Bye! See you at the Technovate!")
                break
            found = False
            for key in self.commands:
                if key in query:
                    self.commands[key]()
                    found = True
                    break
            if not found:
                print("Bot: Sorry, I didn't understand that. Type 'help' to see what I can answer.")

    def about_technovate(self):
        print("Bot: Technovate is our college’s annual tech-cultural fest, blending tech events with cultural performances.")

    def theme(self):
        print(f"Bot: Yes! This year’s theme is \"{self.theme_2025}\" — celebrating innovation, creativity, and collaboration.")

    def team_requirement(self):
        print("Bot: Some events are solo, while others need teams of 2–4. Check event pages for details.")

    def tech_events(self):
        print("Bot: We’ve got hackathons, coding contests, robotics challenges, IoT expos, and tech quizzes!")

    def cultural_events(self):
        print("Bot: Dance battles, band performances, fashion shows, open mic nights, and drama competitions await!")

    def open_stage(self):
        print("Bot: Yes! Our Open Mic Stage welcomes singers, poets, and performers. Registrations opening soon!")

    def external_participation(self):
        print("Bot: Yes, many cultural events are open to participants from outside our college. Check event rules.")

    def registration_info(self):
        print("Bot: You can register on our official website under the 'Register' section. Fest passes and event-wise options are available.")

    def event_registration(self):
        print("Bot: Yes, you need to register separately for each event you want to attend.")

    def accommodation_info(self):
        print("Bot: Outstation participants can get hostel accommodation for a nominal charge. Check the 'Stay' section.")

    def food_info(self):
        print("Bot: Yes, food stalls, canteens, and a food court will be active during the fest!")

    def contact_info(self):
        print("Bot: You can talk to this bot or visit the 'Contact Us' page for event coordinators and support.")

    def previous_theme(self):
        print("Bot: Technovate 2024’s theme was \"Beyond Boundaries\", celebrating limitless innovation and imagination.")

    def celeb_guests(self):
        print("Bot: In past editions, we’ve had Samay Raina and Seedhe Maut perform or speak at the event.")

    def past_sponsors(self):
        print("Bot: Yes! We’ve been sponsored by brands like Jungle Safari in past editions.")

    def help_info(self):
        print("Bot: You can ask about 'theme for 2025', 'technical events', 'how to register', 'accommodation', and more!")

if __name__ == "__main__":
    bot = TechnovateChatbot()
    bot.chat()
