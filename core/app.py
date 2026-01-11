from analyzer import reader, processor, writer
from core import config, logger

def main():
    logger.log_info("Text Analyzer startar...")

    # Säker input - använder default fil från config
    file_path = input(f"Ange textfil (tryck Enter för {config.TEXT_FILE}): ").strip()
    if not file_path:
        file_path = config.TEXT_FILE

    lines = reader.read_file(file_path)
    if not lines:
        logger.log_error("Ingen text att analysera. Avslutar programmet.")
        return

    text_proc = processor.TextProcessor(lines)
    line_count = text_proc.count_lines()
    word_count = text_proc.count_words()
    most_common = text_proc.most_common_word()

    writer.print_results(line_count, word_count, most_common)
    logger.log_info("Text Analyzer klart.")

if __name__ == "__main__":
    main()
