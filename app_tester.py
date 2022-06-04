from app import app
from unittest import TestCase

class tester(TestCase):

    def test_input_form(self):
        """ Test that the input form is displayed correctly """
        with app.test_client() as tester:
                tester = tester.get('/')
                response = tester.get_data(as_text=True)
                self.assertIn('Converting from', response)
                self.assertIn('Converting to', response)
                self.assertIn('Amount', response)
                self.assertIn('Convert', response)
                self.assertIn('button', response)


    def  test_conversion(self):

        
        with app.test_client() as tester:

                """" Test a successful conversion """
                request = tester.get('/convert?from=USD&to=USD&amount=1')
                response = request.get_data(as_text=True)
                self.assertIn('The result is</label> $  1.00', response)

                """ Test for an invalid source currency """
                request = tester.get('/convert?from=uuuu&to=USD&amount=1')
                response = request.get_data(as_text=True)
                self.assertIn('The source currency is not valid', response)

                """ Test for an invalid target currency """
                request = tester.get('/convert?from=USD&to=eee&amount=1')
                response = request.get_data(as_text=True)
                self.assertIn('The target currency is not valid', response)

                """ Test for a negative amount """
                request = tester.get('/convert?from=USD&to=USD&amount=-1')
                response = request.get_data(as_text=True)
                self.assertIn('The amount has to be greater than zero', response)

                """ Test for a failed conversion """
                request = tester.get('/convert?from=USD&to=ILS&amount=1')
                response = request.get_data(as_text=True)
                self.assertIn('The conversion has failed', response)

                

                
             

    
