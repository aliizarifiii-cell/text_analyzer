def read_file(file_path):
    """
    Läser en textfil och returnerar innehållet som en lista av rader.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        print(f"Filen {file_path} hittades inte.")
        return []
    except Exception as e:
        print(f"Något gick fel: {e}")
        return []
