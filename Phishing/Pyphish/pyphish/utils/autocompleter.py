commands = (
    "campaigns", "groups", "templates", 
    "pages", "smtp", "help", "exit",
    "back", "cls", "clear"
)

def auto_complete(text, state):
    options = [command 
               for command in commands if command.startswith(text)
              ]
    try:
        return options[state]
    except IndexError:
        return None
