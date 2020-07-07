class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.pos = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.pos+1] + [url]
        self.pos += 1

    def back(self, steps: int) -> str:
        self.pos = self.pos-steps if self.pos-steps >= 0 else 0
        return self.history[self.pos]

    def forward(self, steps: int) -> str:
        self.pos = self.pos+steps if self.pos+steps < len(self.history) else len(self.history)-1
        return self.history[self.pos]
