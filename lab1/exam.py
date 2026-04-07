# buh useg lowercase bolgono
# useg too hooson zainaas busdiig zaigaar solino
# olon hooson zaig neg zai bolgono.

# def normalize_text(string):
#     sentence = string.split()
#     sen_str = ""
#     for word in sentence:
#         nextword = ""
#         for char in word:
#             if char.isalnum():
#                 nextword += char
#         sen_str += " " + nextword.lower()
#     return sen_str

def normalize_text(text: str) -> str:
    # 1. Split by any whitespace
    # 2. For each word, keep only alnum characters and lowercase them
    # 3. Join back with a single space
    words = text.split()
    clean_words = ["".join(char.lower() for char in word if char.isalnum()) for word in words]
    
    # Filter out any empty strings that might have resulted from purely special chars
    return " ".join(word for word in clean_words if word)


def main():
    print(normalize_text("This is     exa324%@#$ tesxt"))



if __name__ == '__main__':
    main()