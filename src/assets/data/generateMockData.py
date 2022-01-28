import json
import random
import time
import uuid

options = {
    "numOfAuthors": (3, 7),
    "numOfArticlesPerAuthor": (7, 10),
    "numOfCommentsPerArticle": (3, 10),
    "numOfReplysPerComment": (0, 2),
}
authors = []
articles = []
comments = []
replys = []

def getPlaceholderText():
    loremIpsumText = "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Rem maiores nihil alias quam obcaecati magnam, libero iusto ea sed, corporis hic voluptatem in eveniet deserunt. Cupiditate optio voluptas iste dignissimos enim quod laborum nulla vel illum, quisquam excepturi voluptatem pariatur. Quibusdam hic delectus qui? Praesentium tempore repudiandae qui, magni non cum, quae quod voluptatum similique recusandae quos voluptate officia animi ipsum quam omnis minima voluptatem delectus ullam. Nihil neque reiciendis consectetur numquam ab maiores, quidem odit distinctio esse natus, eum nesciunt facere? Laborum veniam voluptates incidunt explicabo odio nihil, est ipsum ipsa, quidem, similique quo perspiciatis error saepe id sequi!"
    return loremIpsumText + " " + loremIpsumText + " " + loremIpsumText + " " + loremIpsumText + " " + loremIpsumText

def getRandomLoremIpsum(size):
    loremIpsumText = "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Rem maiores nihil alias quam obcaecati magnam, libero iusto ea sed, corporis hic voluptatem in eveniet deserunt. Cupiditate optio voluptas iste dignissimos enim quod laborum nulla vel illum, quisquam excepturi voluptatem pariatur. Quibusdam hic delectus qui? Praesentium tempore repudiandae qui, magni non cum, quae quod voluptatum similique recusandae quos voluptate officia animi ipsum quam omnis minima voluptatem delectus ullam. Nihil neque reiciendis consectetur numquam ab maiores, quidem odit distinctio esse natus, eum nesciunt facere? Laborum veniam voluptates incidunt explicabo odio nihil, est ipsum ipsa, quidem, similique quo perspiciatis error saepe id sequi!"
    loremIpsumList = loremIpsumText.split(" ")
    
    res = ""
    for i in range(size):
        rand = random.randint(0, len(loremIpsumList) - 1)
        res = res + " " + loremIpsumList[rand]

    return res

def getRandomName():
    firstNameList = ["John", "Jane", "Olivia", "Liam", "Emma", "Noah", "Amelia", "Oliver", "Ava", "Lucas", "Sophia", "Mason"]
    lastNameList = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller"]
    
    firstName = random.randint(0, len(firstNameList) - 1)
    lastName = random.randint(0, len(lastNameList) - 1)

    return firstNameList[firstName] + " " + lastNameList[lastName]

def getRandomPersonImg():
    imgList = [
        "https://images.unsplash.com/photo-1643057752896-b6fb04a50b85?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&q=80",
        "https://images.unsplash.com/photo-1643104177201-e01a1a87c58f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80",
        "https://images.unsplash.com/photo-1642982156172-32fd217b408c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2050&q=80",
        "https://images.unsplash.com/photo-1643031699343-a35c47d7a2d9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&q=80",
        "https://images.unsplash.com/photo-1642478872194-855316ae300c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&q=80",
        "https://images.unsplash.com/photo-1642328159992-b1d6010e8b40?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&q=80",
        "https://images.unsplash.com/photo-1642760063303-60747504fcb0?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&q=80",
        "https://images.unsplash.com/photo-1642715729583-22dc46d09c8c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&q=80",
        "https://images.unsplash.com/photo-1642978277577-83c6ceac4820?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1364&q=80",
        "https://images.unsplash.com/photo-1642802767826-55fb299a842e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1336&q=80",
        "https://images.unsplash.com/photo-1642882874306-87396d960694?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&q=80",
        "https://images.unsplash.com/photo-1642736468842-c6bdcfbbcd28?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80",
        "https://images.unsplash.com/photo-1642607964505-608b289c0d82?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&q=80"
    ]
    randImg = random.randint(0, len(imgList) - 1)
    return imgList[randImg]

def getRandomImgURL():
    imgList = [
        "https://images.unsplash.com/photo-1641901255710-1683e9cd8b7a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2371&q=80",
        "https://images.unsplash.com/photo-1637263972873-d358c3eb4543?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80",
        "https://images.unsplash.com/photo-1642860086450-f711c98b45fd?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80",
        "https://images.unsplash.com/photo-1545104578-2cc1ae6e74fc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2371&q=80",
        "https://images.unsplash.com/photo-1642841220705-b03194dd9de7?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80",
        "https://images.unsplash.com/photo-1642888374460-a75f4486b014?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2150&q=80",
        "https://images.unsplash.com/photo-1631027761930-bc3bcfd2be74?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80",
        "https://images.unsplash.com/photo-1642107406176-c2e16dff4990?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80",
        "https://images.unsplash.com/photo-1643144282726-8736271c5a95?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2369&q=80",
        "https://images.unsplash.com/photo-1643185694740-7a6ea3bac9f5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2316&q=80",
        "https://images.unsplash.com/photo-1643288939906-5c6c60c9d289?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2833&q=80",
        "https://images.unsplash.com/photo-1643178059754-4d20b0d0a517?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80",
        "https://images.unsplash.com/photo-1643245253265-edb71a2a6161?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80",
        "https://images.unsplash.com/photo-1643325299938-e169dc70b04a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80",
        "https://images.unsplash.com/photo-1643345206288-85316ac8e420?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2364&q=80",
        "https://images.unsplash.com/photo-1643330683233-ff2ac89b002c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2128&q=80",
        "https://images.unsplash.com/photo-1643229901819-5631ef3893b6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2728&q=80",
        "https://images.unsplash.com/photo-1589109139946-d8f9a6e2fbda?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2832&q=80",
        "https://images.unsplash.com/photo-1589110211335-319c28fe49e4?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2369&q=80",
        "https://images.unsplash.com/photo-1576140540933-ecf8322e5f32?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2369&q=80",
        "https://images.unsplash.com/photo-1605354180969-0f3fc29665bf?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2369&q=80",
        "https://images.unsplash.com/photo-1597496328816-5b3113f1f758?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80",
        "https://images.unsplash.com/photo-1642548666500-7990b88e691f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2778&q=80"
    ]
    randImg = random.randint(0, len(imgList) - 1)
    return imgList[randImg]

def getCategory():
    categoryList = [
        "news",
        "business",
        "sport",
        "life",
        "tech",
        "travel"
    ]
    
    randImg = random.randint(0, len(categoryList) - 1)
    return categoryList[randImg]


def generateData():
    minNum, maxNum = options["numOfAuthors"]
    rand = random.randint(minNum, maxNum)
    
    for i in range(rand):
        id = str(uuid.uuid4())
        newAuthor = {}
        
        newAuthor["id"] = id
        newAuthor["name"] = getRandomName()
        newAuthor["date"] = int(time.time())
        newAuthor["imgURL"] = getRandomPersonImg()
        newAuthor["AboutMe"] = getRandomLoremIpsum(50)
        newAuthor["writtenArticles"] = initArticles(id)
        
        authors.append(newAuthor)

def initArticles(authorId):
    minNum, maxNum = options["numOfArticlesPerAuthor"]
    rand = random.randint(minNum, maxNum)
    
    idList = []
    
    for i in range(rand):
        id = str(uuid.uuid4())
        newArticle = {}
        
        newArticle["id"] = id
        newArticle["authorId"] = authorId
        newArticle["date"] = int(time.time())
        newArticle["category"] = getCategory()
        newArticle["imgURL"] = getRandomImgURL()
        newArticle["title"] = getRandomLoremIpsum(6)
        newArticle["content"] = getPlaceholderText()
        newArticle["commentIds"] = initComments(id)
        
        articles.append(newArticle)
        idList.append(id)
        
    return idList

def initComments(articleId):
    minNum, maxNum = options["numOfCommentsPerArticle"]
    rand = random.randint(minNum, maxNum)
    
    idList = []
    
    for i in range(rand):
        id = str(uuid.uuid4())
        newComment = {}
        
        newComment["id"] = id
        newComment["articleId"] = articleId
        newComment["user"] = getRandomName()
        newComment["date"] = int(time.time())
        newComment["imgURL"] = getRandomPersonImg()
        newComment["text"] = getRandomLoremIpsum(20)
        newComment["replyIds"] = initReplys(id)
        
        comments.append(newComment)
        idList.append(id)
        
    return idList

def initReplys(commentId):
    minNum, maxNum = options["numOfReplysPerComment"]
    rand = random.randint(minNum, maxNum)
    
    idList = []
    
    for i in range(rand):
        id = str(uuid.uuid4())
        newReply = {}
        
        newReply["id"] = id
        newReply["commentId"] = commentId
        newReply["user"] = getRandomName()
        newReply["date"] = int(time.time())
        newReply["imgURL"] = getRandomPersonImg()
        newReply["text"] = getRandomLoremIpsum(10)
        
        comments.append(newReply)
        idList.append(id)
        
    return idList
    
    
generateData()

generatedData = {    
    "authors": authors,
    "articles": articles,
    "comments": comments,
    "replys": replys,
}

with open('mockData.json', 'w') as outfile:
    json.dump(generatedData, outfile)
