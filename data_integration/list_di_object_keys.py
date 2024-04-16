import oci

# Check the documentation to se how to create a config file for authentication
# https://docs.oracle.com/en-us/iaas/tools/python/2.125.2/configuration.html
config = oci.config.from_file("path_to_config_file")
data_integration_client = oci.data_integration.DataIntegrationClient(config)

workspace_id = "ocid1.disworkspace........" # OCID do Workspace
compartment_id  = "ocid1.compartment......." # OCID do Compartment

def list_di_objects(fetcher_method, **kwargs):
    objects_dict = {}
    response = fetcher_method(**kwargs)
    for item in response.data.items:
        objects_dict[item.name] = item.key
    return objects_dict

def print_objects_dict(objects_dict, title):
    print(f"\n{'-'*60}\n\n{title}\n")
    for name, key in objects_dict.items():
        print(f"{name}: {key}")

# Create a dict with the objects you need
projects_dict = list_di_objects(data_integration_client.list_projects, workspace_id=workspace_id)
assets_dict = list_di_objects(data_integration_client.list_data_assets, workspace_id=workspace_id)
applications_dict = list_di_objects(data_integration_client.list_dis_applications, workspace_id=workspace_id, compartment_id=compartment_id)
data_flows_dict = list_di_objects(data_integration_client.list_data_flows, workspace_id=workspace_id)
tasks_dict = list_di_objects(data_integration_client.list_tasks, workspace_id=workspace_id)

# Print the results from the dict above
print_objects_dict(projects_dict, "Projects")
print_objects_dict(assets_dict, "Data Assets")
print_objects_dict(applications_dict, "DIS Applications")
print_objects_dict(data_flows_dict, "Data Flows")
print_objects_dict(tasks_dict, "Tasks")