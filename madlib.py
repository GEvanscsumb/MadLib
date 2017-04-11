"""
Mad Lib Generator 
@Autors Trammel May, Gene Evans, Trent Duhart
@Date April 10th, 2017
"""

def readText(filePath):
  text = open(filePath, 'r').read()
  combine(text, getAnalytics(analyze(text)))
 
def combine(text, matchers):
  import re, random
  list = re.findall(r"[\w\-?\w?]+|['s]+|[\(\)\".,!?;']", text)
  length = len(list)
  for i in range(0, length):
    if random.randrange(100) < 5:
      matcher = matchers[i][1]
      if matcher in tagMap():
        userInput = requestString("Please select enter a(n) " + tagMap()[matcher])
        if userInput == "QUIT":
          printNow("returning...")
          return
        else:
          list[i] = userInput
  printList(list, matchers)

def printList(list, matchers):
  import re
  opens = "\(|\{|\[|['\"][^'s]"
  closes = "('s)|[\(\)\}\]'\"\.,?!;:]"
  openQuote = false
  finalString = ""
  for i in range(0, len(list)):
    if list[i] == "\"" and not openQuote:
      finalString += " " + list[i]
      openQuote = true
    elif list[i] == "\"":
      finalString += list[i] + " "
      openQuote = false
    else:
      finalString += list[i]
      if not re.match(opens, list[i]):
        if i+1 < len(list) and not re.match(closes, list[i+1]):
          finalString += " "
  print finalString
      
def getAnalytics(text):
   import re
   return re.findall("\"position\":(\d\d?\d?),.*?partOfSpeech\":\"(.*?)\"", text)
     
def analyze(text):
  import urllib2
  headers = {"x-textrazor-key": "f877580308a886e62ac7eb0b22379cc9c592224dbe62d27291c7e8db"}
  data = "text=" + text + "&extractors=entities,entailments"
  request = urllib2.Request("http://api.textrazor.com", data, headers)
  response = urllib2.urlopen(request)
  return response.read()
  
def tagMap():
  return {"CC": "conjunction, coordinating", "CD": "numeral, cardinal", "DT": "determiner",
  "EX": "existential there", "FW": "foreign word", "IN": "preposition or conjuction, subordinating",
  "JJ": "adjective or numeral, ordinal", "JJR": "adjective, comparative", "JJS": "adjective, superlative",
  "LS": "list item marker", "MD": "modal auxiliary", "NN": "noun, common, singular or mass",
  "NNP": "noun, proper, singular", "NNPS": "noun, proper, plural", "NNS": "noun, common, plural",
  "PDT": "pre-determiner", "POS": "genitive marker", "PRP": "pronoun, personal", "RB": "adverb",
  "RBR": "adverb, comparative", "RBS": "adverb, superlative", "RP": "particle", "SYM": "symbol",
  "TO": "'to' as preposition or infinitive marker", "UH": "interjection", "VB": "verb, base form",
  "VBD": "verb, past tense", "VBG": "verb, present participle or gerund", "VBN": "verb, past participle",
  "VBP": "verb, present tense, not third person singular", "VBZ": "verb, present tense, third person singular",
  "WDT": " WH-determiner", "WP": "WH-pronoun", "WP$": "WH-pronoun, possesive", "WRB": "WH-adverb"}
 
  
