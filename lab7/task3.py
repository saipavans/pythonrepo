"""

Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""


class Time(object):
    """Represents the time of day in seconds since midnight.

    attributes: second
    """

    def __init__(self, second=0):
        self.second = second

    def __str__(self):
        return '%.2d' % (self.second)

    def print_time(self):
        print str(self)

    def time_to_int(self):
        return self.second

    def is_after(self, other):
        return self.second > other.second

    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.

        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two time objects."""
        assert self.is_valid() and other.is_valid()
        seconds = self.time_to_int() + other.time_to_int()
        return Time(seconds)

    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        seconds += self.time_to_int()
        return Time(seconds)

    def is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        if isinstance(self.second, int):
            return self.second > 0
        return False


def main():
    start = Time(35100)
    start.print_time()

    end = start.increment(1337)
    end.print_time()

    print 'Is end after start?',
    print end.is_after(start)

    print 'Using __str__'
    print start, end

    start = Time(35100)
    duration = Time(5700)
    print start + duration
    print start + 1337
    print 1337 + start

    t1 = Time(27780)
    t2 = Time(27660)
    t3 = Time(27420)
    total = sum([t1, t2, t3])
    print total


if __name__ == '__main__':
    main()
