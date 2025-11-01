from stats import number_of_words, get_book_text, number_of_chars, report
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    result = get_book_text(sys.argv[1])

    final = number_of_chars(result)

    report_result = report(final)

    print(sys.argv)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(number_of_words(result))
    print("--------- Character Count -------")

    for i in report_result:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")

main()