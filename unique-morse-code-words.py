class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        arr = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        diff_trans = []

        letter_to_char = {chr(ord('a') + i): arr[i] for i in range(26)}
        for word in words:
           morse_word = ''.join(letter_to_char[char] for char in word)
           diff_trans.append(morse_word)
        return len(set(diff_trans))   
        
