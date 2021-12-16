from unittest import TestCase
import viz


class Test(TestCase):
    def test_is_employee(self):
        # Three GitHub users to test.
        # 1st is a member of the Microsoft organisation.
        # 2nd is not, but has 'Microsoft' listed as his company.
        # 3rd has neither, and is not a Microsoft employee (and is me).
        users = ["bpasero", "mjbvz", "itswilliamleonard"]

        self.assertTrue(viz.is_employee(users[0]))
        self.assertTrue(viz.is_employee(users[1]))
        self.assertFalse(viz.is_employee(users[2]))

