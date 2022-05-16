import time as time


class TrafficLight:

    pattern = ["Green", "Yellow", "Red"]

    def __init__(self, street_name, pos, color_start, tic_time, green_time, yellow_time, red_time):
        if color_start not in TrafficLight.pattern:
            raise ValueError(f"Color must be one of these: {color_start}")
        self.street_name = street_name
        self.pos = pos
        self.color = color_start
        self.color_index = TrafficLight.pattern.index(color_start)
        self.tic = tic_time
        self.time_pattern = [green_time, yellow_time, red_time]
        self.tic_num = 0

    def cycle(self):
        time.sleep(self.tic)
        if self.tic_num == self.time_pattern[self.color_index]:
            self.color_index += 1
            if self.color_index == len(TrafficLight.pattern):
                self.color_index = 0
            self.color = TrafficLight.pattern[self.color_index]
            print(f"Traffic light at {self.street_name} is {self.color}")
            self.tic_num = 0

        self.tic_num += 1

