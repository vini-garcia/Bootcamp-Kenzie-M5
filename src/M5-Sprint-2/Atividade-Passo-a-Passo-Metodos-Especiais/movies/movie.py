class Movie:
    def __init__(self, title: str, running_time: int):
        self.title = title
        self.running_time = running_time
        self.number_of_views = 0

    def __repr__(self) -> str:
        return f"<Filme: {self.title}>"

    def __len__(self):
        return self.running_time

    def __call__(self):
        self.number_of_views += 1
        return self.number_of_views
