import collections

def main():
    filename = "system_logs.txt"
    levels = ["INFO", "WARN", "ERROR", "DEBUG"]

    with open(filename, 'r') as f:
        lines = f.readlines()

    print(f"--- Processing {len(lines)} lines from {filename} (Simulation of Scala Logic) ---\n")

    # 1. MAP PHASE
    # Transform: line -> (Level, 1)
    mapped_data = []
    for line in lines:
        for level in levels:
            if level in line.upper():
                mapped_data.append((level, 1))
                break

    # 2. SHUFFLE AND GROUP PHASE (Implicit in dictionary grouping)
    # Grouping by key
    grouped_data = collections.defaultdict(list)
    for level, value in mapped_data:
        grouped_data[level].append(value)

    # 3. REDUCE PHASE
    # Aggregate values
    reduced_data = {level: sum(counts) for level, counts in grouped_data.items()}

    # Output Results
    print("MapReduce Results:")
    for level, count in reduced_data.items():
        print(f"{level:<6}: {count}")

if __name__ == "__main__":
    main()
