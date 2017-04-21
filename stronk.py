lowers = "abcdefghijklmnopqrstuvwxyz"
uppers = lowers.upper()
nums = "0123456789"
misc = ".?!&#,;:-_*"

def pw_threshold(pw):
    return 1 in [1 for x in pw if x in lowers] and 1 in [1 for x in pw if x in uppers] and 1 in [1 for x in pw if x in nums] and 1 in [1 for x in pw if x in misc]

print pw_threshold("Aa0!")

def how_stronk(pw):
    return min([1 for x in pw if x in lowers].count(1) + [1 for x in pw if x in uppers].count(1) + [1 for x in pw if x in nums].count(1) + [1 for x in pw if x in misc].count(1), 10)

print how_stronk("Aa0!Aa0!Aa0!")
