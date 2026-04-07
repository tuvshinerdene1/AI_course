def normalize(string):
    result = ''
    for x in string:
        if x.isalnum():
            result += x
    return result

def main():
    print(normalize('Aaa$a91!@#$23'))


if __name__ == '__main__':
    main()

