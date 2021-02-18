# quick component to convert degrees F to C.
# Function takes in value, does conversion and puts answer into a list


def to_c(from_f):
    # centigrade =(from_f * 5/9) - 32

    centigrade =(5 / 9) * (from_f - 32)
    return centigrade


# Main Routine
temperature = (0, 32, 100)
converted= []

for item in temperature:
    answer = to_c(item)
    ans_statement = " {} degrees F is {} degrees C".format(item, answer)
    converted.append(ans_statement)

print (converted)
