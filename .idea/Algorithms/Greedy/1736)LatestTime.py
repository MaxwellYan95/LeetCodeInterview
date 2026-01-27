class Solution:
    def maximumTime(self, time: str) -> str:
        lst = time.split(":")
        return self.maxHour(lst[0]) + ":" + self.maxMinute(lst[1])

    def maxHour(self, hr: str) -> str:
        nums = list(hr);
        if nums[0] == '?' and nums[1] == '?':
            return "23"
        elif nums[0] == '?':
            integer = int(nums[1]);
            if integer <= 3:
                nums[0] = "2"
            else:
                nums[0] = "1"
        elif nums[1] == '?':
            integer = int(nums[0]);
            if integer == 2:
                nums[1] = "3";
            else:
                nums[1] = "9"
        return "".join(nums)

    def maxMinute(self, minute: str) -> str:
        nums = list(minute);
        if nums[0] == '?' and nums[1] == '?':
            return "59"
        elif nums[0] == '?':
            nums[0] = '5'
        elif nums[1] == '?':
            nums[1] = '9'
        return "".join(nums)