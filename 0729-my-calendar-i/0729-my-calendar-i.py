class MyCalendar(object):

    def __init__(self):
        self.bookings = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        # Use binary search to find the insertion position
        pos = bisect.bisect_right(self.bookings, (start, end))

        # Check if the new event overlaps with adjacent bookings
        if pos > 0 and start < self.bookings[pos - 1][1]:
            return False
        if pos < len(self.bookings) and end > self.bookings[pos][0]:
            return False

        # If no overlap, insert the new booking and return True
        self.bookings.insert(pos, (start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)