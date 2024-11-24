class VideoSystem(object):
    cycle = 0
    register = 1
    interesting_signal_strengths = []
    pixels = []

    def add_interesting_signal_strength(self):
        self.interesting_signal_strengths.append(
            round(self.cycle // 10) * 10 * self.register
        )

    def draw_pixel(self):
        if self.register - 1 <= self.cycle % 40 <= self.register + 1:
            self.pixels.append("#")
        else:
            self.pixels.append(".")
        self.cycle += 1

    def addx(self, value: int):
        self.draw_pixel()
        self.draw_pixel()

        if self.cycle % 40 in [20, 21]:
            self.add_interesting_signal_strength()

        self.register += value

    def noop(self):
        self.draw_pixel()

        if self.cycle % 40 == 20:
            self.add_interesting_signal_strength()

    def perform_command(self, command_name: str, value: int | None):
        match command_name:
            case "addx":
                self.addx(value)
            case "noop":
                self.noop()

    def print_display(self):
        for i in range(0, len(self.pixels), 40):
            line = "".join(self.pixels[i : i + 40])
            print(line)
