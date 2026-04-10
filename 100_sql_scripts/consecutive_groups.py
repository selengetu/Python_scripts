def longest_consecutive(nums):
    nums.sort()
    best = current = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            current += 1
            best = max(best, current)
        else:
            current = 1
    return best

def max_consecutive(workshops):
    workshops.sort()
    best = current = workshops[0][1]
    prev = workshops[0][0]
    for year, count in workshops[1:]:
        if year == prev + 1:
            current += count
        else:
            current = count
        best = max(best, current)
        prev = year
    return best


def max_two_consecutive(workshops):
    workshops.sort()
    best = 0
    for i in range(len(workshops)-1):
        y1, c1 = workshops[i]
        y2, c2 = workshops[i+1]
        if y2 == y1 + 1:
            best = max(best, c1+c2)
    return best

def count_streaks(daily):
    streaks = 0
    in_streak = False
    for d in daily:
        if d > 0 and not in_streak:
            streaks += 1
            in_streak = True
        elif d == 0:
            in_streak = False
    return streaks

def best_3month_start(monthly):
    best_sum = 0
    best_idx = 0
    for i in range(len(monthly) - 2):
        window = sum(monthly[i:i+3])
        if window > best_sum:
            best_sum = window
            best_idx = i
    return best_idx

def longest_growth_streak(yearly):
    max_streak = 0
    curr_streak = 0

    for i in range(1, len(yearly)):
        if yearly[i][1] > yearly[i-1][1]:
            curr_streak += 1
            max_streak = max(max_streak, curr_streak)
        else:
            curr_streak = 0

    return max_streak


def missing_years(workshops):
    workshops.sort()
    missing = []
    years = [y for y, _ in workshops]
    for i in range(years[0], years[-1]+1):
        if i not in set(years):
            missing.append(i)
    return missing

def longest_no_refund(transactions):
    best = current = 0
    for t in transactions:
        if t > 0:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best