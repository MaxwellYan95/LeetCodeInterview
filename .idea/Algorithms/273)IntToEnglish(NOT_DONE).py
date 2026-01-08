class Solution:

    nums = dict();
    ten1 = dict();
    tens = dict();
    hundred = dict();
    billion = dict();

    def numberToWords(self, num: int) -> str:
        place = 10**9;
        while place > num:
            place /= 10;
        digit = num//place;


    def createMap(self):
        lst = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"];
        for i in range(1, 10):
            index = i-1;
            self.nums[i] = lst[index];
        lst = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen"]
        for i in range(10, 16):
            index = i-10;
            self.ten1[i] = lst[index];
        lst = ["Six", "Seven", "Eight", "Nine"];
        for i in range(16, 20):
            index = i-16;
            self.ten1[i] = (lst[index] + "teen");
            if i == 18:
                self.ten1[i] = (lst[index][:len(lst[index])-1] + "teen");
        lst = ["Twenty", "Thirty", "Fourty", "Fifty"]
        index = 0;
        for i in range(20, 51, 10):
            self.tens[i] = lst[index]
            index += 1;
        lst = ["Six", "Seven", "Eight", "Nine"];
        index = 0;
        for i in range(60, 91, 10):
            self.tens[i] = (lst[index] + "ty");
            if i == 80:
                self.tens[i] = (lst[index][:len(lst[index])-1] + "ty");
            index += 1;
        self.hundred[100] = "Hundred"
        self.billion[10**3] = "Thousand"
        self.billion[10**6] = "Million"
        self.billion[10**9] = "Billion"

sol = Solution();
sol.createMap();