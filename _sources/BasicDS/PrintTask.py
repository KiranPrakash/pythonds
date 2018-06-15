import random
from QueueDS import Queue


class Printer:
    """ This class will track the current task. If there is a task, it is busy and then computes time needed to complete th
    task based on number of pages, the constructor allows pages per minute setting to be initialized. The tick method decrements
     the internal timer and sets printer ot idle if the task was completed"""
    def __init__(self, ppm):
        self.paper_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task is not None:
            return True
        else:
            return False

    def start_next(self, next_task):
        self.current_task = next_task
        self.time_remaining = next_task.get_pages()*60 / self.paper_rate


class Task:
    """ This class creates a single printing task. A random number generator will specify how many pages in a single task
    varying from 1-20 pages. Each task will also need to keep a timestamp to be used for computing wating time. THe timestamp
    that was created would represent the time the task was created and placed in the queue.Waittime method can be then used
     to retreive the amount of time spent in the queue before printing begins"""

    def __init__(self, time):
        self.time_stamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.time_stamp

    def get_pages(self):
        return self.pages

    def get_wait_time(self, current_time):
        return current_time - self.time_stamp


def simulate(num_seconds, pages_per_minute):
    """ This method implements the algorithm of creating an instance of the printer queue and """
    lab_printer = Printer(pages_per_minute)
    printer_queue = Queue()
    waiting_time = []

    for current_second in range(num_seconds):

        if generate_task():
            task = Task(current_second)
            printer_queue.enqueue(task)

        if not lab_printer.busy() and not printer_queue.isEmpty():
            next_task = printer_queue.dequeue()
            waiting_time.append(next_task.get_wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    average_wait = sum(waiting_time)//len(waiting_time)
    print("Average wait {0:6.2f} sec {1:3d} tasks remaining".format(average_wait, printer_queue.size()))


def generate_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def main():
    for i in range(10):
        simulate(3600,10)


if __name__ == '__main__':
    main()
