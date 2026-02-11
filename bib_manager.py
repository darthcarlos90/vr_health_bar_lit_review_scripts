
def parse_bib_field(entry_text, field_name):
    """
    Extract a field value from a BIB entry.
    Simple string parsing approach with exact field matching.
    """
    # Look for the field name with exact matching (not substring)
    field_lower = field_name.lower()
    text_lower = entry_text.lower()
    
    # Find where the field starts - must be preceded by whitespace or start of string
    search_pos = 0
    field_start = -1
    
    while True:
        pos = text_lower.find(field_lower + '=', search_pos)
        if pos == -1:
            break
        
        # Check if it's at the start OR preceded by whitespace/newline
        if pos == 0 or text_lower[pos - 1] in ' \t\n,{':
            field_start = pos
            break
        
        search_pos = pos + 1
    
    if field_start == -1:
        return ''
    
    # Move past "field="
    value_start = entry_text.find('=', field_start) + 1
    
    # Skip whitespace
    while value_start < len(entry_text) and entry_text[value_start] in ' \t\n':
        value_start += 1
    
    # Check if value is in braces {}
    if value_start < len(entry_text) and entry_text[value_start] == '{':
        # Find matching closing brace
        brace_count = 0
        value_end = value_start
        for i in range(value_start, len(entry_text)):
            if entry_text[i] == '{':
                brace_count += 1
            elif entry_text[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    value_end = i
                    break
        
        # Extract value between braces
        value = entry_text[value_start + 1:value_end]
    else:
        # Value without braces - read until comma or newline
        value_end = value_start
        while value_end < len(entry_text) and entry_text[value_end] not in ',\n':
            value_end += 1
        value = entry_text[value_start:value_end]
    
    # Clean up the value
    value = value.strip().strip('"').strip(',').strip()
    return value





def extract_from_bib(file_path):
    """
    Extract bibliographic data from a BIB file.
    Extracts 'title' as paper title and 'booktitle' as outlet (conference/journal name)
    """
    extracted_data = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split by @ to get individual entries
        entries = [e for e in content.split('@') if e.strip()]
        
        for entry in entries:
            entry = entry.replace('\n', ' ')
            entry = entry.replace(' = ', '=')
            # Extract title (paper title)
            title = parse_bib_field(entry, 'title')
            
            # Extract booktitle (conference/journal name)
            outlet = parse_bib_field(entry, 'booktitle')
            if not outlet or outlet.strip() == '':
                outlet = parse_bib_field(entry, 'journal')
            
            # Try both 'author' and 'authors'
            authors = parse_bib_field(entry, 'author')
            if not authors:
                authors = parse_bib_field(entry, 'authors')
            
            # Skip this entry if authors is empty
            if not authors or authors.strip() == '':
                continue
            
            year = parse_bib_field(entry, 'year')
            keywords = parse_bib_field(entry, 'keywords')
            abstract = parse_bib_field(entry, 'abstract')
            doi = parse_bib_field(entry, 'doi')
            
            data = {
                'Title': title,
                'Authors': authors,
                'Year': year,
                'Keywords': keywords,
                'Abstract': abstract,
                'DOI': doi,
                'Outlet': outlet,
                'Source_File': file_path
            }
            
            extracted_data.append(data)
            
    except Exception as e:
        print(f"Error reading BIB {file_path}: {e}")
    
    return extracted_data