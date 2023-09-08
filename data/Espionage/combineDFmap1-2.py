import pandas as pd
import os


def combine_and_sum(file1, file2, output_file):
    # Read both CSV files into pandas DataFrames
    try:
        df1 = pd.read_csv(file1)
        df2 = pd.read_csv(file2)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return

    # Concatenate both DataFrames into a single DataFrame
    combined_df = pd.concat([df1, df2], ignore_index=True)

    # Group by "Nickname" and sum the other columns
    grouped_df = combined_df.groupby("Nickname").sum().reset_index()

    # Write the resulting DataFrame back to a new CSV file
    try:
        grouped_df.to_csv(output_file, index=False)
        print(f"File has been saved as {output_file}")
    except Exception as e:
        print(f"An error occurred while saving the CSV file: {e}")


if __name__ == "__main__":
    directory = "C:\\Users\\Lazaro B\\Documents\\GitHub\\CSGOProject\\data\\Espionage"
    file1 = os.path.join(directory, "EspionageVersusloskogutos21-08-2023bo3-1.csv")
    file2 = os.path.join(directory, "EspionageVersusloskogutos21-08-2023bo3-2.csv")
    output_file = os.path.join(directory, "EspionageVersusloskogutos21-08-2023.csv")

    combine_and_sum(file1, file2, output_file)