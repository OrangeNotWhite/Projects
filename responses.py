import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if message == 'roll':
     return str(random.randint(1, 6))
    if p_message := '!help':
     return '`nice i guess`'
return 'i dont understand not english'

