from pydantic import BaseModel

# serialization and validation

class contextDisplayString(BaseModel):
    displaystring_holder :str
    locale :str 
    context :str
    
    
class resolveDisplayString(BaseModel):
    dictionary :dict
    locale :str
    context :str
