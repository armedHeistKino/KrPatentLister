import xml.etree.ElementTree as ET

def parseXmlByOneLineFromString(text):
    try:
        text = text.replace("<?xml version=1.0 encoding=utf-8?>",
                            "<?xml version=\"1.0\" encoding=\"utf-8\"?>")
        root = ET.fromstring(text)
        
        return root
    except ET.ParseError as e:
        return None

def parseXmlByOneLineFromTextFile(path):
    parseForest = list()

    try:
        with open(path, "r", encoding="utf8") as f:
            while rawData := f.readline() != None: 
                xmlData = parseXmlByOneLineFromString(rawData)
                if xmlData == None:
                    raise RuntimeError('Parsing tree error')
                parseForest.append(xmlData)
    except RuntimeError: 
        return None
    finally:
        return parseForest

