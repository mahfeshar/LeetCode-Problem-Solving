class Solution:

    def encode(self, strs: List[str]) -> str:
        stringList = "["
        for i in range(len(strs)):
            stringList += "\"" + strs[i] + "\""
            if i != len(strs) - 1:
                stringList += ","
        stringList += "]"
        return stringList
    
    def decode(self, s: str) -> List[str]:
        newList = []
        word =  ""
        newWord = 0
        for i in range(1, len(s) - 1):
            if s[i] == "\"":
                newWord += 1
                if newWord == 2:
                    newList.append(word)
                    word = ""
                    newWord = 0
                    
                continue
            if s[i] == "," and newWord != 1:
                continue
            word += s[i]
        return newList
