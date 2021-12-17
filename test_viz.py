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
        userdict = viz.process_user(user)
        self.assertEquals(userdict.get('name'), "bpasero")
        self.assertTrue(userdict.get('employed'))
        # Tricky to test contribs, because it is always updating. Just check if it's an int.
        self.assertTrue(isinstance(userdict.get('contribs'), int))
