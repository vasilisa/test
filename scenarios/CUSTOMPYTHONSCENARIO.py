# This sample code helps you get started with the custom scenario API.
#For more details and samples, please see our Documentation
import dataiku 
from dataiku.scenario import Scenario

# The Scenario object is the main handle from which you initiate steps
scenario = Scenario()

# A few example steps follow

# Building a dataset
scenario.build_dataset("transactions_MES_filtered_scored", partitions="NP")


client     = dataiku.api_client()
project    = client.get_default_project()

# get the email from the variable
recipients = project.get_variables()["standard"]["recipient_list"]

    
# Sending custom reports

message_sender = scenario.get_message_sender("VS_test_emails")

# You can then call send() with message params.
# params are specific to each message channel types

# SMTP mail example
message_sender.send(sender="vasilisa.skvortsova@dataiku.com", recipient=recipients, subject="All is well", message="Scenario is working as expected")

# You can also call set_params to set params on the sender that will be reused for all subsequent 'send' calls
#message_sender.set_params(sender="dss@company.com", recipent="data-scientists@company.com")
#message_sender.send(subject="All is well", message="Scenario is working as expected")
