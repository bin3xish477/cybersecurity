addrs = (
    "campaigns", "groups", "templates", 
    "pages", "smtp", "help", "exit",
    "back", "cls", "clear"
)

def auto_complete(text, state):
    options = [x for x in addrs if x.startswith(text)]
    try:
        return options[state]
    except IndexError:
        return None
