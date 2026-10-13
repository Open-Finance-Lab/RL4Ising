import csv
import re
import os
import argparse
from collections import defaultdict


ACRONYMS = {
    "EA": "Edwards-Anderson",
    "SK": "Sherrington-Kirkpatrick",
    # "FM": "Ferromagnetic",
    # "AFM": "Antiferromagnetic",
    # "RRG": "Random Regular Graph",
    # "VNA": "Vertex-Normalized Adjacency",
    # "BA": "Barabási-Albert",
    # "ER": "Erdős-Rényi"
}


def natural_sort_key(text):
    """
    Splits a string into string and integer components so that lists sort naturally.
    Example: 10x10 comes before 20x20. 2 comes before 10.
    """
    return [int(c) if c.isdigit() else c.lower() for c in re.split(r"(\d+)", str(text))]


def format_header_name(text):
    """
    Cleans up folder names by replacing underscores with spaces and
    expanding known acronyms.
    """
    text = text.replace("_", " ")
    words = text.split()
    expanded_words = [ACRONYMS.get(w, w) for w in words]
    return " ".join(expanded_words)


def format_csv(input_csv, output_csv):
    if not os.path.exists(input_csv):
        print(f"[!] Input file '{input_csv}' not found.")
        return

    # Data Structure: grouped_data[hierarchy_tuple][size_label] = [(seed, energy)]
    grouped_data = defaultdict(lambda: defaultdict(list))

    with open(input_csv, mode="r", newline="") as infile:
        reader = csv.reader(infile)
        header = next(reader, None)

        for row in reader:
            if len(row) < 2:
                continue

            raw_path = row[0].replace("\\", "/")
            obj_val = row[1]

            clean_path = re.sub(r"^.*?/data/[^/]+/", "", raw_path)

            parts = clean_path.split("/")
            if len(parts) < 2:
                continue

            filename = parts[-1]
            original_size_folder = parts[-2]
            hierarchy_folders = parts[:-2]

            size_match = re.search(r"(\d+x\d+)", filename)
            if size_match:
                size_label = size_match.group(1)
            else:
                size_label = original_size_folder

            # Always grab the last number in the filename
            numbers = re.findall(r"\d+", filename)
            seed = int(numbers[-1]) if numbers else 0

            hierarchy_tuple = tuple(hierarchy_folders)
            grouped_data[hierarchy_tuple][size_label].append((seed, obj_val))

    with open(output_csv, mode="w", newline="") as outfile:
        writer = csv.writer(outfile)

        sorted_hierarchies = sorted(
            grouped_data.keys(), key=lambda x: [natural_sort_key(part) for part in x]
        )

        for hierarchy in sorted_hierarchies:
            sizes_dict = grouped_data[hierarchy]

            for folder_name in hierarchy:
                writer.writerow([format_header_name(folder_name)])

            sorted_sizes = sorted(sizes_dict.keys(), key=natural_sort_key)

            size_row = []
            for size in sorted_sizes:
                size_row.extend([size, "", ""])
            writer.writerow(size_row)

            header_row = []
            for _ in sorted_sizes:
                header_row.extend(["Seed", "Min Energy", ""])
            writer.writerow(header_row)

            for size in sorted_sizes:
                sizes_dict[size].sort(key=lambda x: x[0])

            max_rows = max(len(sizes_dict[size]) for size in sorted_sizes)

            for i in range(max_rows):
                data_row = []
                for size in sorted_sizes:
                    lst = sizes_dict[size]
                    if i < len(lst):
                        seed_val, energy_val = lst[i]
                        data_row.extend([seed_val, energy_val, ""])
                    else:
                        data_row.extend(["", "", ""])

                writer.writerow(data_row)

            writer.writerow([])

    print(f"Spreadsheet formatting complete. Saved to '{output_csv}'.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Format Gurobi batch CSV into a readable spreadsheet grid."
    )

    parser.add_argument(
        "input_csv",
        type=str,
        default="gurobi_batch_results.csv",
        nargs="?",
        help="The raw CSV output from the Gurobi batch solver.",
    )

    parser.add_argument(
        "-o",
        "--output_csv",
        type=str,
        default="formatted_results.csv",
        help="The name of the new formatted output file.",
    )

    args = parser.parse_args()
    format_csv(args.input_csv, args.output_csv)
