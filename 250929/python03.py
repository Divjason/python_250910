from datetime import datetime

class BankAccount :
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        self.history = []
    
    def _log(self, typ, amount, memo="") :
        self.history.append(
            (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), typ, amount, self.balance, memo)
        )

    def deposit(self, amount, memo="") :
        if amount <= 0 :
            print("입금 금액은 양수여야 합니다!")
        self.balance += amount
        self._log("DEPOSIT", amount, memo)

    def withdraw(self, amount, memo="") :
        if amount <= 0 :
            print("출금 금액은 양수여야 합니다!")
        if amount > self.balance :
            print("잔액부족")
        self.balance -= amount
        self._log("WITHDRAW", amount, memo)

    def show_history(self, limit=None) :
        rows = self.history[-limit:] if limit else self.history
        print("[거래내역]")
        print("[시간 \ 유형 \ 금액 \ 잔액 \ 메모]")
        for t, typ, amt, bal, memo in rows :
            print(f"{t} \ {typ} \ {amt} \ {bal} \ {memo}")
    
    def __repr__(self) :
        return f"BankAccount(owner={self.owner}, balance={self.balance})"

def main() :
    print("=== 미니 가계부 ===")
    owner = input("예금주명을 입력하세요 : ").strip() or "User"
    account = BankAccount(owner, 0)
    menu = "[메뉴] \ 1) 입금 \ 2) 출금 \ 3) 잔액조회 \ 4) 거래내역 \ 5) 종료 \ 선택 : "

    while True :
        choice = input(menu).strip()

        try :
            if choice == "1" :
                amount = int(input("입금액 : "))
                memo = input("메모(선택) : ")
                account.deposit(amount, memo)
                print(f"입금 완료. 현재 잔액 : {account.balance}")
            elif choice == "2" :
                amount = int(input("출금액 : "))
                memo = input("메모(선택) : ")
                account.withdraw(amount, memo)
                print(f"출금 완료. 현재 잔액 : {account.balance}")
            elif choice == "3" :
                print(f"예금주 : {account.owner}, 현재잔액 : {account.balance}")
            elif choice == "4" :
                account.show_history()
            elif choice == "5" :
                print("종료합니다.")
                break
            else :
                print("메뉴 번호를 다시 선택해주세요.")
        except :
            print("[오류]")

if __name__ == "__main__" :
    main()