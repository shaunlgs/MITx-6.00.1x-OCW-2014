def countVowel(x):
     vowel = 0
     for i in x:
         if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
             vowel += 1
     print("Number of vowels: " + str(vowel))
s = 'azcbobobegghakl'
countVowel(s)