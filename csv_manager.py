import csv

def extract_from_csv(file_path):
    """
    Extract bibliographic data from a CSV file.
    
    Returns:
        List of dictionaries with extracted data
    """
    extracted_data = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                data = {
                    'Title': row.get('Title') or row.get('title') or '',
                    'Authors': row.get('Authors') or row.get('authors') or row.get('Author') or row.get('author') or '',
                    'Year': row.get('Year') or row.get('year') or '',
                    'Keywords': row.get('Keywords') or row.get('keywords') or '',
                    'Abstract': row.get('Abstract') or row.get('abstract') or '',
                    'DOI': row.get('DOI') or row.get('doi') or '',
                    'Source_File': file_path
                }
                extracted_data.append(data)
                
    except Exception as e:
        print(f"Error reading CSV {file_path}: {e}")
    
    return extracted_data




def export_to_csv(all_data):
    filename = "database.csv"
    
    keys = all_data[0].keys()
    
    with open(filename, "w", newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        
        dict_writer.writerows(all_data)
        
    print("Finished")