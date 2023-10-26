import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, max_requests: int, period: int):
        """
        :param max_requests: Maximum requests allowed in the given period.
        :param period: Time period in seconds.
        """
        self.max_requests = max_requests
        self.period = period
        self.timestamps = defaultdict(list)  # Store timestamps of requests for each route

    def is_allowed(self, key: str) -> bool:
        """
        Check if a request to the route (key) should be allowed or not.
        
        :param key: Route or endpoint to be checked.
        :return: True if request should be allowed, False otherwise.
        """
        now = time.time()
        
        # Remove timestamps older than the specified period
        self.timestamps[key] = [timestamp for timestamp in self.timestamps[key] if now - timestamp < self.period]

        # Check if we have exceeded the rate limit
        if len(self.timestamps[key]) < self.max_requests:
            self.timestamps[key].append(now)
            return True
        return False

# Creating a rate limiter instance with a limit of, say, 100 requests per minute (60 seconds) for the MVP.
rate_limiter = RateLimiter(max_requests=100, period=60)
