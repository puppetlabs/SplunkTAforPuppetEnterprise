
# encoding = utf-8
# Always put this line at the beginning of this file
import splunktaforpuppetenterprise_declare

import os
import sys

from alert_actions_base import ModularAlertBase
import modalert_puppet_enterprise_victorops_integration_helper

class AlertActionWorkerpuppet_enterprise_victorops_integration(ModularAlertBase):

    def __init__(self, ta_name, alert_name):
        super(AlertActionWorkerpuppet_enterprise_victorops_integration, self).__init__(ta_name, alert_name)

    def validate_params(self):

        if not self.get_global_setting("victor_ops_token"):
            self.log_error('victor_ops_token is a mandatory setup parameter, but its value is None.')
            return False

        if not self.get_param("dropdown_list"):
            self.log_error('dropdown_list is a mandatory parameter, but its value is None.')
            return False

        if not self.get_param("alert_entity_id"):
            self.log_error('alert_entity_id is a mandatory parameter, but its value is None.')
            return False

        if not self.get_param("state_message"):
            self.log_error('state_message is a mandatory parameter, but its value is None.')
            return False
        return True

    def process_event(self, *args, **kwargs):
        status = 0
        try:
            if not self.validate_params():
                return 3
            status = modalert_puppet_enterprise_victorops_integration_helper.process_event(self, *args, **kwargs)
        except (AttributeError, TypeError) as ae:
            self.log_error("Error: {}. Please double check spelling and also verify that a compatible version of Splunk_SA_CIM is installed.".format(ae.message))
            return 4
        except Exception as e:
            msg = "Unexpected error: {}."
            if e.message:
                self.log_error(msg.format(e.message))
            else:
                import traceback
                self.log_error(msg.format(traceback.format_exc()))
            return 5
        return status

if __name__ == "__main__":
    exitcode = AlertActionWorkerpuppet_enterprise_victorops_integration("SplunkTAforPuppetEnterprise", "puppet_enterprise_victorops_integration").run(sys.argv)
    sys.exit(exitcode)
