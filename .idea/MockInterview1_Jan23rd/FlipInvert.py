class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        self.flip(image)
        self.invert(image)
        return image

    def flip(self, image: list[list[int]]):
        for index in range(len(image)):
            image[index].reverse();

    def invert(self, image: list[list[int]]):
        for row in range(len(image)):
            for col in range(len(image[0])):
                image[row][col] = (image[row][col]+1) % 2;