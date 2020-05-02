# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from django.shortcuts import render
from django.http import (HttpResponse, HttpResponseRedirect, JsonResponse)
from django.urls import reverse
from tutorial.auth_helper import get_sign_in_url, get_token_from_code, store_token, store_user, remove_user_and_token, get_token
from tutorial.graph_helper import get_user, get_drive_files
import dateutil.parser

# <HomeViewSnippet>
def home(request):
  context = initialize_context(request)

  return render(request, 'tutorial/home.html', context)
# </HomeViewSnippet>

# <InitializeContextSnippet>
def initialize_context(request):
  context = {}

  # Check for any errors in the session
  error = request.session.pop('flash_error', None)

  if error != None:
    context['errors'] = []
    context['errors'].append(error)

  # Check for user in the session
  context['user'] = request.session.get('user', {'is_authenticated': False})
  return context
# </InitializeContextSnippet>

# <SignInViewSnippet>
def sign_in(request):
  # Get the sign-in URL
  sign_in_url, state = get_sign_in_url()
  # Save the expected state so we can validate in the callback
  request.session['auth_state'] = state
  # Redirect to the Azure sign-in page
  return HttpResponseRedirect(sign_in_url)
# </SignInViewSnippet>

# <SignOutViewSnippet>
def sign_out(request):
  # Clear out the user and token
  remove_user_and_token(request)

  return HttpResponseRedirect(reverse('home'))
# </SignOutViewSnippet>

# <CallbackViewSnippet>
def callback(request):
  # Get the state saved in session
  expected_state = request.session.pop('auth_state', '')
  # Make the token request
  token = get_token_from_code(request.get_full_path(), expected_state)

  # Get the user's profile
  user = get_user(token)

  # Save token and user
  store_token(request, token)
  store_user(request, user)

  return HttpResponseRedirect(reverse('admin:index'))
# </CallbackViewSnippet>


def list_files(request):

    context = initialize_context(request)
    token = get_token(request)
    resp = get_drive_files(token,'/me/drive/root/children')
    if request.GET.get('raw'):
      return JsonResponse(resp)


    from dacite import from_dict
    from .models import MsGraph, File, Folder

    files = []
    folders = []

    # differentiate between a 'file' key and a 'folder' key
    for r in resp.get('value'):
      if type(r.get('folder')) == dict:
        r['folder_name'] = r.get('name')
        obj = from_dict(data_class=Folder,data=r)
        folders.append(obj)
      if type(r.get('file')) == dict:
        r['url'] = r['@microsoft.graph.downloadUrl']
        obj = from_dict(data_class=File,data=r)
        files.append(obj)
      else:
        continue
      
      
    # example = resp['value'][4]
    # obj = from_dict(data_class=MsGraph, data=example)
    d_files = File.schema().dump(files, many=True)
    d_folders = Folder.schema().dump(folders, many=True)
    # return JsonResponse({**d_files, **d_folders}, safe=False)

    return JsonResponse(d_files+d_folders, safe=False)
    

  # Docs
  # https://docs.microsoft.com/en-us/graph/api/resources/onedrive?view=graph-rest-1.0
  # https://docs.microsoft.com/en-us/graph/api/driveitem-get-content?view=graph-rest-1.0&tabs=http
  
    # return JsonResponse(resp)


def download_files(request):
    return JsonResponse({'download':'files'})

def get_onedrive_drive_contents(token):
  pass

def download_onedrive_driveitem(token):
  pass
  # Docs
  #   # https://docs.microsoft.com/en-us/graph/api/driveitem-get-content?view=graph-rest-1.0&tabs=http

def cleanup_downloaded_driveitem(token):
  pass
  # Remove the downloaded file from instance storage
  # .. after fetching

def move_processed_orderforms_to_processed_folder(token):
  pass
  # on one drive, succesfull parsed files get moved to:
  # farmbox/processed/
