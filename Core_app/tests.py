from django.test import TestCase
from django.contrib.auth.models import User
from colorama import Style, Fore

class TestCaseColor(TestCase):
    
    def assert_equal_color(self, object1, object2, message):
        try:
            if not self.assertEqual(object1, object2):
                print(f"{Fore.GREEN} {message}, SUCCESS {Style.RESET_ALL}")
        except Exception as error:
            print(f"{Fore.RED} {message}, ERROR: {error} {Style.RESET_ALL}")
    
    def assert_not_equal_color(self, object1, object2, message):
        try:
            if not self.assertNotEqual(object1, object2):
                print(f"{Fore.GREEN} {message}, SUCCESS {Style.RESET_ALL}")
        except Exception as error:
            print(f"{Fore.RED} {message}, ERROR: {error} {Style.RESET_ALL}")