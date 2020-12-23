games = int(input())
swifts = input()
swifts = swifts.split(" ")
sema = input()
sema = sema.split(" ")

def makeNum(seq):
    hold = []
    for i in seq:
        hold.append(int(i))
    return hold

swifts = makeNum(swifts)
sema = makeNum(sema)

def mostGames(seq1, seq2, nums):
    for i in range(len(seq1)):
        score1 = sum(seq1[:nums - i])
        score2 = sum(seq2[:nums - i])
        if score1 == score2 :
            return nums - i
    return 0

print(mostGames(swifts,sema,games))