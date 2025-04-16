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
            "help": self.help_info,
            "opening ceremony": self.opening_ceremony
        }
        self.greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]
    
    def chat(self):
        print("Bot 🤖: Hey there! I’m your friendly Technovate Bot. Ask me anything about our college fest!")
        while True:
            query = input("\nYou: ").lower().strip()
            if query in ["exit", "quit", "bye"]:
                print("Bot 🤖: Goodbye! See you at Technovate 🎉")
                break

            if query in self.greetings:
                print("Bot 🤖: Hello! 😊 How can I help you today?")
                continue

            found = False
            for key in self.commands:
                if key in query:
                    self.commands[key]()
                    found = True
                    break
            if not found:
                print("Bot 🤖: Hmm... I didn’t quite catch that. Try asking something else or type 'help' for options.")

    def about_technovate(self):
        print("Bot 🤖: Technovate is our college’s annual tech-cultural fest, blending tech events with cultural performances.")

    def theme(self):
        print(f"Bot 🤖: Yes! This year’s theme is “{self.theme_2025}” — celebrating innovation, creativity, and collaboration.")

    def team_requirement(self):
        print("Bot 🤖: Some events are solo, while others need teams of 2–4. Check event pages for more info.")

    def tech_events(self):
        print("Bot 🤖: We’ve got hackathons, coding contests, robotics challenges, IoT expos, and tech quizzes!")

    def cultural_events(self):
        print("Bot 🤖: You can enjoy dance battles, band performances, fashion shows, open mic nights, and drama competitions!")

    def open_stage(self):
        print("Bot 🤖: Totally! The Open Mic Stage is perfect for singers, poets, and performers. Registration opens soon!")

    def external_participation(self):
        print("Bot 🤖: Yes, many cultural events are open to people from outside our college. Just check the event rules.")

    def registration_info(self):
        print("Bot 🤖: Register through our official website under the 'Register' section. Fest passes and individual event options are available.")

    def event_registration(self):
        print("Bot 🤖: Yep! You'll need to register separately for each event you'd like to attend.")

    def accommodation_info(self):
        print("Bot 🤖: Outstation participants can get hostel accommodation at a small charge. Info is on the 'Stay' section.")

    def food_info(self):
        print("Bot 🤖: Food? We got you! Canteens, food stalls, and a dedicated food court will be available during the fest!")

    def contact_info(self):
        print("Bot 🤖: You can always talk to me or check the 'Contact Us' page for reaching coordinators or support.")

    def previous_theme(self):
        print("Bot 🤖: The theme for Technovate 2024 was “Beyond Boundaries” — all about limitless innovation!")

    def celeb_guests(self):
        print("Bot 🤖: Past guests include Samay Raina and Seedhe Maut! We always aim to bring in exciting names.")

    def past_sponsors(self):
        print("Bot 🤖: We’ve had sponsors like Jungle Safari support us in earlier editions of Technovate.")

    def help_info(self):
        print("Bot 🤖: You can ask about events, how to register, food, accommodation, previous themes, and more!")

    def opening_ceremony(self):
        print("""
Bot 🤖: Here's the Opening Ceremony Schedule for Technovate 6.0 (21st March, Day 1):
--------------------------------------------------
🕥 10:30 AM - Commencement of Opening Ceremony  
🪔 10:30 AM – 10:35 AM - Lighting of the Lamp  
🎵 10:35 AM – 10:40 AM - Saraswati Vandana  
🎤 10:40 AM – 10:45 AM - Speech by Dean Academics & Registrar  
📋 10:45 AM – 10:50 AM - Program Overview by Faculty Coordinator  
🎙 10:50 AM – 10:55 AM - Speech by Student Coordinator  
🙏 10:55 AM – 11:00 AM - Vote of Thanks by SAC President  
💃 11:00 AM – 11:10 AM - Flashmob by Students  
✅ 11:10 AM – 11:15 AM - Conclusion of Opening Ceremony
        """)

if __name__ == "__main__":
    bot = TechnovateChatbot()
    bot.chat()
