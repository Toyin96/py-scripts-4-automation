"""This program can automatically extract phone numbers and email addresses from a block of text"""
import sys
import pyperclip


def is_phone_number(text):
    if len(text) != 12:
        return False
    for j in range(0, 3):
        if not text[j].isdecimal():
            return False
    if text[3] != "-":
        return False
    for m in range(4, 7):
        if not text[m].isdecimal():
            return False
    if text[7] != "-":
        return False
    for num in range(8, 12):
        if not text[num].isdecimal():
            return False
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("You didnt enter the block of text you want to extract the text from")
        sys.exit()
    else:
        i = 1
        statement = ""
        comma = " "

        while i < len(sys.argv):
            statement += sys.argv[i]
            statement += comma
            i += 1
    print(f"\nmessage is: {statement}")
    phone_list = []
    for i in range(len(statement)):
        chunk = statement[i:i+12]

        if is_phone_number(chunk):
            phone_list.append(chunk)

    if len(phone_list) == 1:
        print(f"Success!!! found {len(phone_list)} valid phone number")
    elif len(phone_list) > 1:
        print(f"Success!!! found {len(phone_list)} valid phone numbers")
    else:
        print("Sorry...no valid US phone number found in the block of text submitted")
        sys.exit()

    final_list = ", ".join(phone_list)
    print(phone_list)
    pyperclip.copy(final_list)

    if len(final_list) > 1:
        print("Process completed...the numbers have been copied to your clipboard")
    elif len(final_list) == 1:
        print("Process completed...The number have been copied to your clipboard")
