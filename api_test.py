import time
import json
import glob
import argparse

import grafeas
from grafeas.rest import ApiException
from pprint import pprint
from grafeas.configuration import Configuration
from totoify_grafeas.totoify_grafeas.totoifylib import GrafeasInTotoOccurrence
from in_toto.models.metadata import Metablock
from in_toto.models.link import Link
from securesystemslib.interface import import_rsa_privatekey_from_file


def create_proj():
    api_instance = grafeas.GrafeasProjectsApi()
    body = grafeas.ApiProject(name="projects/testproj") # ApiProject | The project to create.

    try:
        # Creates a new project.
        api_response = api_instance.create_project(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GrafeasProjectsApi->create_project: %s\n" % e)

def create_note():
    configuration = None
    api_instance = grafeas.GrafeasV1Beta1Api(grafeas.ApiClient(configuration))
    parent = 'projects/testproj' # str | This field contains the project Id for example: \"project/{project_id}
    body = grafeas.ApiNote() # ApiNote | The Note to be inserted

    try:
        # Creates a new `Note`.
        api_response = api_instance.create_note(parent, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GrafeasApi->create_note: %s\n" % e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert in-toto link to Grafeas Occurance")
    parser.add_argument("path", help="path to link file")
    parser.add_argument("note_id", help="note id")

    try:
        args = parser.parse_args()
        file_path = args.path

        link_files = glob.glob(file_path)
        if len(link_files) != 1:
            raise Exception(f"multiple link files: {link_files}")
        note_id = args.note_id

        link_to_occurence(file_path, note_id)

    except Exception as e:
        print(f"Conversion failed {e}")
