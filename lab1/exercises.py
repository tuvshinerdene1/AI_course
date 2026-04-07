def normalizer(cities):
    result = [city.lower().replace(" ", "") for city in cities]
    return result

def checkalnum(str):
    return "".join([x for x in str if x.isalnum()])

# def multispacecruncher(str):
    # result = ""
    # isspace = False
    # for x in str:
    #     if x != " ":
    #         result += x
    #         isspace = False
    #     else:
    #         if not isspace:
    #             result += x
    #             isspace = True
    # return result 


def multispacecruncher(str):
    return " ".join(str.split())

# def currencyconverter(str):
    # result = ""
    # for char in str:
    #     if char.isalnum() or char == ".":
    #         result += char

    # return result
def currencyconverter(str):
    clean_str = "".join(char for char in str if char.isdigit() or char==".")
    return clean_str

def domainextractor(str):
    afterat = str.split("@")[1]
    email = afterat.split(".")[0]
    return email

def letteronly(str):
    return "".join([char for char in str if char.isalpha()])

def numberonly(str):
    return "".join([char for char in str if char.isdigit()])

def lowerstring(str):
    return str.lower()

def stopwordstripper(sentence):
    result = []
    sentence = sentence.split()
    stopwords = ["a","an","the"]
    for word in sentence:
        if word.lower() in stopwords:
            continue
        result.append(word)
    return result
        
def onehotmapper(str):
    sentence = str.split()
    result = {}
    for word in sentence:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result


def unique(lst):
    """
    Returns the list of unique elements 
    """
    return list(set(lst))

def logparser(str):
    keyword = ""
    if str.find("ERROR:") == -1 and str.find("CRITICAL:") == -1:
        return
    if str.find("ERROR:") != -1:
        keyword = "ERROR:"
    if str.find("CRITICAL:") != -1:
        keyword = "CRITICAL:"
    
    msg = str.split(keyword)[1].strip()

    datetime = str.split(keyword)[0].strip()

    time = datetime[12:-1]
    result = {}
    
    time : int = 8
    
    result["time"] = time
    result["message"] = msg
    for key in result:
        print(result[key])

    return result




        

def main():
    # print(normalizer(["New     york", "adsfADSF"]))
    # print(checkalnum("123!@#$af#"))
    # print(multispacecruncher("adf          adf            da  ad"))
    # print(currencyconverter("$4,999.99"))
    # print(domainextractor("tuvshin.erdene@gmail.com"))
    # print(letteronly("hell5o"))
    # print(numberonly("5324adf1"))
    # print(lowerstring("afadsAFSDjfasdf"))
    # print(stopwordstripper("this is a apple the fuck the hell"))
    # print(onehotmapper("cat dog cat dog bee cat"))
    # print(unique([1,1,1,1,2,2,2,2,3,3,3,4,4,4,4]))
    # print(help(unique))
    # print(unique.__code__)
    # print(unique.__str__)
    print(logparser("[2026-02-24 10:16:01] ERROR: Connection failed"))
    print(main.__name__)



if __name__ == '__main__':
    main()