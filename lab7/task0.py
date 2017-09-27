"""

Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""


class Time(object):
    """Represents the time of day.

    attributes: hour, minute, second
    """

    hour = 0
    minute = 0
    second = 0


    def print_time(self):
        print '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    @staticmethod
    def int_to_time(seconds):
        """Makes a new Time object.

        seconds: int seconds since midnight.
        """
        time = Time()
        minutes, second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time


    def time_to_int(self):
        """Computes the number of seconds since midnight.

        time: Time object.
        """
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds


    def add_times(self, time):
        """Adds two time objects."""
        assert self.valid_time() and time.valid_time()
        seconds = self.time_to_int() + time.time_to_int()
        return time.int_to_time(seconds)


    def valid_time(self):
        """Checks whether a Time object satisfies the invariants."""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        return True


def main():
    # if a movie starts at noon...
    noon_time = Time()
    noon_time.hour = 12
    noon_time.minute = 0
    noon_time.second = 0

    print 'Starts at',
    noon_time.print_time()

    # and the run time of the movie is 109 minutes...
    movie_minutes = 109
    run_time = Time.int_to_time(movie_minutes * 60)
    print 'Run time',
    run_time.print_time()

    # what time does the movie end?
    end_time = noon_time.add_times(run_time)
    print 'Ends at',
    end_time.print_time()


if __name__ == '__main__':
    main()
