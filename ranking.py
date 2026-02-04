def rank_entries(all_data, keywords):
    """
    Rank entries based on keyword appearances.
    All searches are case-insensitive.
    
    Args:
        all_data: List of dictionaries with extracted bibliographic data
        keywords: List of keywords to search for
        
    Returns:
        List of dictionaries with added 'Rank' field
    """
    # Convert all keywords to lowercase once
    keywords_lower = [keyword.lower() for keyword in keywords]
    
    for entry in all_data:
        rank = 0
        
        # Get fields and convert to lowercase
        title = entry.get('Title', '').lower()
        keywords_field = entry.get('Keywords', '').lower()
        abstract = entry.get('Abstract', '').lower()
        
        # Check each keyword
        for keyword in keywords_lower:
            found = False
            
            # Check if keyword appears in any of the three fields
            if keyword in title:
                found = True
            elif keyword in keywords_field:
                found = True
            elif keyword in abstract:
                found = True
            
            # Only count once per keyword (first appearance)
            if found:
                rank += 1
        
        # Add rank to the entry
        entry['Rank'] = rank
    
    all_data.sort(key=lambda x: x['Rank'], reverse=True)
    
    return all_data