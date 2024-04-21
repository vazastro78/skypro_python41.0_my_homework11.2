def uppercase(text: str):
    '''
    local function long description uppercase of input text
    '''
    return text.upper()

def capitalize(text: str):
    '''
    local function long description capitalize of input text
    '''
    return " ".join([item_text.capitalize() for item_text in text.split(" ")])
