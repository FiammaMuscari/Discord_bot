from random import choice, randint

def get_response(user_input:str)-> str:
    lowered: str = user_input.lower()
    
    if lowered == '':
        return 'Estas muy callado...'
    elif 'hola' in lowered:
        return 'Hola amig@!'
    elif 'como estas?' in lowered:
        return 'Bien, gracias!'
    elif 'chau' in lowered:
        return 'Nos vemos!'
    elif 'roll dice' in lowered:
        return f'You rolled:{randint(1,6)}'
    else:
        return choice(['No entiendo...',
                       'De qué estás hablando?',
                       'Puedes repetirlo?'])
    