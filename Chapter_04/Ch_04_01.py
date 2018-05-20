# Hanoi tower recursive version


class Hanoi:
    def __init__(self):
        self.total = 0
        pass

    def move(self, where_from, where_to):
        self.total += 1
        print("[", self.total, "] Move from", where_from, "to", where_to)

    def hanoi(self, num, where_from, where_by, where_to):
        if num == 1:
            self.move (where_from, where_to)
        else:
            self.hanoi (num-1, where_from, where_to, where_by)
            self.move(where_from, where_to)
            self.hanoi(num - 1, where_by, where_from, where_to)


# main() function
if __name__ == "__main__":
    number = int(input("Enter height of HANOI tower -> "))
    hanoi = Hanoi()
    # From 1st pole to 3rd pole by using 2nd pole
    hanoi.hanoi(number, 1, 2, 3)