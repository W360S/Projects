from odoo.tests.common import TransactionCase

class TestProjectCaseDefault(TransactionCase):
    # Use case : Prepare some data for current test case
    def setUp(self):
        super(TestProjectCaseDefault, self).setUp()
        self.project = self.env['project.project'].create({
            'name': 'Project Test'
        })

    def test_project_new(self):
        self.assertEqual(len(self.project.type_ids), 7)
