from collections import defaultdict

class FrequencyTracker:

    def __init__(self):
        # count of each number
        self.cnt = defaultdict(int)
        # number of numbers that appear exactly f times
        self.freq = defaultdict(int)

    def add(self, number: int) -> None:
        old_count = self.cnt[number]
        new_count = old_count + 1
        self.cnt[number] = new_count

        # update frequency maps
        if old_count > 0:
            self.freq[old_count] -= 1
        self.freq[new_count] += 1

    def deleteOne(self, number: int) -> None:
        if self.cnt[number] == 0:
            return  # number not present

        old_count = self.cnt[number]
        new_count = old_count - 1
        self.cnt[number] = new_count

        # update frequency maps
        self.freq[old_count] -= 1
        if new_count > 0:
            self.freq[new_count] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0