class Solution:
    def reverse(self, x: int) -> int:
       sign = -1 if x < 0 else 1
       x = abs(x)

       rev_num = 0
       while x > 0:
           digit = x % 10
           x //= 10
           rev_num = rev_num * 10 + digit
       rev_num *= sign

       if -2**31 <= rev_num <= 2**31 -1:
          return rev_num
       return 0