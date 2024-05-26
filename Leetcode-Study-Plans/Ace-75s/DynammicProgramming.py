# STUDENT ABSENTS RECORD - II :
def checkRecord(n: int) -> int:
    MOD = (10 ** 9) + 7
    bool_cache = [[[False] * 3 for _ in range(2)] for _ in range(n)]
    value_cache = [[[None] * 3 for _ in range(2)] for _ in range(n)]
    # Utility function for recursive call :
    # Day => No.of days [N]
    # Absent => No.of consecutive absents [0, 1]
    # Late => No.of consecutive lates [0, 1, 2]
    def count(day, absent, late):
        if day == n:
            return 1
        if bool_cache[day][absent][late]:
            return value_cache[day][absent][late]
        total = 0
        # Present ->
        total += count(day + 1, absent, 0)
        # Add absent if consecutive absent < [0,1] ->
        if absent < 1:
            total += count(day + 1, absent + 1, 0)
        # Add late if consecutive late < [0,1,2] ->
        if late < 2:
            total += count(day + 1, absent, late + 1)
        # Adding bool_cache & value_cache ->
        bool_cache[day][absent][late] = True
        value_cache[day][absent][late] = total % MOD
        return value_cache[day][absent][late]
    return count(0, 0, 0)

