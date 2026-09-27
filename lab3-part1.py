# LAB 3 - PART 1: FILES

print("PART 1")

# 1
with open("user_ids.txt", "r") as f:
    for line in f:
        print(line)

# 2
user_ids = []

with open("user_ids.txt", "r") as f:
    for line in f:
        user_id = line.strip()
        user_ids.append(user_id)

print(user_ids[:5])
print(user_ids[-1])

# 3
print(len(user_ids))

unique_ids = set(user_ids)
print("Unique IDs in the file {}".format(len(unique_ids)))

# 4
Started = True

with open("user_ids_header.txt", "r") as f:
    for line in f:
        if Started:
            Started = False
        else:
            print(line.strip())

# 5
with open("data_3_columns.txt", "r") as f:
    for line in f:
        line = line.strip().split("\t")
        print(line)

# 6
with open("data_3_columns.txt", "r") as f:
    for line in f:
        line = line.strip().split("\t")
        medium = line[0]
        source = line[1]
        amount_paid = line[2].replace(",", ".")
        print(source, medium, amount_paid)

# 7
with open("data_3_columns.txt", "r") as f:
    for line in f:
        line = line.strip().split("\t")
        medium = line[0]
        source = line[1]
        amount_paid = float(line[2].replace(",", "."))
        print(source, medium, amount_paid)

print(amount_paid)

# 8
total_sum = 0

with open("data_3_columns.txt", "r") as f:
    for line in f:
        line = line.strip().split("\t")
        amount_paid = float(line[2].replace(",", "."))
        total_sum += amount_paid
        print("Current expenses: {:.2f}".format(total_sum))

print(total_sum)

# 9
total_sum = 0

with open("data_3_columns.txt", "r") as f:
    for line in f:
        line = line.strip().split("\t")
        medium = line[0]
        source = line[1]
        amount_paid = float(line[2].replace(",", "."))

        if source == "google":
            total_sum += amount_paid
            print("Current expenses google: {:.2f}".format(total_sum))

# 10
total_sum = 0

with open("data_3_columns.txt", "r") as f:
    for line in f:
        line = line.strip().split("\t")
        medium = line[0]
        source = line[1]
        amount_paid = float(line[2].replace(",", "."))

        if source == "yandex" and medium == "seo":
            total_sum += amount_paid

print("Yandex SEO amount: {:.2f}".format(total_sum))


# LAB 3 - PART 2: FUNCTIONS

print("PART 2")

# 1
with open("data_no_header.txt", "r") as f:
    for line in f:
        line = line.strip().split("\t")
        source = line[5]
        medium = line[4]

        if source == "google" or source == "yandex":
            if medium == "seo" or medium == "sem":
                sourceType = "search engines seo"
            elif medium == "brand":
                sourceType = "search engines brand"
            else:
                sourceType = "search engines undefined"
        else:
            sourceType = "other"

print(sourceType)

# 2
def source_type_classification(source, medium):
    if source == "google" or source == "yandex":
        if medium == "seo" or medium == "sem":
            return "search engines seo"
        elif medium == "brand":
            return "search engines brand"
        else:
            return "search engines undefined"
    else:
        return "other"

print(source_type_classification("google", "seo"))
print(source_type_classification("yandex", "seo"))
print(source_type_classification("google", "brand"))
print(source_type_classification("google", "123"))

# 3
source_type_stats = {}

with open("data_no_header.txt", "r") as f:
    for line in f:
        line = line.strip().split("\t")
        source = line[5]
        medium = line[4]
        sourceType = source_type_classification(source, medium)

        if sourceType in source_type_stats:
            source_type_stats[sourceType] += 1
        else:
            source_type_stats[sourceType] = 1

print(source_type_stats)
print(source_type_stats["search engines seo"])

# 4
def source_type_classification_line(line):
    source = line[5]
    medium = line[4]

    if source == "google" or source == "yandex":
        if medium == "seo" or medium == "sem":
            return "search engines seo"
        elif medium == "brand":
            return "search engines brand"
        else:
            return "search engines undefined"
    else:
        return "other"

test_line = [
    "40443",
    "05.10.2016 23:18",
    "1010",
    "0,000925926",
    "seo",
    "google",
    "0",
    "6243",
    "20,20"
]

print(source_type_classification_line(test_line))

# 5
def source_type_classification_final(line):
    source = line[5]
    medium = line[4]
    amount_paid = float(line[-1].replace(",", "."))

    if amount_paid >= 20:
        orderType = "expensive"
    else:
        orderType = "cheap"

    if source == "google" or source == "yandex":
        if medium == "seo" or medium == "sem":
            sourceType = "search engines seo"
        elif medium == "brand":
            sourceType = "search engines brand"
        else:
            sourceType = "search engines undefined"
    else:
        sourceType = "other"

    return sourceType, orderType

source_type_stats = {}

with open("data_no_header.txt", "r") as f:
    for line in f:
        line = line.strip().split("\t")
        sourceType, orderType = source_type_classification_final(line)
        source_order_type = sourceType + " " + orderType

        if source_order_type in source_type_stats:
            source_type_stats[source_order_type] += 1
        else:
            source_type_stats[source_order_type] = 1

print(source_type_stats)
print(source_type_stats["search engines seo cheap"])
