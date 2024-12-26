def load_verbs_and_nouns(filename):
    """
    Wczytuje czasowniki i odpowiadające im rzeczowniki z pliku.
    """
    verbs_and_nouns = {}
    with open(filename, 'r', encoding='utf8') as file:
        for line in file:
            verb, nouns = line.strip().split(': ', 1)
            verbs_and_nouns[verb] = set(nouns.split())
    return verbs_and_nouns


def perform_operation(verbs_and_nouns, verbs, operation):
    """
    Wykonuje wybraną operację logiczną ('intersection' lub 'union')
    na zbiorach rzeczowników odpowiadających podanym czasownikom.
    """
    if not all(verb in verbs_and_nouns for verb in verbs):
        raise ValueError("Niektóre z podanych czasowników nie istnieją w danych.")

    # Pobranie zbiorów rzeczowników dla wybranych czasowników
    selected_sets = [verbs_and_nouns[verb] for verb in verbs]

    # Wykonanie operacji
    if operation == 'intersection':
        result = set.intersection(*selected_sets)
    elif operation == 'union':
        result = set.union(*selected_sets)
    else:
        raise ValueError("Niepoprawna operacja. Dozwolone: 'intersection', 'union'.")

    return result


def main():
    filename = "100_verbs_and_nouns.txt"
    try:
        verbs_and_nouns = load_verbs_and_nouns(filename)
    except FileNotFoundError:
        print(f"Plik {filename} nie został znaleziony.")
        return

    print("Dostępne czasowniki:")
    print(", ".join(verbs_and_nouns.keys()))

    while True:
        # Pobranie czasowników od użytkownika
        verbs = input(
            "\nPodaj czasowniki (oddzielone spacją), na których chcesz wykonać operacje, lub wpisz 'exit', aby zakończyć: ").strip().split()
        if "exit" in verbs:
            break

        # Sprawdzenie poprawności wyboru czasowników
        invalid_verbs = [v for v in verbs if v not in verbs_and_nouns]
        if invalid_verbs:
            print(f"Następujące czasowniki są niepoprawne: {', '.join(invalid_verbs)}")
            continue

        # Pobranie operacji od użytkownika
        operation = input("Wybierz operację ('intersection' dla części wspólnej, 'union' dla sumy): ").strip().lower()
        if operation not in {'intersection', 'union'}:
            print("Niepoprawna operacja. Wybierz 'intersection' lub 'union'.")
            continue

        # Wykonanie operacji i wyświetlenie wyniku
        try:
            result = perform_operation(verbs_and_nouns, verbs, operation)
            print(f"\nWynik ({operation} dla {', '.join(verbs)}):")
            print(", ".join(result) if result else "Brak wspólnych/sumowanych elementów.")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()