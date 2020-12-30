from scipy.stats import chisquare

x = list(range(1000))

nsegments = len(x)
min = x[0]
max = x[-1]
segment_size = (max - min) / nsegments
uniform_nelements_per_segment = len(x) / nsegments

elements_per_segment = [0] * nsegments

for element in x[:-1]:
    current_segment = int((element - min) // segment_size)
    elements_per_segment[current_segment] += 1

elements_per_segment[-1] += 1

other_unfiformity_index = chisquare(elements_per_segment)
other_other_unif = chisquare(elements_per_segment, [uniform_nelements_per_segment] * len(elements_per_segment))
print(other_unfiformity_index, other_other_unif)

uniformity_index = sum([((nelements - uniform_nelements_per_segment) ** 2) / uniform_nelements_per_segment for nelements in elements_per_segment])

print(f"segment size: {segment_size}, uniformity index: {uniformity_index}, index 2: {other_unfiformity_index}")
