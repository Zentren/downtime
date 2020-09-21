import argparse

from downtime.app_container import container


parser = argparse.ArgumentParser(description='Reminds you to take breaks from the computer')
parser.add_argument('profile_name', type=str)
args = parser.parse_args()

profile_runner = container.profile_runner()
profile_runner.run(args.profile_name)