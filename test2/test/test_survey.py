import unittest
from survey import AnonymouSurvey


class TestAnonymouSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymouSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)


if __name__ == '__main__':
    unittest.main()
