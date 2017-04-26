def solution(X, Y, K, A, B):
    result = 0
    widths = calculate_lengths(X, A)
    heights = calculate_lengths(Y, B)
    return piece_size(widths, heights, K)


def calculate_lengths(side_length, cuts):
    result = []
    prev_cut = 0
    for cut in cuts:
        result.append(cut - prev_cut)
        prev_cut = cut
    result.append(side_length - prev_cut)
    result.sort()  # from lowest to highest
    return result


def piece_size(widths, heights, piece_ordinal):  # has log(n) time complexity
    print widths
    print heights
    print K
    N = len(widths)
    min_size = 1
    max_size = widths[N - 1] * heights[N - 1]
    while min_size <= max_size:
        size = (min_size + max_size) // 2
        if ordinal(widths, heights, size) >= piece_ordinal:
            min_size = size + 1
            result = size
        else:
            max_size = size - 1
    return result


def ordinal(widths, heights, size):  # has O(n) time complexity.
    N = len(widths)
    result = 0
    heightIndex = N - 1
    height = heights[heightIndex]
    for widthIndex in xrange(N):
        width = widths[widthIndex]
        while heightIndex >= 0 and width * height >= size:
            heightIndex -= 1
            height = heights[heightIndex]
        result += N - 1 - heightIndex
    return result


# X = 58
# Y = 45
# A = [1, 3, 8, 17, 27]
# # yields the widths: [30, 5, 4, 3, 2, 1]
# B = [1, 3, 6, 10, 15]
# # yields the heights: [31, 10, 9, 5, 2, 1]
# K = 12  # Per the table below, the 7th largest piece should have a size of 93
#
# print(solution(X, Y, K, A, B))

# Piece Size Rankings:
# 1: 30 x 31: 930
# 2: 30 x 10: 300
# 3: 30 x 9: 270
# 4: 5 x 31: 155
# 5: 30 x 5: 150
# 6: 4 x 31: 124
# 7: 3 x 31: 93
# 8: 2 x 31: 62
# 9: 30 x 2: 60
# 10: 5 x 10: 50
# 11: 5 x 9: 45
# 12: 4 x 10: 40
# 13: 4 x 9: 36
# 14: 1 x 31: 31
# 15: 30 x 1: 30
# 16: 3 x 10: 30
# 17: 3 x 9: 27
# 18: 5 x 5: 25
# 19: 2 x 10: 20
# 20: 4 x 5: 20
# 21: 2 x 9: 18
# 22: 3 x 5: 15
# 23: 2 x 5: 10
# 24: 1 x 10: 10
# 25: 5 x 2: 10
# 26: 1 x 9: 9
# 27: 4 x 2: 8
# 28: 3 x 2: 6
# 29: 1 x 5: 5
# 30: 5 x 1: 5
# 31: 4 x 1: 4
# 32: 2 x 2: 4
# 33: 3 x 1: 3
# 34: 2 x 1: 2
# 35: 1 x 2: 2
# 36: 1 x 1: 1

# Piece Sizes Indices
# 0: 30 x 31: 930
# 1: 30 x 10: 300
# 2: 30 x 9: 270
# 3: 5 x 31: 155
# 4: 30 x 5: 150
# 5: 4 x 31: 124
# 6: 3 x 31: 93
# 7: 2 x 31: 62
# 8: 30 x 2: 60
# 9: 5 x 10: 50
# 10: 5 x 9: 45
# 11: 4 x 10: 40
# 12: 4 x 9: 36
# 13: 1 x 31: 31
# 14: 30 x 1: 30
# 15: 3 x 10: 30
# 16: 3 x 9: 27
# 17: 5 x 5: 25
# 18: 2 x 10: 20
# 19: 4 x 5: 20
# 20: 2 x 9: 18
# 21: 3 x 5: 15
# 22: 2 x 5: 10
# 23: 1 x 10: 10
# 24: 5 x 2: 10
# 25: 1 x 9: 9
# 26: 4 x 2: 8
# 27: 3 x 2: 6
# 28: 1 x 5: 5
# 29: 5 x 1: 5
# 30: 4 x 1: 4
# 31: 2 x 2: 4
# 32: 3 x 1: 3
# 33: 2 x 1: 2
# 34: 1 x 2: 2
# 35: 1 x 1: 1
