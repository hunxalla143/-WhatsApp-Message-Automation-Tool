sent_messages = set()

def already_sent(phone, message):
    key = f"{phone}_{message}"

    if key in sent_messages:
        return True

    sent_messages.add(key)
    return False