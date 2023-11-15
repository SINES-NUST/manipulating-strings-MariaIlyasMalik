text = input()

def extract_host(text):
    atpos = text.find('@')
    if atpos != -1:
        sppos = text.find(' ', atpos)
        if sppos != -1:
            host = text[atpos + 1 : sppos]
            return host
    return None

result = extract_host(text)
print(result)