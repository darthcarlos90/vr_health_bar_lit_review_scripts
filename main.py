from file_manager import get_files_in_folder
from bib_manager import extract_from_bib
from csv_manager import extract_from_csv
from ranking import rank_entries


FOLDER_PATH = "C:\\Users\\ctir0789\\Documents\\Dev\\datasets\\hci_lit_rev\\"
KEYWORDS = [
    "VR", "Virtual Reality", "HMD", "Head-Mounted Display", "Head Mounted Display",
    "Physiological", "Wearable", "IMU", "heart-rate monitor", "HRV", "Cybersickness",
    "Motion Sickness", "Postural Instability", "Congnitive Load", "Working Memory", "Eye Tracker",
    "EEG", "Heart rate monitor", "BCI", "brain-computer interface", "motion tracker", "HRV", "Skin Conductance",
    "pupil dilatation", "attention", "position", "wearable sensor", "sensor", "wearable device", "electroencephalogra",
    "heart", "HCI", "human-computer"
]



def main():
    files = get_files_in_folder(FOLDER_PATH)
    
    database = []
    for file_path in files:
        
        if file_path.endswith('.csv'):
            data = extract_from_csv(file_path)
        elif file_path.endswith('.bib'):
            data = extract_from_bib(file_path)
        else:
            print("File must be .csv or .bib")
            data = []
        
        #print(f"File {file_path} has: {len(data)} entries")
        database.extend(data)
    
    print(f"\nExtracted {len(database)} entries:")
    rank_entries(database, KEYWORDS)
    for item in database:
        print(item)



if __name__ == "__main__":
    main()