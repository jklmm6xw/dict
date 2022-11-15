while True:
    verb = input("Verbe à ajouter?: ")
    verb = verb.upper()

    terminaisons = "a/e/ai/as/at/ee/er/es/ez/ais/ait/ant/ees/ent/era/iez/ons/ames/asse/ates/erai/eras/erez/ions/aient/asses/erais/erait/erent/eriez/erons/eront/assent/assiez/erions/assions/eraient"
    terminaisons = terminaisons.split("/")
    words = []

    for i in terminaisons:
        words.append(verb + i.upper())

    for i in words:
        with open("dict.txt", "a", encoding="utf-8") as f:
            f.write(i + "\n")