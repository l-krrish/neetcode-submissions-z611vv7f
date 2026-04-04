class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_p=0
        right_p=len(s)-1
        while left_p<right_p:
            while not s[left_p].isalnum() and left_p<right_p:
                left_p+=1
            while not s[right_p].isalnum() and left_p<right_p:
                right_p-=1
            if s[left_p].lower()!=s[right_p].lower():
                return False
            left_p+=1
            right_p-=1
        return True