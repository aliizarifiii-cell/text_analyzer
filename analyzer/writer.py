def print_results(line_count, word_count, most_common):
    """
    Skriver ut resultatet på ett snyggt sätt.
    """
    print("=== Resultat från Text Analyzer ===")
    print(f"Antal rader: {line_count}")
    print(f"Antal ord: {word_count}")
    if most_common:
        print(f"Vanligaste ordet: {most_common}")
    else:
        print("Ingen text att analysera.")
