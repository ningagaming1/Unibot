from modules import budget, tic_tac_toe, todo, contacts, journal, web,lpu,grades
from files import organizer
from core import chatbot



INTENTS = {
    "budget": {
        "keywords": [
            "budget",
            "money",
            "expense",
            "spend",
            "cash"
            ],
        "module": budget
    },
    "todo": {
        "keywords": [
            "task",
            "homework",
            "todo",
            "remind",
            "work"
            ],
        "module": todo
    },
    "contacts": {
        "keywords": [
            "contact",
            "phone",
            "number"
            ],
        "module": contacts
    },
    "journal": {
        "keywords": [
            "journal",
            "diary",
            "note"
            ],
        "module": journal
    },
    "tic tac toe": {
        "keywords": [
            "tic tac toe",
            "fun",
            "game"
            ],
        "module": tic_tac_toe
    },
    "files": {
        "keywords": [
            "organize",
            "file",
            "sort",
            "clean"
            ],
        "module": organizer
    },
    "chatbot": {
    "keywords": [
            "hi",
            "hello",
            "hey",
            "chill",
            "help"
        ],
    "module": chatbot
    },
    "web": {
    "keywords": [
        "spotify",
        "youtube",
        "google",
        "search",
        "open",
        "what",
        "play",
        "wiki",
        "yt",
        "wikipedia"
        ],
    "module": web
    },
    "lpu":{
    "keywords":[
            "dashboard",
            "ums",
            "lpu touch",
            "class"
        ],
    "module": lpu
    },
    "grades":{
    "keywords":[
        "grade",
        "grades",
        "marks",
        "analyze",
        "stats",
        "subject"
    ],
    "module":grades
    }
}


def route(user_input, user_data):

    input_data = user_input.lower().split("and")

    for n in input_data:
        n = n.strip()  # remove extra spaces

        matched = False
        
        for intent_name, intent_data in INTENTS.items():
            for keyword in intent_data["keywords"]:
                if keyword in n:

                    # call module
                    intent_data["module"].handle(n, user_data)

                    matched = True
                    break

            if matched:
                break

        if not matched:
            print(f"❌ Could not understand: {n}")
            