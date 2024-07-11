class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        sDict = {}
        tDict = {}

        # convert string s and string t into hashmaps char by char keep track of char freq
        for letter in s:
            if letter in sDict:
                sDict[letter] += 1
            else:
                sDict[letter] = 1
        
        for letter in t:
            if letter in tDict:
                tDict[letter] += 1
            else:
                tDict[letter] = 1
        
        # if a char in t and not in s, return char
        # or if char freq in t > char freq in s, return char
        for item in tDict:
            if item not in sDict or tDict[item] > sDict[item]:
                return item
            
            

if __name__ == "__main__":
    # do something here
    print("success")