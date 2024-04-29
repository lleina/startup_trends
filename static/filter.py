# Borrowed code from Jeff

import csv


def passes_filter(row):
    # Filter criteria:
    # only want companies that are in NY and CA and are considered 'tech' aka is software/web/mobile
    # if true, it is appended

    if row["is_CA"] == "1" or row["is_NY"] == "1":
        if row["is_software"] == "1" or row["is_web"] == "1" or row["is_mobile"] == "1":
            return True
    else:
        return False


# import and run passes_filter
data = []
header = []
with open("./startup.csv", "r") as f:
    reader = csv.DictReader(f)

    header = reader.fieldnames

    # Reset file pointer to the beginning of the file
    f.seek(0)

    for row in reader:
        if passes_filter(row):
            data.append(row)

print(len(data))

# export to new CSV
with open("startup_filtered.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
