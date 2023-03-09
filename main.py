import argparse
import yaml
from src.tools.utils import upload_to_google_sheet, upload_to_s3, process_task

args = argparse.ArgumentParser(
    description="Provies some inforamtion on the job to process"
)
args.add_argument(
    "-t", "--task", type=str, required=True,
    help="This will point to a task location into the config.yaml file.\
        Then it will follow the step of this specific task.")
args = args.parse_args()

with open("./config/config.yaml", 'r') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

args_task = "sql_python"
config_export = config[args_task]["export"]

if config_export[0]["export"]["host"] == 's3':
    upload_to_s3(process_task(args_task), config_export[0]["export"]["filename"])
elif config_export[0]["export"]["host"] == 'gsheet':
    upload_to_google_sheet(config_export[0]["export"]["spreadsheet_id"], process_task(args.task), 
                     config_export[0]["export"]["clear_sheet"])