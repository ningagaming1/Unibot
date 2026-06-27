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
    found = False    
    #devide and concure
    input_list = user_input.split("and")
    
    #print(INTENTS)    #dont remove this "#" if you dont know how to read through a mess 
    
    #cleaning and procesing the devided values
    for input_value in input_list:
        input_value = input_value.strip() 

        for module_name,module_data in INTENTS.items():
            
            #print(module_name)   #rremove this comment to see all the modules present
            #print(module_data)   #remove the coment to check the format of data

            for keyword in module_data["keywords"]:
                if keyword in input_value:
#calling module data taken from module data and send it to def handel of that modue
                    print(f"\n----Using {module_name} module.-----")
                    module_data["module"].handle(user_input,user_data)
                    found = True
                    #print("found")
                    break
            #this is to break the second internal loop
            if found == True:
                break
    if found == False:
        print("The bot did not understand you.")        
