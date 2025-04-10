class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:

        def solve(number: str) -> int:
            number_len = len(number)
            number_int = int(number)
            s_len = len(s)
            s_int = int(s)
            if number_int == 0:
                return 0
            elif number_int < s_int:
                return 0
            elif number_int >= s_int and number_len == s_len:
                return 1
            first_digit = int(number[0])
            diff = number_len - s_len - 1 
            ret = min(first_digit, limit)
            tmp = ret
            if ret != first_digit:
                ret += 1
            for _ in range(diff):
                ret *= (limit+1)
            if tmp == first_digit:
                ret += solve(number[1:])
            return ret

        ans = solve(str(finish)) - solve(str(start-1))
        return ans
