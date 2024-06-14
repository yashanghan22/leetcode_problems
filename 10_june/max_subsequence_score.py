from typing import List


class Solution:
    def custom_dynamic_pairs(self, lst, pair_size: int) -> List[List[int]]:
        def generate_pairs(current_list, current_pair: List[int], start: int):
            if len(current_pair) == pair_size:
                pairs.append(tuple(current_pair))
                return
            for i in range(start, len(current_list)):
                generate_pairs(current_list, current_pair +
                               [current_list[i]], i + 1)

        pairs = []
        generate_pairs(lst, [], 0)
        return pairs

    # def custom_three_pairs(self, lst: List[int]):
    #     pairs = []
    #     for i in range(len(lst)):
    #         for j in range(i + 1, len(lst)):
    #             for k in range(j + 1, len(lst)):
    #                 pairs.append((lst[i], lst[j], lst[k]))
    #     return pairs

    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        max = 0
        lef = self.custom_dynamic_pairs(nums1, k)
        right = self.custom_dynamic_pairs(nums2, k)

        for u, v in zip(lef, right):
            sum = 0
            min = v[0]
            for i in u:
                sum += i
            for j in v:
                if min > j:
                    min = j
            v = sum*min
            if v > max:
                max = v
        return max


if __name__ == '__main__':
    solution = Solution()
    # max = solution.maxScore([1, 3, 3, 2], [2, 1, 3, 4], 3)
    max = solution.maxScore([4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1)
    print(max)
    # pair = solution.custom_three_pairs([1, 3, 3, 2])
    # print(pair)
    # print(solution.custom_dynamic_pairs([1, 3, 3, 2], 1))
