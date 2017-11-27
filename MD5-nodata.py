from createLocData import *
from createDistancePer import *
import xml.etree.ElementTree as ET
import hashlib
import json


def makeString():
    beforeStr = input("input:")
    jsonall = json.loads(beforeStr)
    print(jsonall)
    strall = ''
    keyList = []
    for i in jsonall:
        keyList.append(i)
        # print(keyList)
        # keyList.sort()
        # print(keyList)
        # for i in keyList:
        #     if (i != "signature"):
        # jsonsecond=json.loads(jsonall[i])
        # strall= i + "=" + jsonsecond["allLocJson"]
        # if(isinstance(jsonall[i],str)):
        # strall =  i + "=" + jsonall[i]
        # else:
        #     strall = strall + i + "=" + str(jsonall[i])
        # break
        # try:
        #     print("before:"+strall)
        #     strall = strall + i + "=" + jsonall[i]
        #     print("after:"+strall)
        # except TypeError:
        #     strall = strall + i + "=" + str(jsonall[i])
        # else:
        #     strall = strall + i + "=" + "null"

    for i in keyList:
        if i != "signature":
            if strall == '':
                try:
                    strall = strall + i + "=" + jsonall[i]
                except TypeError:
                    strall = strall + i + "=" + str(jsonall[i])

            else:
                try:
                    strall = strall + "&" + i + "=" + jsonall[i]
                except TypeError:
                    strall = strall + "&" + i + "=" + str(jsonall[i])
    strall = strall + "&"
    print(strall)

    List = XMLhandle()
    for z in List:
        addSalt = strall + z
        strmd5 = MD5cry(addSalt)
        print(strmd5)
        if strmd5 == jsonall["signature"]:
            print("Final:" + z)
            return 1
    print(strall)
    print(keyList)
    # strall = "allLocJson" + "=" + jsonall["allLocJson"]

    # for i in jsonall:
    #     try:
    #         strall = i + "=" + jsonall[i]
    #     except TypeError:
    #         strall = i + "=" + str(jsonall[i])
    #     for z in List:
    #         addSalt = strall + z
    #         strmd5 = MD5cry(addSalt)
    #         print(strmd5)
    #         if strmd5 == jsonall["signature"]:
    #             print("Final:" + z)
    #             return 1
    # strall=strall+"md5_sign_salt_run"

    # nothing wrong down here
    # print(MD5cry(strall))
    print("REAL:" + jsonall["signature"])
    # print(strall)
    # print(len(keyList))

def makeString2():
    beforeStr = input("input:")
    jsonall = json.loads(beforeStr)
    print(jsonall)
    strall = ''
    print(strall)
    jsonALoc=json.loads(jsonall["allLocJson"])
    listLov=json.loads(jsonALoc["allLocJson"])
    print(listLov)
    #jsonALoc["allLocJson"]=listLov
    jsonall["allLocJson"]=jsonALoc
    strall = "allLocJson" + "=" + (str)(jsonALoc["allLocJson"])
    strall = strall + "md5_sign_salt_run"
    print((str)(jsonall["allLocJson"]))
    # nothing wrong down here
    print("MyRe:" + MD5cry(strall))
    print("REAL:" + jsonall["signature"])
    # print(strall)
    # print(len(keyList))
    #have tried to

def makeStringDefalt():
    beforeStr = input("input:")
    jsonall = json.loads(beforeStr)
    print(jsonall)
    strall = ''
    jsonALoc = jsonall["allLocJson"]
    strall = "allLocJson" + "=" + jsonALoc
    strall = strall + "md5_sign_salt_run"
    print(strall)
    # nothing wrong down here
    print("MyRe:" + MD5cry(strall))
    print("REAL:" + jsonall["signature"])

def makeStringDelZip():
    beforeStr = input("input:")
    jsonall = json.loads(beforeStr)
    print(jsonall)
    strall = ''
    jsonALocPlusKeyStr = jsonall["allLocJson"]

    jsonALoc=json.loads(jsonALocPlusKeyStr)

    dicN={
        "allLocJson":jsonALoc["allLocJson"]
    }
    strall = "allLocJson" + "=" + json.dumps(dicN)
    strall = strall + "md5_sign_salt_run"
    print(strall)
    # nothing wrong down here
    print("MyRe:" + MD5cry(strall))
    print("REAL:" + jsonall["signature"])

def makeStringAddAndBeforeSalt():
    beforeStr = input("input:")
    jsonall = json.loads(beforeStr)
    print(jsonall)
    strall = ''
    jsonALoc = jsonall["allLocJson"]
    strall = "allLocJson" + "=" + jsonALoc+"&"
    strall = strall + "md5_sign_salt_run"
    print(strall)
    # nothing wrong down here
    print("MyRe:" + MD5cry(strall))
    print("REAL:" + jsonall["signature"])

def makeStringByUsingList():   #bug exist
    beforeStr = input("input:")
    jsonall = json.loads(beforeStr)
    print(jsonall)
    strall = ''
    jsonALocStr = jsonall["allLocJson"]
    jsonALoc=json.loads(jsonALocStr)
    listLoc=json.loads(jsonALoc["allLocJson"])
    strall = "allLocJson" + "=" + listLoc   #here is the bug .which should be str but a list
    strall = strall + "md5_sign_salt_run"
    print(strall)
    # nothing wrong down here
    print("MyRe:" + MD5cry(strall))
    print("REAL:" + jsonall["signature"])

def makeStringBychangeKeyName():
    beforeStr = input("input:")
    jsonall = json.loads(beforeStr)
    print(jsonall)
    strall = ''
    jsonALoc = jsonall["allLocJson"]
    strall = "allLoc" + "=" + jsonALoc
    strall = strall + "md5_sign_salt_run"
    print(strall)
    # nothing wrong down here
    print("MyRe:" + MD5cry(strall))
    print("REAL:" + jsonall["signature"])

def makeStringByCopy():
    '''delete for having no idea to delete data'''

def makeStringBycopyAndby():
    beforeStr = input("input:")
    strall =beforeStr
    strall = strall + "md5_sign_salt_run"
    print(strall)
    # nothing wrong down here
    print("MyRe:" + MD5cry(strall))
    print("REAL:" + "signature=signatureToReplace")

def makeStringAll():
    beforeStr = input("input:")
    jsonall = json.loads(beforeStr)
    print(jsonall)
    strall = ''
    keyList = []
    for i in jsonall:

        try:
                strall=i+"="+jsonall[i]+"md5_sign_salt_run"
                print(strall)
                print(MD5cry(strall))
                if(MD5cry(strall)==jsonall["signature"]):
                    print("real i :"+i)
                    break
        except :
            strall = i + "=" + str(jsonall[i]) + "md5_sign_salt_run"
            print(strall)
            print(MD5cry(strall))
            if (MD5cry(strall) == jsonall["signature"]):
                print("real i :" + i)
                break

def makeStringAddAll():
    beforeStr = input("input:")
    jsonall = json.loads(beforeStr)
    strall=""
    ture="true"
    false="false"
    for i in jsonall:
        print(i)
        if strall=="":
            strall=i+"="+jsonall[i]
        elif i != "signature":
            try:
                strall=strall+"&"+i+"="+jsonall[i]
            except:
                strall = strall + "&" + i + "=" + str(jsonall[i])
    print(strall)
    strall=strall+"&"+"md5_sign_salt_run"
    signature=MD5cry(strall)
    print(signature)

def makeStringAddAllNoAnd():
    beforeStr = input("input:")
    jsonall = json.loads(beforeStr)
    strall=""
    for i in jsonall:
        print(i)
        if strall=="":
            strall=i+"="+jsonall[i]
        elif i != "signature":
            try:
                strall=strall+i+"="+jsonall[i]
            except:
                strall = strall  + i + "=" + str(jsonall[i])

    strall=strall+"md5_sign_salt_run"
    print(strall)
    signature=MD5cry(strall)
    print(signature)

def makeStringAddAllMoreS():
    beforeStr = input("input:")
    jsonall = json.loads(beforeStr)
    strall=""
    ture="true"
    false="false"
    for i in jsonall:
        print(i)
        if strall=="":
            strall=i+"="+jsonall[i]
            strall = strall + "&" + "md5_sign_salt_run"
        elif i != "signature":
            try:
                strall=strall+"&"+i+"="+jsonall[i]
                strall = strall + "&" + "md5_sign_salt_run"
            except:
                strall = strall + "&" + i + "=" + str(jsonall[i])
                strall = strall + "&" + "md5_sign_salt_run"
    print(strall)

    signature=MD5cry(strall)
    print(signature)

def makeStringAddAllOnwA():
    beforeStr = input("input:")
    jsonall = json.loads(beforeStr)
    strall=""
    ture="true"
    false="false"
    for i in jsonall:
        print(i)
        if strall=="":
            strall=i+"="+jsonall[i]
        elif i != "signature":
            try:
                strall=strall+i+"="+jsonall[i]
            except:
                strall = strall  + i + "=" + str(jsonall[i])
    print(strall)
    strall = strall + "&md5_sign_salt_run"
    signature=MD5cry(strall)
    print(signature)

def makeStringAddAllBackDire():
    beforeStr = input("input:")
    jsonall = json.loads(beforeStr)
    strall=""
    ture="true"
    false="false"
    for i in jsonall:
        print(i)
        if i != "signature":
            try:
                strall=i+"="+jsonall[i]+"&"+strall
            except:
                strall =i + "=" + str(jsonall[i])+"&"+strall
    print(strall)
    strall=strall+"md5_sign_salt_run"
    signature=MD5cry(strall)
    print(signature)

def makeStringAddAllBugS():
    ture = "true"
    false = "false"
    beforeStr = input("input:")
    jsonall = json.loads(beforeStr)
    strall=""
    for i in jsonall:
        print(i)
        if i != "signature":
            try:
                strall=strall+i+"="+jsonall[i]+"&"
            except:
                strall = strall  + i + "=" + str(jsonall[i])+ "&"
    strall=strall+"md5_sign_salt_run"
    print(strall)
    signature=MD5cry(strall)
    print(signature)


def makeStringAddAllSigna():
    beforeStr = input("input:")
    jsonall = json.loads(beforeStr)
    strall=""
    ture="true"
    false="false"
    for i in jsonall:
        print(i)
        if strall=="":
            strall=i+"="+jsonall[i]
        elif i != "signature":
            try:
                strall=strall+"&"+i+"="+jsonall[i]
            except:
                strall = strall + "&" + i + "=" + str(jsonall[i])
    print(strall)
    signature=MD5cry(strall)
    print(signature)
    strall=signature+"md5_sign_salt_run"
    signature = MD5cry(strall)
    print(signature)

def tokensign():

    namelist=["timeStamp","token","uid",""]
    valuelist=["timeStampToReplace","tokenToReplace","UIDToReplace",""]
    salt=["md5_sign_salt","2131296439",""]
    mark=["&","=",""]
    a=0
    d=1
    e=2

    b = 0
    while(b<3):
        c = 0
        while(c<3):
            f = 0
            while(f<3):
                g = 0
                while(g<2):
                    if(g==1):
                        a=3
                        d=3
                        e=3
                    else:
                        a = 0
                        d = 1
                        e = 2
                    strall=namelist[a]+mark[b]+valuelist[a]+mark[c]+   namelist[d]+mark[b]+valuelist[d]+mark[c]+   namelist[e]+mark[b]+valuelist[e]+mark[c]+ salt[f]
                    print(strall)
                    sign=MD5cry(strall)
                    print(sign)
                    if(sign=="signToReplace"):
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        return
                    g=g+1
                f=f+1
            c=c+1
        b=b+1
def token():
    strall = "timeStamp=" + "timeStampToReplace" + "token=" + "tokenToReplace" + "uid=" + "UIDToReplace" + "md5_sign_salt"
    print(MD5cry(strall))
    print("signToReplace")

def tokenA():
    strall = "timeStamp=" + "timeStampToReplace&" + "token=" + "tokenToReplace&" + "uid=" + "UIDToReplace&" + "md5_sign_salt"
    print(MD5cry(strall))
    print("signToReplace")

def tokendai():
    strall = "timeStamp"+"=" + "timeStampToReplace"+ "md5_sign_salt"
    print(MD5cry(strall))
    print("signToReplace")

def tokendai1():
    strall = "timeStamp"+"=" + "timeStampToReplace"+ "2131296439"
    print(MD5cry(strall))
    print("signToReplace")


def tokenMyself():
    strall = "timeStamp=" + "timeStampToReplace"+"timeStamp=" + "timeStampToReplace&" + "token=" + "tokenToReplace&" + "uid=" + "UIDToReplace&" + "md5_sign_salt"
    print(MD5cry(strall))
    print("signToReplace")

def makeStringAddAllInt():
    ture = "true"
    false = "false"
    beforeStr = input("input:")
    jsonall = json.loads(beforeStr)
    strall=""
    for i in jsonall:
        print(i)
        if i != "signature":
            try:
                strall=strall+i+"="+jsonall[i]+"&"
            except:
                strall = strall  + i + "=" + str(jsonall[i])+ "&"
    strall=strall+"2131296440"
    print(strall)
    signature=MD5cry(strall)
    print(signature)



def MD5cry(stringTo):
    hash_md5 = hashlib.md5(stringTo.encode("utf8"))
    return hash_md5.hexdigest()

def XMLhandle():
    tree = ET.ElementTree(file="public.xml")
    child1 = tree.getroot()
    strList = []
    for i in child1:
        strList.append(i.attrib['name'])
        print(i.attrib['name'])
    return strList


if __name__ == '__main__':
    tokendai1()