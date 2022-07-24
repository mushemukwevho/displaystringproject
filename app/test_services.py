import pytest

from services import DisplayStringService

class TestDisplayStringService:
    
    @pytest.mark.parametrize('displaystring_holder, locale, context, results',
                             [
                                 ('question.tire1_r_profile_picture.description', 'en-GB', 'assessment','On the passenger side'),
                                 ('question.tire1_r_profile_picture.description', 'non-existing-locale', 'tag','On the passenger side'),
                                 ('non_existing.uid', 'en-GB', 'assessment', None),
                                 ('question.tire1_r_profile.description', 'en-GB', 'tag','at the passenger side'),
                                 ('question.tire1_r_profile.description', 'it-IT', 'offer','at the passenger side'),
                                 ])
    def test_get_displaystring_for_context(self, displaystring_holder, locale, context, results):
        data = DisplayStringService.\
            get_displaystring_for_context(displaystring_holder=displaystring_holder, locale=locale, context=context)
        assert data == results


    @pytest.mark.parametrize('dictionary, locale, context, results',
                             [
                                 (({
                                    "displayStringUID": "question.tire1_r_profile_picture.description",
                                        "subdocument_01": [{"displayStringUID": "question.tire1_r_profile_picture.description"}]
                                        }), 'en-GB', 'assessment',({"displayStringUID": "On the passenger side",
                                        "subdocument_01": [
                                            {
                                                "displayStringUID": "On the passenger side"
                                            }
                                        ]
                                    })),
                                 (({
                                    "displayStringUID": "question.tire1_r_profile_picture.description",
                                        "subdocument_01": [{"displayStringUID": "non_existing.uid"}]
                                        }), 'en-GB', 'assessment',({"displayStringUID": "On the passenger side",
                                        "subdocument_01": [
                                            {
                                                "displayStringUID": None
                                            }
                                        ]
                                    })),
                                 ]) 
    def test_resolve_displaystrings(self, dictionary, locale, context, results):
        data = DisplayStringService.resolve_displaystrings(dictionary, locale, context)
        assert data == results