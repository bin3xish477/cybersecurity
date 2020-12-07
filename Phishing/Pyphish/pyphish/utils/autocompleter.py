addrs = (
    "Campaigns", "Group", "Templates", 
    "Pages", "SMTP"
)

def auto_complete(text, state):
    options = [x for x in addrs if x.startswith(text)]
    try:
        return options[state]
    except IndexError:
        return None
