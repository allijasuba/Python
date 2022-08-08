eff = 100
percent = .04
times = 0
print("month: 0        effectiveness:100.0")
while eff > 51:
    one = eff * percent
    eff = eff - one
    times = times +1
    print(f"month: {times}\teffectiveness:{eff}")
print("DISCARDED")