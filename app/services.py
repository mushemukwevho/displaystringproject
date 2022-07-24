import json
from pathlib import Path

class DisplayStringService():
    """Displaystring Service.
    """
    
    CONTEXTS = {
        'tag':'tag',
        'preference':'prefence',
        'offer':'offer',
        'assignment':'assignment',
    }
    
    @staticmethod
    def load_displaystring_data()-> list:
        """Load displaystring_database JSON file.

        Returns:
            list: list of displaystring objects
        """
        data =[]

        try:
            # Using pathlib to resolve path
            file_path = Path(__file__).resolve(strict=True).parent
            file_path = file_path / 'fixtures'/ 'displaystring_database.json'
            
            with open(file_path) as file: # Use file to refer to the file object
                data = json.load(file)
        except:
            pass # Log error (e)
        
        finally:
            return data
        
    @staticmethod
    def resolve_dict_extract(key :str,
                             dictionary :dict,
                             locale :str, 
                             context :str)-> dict:
        if isinstance(dictionary, dict):
            for k, v in dictionary.items():
                if k == key:
                    dictionary[k] =\
                        DisplayStringService.\
                            get_displaystring_for_context(displaystring_holder=v,
                                                          locale=locale,
                                                          context=context)
                if isinstance(v, dict):
                    DisplayStringService.resolve_dict_extract(key, 
                                                              v, 
                                                              locale, 
                                                              context)
                elif isinstance(v, list):
                    for d in v:
                        DisplayStringService.resolve_dict_extract(key, 
                                                                  d, 
                                                                  locale, 
                                                                  context)
        elif isinstance(dictionary, list): # "dictionary" - probably a list at this point
            for d in dictionary:
                DisplayStringService.resolve_dict_extract(key, 
                                                          d, 
                                                          locale, 
                                                          context)
        return dictionary
    
    @staticmethod
    def get_displaystring_for_context(displaystring_holder :str, 
                                      locale :str, 
                                      context :str
                                      )-> str:
        """Provide displaystring for context from displaystring database. 

        Args:
            displaystring_holder (str): uid
            locale (str): e.g. en-EN
            context (str): e.g. tag

        Returns:
            displaystring:
            None: When there is no data to return
        """
        displaystring_data = DisplayStringService.load_displaystring_data()
        for displaystring in displaystring_data:
            if displaystring['uid'] == displaystring_holder:
                locale_data = None
                
                # Fallback hierachy for a given locale
                if displaystring['contexts'].get(context, None) and not locale_data:
                    locale_data = displaystring['contexts'][context].get(locale, None)
                
                if ((context==DisplayStringService.CONTEXTS['tag'] or 
                     context==DisplayStringService.CONTEXTS['preference']) and
                    not locale_data):
                    # Check if the database has context before a fallback
                    if displaystring['contexts'].get('offer', None):
                        locale_data = displaystring['contexts']['offer'].get(locale, None)
                
                if context in DisplayStringService.CONTEXTS and not locale_data:
                    locale_data = displaystring['contexts']['assessment'].get(locale, None)
                
                # Defaulting to en-GB locale fallback hierachy
                if displaystring['contexts'].get(context, None) and not locale_data:
                    locale_data = displaystring['contexts'][context].get('en-GB', None)
                
                if ((context==DisplayStringService.CONTEXTS['tag'] or 
                     context==DisplayStringService.CONTEXTS['preference']) and
                    not locale_data):
                    # Check if the database has context before a fallback
                    if displaystring['contexts'].get('offer', None):
                        locale_data = displaystring['contexts']['offer'].get('en-GB', None)
                
                
                if context in DisplayStringService.CONTEXTS and not locale_data:
                    # Check if the database has context before a fallback
                    if displaystring['contexts'].get('assessment', None):
                        locale_data = displaystring['contexts']['assessment'].get('en-GB', None)    
                            
                return locale_data
            
        return None

    @staticmethod
    def resolve_displaystrings(dictionary :dict, 
                               locale :str, 
                               context :str, 
                               key :str ='displayStringUID')-> dict:
        
        return DisplayStringService.resolve_dict_extract(key=key,
                                                         dictionary=dictionary,
                                                         locale=locale,
                                                         context=context)
