# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

# <FirstCodeSnippet>
from requests_oauthlib import OAuth2Session

graph_url = 'https://graph.microsoft.com/v1.0'

def get_user(token):
  graph_client = OAuth2Session(token=token)
  # Send GET to /me
  user = graph_client.get('{0}/me'.format(graph_url))
  # Return the JSON result
  return user.json()
# </FirstCodeSnippet>


def get_drive_files(token, onedrive_path=None):
  if not onedrive_path:
    onedrive_path = '/me/drive/root/children'
  graph_client = OAuth2Session(token=token)

  # Configure query parameters to
  # modify the results
  query_params = {
    # '$select': 'subject,organizer,start,end',
    # '$orderby': 'createdDateTime DESC'
  }

  resp = graph_client.get('{0}{1}'.format(graph_url,onedrive_path), params=query_params)
  # Return the JSON result
  return resp.json()