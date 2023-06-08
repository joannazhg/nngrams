sampleConstraints1 = {}
sampleConstraints1['rows'] = [[3], [4], [1, 3], [1], [1]]
sampleConstraints1['cols'] = [[3], [1], [3], [3], [3]]
sampleSoln1 = [[False, False, True, True, True],
               [False, True, True, True, True],
               [True, False, True, True, True],
               [True, False, False, False, False],
               [True, False, False, False, False]]

sampleConstraints2 = {}
sampleConstraints2['cols'] = [[1], [2], [3], [
    1], [1, 5], [1, 5], [1, 2], [6], [4], [1]]
sampleConstraints2['rows'] = [[6], [3, 3], [
    2, 2], [2], [3], [4], [2], [2], [2], [2]]
sampleSoln2 = [[False, False, True, True, True, True, True, True, False, False],
               [True, True, True, False, False, False, False, True, True, True],
               [False, True, True, False, False, False, False, True, True, False],
               [False, False, False, False, False,
                   False, False, True, True, False],
               [False, False, False, False, False, False, True, True, True, False],
               [False, False, False, False, True, True, True, True, False, False],
               [False, False, False, False, True, True, False, False, False, False],
               [False, False, False, False, True, True, False, False, False, False],
               [False, False, False, False, True, True, False, False, False, False],
               [False, False, False, False, True, True, False, False, False, False]]

sampleConstraints3 = {}
sampleConstraints3['cols'] = [[15], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [
    1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [15]]
sampleConstraints3['rows'] = [[15], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [
    1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [15]]
sampleSoln3 = [[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
               [True, False, False, False, False, False, False, False,
                   False, False, False, False, False, False, True],
               [True, False, False, False, False, False, False, False,
                   False, False, False, False, False, False, True],
               [True, False, False, False, False, False, False, False,
                   False, False, False, False, False, False, True],
               [True, False, False, False, False, False, False, False,
                   False, False, False, False, False, False, True],
               [True, False, False, False, False, False, False, False,
                   False, False, False, False, False, False, True],
               [True, False, False, False, False, False, False, False,
                   False, False, False, False, False, False, True],
               [True, False, False, False, False, False, False, False,
                   False, False, False, False, False, False, True],
               [True, False, False, False, False, False, False, False,
                   False, False, False, False, False, False, True],
               [True, False, False, False, False, False, False, False,
                   False, False, False, False, False, False, True],
               [True, False, False, False, False, False, False, False,
                   False, False, False, False, False, False, True],
               [True, False, False, False, False, False, False, False,
                   False, False, False, False, False, False, True],
               [True, False, False, False, False, False, False, False,
                   False, False, False, False, False, False, True],
               [True, False, False, False, False, False, False, False,
                   False, False, False, False, False, False, True],
               [True, True, True, True, True, True, True, True,
                   True, True, True, True, True, True, True]
               ]

sampleConstraints4 = {}
sampleConstraints4['cols'] = [[8, 5], [6, 5], [1, 1, 3, 7], [1, 2, 1, 3], [1, 1, 1],
                              [3, 3, 2], [3, 1, 1], [3, 1, 7], [
                                  3, 2, 4, 1], [6, 6],
                              [8, 6], [4, 5, 4], [4, 5, 4], [4, 1, 7], [8],
                              [2, 1, 1, 6], [3, 1, 1], [4, 1, 1, 1, 2], [1, 1, 3, 2, 2], [9, 6]]
sampleConstraints4['rows'] = [[1, 2, 3], [1, 5, 2, 3], [1, 4, 4, 2], [3, 2, 4, 1, 1], [2, 1, 4, 1],
                              [4, 1, 2, 1, 3], [2, 2, 4, 1], [
                                  4, 5, 3], [4, 4, 1], [1, 6, 1, 1],
                              [1, 3, 4, 2], [3, 2, 2], [
                                  3, 1, 1, 3, 3], [4, 9], [3, 10, 1],
                              [3, 9, 2], [2, 1, 5, 3, 2], [4, 1, 2, 2, 1], [2, 1, 5], [3]]

checkerboard10 = {}
checkerboard10['rows'] = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
checkerboard10['cols'] = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]


checkerboard20 = {}
checkerboard20['rows'] = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

checkerboard20['cols'] = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
