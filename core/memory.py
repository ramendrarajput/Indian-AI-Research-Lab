class Memory:

    def __init__(self):

        self.history = []

    def add(self, user, assistant):

        self.history.append(
            {
                "user": user,
                "assistant": assistant
            }
        )

    def get(self):

        return self.history

    def clear(self):

        self.history.clear()