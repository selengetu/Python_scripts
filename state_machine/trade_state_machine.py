class OrderState:
    NEW = "new"
    SUBMITTED = "submitted"
    FILLED = "filled"
    CANCELLED = "cancelled"


transition_table = {
    OrderState.NEW: [
        ("submit", lambda: True, OrderState.SUBMITTED)
    ],
    OrderState.SUBMITTED: [
        ("fill", lambda: True, OrderState.FILLED),
        ("cancel", lambda: True, OrderState.CANCELLED)
    ],
    OrderState.FILLED: [],
    OrderState.CANCELLED: []
}


class Order:
    def __init__(self):
        self.state = OrderState.NEW

    def next(self, action):
        for act, check, next_state in transition_table[self.state]:
            if act == action and check():
                self.state = next_state
                return True
        return False

if __name__ == "__main__":
    order = Order()

    print(order.state)  # new
    print(order.next("submit"))  # True
    print(order.state)  # submitted
    print(order.next("fill"))  # True
    print(order.state)  # filled
    print(order.next("cancel"))  # False (invalid)