def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    for i in range(n//2, -1, -1):
        swaps = sift_down(i, data, swaps)

    return swaps

def sift_down(i, data, swaps):
    n = len(data)
    index_min = i
    lchild = 2*i + 1
    if lchild < n and data[lchild] < data[index_min]:
        index_min = lchild
    rchild = 2*i + 2
    if rchild < n and data[rchild] < data[index_min]:
        index_min = rchild
    if i != index_min:
        swaps.append((i, index_min))
        data[i], data[index_min] = data[index_min], data[i]
        swaps = sift_down(index_min, data, swaps)
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    decis = input()

    # input from keyboard
    if "I" in decis:
        n = int(input())
        unsplit_data = input()
        data = list(map(int, unsplit_data.split(" ")))
        # checks if lenght of data is the same as the said lenght
        assert len(data) == n

    elif "F" in decis:
        file= input()
        if "a" in file:
            return
        with open(f"./tests/{file}", mode="r") as file:
            n=int(file.readline())
            data = list(map(int, file.readline().split(" ")))
        assert len(data) == n

    else:
        return
    

    liste = [[] for i in range(n)]
    for i in range(n):
        #liste[data[i]].append(i)
        if data[i] < n:
            liste[data[i]].append(i)
    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
