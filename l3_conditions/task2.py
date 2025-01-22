# Write the function body to make the script work without errors
def full_none(s: str=None) -> str:
    if s == "full":         
        return s.upper()    
    elif s == "":           
        return "NONE"       
    else:                   
        return "FULL" 


# Do not change the below's code
if __name__ == "__main__":
    assert full_none("full") == "FULL"
    assert full_none("something") == "FULL"
    assert full_none("") == "NONE"
