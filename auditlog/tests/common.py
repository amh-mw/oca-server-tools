from odoo.tests.common import TransactionCase


class AuditLogRuleCommon(TransactionCase):
    @classmethod
    def tearDownClass(cls):
        cls.auditlog_rule.unlink()
        super().tearDownClass()
