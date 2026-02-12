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


def test_order_state_machine():
    order = Order()

    assert order.state == OrderState.NEW

    assert order.next("submit") is True
    assert order.state == OrderState.SUBMITTED

    assert order.next("fill") is True
    assert order.state == OrderState.FILLED

    assert order.next("cancel") is False