from dataiku.scenario import Scenario 
import dataiku
from dataiku.scenario import Trigger
scn = Scenario()
client = dataiku.api_client()
project = client.get_default_project()
scenario = project.get_scenario("Recursive_MES")

Q_start = ["2017-04-01 00:00","2017-07-01 00:00","2017-10-01 00:00"]
Q_end = ["2017-06-30 00:00","2017-09-30 00:00","2017-12-31 00:00"]
variables = project.get_variables()
dataset = project.get_dataset("transactions_MES_filtered")
scn.build_dataset(dataset_name = "transactions_MES_filtered")

for i,q in enumerate(Q_start):
    variables['standard']["quarter_start"] = q
    variables['standard']["quarter_finish"] = Q_end[i]
    project.set_variables(variables)
    trigger_fire = scenario.run_and_wait()
    last_run = scenario.get_last_finished_run()
    last_run_details = last_run.get_details()
