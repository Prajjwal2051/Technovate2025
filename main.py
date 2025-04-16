import random

class TechnovateChatbot:
    def __init__(self):
        self.theme_2025 = "the theme will be inserted here"
        self.commands = {
            "technovate": self.about_technovate,
            "theme": self.theme,
            "team": self.team_requirement,
            "technical": self.tech_events,
            "cultural": self.cultural_events,
            "talent": self.open_stage,
            "external": self.external_participation,
            "register": self.registration_info,
            "accommodation": self.accommodation_info,
            "food": self.food_info,
            "contact": self.contact_info,
            "last year": self.previous_theme,
            "celebrity": self.celeb_guests,
            "sponsor": self.past_sponsors,
            "help": self.help_info
        }

        self.greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]
        self.small_talk = {
            "how are you": "I'm doing great! Excited for Technovate. What about you?",
            "what's up": "All set for Technovate! Have you checked the events?",
            "how's it going": "Going well! There's a lot of energy building up for the fest!"
        }

    def chat(self):
        print("Bot: Hey! I’m the Technovate Bot 🤖")
        print("Ask me anything about our college fest or just say hi!")

        while True:
            query = input("\nYou: ").lower().strip()

            if query in ["exit", "quit", "bye"]:
                print("Bot: Bye! Hope to see you at Technovate 😊")
                break

            if any(greet in query for greet in self.greetings):
                print(random.choice([
                    "Bot: Hello! 😊 What would you like to know about Technovate?",
                    "Bot: Hey there! Ask me anything about the fest.",
                    "Bot: Hi! Ready to explore Technovate?"
                ]))
                continue

            for phrase in self.small_talk:
                if phrase in query:
                    print(f"Bot: {self.small_talk[phrase]}")
                    break
            else:
                found = False
                for key in self.commands:
                    if key in query:
                        self.commands[key]()
                        found = True
                        break

                if not found:
                    print("Bot: Hmm, I didn't get that. Maybe ask about the theme, events, or registration? Type 'help' if you're stuck.")

    # ----- FEST RESPONSES -----

    def about_technovate(self):
        print("Bot: Technovate is our college’s annual tech-cultural fest, blending tech events with cultural performances.")

    def theme(self):
        print(f"Bot: Yes! This year’s theme is \"{self.theme_2025}\" — celebrating innovation, creativity, and collaboration.")

    def team_requirement(self):
        print("Bot: Some events are solo, others need teams of 2–4. You’ll find details on the event pages.")

    def tech_events(self):
        print("Bot: We’ve got hackathons, coding contests, robotics, IoT expos, and tech quizzes!")

    def cultural_events(self):
        print("Bot: Dance battles, band shows, fashion walk, open mic nights, and drama performances await!")

    def open_stage(self):
        print("Bot: Yes! Our Open Mic Stage welcomes singers, poets, and performers. Registrations open soon!")

    def external_participation(self):
        print("Bot: Definitely! Many cultural events are open to students from other colleges too.")

    def registration_info(self):
        print("Bot: You can register on our official website. Event-wise and fest passes both are available.")

    def event_registration(self):
        print("Bot: Yes, you need to register separately for each event you wish to join.")

    def accommodation_info(self):
        print("Bot: Yes, outstation participants can get hostel accommodation for a nominal charge.")

    def food_info(self):
        print("Bot: Lots of food options! Food court, stalls, and the canteen will all be active.")

    def contact_info(self):
        print("Bot: You can contact us through the website or ask me and I’ll guide you!")

    def previous_theme(self):
        print("Bot: Technovate 2024’s theme was \"Beyond Boundaries\" – celebrating limitless creativity!")

    def celeb_guests(self):
        print("Bot: Past guests include Samay Raina and Seedhe Maut! We love hosting cool people.")

    def past_sponsors(self):
        print("Bot: Yes! We’ve had brands like Jungle Safari as sponsors in earlier editions.")

    def help_info(self):
        print("Bot: You can ask about 'theme', 'technical events', 'cultural events', 'registration', 'accommodation', and more!")

if __name__ == "__main__":
    bot = TechnovateChatbot()
    bot.chat()
