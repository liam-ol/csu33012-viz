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

    def test_process_user(self):
        # Test on a certain user.
        user = viz.vscode.get_contributors()[0]
        # Hard to test reliably, because a user's contributions count will increase over time.
        # We'll just check the first two entries.
        self.assertTrue('{"name": "bpasero", "employed": true, "contribs":' in viz.process_user(user))