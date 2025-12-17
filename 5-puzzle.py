with open('5-input.txt','r') as file:
    lines = [line.strip() for line in file]
    fresh_ranges = [[int(range.split('-')[0]),int(range.split('-')[1])] for range in lines[:lines.index('')]]
    ingredients = [int(ingredient) for ingredient in lines[lines.index('')+1:]]
    
def merge_ranges(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged_intervals = [intervals[0]]
    for current in intervals[1:]:
        last_merged = merged_intervals[-1]
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged_intervals.append(current)
    return merged_intervals

# Part 1
fresh_ranges = merge_ranges(fresh_ranges)
fresh_counter = 0
for i in ingredients:
    for range in fresh_ranges:
        if (i > range[0]) and (i < range[1]):
            fresh_counter += 1
            continue
print(fresh_counter)

# Part 2
total_fresh_ingredient_ids = 0
for range in fresh_ranges:
    total_fresh_ingredient_ids += range[1] - range[0] + 1
print(total_fresh_ingredient_ids)