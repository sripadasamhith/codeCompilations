# Leetcode:       1768. Merge Strings Alternately
# 
# Description:    Given two strings: word1 and word2, merge strings by adding letters in alternating order starting with word1.
#                 If a word is longer than the other, then add the remaining letters to the end of the merged string.
#                 Return the merged string. 
# 
# Constraints:    1 <= word1.length, word2.length <= 100
# Examples:
# 
                    # Example 1:

                    # Input: word1 = "abc", word2 = "pqr"
                    # Output: "apbqcr"
                    # Explanation: The merged string will be merged as so:
                    # word1:  a   b   c
                    # word2:    p   q   r
                    # merged: a p b q c r

                    # Example 2:
                    # Input: word1 = "ab", word2 = "pqrs"
                    # Output: "apbqrs"
                    # Explanation: Notice that as word2 is longer, "rs" is appended to the end.
                    # word1:  a   b 
                    # word2:    p   q   r   s
                    # merged: a p b q   r   s

class Solution:

    # def alternateChars(self, word1, word2) -> str:
    #     mergedWord: str = ""
    #     # print(f"{word1}, {word2}")
    #     for i in range(len(word1)):
    #         mergedWord += word1[i]
    #         mergedWord += word2[i]
    #     # print(mergedWord)
    #     return mergedWord

    # def mergeAlternately1(self, word1: str, word2: str) -> str:
    #     mergedWord: str = ""

    #     # check if word1 longer than word2
    #     lengthDelta = len(word1) - len(word2)
    #     # print(lengthDelta)

    #     # if word1 longer
    #     if lengthDelta > 0:
    #         mergedWord = self.alternateChars(word1[:len(word2)], word2)
    #         mergedWord += word1[len(word2):]
        
    #     # if word2 longer
    #     elif lengthDelta < 0:
    #         lengthDelta *= -1
    #         mergedWord = self.alternateChars(word1, word2[:len(word1)])
    #         mergedWord += word2[len(word1):]

    #     # if word1 and word2 are the same length
    #     else:
    #         mergedWord = self.alternateChars(word1, word2)
        
    #     return mergedWord

    def mergeAlternately(self, word1: str, word2: str) -> str:

        # create an empty string
        mergedWord: str = ""

        # find the smallest word
        n = min(len(word1), len(word2))

        for i in range(n):
            mergedWord += word1[i]
            mergedWord += word2[i]

        mergedWord += word1[n:]
        mergedWord += word2[n:]
        
        return mergedWord

if __name__ == "__main__":
    word1 = "abc"
    word2 = "pqrs"

    sol = Solution()
    sol.mergeAlternately(word1,word2)
    print(sol.mergeAlternately(word1,word2))

