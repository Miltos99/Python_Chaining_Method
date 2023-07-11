class VersionManager():
    def __init__(self,version= ""):
        #Search if the elements of the given str
        #are digits
        Digit_search = version.split(".") 
        if not all(element.isdigit() or element=="" for element in Digit_search[:3]):
            raise ValueError("Error occured while parsing version!")
        self.version = version
        self.rollback_history = []

    def release(self):
        version = self.final_form(self.version)
        return version
    
    def major(self):
        self.rollback_history.append(self.version)
        self.version = self.ver_change(self.version,0)
        return self
        
    def minor(self):
        self.rollback_history.append(self.version)
        self.version = self.ver_change(self.version, 1)
        return self

    def patch(self):
        self.rollback_history.append(self.version)
        self.version = self.ver_change(self.version, 2)
        return self
    
    def rollback(self):
        self.version = self.Roll_Back(self.version)
        return self
    

    #Function that gives the previous Versions
    def Roll_Back(self, version:str)-> str:
        if not self.rollback_history:
            raise ValueError("Cannot rollback!")
        elif version == "0.0.0":
            return "0.0.1"
        else:
            version = self.rollback_history[-1]
            self.rollback_history = self.rollback_history[:-1]
        return version
    




    def ver_change(self,version:str, numb: int) -> str:
        max_version_size = 3
        #Default form if version is empty
        if not version:
            version = "0.0.1"       
        version = version.split(".")
        
        #If version < max_version_size then add 0 in the empty seats
        version.extend(["0"]*(max_version_size-len(version)))

        #Add one in the correct number of the version
        version[numb] = str(int(version[numb]) + 1)
        version = version[:3]

        #Convert the two last digits of the version
        #Into Zeros if the major is called 
        if numb == 0:
            version[numb+1] = "0"
            version[numb+2] = "0"

        #Convert the last digit into zero if the minor
        #Is called
        elif numb == 1:
            version[numb+1] = "0"
        version =".".join(version) 
        return version

    #When release is called the program stops and 
    #returns the value
    def final_form(self,version) -> str:
        max_string_size = 5
        if not version or version =="" or version == "0.0.0":
            return "0.0.1"
        number_of_zero = int((max_string_size-len(version))/2)
        base_form_string = ".".join([version] + ["0"] * number_of_zero)
        version = base_form_string.split(".")
        version = ".".join(version[:3])
        return version

test= VersionManager().major().rollback().release()
print(test)