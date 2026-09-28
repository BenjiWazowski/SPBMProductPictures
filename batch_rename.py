import os
import csv

mapping_file = 'rename_map.csv'

if not os.path.exists(mapping_file):
    print(f"Error: {mapping_file} not found in current directory.")
    exit()

renamed_count = 0
skipped_count = 0

with open(mapping_file, mode='r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        old_file = row['old_name'].strip()
        new_file = row['new_name'].strip()
        
        if os.path.exists(old_file):
            # Resolve potential filename collisions automatically
            if os.path.exists(new_file) and old_file != new_file:
                base, ext = os.path.splitext(new_file)
                counter = 2
                alt_new_file = f"{base}_{counter}{ext}"
                while os.path.exists(alt_new_file):
                    counter += 1
                    alt_new_file = f"{base}_{counter}{ext}"
                new_file = alt_new_file

            os.rename(old_file, new_file)
            print(f"Renamed: '{old_file}' -> '{new_file}'")
            renamed_count += 1
        else:
            print(f"Skipped (not found): '{old_file}'")
            skipped_count += 1

print(f"\nCompleted! Total Renamed: {renamed_count}, Skipped: {skipped_count}")