from rest_framework.throttling import UserRateThrottle

class MatriculaAnonRateThrottle(UserRateThrottle):
    rate = '5/day'