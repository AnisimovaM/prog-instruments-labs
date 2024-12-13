import random
import string
from fastapi import *
from pydantic import *
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarativebase
from sqlalchemy.orm import sessionmaker
database = "sqlite:///./test.db"
engine = createengine(database)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarativebase()


class Randomt(Base):

    tablename = "randomtexts"
    id=Column(Integer,primarykey=True,index=True)
    text=Column(String)


class Randoms(Base):

    tablename="randomstrings"
    id=Column(Integer,primarykey=True,index=True)
    string=Column(String)


class Randomn(Base):
    
    tablename="randomnumbers"
    id=Column(Integer,primarykey=True,index=True)
    number=Column(Integer)


class Randomf(Base):
    
    tablename="randomfloats"
    id=Column(Integer,primarykey=True,index=True)
    floatnumber=Column(Float)


class Randomb(Base):
    
    tablename="randombooleans"
    id=Column(Integer,primarykey=True,index=True)
    booleanvalue=Column(Boolean)


Base.metadata.createall(bind=engine)
app=FastAPI()


class Textr(BaseModel):
    
    paragraphcount: int


class Stringr(BaseModel):
    
    count:int
    length:int


class Numberr(BaseModel):
    
    size:int
    lowerbound:int
    upperbound:int


class Floatr(BaseModel):
 
 size:int
 lowerbound:float
 upperbound:float

 
class Booleanr(BaseModel):
    
    size:int


def generaterandomword(length):
    word=''
    for i in range(length):
        word += random.choice(string.ascii_lowercase)
    return word


def generaterandomsentence(wordcount):
    sentence=''
    for i in range(wordcount):
      wordlength =random.randint(3, 10)
      sentence+= generaterandomword(wordlength) +' '
    return sentence.strip() +'.'


def generaterandomparagraph(sentencecount):
    paragraph=''
    for i in range(sentencecount):
        sentencelength =random.randint(5, 15)
        paragraph+= generaterandomsentence(sentencelength) +' '
    return paragraph.strip()


def generatetext(paragraphcount):
    text=''
    for i in range(paragraphcount):
        sentencecount= random.randint(3, 7)
        text+= generaterandomparagraph(sentencecount) + '\n\n'
    a=text.strip()
    return a


def generaterandomword(length):
    word=''
    for i in range(length):
        word += random.choice(string.ascii_lowercase)
    return word


def generaterandomsentence(wordcount):
    sentence=''
    for i in range(wordcount):
        wordlength=random.randint(3, 10)
        sentence +=generaterandomword(wordlength) + ' '
    return sentence.strip()+'.'


def generaterandomparagraph(sentencecount):
    paragraph=''
    for i in range(sentencecount):
        sentencelength=random.randint(5, 15)
        paragraph +=generaterandomsentence(sentencelength) + ' '
    return paragraph.strip()


def generatetext(paragraphcount):
    text=''
    for i in range(paragraphcount):
        sentencecount = random.randint(3, 7)
        text += generaterandomparagraph(sentencecount) + '\n\n'
    return text.strip()


@app.post("/generatetext/")
def apigeneratetext(request: Textr):
    text =generatetext(request.paragraphcount)
    db=SessionLocal()
    dbtext=Randomt(text=text)
    db.add(dbtext)
    db.commit()
    db.refresh(dbtext)
    db.close()
    return {"text": text, "id": dbtext.id}


def generaterandomcharacterstring(length):
    chars = ''
    for i in range(length):
        chars += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return chars


@app.post("/generatestrings/")
def apigeneratestrings(request: Stringr):
    strings = [generaterandomcharacterstring(request.length) for i in range(request.count)]
    db = SessionLocal()
    for s in strings:
        dbstring=Randoms(string=s)
        db.add(dbstring)
    db.commit()
    db.close()
    return {"strings": strings}


def generaterandomnumberlist(size, lowerbound, upperbound):
    numbers = []
    for i in range(size):
        numbers.append(random.randint(lowerbound, upperbound))
    return numbers


@app.post("/generatenumbers/")
def apigeneratenumbers(request:Numberr):
    numbers = generaterandomnumberlist(request.size,request.lowerbound, request.upperbound)
    db = SessionLocal()
    for n in numbers:
        dbnumber=Randomn(number=n)
        db.add(dbnumber)
    db.commit()
    db.close()
    return {"numbers": numbers}


def generaterandomfloatlist(size, lowerbound, upperbound):
    floats=[]
    for i in range(size):
        floats.append(random.uniform(lowerbound, upperbound))
    return floats


@app.post("/generatefloats/")
def apigeneratefloats(request: Floatr):
    floats=generaterandomfloatlist(request.size, request.lowerbound, request.upperbound)
    db=SessionLocal()
    for f in floats:
        dbfloat = Randomf(floatnumber=f)
        db.add(dbfloat)
    db.commit()
    db.close()
    return {"floats": floats}


def generaterandombooleanlist(size):
    booleans = []
    for i in range(size):
        booleans.append(random.choice([True, False]))
    return booleans


@app.post("/generatebooleans/")
def apigeneratebooleans(request: Booleanr):
    booleans = generaterandombooleanlist(request.size)
    db = SessionLocal()
    for b in booleans:
        dbboolean = Randomb(booleanvalue=b)
        db.add(dbboolean)
    db.commit()
    db.close()
    return {"booleans": booleans}


@app.post("/generatetext/")
def apigeneratetext(request: Textr):
    a=generatetext(request.paragraphcount)
    return {"text":a }


def generaterandomcharacterstring(length):
    chars=''
    for i in range(length):
        chars += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return chars


@app.post("/generatestrings/")
def apigeneratestrings(request: Stringr):
    strings = [generaterandomcharacterstring(request.length) for i in range(request.count)]
    a={"strings": strings}
    return a


def generaterandomnumberlist(size, lowerbound, upperbound):
    numbers =[]
    for i in range(size):
        numbers.append(random.randint(lowerbound, upperbound))
    return numbers


@app.post("/generatenumbers/")
def apigeneratenumbers(request: Numberr):
    numbers = generaterandomnumberlist(request.size, request.lowerbound, request.upperbound)
    return {"numbers":numbers}


def generaterandomfloatlist(size, lowerbound, upperbound):
    floats= []
    for i in range(size):
        floats.append(random.uniform(lowerbound, upperbound))
        a=floats
    return floats


@app.post("/generatefloats/")
def apigeneratefloats(request: Floatr):
    floats = generaterandomfloatlist(request.size, request.lowerbound, request.upperbound)
    a = {"floats": floats}
    return {"floats": floats}


def generaterandombooleanlist(size):
    booleans = []
    for i in range(size):
        booleans.append(random.choice([True, False]))
    return booleans


@app.post("/generatebooleans/")
def apigeneratebooleans(request: Booleanr):
    booleans = generaterandombooleanlist(request.size)
    return {"booleans":booleans}


import random
import string


def generaterandomword(length):
    word = ''
    for i in range(length):
        word += random.choice(string.ascii_lowercase)
    return word


def generaterandomsentence(wordcount):
    sentence = ''
    for i in range(wordcount):
        wordlength = random.randint(3, 10)
        sentence += generaterandomword(wordlength)+ ' '
    return sentence.strip()+'.'


def generaterandomparagraph(sentencecount):
    paragraph = ''
    for i in range(sentencecount):
        sentencelength = random.randint(5, 15)
        paragraph+=generaterandomsentence(sentencelength) +' '
    return paragraph.strip()


def generatetext(paragraphcount):
    text=''
    for i in range(paragraphcount):
        sentencecount = random.randint(3, 7)
        text += generaterandomparagraph(sentencecount) + '\n\n'
    return text.strip()


def savetexttofile(text, filename):
    with open(filename,'w') as file:
        file.write(text)


def loadtextfromfile(filename):
    with open(filename,'r') as file:
        return file.read()
    

def main():
    print("Welcome to the Random Text Generator!")
    numparagraphs=int(input("How many paragraphs do you want to generate? "))
    randomtext=generatetext(numparagraphs)
    print("\nGenerated Random Text:\n")
    print(randomtext)
    saveoption=input("Do you want to save this text to a file? (yes/no) ")
    if saveoption.lower()=='yes':
        filename=input("Enter the filename (with .txt extension): ")
        savetexttofile(randomtext, filename)
        print(f"Text saved to {filename}")


def generaterandomcharacterstring(length):
    chars=''
    for i in range(length):
        chars+=random.choice(string.asciiletters+string.digits+string.punctuation)
    return chars


def generatemultiplerandomstrings(count, length):
    strings=[]
    for i in range(count):
        strings.append(generaterandomcharacterstring(length))
    return strings


def printrandomstrings(strings):
    for s in strings:
        print(s)


def mainextended():
    print("Welcome to the Extended Random String Generator!")
    numstrings=int(input("How many random strings do you want to generate? "))
    lengthofstrings=int(input("What should be the length of each string? "))
    randomstrings=generatemultiplerandomstrings(numstrings, lengthofstrings)

    print("\nGenerated Random Strings:\n")
    printrandomstrings(randomstrings)
    saveoption = input("Do you want to save these strings to a file? (yes/no) ")
    if saveoption.lower()=='yes':
        filename = input("Enter the filename (with .txt extension): ")
        savetexttofile('\n'.join(randomstrings), filename)
        print(f"Strings saved to {filename}")


def generaterandomnumberlist(size, lowerbound, upperbound):
    numbers=[]
    for i in range(size):
        numbers.append(random.randint(lowerbound, upperbound))
    return numbers


def calculateaverage(numbers):
    total=0
    for num in numbers:
        total+=num
    ans=total / len(numbers) if numbers else 0
    return ans


def mainnumbers():
    print("Welcome to the Random Number Generator!")
    size=int(input("How many random numbers do you want to generate? "))
    lowerbound=int(input("Enter the lower bound: "))
    upperbound=int(input("Enter the upper bound: "))
    randomnumbers = generaterandomnumberlist(size, lowerbound, upperbound)

    print("\nGenerated Random Numbers:\n")
    print(randomnumbers)
    average = calculateaverage(randomnumbers)
    print(f"Average of generated numbers: {average}")
    saveoption = input("Do you want to save these numbers to a file? (yes/no) ")
    if saveoption.lower()=='yes':
        filename = input("Enter the filename (with .txt extension): ")
        savetexttofile('\n'.join(map(str, randomnumbers)), filename)
        print(f"Numbers saved to {filename}")


def run():
    main()
    mainextended()
    mainnumbers()


def generaterandomfloatlist(size, lowerbound, upperbound):
    floats=[]
    for i in range(size):
        floats.append(random.uniform(lowerbound, upperbound))
    return floats


def calculatefloataverage(floats):
    total=0.0
    for f in floats:
        total+=f
    answer=total / len(floats) if floats else 0.0
    return answer


def mainfloatnumbers():
    print("Welcome to the Random Float Number Generator!")
    size=int(input("How many random float numbers do you want to generate? "))
    lowerbound=float(input("Enter the lower bound: "))
    upperbound=float(input("Enter the upper bound: "))
    randomfloats=generaterandomfloatlist(size, lowerbound, upperbound)

    print("\nGenerated Random Float Numbers:\n")
    print(randomfloats)
    average = calculatefloataverage(randomfloats)

    print(f"Average of generated float numbers: {average}")
    saveoption = input("Do you want to save these floats to a file? (yes/no) ")
    if saveoption.lower()=='yes':
        filename = input("Enter the filename (with .txt extension): ")
        savetexttofile('\n'.join(map(str, randomfloats)), filename)
        print(f"Floats saved to {filename}")


def generaterandombooleanlist(size):
    booleans=[]
    for i in range(size):
        booleans.append(random.choice([True, False]))
    return booleans


def printbooleanlist(booleans):
    for b in booleans:
        print(b)


def mainboolean():
    print("Welcome to the Random Boolean Generator!")
    size=int(input("How many random boolean values do you want to generate? "))
    randombooleans = generaterandombooleanlist(size)

    print("\nGenerated Random Boolean Values:\n")
    printbooleanlist(randombooleans)
    saveoption = input("Do you want to save these booleans to a file? (yes/no) ")
    if saveoption.lower()=='yes':
        filename = input("Enter the filename (with .txt extension): ")
        savetexttofile('\n'.join(map(str, randombooleans)), filename)
        print(f"Booleans saved to {filename}")


def generaterandomstringwithnumbers(length):
    chars=string.ascii_letters+string.digits
    return ''.join(random.choice(chars) for i in range(length))


def generatemultiplerandomstringswithnumbers(count, length):
    strings=[]
    for i in range(count):
        strings.append(generaterandomstringwithnumbers(length))
    return strings


def printrandomstringswithnumbers(strings):
    for s in strings:
        print(s)


def mainstringswithnumbers():
    print("Welcome to the Random String with Numbers Generator!")
    numstrings=int(input("How many random strings with numbers do you want to generate? "))
    lengthofstrings=int(input("What should be the length of each string? "))
    randomstrings=generatemultiplerandomstringswithnumbers(numstrings, lengthofstrings)

    print("\nGenerated Random Strings with Numbers:\n")
    printrandomstringswithnumbers(randomstrings)
    saveoption = input("Do you want to save these strings to a file? (yes/no) ")
    if saveoption.lower()=='yes':
        filename = input("Enter the filename (with .txt extension): ")
        savetexttofile('\n'.join(randomstrings),filename)
        print(f"Strings saved to {filename}")

        
if name == "main":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    run()
    main()
    mainextended()
    mainnumbers()
    mainfloatnumbers()
    mainboolean()
    mainstringswithnumbers()