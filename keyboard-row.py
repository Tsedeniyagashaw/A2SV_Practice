class Solution:
    def findWords(self, words: List[str]) -> List[str]:
      belonging_words = []
      rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
      for word in words:
        lower_word = word.lower()
        for row in rows:
          if set(lower_word) <= set(row):
             belonging_words.append(word)
      return belonging_words          
