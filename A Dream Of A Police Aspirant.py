import random
import time


def main():

    cards = []
    pcards = []
    dcards = []

    # 1. 카드뭉치, 플레이어 카드, 딜러 카드 변수 선언

    for _ in range(4):
        for i in range(1, 14):
            cards.append(i)

    cards.append("JOKER")
    random.shuffle(cards)

    # 2. 카드뭉치에 53장(1~13*4+조커)를 넣고 섞음
    # random.shuffle이 하는 일 : 리스트를 섞어준다.

    for i in range(7):
        pcards.append(cards[0])
        dcards.append(cards[1])
        del cards[0]
        del cards[0]

    # 3. 카드뭉치에서 가장 위에 있는 카드를 플레이어/딜러의 카드 덱에 놓는다. (총 7번 반복)

    print(f"초기 카드 : {pcards}")
    pcards = delsame(pcards, "p")
    dcards = delsame(dcards, "d")

    # 4. 초기 카드가 뭔지 알려준 다음, 중복 카드를 제거한다.

    while True:
        if len(cards) != 0:
            pcards.append(cards[0])
            del cards[0]

        # 5. 카드뭉치에 카드가 남아있는지 확인후에, 남아 있으면 플레이어의 덱에 카드를 하나 추가.

        print(f"당신의 카드 : {pcards}")
        if len(dcards) != 0:
            ask = int(
                input(f"딜러에게는 {len(dcards)}개의 카드가 있습니다.\n몇번째 카드를 뽑으시겠습니까?\n응답 : "))

            # 6. 상대의 카드 갯수를 알려준 뒤, 몇번째 카드를 가져올지 질문

            print(f"상대의 {ask}번째 카드는 {dcards[ask-1]}이였습니다.")
            pcards.append(dcards[ask-1])
            del dcards[ask-1]

            # 7. 뽑은 카드의 값을 보여주고, 그 카드를 플레이어의 덱에 넣음

        else:
            print("상대의 카드가 없습니다. (패배)")
            return

            # !. 상대의 카드가 없으면, 패배

        print(f"당신의 카드 : {pcards}")

        print("당신의 턴이 끝나 중복된 카드를 지웁니다.")
        pcards = delsame(pcards, 'p')

        # 8. 플레이어에게 자신의 카드를 보여주고, 중복 카드 제거

        if len(pcards) == 1:
            if pcards[0] == 'JOKER':
                print("플레이어 조커 하나만 가지고 있습니다.\n딜러 승리")
                return

            # !. 플레이어가 조커 한장만 가지고 있다면, 패배

        print("===================================")
        print('상대의 턴입니다.')
        if (len(cards) != 0):
            dcards.append(cards[0])
            del cards[0]

            # 9. 카드뭉치에 카드가 남아있는지 확인 후, 남아있다면 딜러의 덱에 카드 가져오기

        if len(pcards) != 0:
            ask = random.randint(0, len(pcards)-1)
            dcards.append(pcards[ask])
            del pcards[ask]

            # 10. 플레이어의 덱에 카드가 남아있다면, 0부터 상대방 카드의 갯수 -1 사이의 난수를 뽑은뒤,
            # 플레이어의 덱의 난수+1 (난수번째 인덱스)의 값을 딜러의 덱에 넣음.

        else:
            print("당신의 카드가 없습니다. (승리)")
            return

            # !. 플레이어의 카드의 갯수가 0이라면, 승리

        dcards = delsame(dcards, 'd')

        # 11. 딜러의 덱에서 중복 카드를 제거함

        if len(dcards) == 1:
            if dcards[0] == 'JOKER':
                print("상대가 조커 하나만 가지고 있습니다.\n플레이어 승리")
                print("상대의 카드 : ", dcards, "플레이어의 카드 : ", pcards)
                return

                # !. 딜러가 조커 한장만 가지고 있다면, 승리

        print('==========================')

        print("당신의 턴입니다.")

        # 12. 턴을 플레이어에게 넘긴다. (while문 사용)


def delsame(cards, p):
    # cards (카드 덱)과 p (플레이어인지, 딜러인지)를
    # 인자 값 (파라미터)로 가져오는 delsame이라는 함수를 선언한다.

    for i in cards:
        num = cards.count(i)
        pcheck = {}
        dcheck = {}
        if num == 1:
            continue

    # 카드 덱에 있는 값들을 i에 넣는다.
    # num 변수에 cards.count(i)의 값 (cards에 i가 몇개가 있는지)를 넣는다.
    # 중복을 체크하기 위해 pcheck와 dcheck 딕셔너리를 만든다.
    # num 변수의 값이 1이면, 다음 반복으로 넘어간다.

        for n in range(num):
            if p == "p":
                try:
                    if pcheck[i] == 1:
                        ''
                except:
                    print(f"플레이어의 {i}를 지웠습니다.")
                    pcheck[i] = 1

            elif p == "d":
                try:
                    if dcheck[i] == 1:
                        ''
                except:
                    print(f"상대의 {i}를 지웠습니다.")
                    dcheck[i] = 1

        # num번 반복한다. (n에 그 반복 번수를 저장)
        # 만약, 플레이어의 카드 덱이라면, pcheck 딕셔너리의 자기 자신의 값과 같은 키를 만들고 그 값을 1로 한다.
        # 만약, pcheck에 자기 자신의 값과 같은 키가 없다면, 에러가 날것이므로,
        # 이를 이용하여 print문이 한번만 실행되게 한다.

        # 딜러의 경우도 이와 같다.

            cards.remove(i)

        # 만약 i가 중복이라면, i를 지워준다.

    return cards
    # 중복이 모두 없어진 카드 덱을 반환 (return)한다.


if __name__ == "__main__":
    while True:
        main()
        if input("게임이 끝났습니다. \n다시 실행하시겟습니까? (y/n)\n") != "y":
            break

# 만약, 이 파이썬 파일이 다른 파일의 모듈로서 실행 되지 않고,
# 이 파일을 메인으로 하여 실행하고 있다면, main을 계속 반복하고,
# main 함수의 실행이 끝날때마다 다시 실행할지 물어 본 후,
# 다시 실행한다는 답변이 돌아오면, 다시 실행하고, 아니면, 멈춘다 (break).
