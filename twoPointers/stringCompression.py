class Solution:
    def compress(self, chars: List[str]) -> int:
        slow = 0
        count = 1

        for fast in range(1, len(chars)):
            if chars[slow] != chars[fast]:
                chars[slow + 1] = count
                slow = fast
                count = 1
            elif fast == len(chars) - 1:
                chars[slow + 1] = count + 1
                count = 1
            else:
                count += 1
        print(chars)


# couldn't finish            