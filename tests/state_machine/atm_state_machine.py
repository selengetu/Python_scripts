#!/bin/python3

from typing import Optional, Tuple

Action = str


class State:
    authorized = "authorized"
    unauthorized = "unauthorized"


# ----------------------
# Checker Functions
# ----------------------

def login_check(param, passwd, balance):
    if param == passwd:
        return True, balance, None
    return False, balance, None


def logout_check(param, passwd, balance):
    return True, balance, None


def deposit_check(param, passwd, balance):
    if param is None or param < 0:
        return False, balance, None
    return True, balance + param, None


def withdraw_check(param, passwd, balance):
    if param is None or param < 0:
        return False, balance, None
    if balance >= param:
        return True, balance - param, None
    return False, balance, None


def check_balance(param, passwd, balance):
    return True, balance, balance


# ----------------------
# Transition Table
# ----------------------

transition_table = {
    State.unauthorized: [
        ("login", login_check, State.authorized)
    ],
    State.authorized: [
        ("logout", logout_check, State.unauthorized),
        ("deposit", deposit_check, State.authorized),
        ("withdraw", withdraw_check, State.authorized),
        ("balance", check_balance, State.authorized)
    ]
}

init_state = State.unauthorized


# ----------------------
# ATM Class (Provided in problem)
# ----------------------

class ATM:
    def __init__(self, init_state: State, init_balance: int, password: str, transition_table: dict):
        self.state = init_state
        self._balance = init_balance
        self._password = password
        self._transition_table = transition_table

    def next(self, action: Action, param: Optional[int]) -> Tuple[bool, Optional[int]]:
        try:
            for transition_action, check, next_state in self._transition_table[self.state]:
                if action == transition_action:
                    passed, new_balance, res = check(param, self._password, self._balance)
                    if passed:
                        self._balance = new_balance
                        self.state = next_state
                        return True, res
        except KeyError:
            pass

        return False, None
    
if __name__ == "__main__":
    atm = ATM(init_state, 1000, "1234", transition_table)

    print(atm.next("login", "1234"))     # expect True
    print(atm.next("deposit", 500))      # expect True
    print(atm.next("balance", None))     # expect True, 1500
    print(atm.next("withdraw", 200))     # expect True
    print(atm.next("balance", None))     # expect True, 1300
    print(atm.next("logout", None))      # expect True
    print(atm.next("deposit", 100))      # expect False (unauthorized)