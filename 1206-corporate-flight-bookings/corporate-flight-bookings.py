class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        output = [0] * (n+1)
        for i in bookings:
            output[i[0]-1] += i[2]
            output[i[1]] -= i[2]
        for i in range(1, len(output)):
            output[i] += output[i-1]
        return output[:n]