from streams.out_stream import PersonOutputPrintStream, PersonOutputFileStream, PersonOutputTCPStream
from person import Person


def main():

    # name, cpf(cpf is a str number with 11 digits), age

    people = [
        Person("João", "12345678901", 20),
        Person("Maria", "12345678902", 21),
        Person("José", "12345678903", 22),
    ]

    pops = PersonOutputPrintStream(people)
    pofs = PersonOutputFileStream(people)
    pots = PersonOutputTCPStream(people)
    pops.write()
    pofs.write()
    pots.write()


if __name__ == "__main__":
    main()
