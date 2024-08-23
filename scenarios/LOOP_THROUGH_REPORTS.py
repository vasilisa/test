import dataiku 
from dataiku.scenario import Scenario

client  = dataiku.api_client()
project = client.get_default_project()


scenario = Scenario()

# Get a list of mails to send the dashboard to
mail_list    = dataiku.Dataset("EMAILLOOPDEMO.mail-list")
mail_df      = mail_list.get_dataframe()
program_list = mail_df['reward_program']

scenario_mail = project.get_scenario("SENDREPORT")
settings      = scenario_mail.get_settings() # get the settings of the scenario mail 
    
for program in program_list:
    
    # get a mail list for this group
    recipients = mail_df.loc[mail_df['reward_program']==program]['email'].values[0]
    
    print(recipients)
    
    # step 1: set the project variables
    f"Step 1: Setting project variable: reward program to {program} and recipients to {recipients}"
    scenario.set_project_variables('EMAILLOOPDEMO', reward_program=program) 
    scenario.set_project_variables('EMAILLOOPDEMO', recipients=recipients) 
    
    # customize the subject of the mail and the mail body
    message = f'Hello, \nPlease find attached a dashboard with the last updates on the reward program {program}. \n Best regards from Dataiku '
    subject =f'LAST UPDATE FOR reward program {program}'
    
    
    # Change the message and subject for the scenario_mail and save it 
    settings.raw_reporters[0]['messaging']['configuration']['message'] = message
    settings.raw_reporters[0]['messaging']['configuration']['subject'] = subject
    settings.save()

    
    f"Step 2: calling a mail scenario and if all checks are good it will send a report"
    scenario.run_scenario("SENDREPORT", name="run send dashboard scenario", fail_fatal=True)
   
    
  