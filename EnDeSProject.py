import sys
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


dict_let_to_num = {
    # Mapping of letters to numbers according to the table
    "A": 56, "B": 57, "C": 58, "D": 59, "E": 40, "F": 41,
    "G": 42, "H": 43, "I": 44, "J": 45, "K": 46, "L": 47,
    "M": 48, "N": 49, "O": 60, "P": 61, "Q": 62, "R": 63,
    "S": 64, "T": 65, "U": 66, "V": 67, "W": 68, "X": 69,
    "Y": 10, "Z": 11,
    "a": 12, "b": 13, "c": 14, "d": 15, "e": 16, "f": 17,
    "g": 18, "h": 19, "i": 30, "j": 31, "k": 32, "l": 33,
    "m": 34, "n": 35, "o": 36, "p": 37, "q": 38, "r": 39,
    "s": 90, "t": 91, "u": 92, "v": 93, "w": 94, "x": 95,
    "y": 96, "z": 97,
    " ": 98, ",": 99, ".": 100, "'": 101, "!": 102, "-": 103,
}

dict_num_to_let = {
    # Mapping of numbers to letters according to the table
    56: "A", 57: "B", 58: "C", 59: "D", 40: "E", 41: "F",
    42: "G", 43: "H", 44: "I", 45: "J", 46: "K", 47: "L",
    48: "M", 49: "N", 60: "O", 61: "P", 62: "Q", 63: "R",
    64: "S", 65: "T", 66: "U", 67: "V", 68: "W", 69: "X",
    10: "Y", 11: "Z",
    12: "a", 13: "b", 14: "c", 15: "d", 16: "e", 17: "f",
    18: "g", 19: "h", 30: "i", 31: "j", 32: "k", 33: "l",
    34: "m", 35: "n", 36: "o", 37: "p", 38: "q", 39: "r",
    90: "s", 91: "t", 92: "u", 93: "v", 94: "w", 95: "x",
    96: "y", 97: "z",
    98: " ", 99: ",", 100: ".", 101: "'", 102: "!", 103: "-",
}


def ass_dec_func(string):
    """
    Decrypts a string of comma-separated numbers into letters.

    param: string (str)
    return: decrypted message as plain text
    """
    ass_finaleword = ""
    ass_nums = string.split(',')

    if ass_nums == [""]:
        print("")
        return ""

    for num in ass_nums:
        ass_helper_num = int(num)  # Convert string to integer
        ass_letter = dict_num_to_let[ass_helper_num]  # Map number to letter
        ass_finaleword += ass_letter  # Add the letter to the final string

    return ass_finaleword


def enc_words(words):
    """
    Encrypts a string into comma-separated numbers.

    param: words (str)
    return: encrypted string of numbers
    """
    finale_num = []  # Create a list to hold the numeric strings

    for char in words:
        num = dict_let_to_num[char]
        finale_num.append(str(num))

    return ",".join(finale_num)  # Join numbers with commas


def dec_numbers(input_file):
    """
    Reads a file and decrypts its comma-separated numbers.

    param: input_file (str)
    return: decrypted message from file
    """
    decrypted_msg_finale = ""

    with open("encrypted_msg.txt", "r"):
        nums_of_txt = open("encrypted_msg.txt", "r").read().split(",")

        if nums_of_txt == [""]:
            # Check if file is empty
            print("File is empty")
            logging.info("The file was empty")
            return ""

        for num in nums_of_txt:
            number = int(num)  # Convert to integer
            letter = dict_num_to_let[number]  # Convert to letter
            decrypted_msg_finale += letter  # Append to final string

        logging.info(f"Decrypted message is {decrypted_msg_finale}")
        print(decrypted_msg_finale)
        return decrypted_msg_finale


def test_assest():
    """
    Runs tests to check encryption and decryption.
    """
    as_msg = "abcdefghijklmnopqrstuvwxyz ,.'!-"
    as_encrypted = enc_words(as_msg)
    as_decrypted = ass_dec_func(as_encrypted)
    assert as_decrypted == as_msg
    logging.info("Assert1 passed")

    as_msg = "ABCDEFGHIJKLMNOPQRSTUVWXY"
    as_encrypted = enc_words(as_msg)
    as_decrypted = ass_dec_func(as_encrypted)
    assert as_decrypted == as_msg
    logging.info("Assert2 passed")

    as_msg = "a.B"
    as_encrypted = enc_words(as_msg)
    as_decrypted = ass_dec_func(as_encrypted)
    assert as_decrypted == as_msg
    logging.info("Assert3 passed")

    logging.info("All tests passed")


def main():
    """
    Handles user input to encrypt or decrypt.
    """
    arguments = sys.argv[1:]  # Slice parameters to remove script name
    arguments = arguments[0]

    if arguments == 'Encrypt':
        logging.info("The user chose to encrypt the message")
        user_word = input("Enter a word you would like to encrypt: ")
        logging.info(f"User entered word to encrypt: {user_word}")

        with open("encrypted_msg.txt", "w") as file:
            file.write(enc_words(user_word))
            logging.info(
                "The encrypted message was written to encrypted_msg.txt"
            )

    elif arguments == 'Decrypt':
        logging.info("The user chose to decrypt the message")

        try:
            with open("encrypted_msg.txt", "r"):
                dec_numbers('encrypted_msg.txt')
        except FileNotFoundError:
            print("ERROR, file not found")
            logging.error("ERROR, file not found")


if __name__ == "__main__":
    test_assest()
    main()
