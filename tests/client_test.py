from testingfixtures import add_surrounding_dir_to_path
# add surrounding dir to path to enable importing
add_surrounding_dir_to_path()

from ceptic.client import CepticClientTemplate, main
from ceptic.common import normalize_path
from shutil import rmtree, copytree
from time import sleep
import sys
import os


class ExampleClient(CepticClientTemplate):

	def __init__(self, location, start_terminal):
		name = "test"
		version = "3.0.0"
		CepticClientTemplate.__init__(self, location, start_terminal, name=name, version=version)

	def add_terminal_commands(self):
		self.terminalManager.add_command("ping", lambda data: self.ping_terminal_command(data[1]))


# TESTS:

def test_creation():

	client = ExampleClient(location=test_creation.test_location,start_terminal=False)
	# list of directories that should exist
	directories = [
		"resources",
		"resources/protocols",
		"resources/cache",
		"resources/programparts",
		"resources/uploads",
		"resources/downloads",
		"resources/networkpass",
		"resources/certification"
	]
	# list of directories that should NOT exist
	not_directories = [
	]
	# list of files that should exist
	files = [
		"resources/certification/techtem_cert_client.pem",
		"resources/certification/techtem_cert_server.pem",
		"resources/certification/techtem_key_client.pem"
	]
	# list of files that shoudl NOT exist
	not_files = [
		"resources/certification/techtem_key_server.pem"
	]
	# check if directories exist
	for directory in directories:
		fullpath = os.path.join(test_creation.test_location,directory)
		print(fullpath)
		assert os.path.isdir(fullpath)
	# check if directories DON'T exist
	for directory in not_directories:
		fullpath = os.path.join(test_creation.test_location,directory)
		print(fullpath)
		assert not os.path.isdir(fullpath)
	# check if files exist
	for file in files:
		fullpath = os.path.join(test_creation.test_location,file)
		print(fullpath)
		assert os.path.isfile(fullpath)
	# check if files DON'T exist
	for file in not_files:
		fullpath = os.path.join(test_creation.test_location,file)
		print(fullpath)
		assert not os.path.isfile(fullpath)

# END TESTS


# set up for each function
def setup_function(function):
	testfiles_name = "testfiles"
	function.test_dir = os.path.join(os.path.realpath(
		os.path.join(os.getcwd(), os.path.dirname(__file__))))
	function.test_location = os.path.join(function.test_dir,testfiles_name)
	resource_dir = os.path.join(function.test_location,"resources")
	function.actual_certification_dir = os.path.join(resource_dir, "certification")
	function.archive_certification_dir = os.path.join(function.test_dir,"client_certs/certification")
	copytree(function.archive_certification_dir,function.actual_certification_dir)

def teardown_function(function):
	# remove everything BUT the resources/certification directory
	rmtree(function.test_location)

# done setting up objects for each module


# setup objects for this module
def setup_module(module):
	pass

def teardown_module(module):
	pass

# done setting up objects for this module
