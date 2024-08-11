from typing import List
def create_txt_file(path:str,data:str) -> None:
    with open(path,mode="w") as file:
        for lines in data:
            file.write(lines)
        file.close()

def open_file_txt(path:str) -> List[str]:
    try:    
        with open(path, mode="r") as txt:
            content: List[str] = txt.readlines()
        
        if len(content) > 0 : 
            return content
        else:
            return False
        
    except FileNotFoundError:
        return False