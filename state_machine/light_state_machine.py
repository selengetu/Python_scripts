class LightState:
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"


transition_table = {
    LightState.RED: [
        ("timer", lambda: True, LightState.GREEN)
    ],
    LightState.GREEN: [
        ("timer", lambda: True, LightState.YELLOW)
    ],
    LightState.YELLOW: [
        ("timer", lambda: True, LightState.RED)
    ]
}


class TrafficLight:
    def __init__(self):
        self.state = LightState.RED

    def next(self, action):
        for act, check, next_state in transition_table[self.state]:
            if act == action and check():
                self.state = next_state
                return self.state
            
if __name__ == "__main__":
    light = TrafficLight()

    print(light.state)  # red
    print(light.next("timer"))  # green
    print(light.next("timer"))  # yellow
    print(light.next("timer"))  # red