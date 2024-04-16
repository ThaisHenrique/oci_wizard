"""
Project Name: Full Export OCI Data Integration
Author: Thais Henrique
Contact: thaishenrique3110@gmail.com
Creation Date: 09/04/2024
Last Modification: 09/04/2024
Version: 1.0
Oracle Cloud Infrastructure Python SDK - 2.125.1
Description: This file contains an example of how to create a full export of the objects of OCI Data Integration.
Make sure to change all the variables like your OCID and object names, all the value below are examples only.
"""

import oci
from datetime import datetime
import pytz

# https://docs.oracle.com/en-us/iaas/tools/python/2.125.1/api/data_integration/client/oci.data_integration.DataIntegrationClient.html#oci.data_integration.DataIntegrationClient.create_export_request
# https://docs.oracle.com/en-us/iaas/tools/python/2.125.1/api/data_integration/models/oci.data_integration.models.CreateExportRequestDetails.html#oci.data_integration.models.CreateExportRequestDetails
# https://dave-allan-us.medium.com/exporting-and-importing-in-oci-data-integration-89ef0d75042a
# https://www.ateam-oracle.com/post/oci-data-integration-exportimport-use-cases

timezone = pytz.timezone('America/Sao_Paulo')
timestamp = datetime.now(timezone).strftime("%d%m%Y_%H%M%S")

file_name_now = f"file_name_{timestamp}.workspace.zip"

# Authentication
config = oci.config.from_file("path_to_config_file")
data_integration_client = oci.data_integration.DataIntegrationClient(config)

workspace_id = "ocid1.disworkspace.......pq"
bucket="bucket_name"

export_details = oci.data_integration.models.CreateExportRequestDetails(
    bucket_name=bucket,
    file_name=file_name_now,
    )
data_integration_client.create_export_request(workspace_id,export_details)

try:
    response = data_integration_client.create_export_request(workspace_id, export_details)
    print("Export request created successfully.")

except oci.exceptions.ServiceError as e:
    print(f"Error creating export request: {e.message}")

# Have fun customizing and improving this code for your need 😎💻.