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