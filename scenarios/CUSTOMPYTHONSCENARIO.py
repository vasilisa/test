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
sender = scenario.get_message_sender("mail-scenario", "local-mail") # A messaging channel
sender.set_params(sender="dss@company.com", recipient=recipients)

sender.send(subject="The scenario is doing well", message="New data scored")
