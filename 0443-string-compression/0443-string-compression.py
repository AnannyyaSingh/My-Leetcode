class Solution:
    def compress(self, chars: List[str]) -> int:
        read, write = 0, 0
        n = len(chars)

        while(read < n):
            curr = chars[read]
            group_start = read

            while read < n and chars[read] == curr:
                read += 1
            count = read - group_start
            chars[write] = curr
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write