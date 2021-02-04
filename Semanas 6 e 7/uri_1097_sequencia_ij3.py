def main():
    ih = 1
    j = 7

    while ih <= 9:
        for i in range(3):
            print(f'I = {ih}  J = {j}')
            j = j - 1
        ih = ih + 2
        j = ih + 6



main()