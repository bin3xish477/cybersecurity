commands = (
    "campaigns", "groups", "templates", 
    "pages", "profiles", "help", "exit",
    "cls", "clear", "edit", "create",
    "get", "delete", "info", "set", "back",

    "name", "host", "email_address", "ignore_cert_errors"
)

def auto_complete(text, state):
    options = [command 
               for command in commands if command.startswith(text)
              ]
    try:
        return options[state]
    except IndexError:
        return None

