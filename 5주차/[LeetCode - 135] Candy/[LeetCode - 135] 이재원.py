class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = []
        leng = len(ratings)
        endIndex = 0

        i = 1

        # index 0 candy
        if leng > 1:
            if ratings[0] <= ratings[1]:
                candy.append(1)
            else:
                count = 2
                endIndex = 1

                for j in range(0, leng - 1):
                    if ratings[j] <= ratings[j+1]:
                        endIndex = j
                        break
                    if j == leng - 2:
                        endIndex = j + 1
                        break

                count = endIndex + 1

                candy.append(count)
                i = endIndex + 1

                for num in range(count-1, 0, -1):
                    candy.append(num)

            # from 1 to (leng - 2) index
            while i < leng - 1:
                if ratings[i] < ratings[i+1]:
                    if ratings[i-1] == ratings[i]:
                        candy.append(1)
                    else:
                        candy.append(candy[-1] + 1)

                elif ratings[i] > ratings[i+1]:
                    count = 2
                    endIndex = i + 1

                    if i != leng - 2:
                        for j in range(i, leng - 1):
                            if ratings[j] <= ratings[j+1]:
                                endIndex = j
                                break
                            if j == leng - 2:
                                endIndex = j + 1
                                break
                        count = endIndex - i + 1

                    if ratings[i] == ratings[i-1]:
                        candy.append(count)
                    else:
                        candy.append(max(candy[-1] + 1, count))

                    for num in range(count-1, 0, -1):
                        candy.append(num)

                    i = endIndex

                else:   # ratings[i] == ratings[i+1]
                    if ratings[i-1] < ratings[i]:
                        candy.append(candy[-1] + 1)
                    else:  # ratings[i-1] == ratings[i]:
                        candy.append(1)
                    # else:   # ratings[i-1] > ratings[i]
                        # 지급되었어야 정상
                    if i+2 != leng:
                        if ratings[i+1] < ratings[i+2]:
                            candy.append(1)
                            i += 1

                i += 1

            # last number of children
            if len(candy) != leng:
                if ratings[-2] < ratings[-1]:
                    candy.append(candy[-1] + 1)
                else:  # ratings[-2] == ratings[-1]
                    candy.append(1)

        else:
            candy.append(1)

        return sum(candy)
