from django.shortcuts import render, HttpResponse
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

from .models import *
# Create your views here.

def index(request):
    return HttpResponse('This page is working')

@csrf_exempt
def github_webhook(request):
    if request.method == 'POST':
        try:
            payload = json.loads(request.body)
            event_type = request.headers.get('X-GitHub-Event')
            
            if event_type == 'push':
                return push_event(payload)
            elif event_type == 'pull_request':
                return pull_request_event(payload)
            elif event_type=='ping':
                print(payload)
            
            return JsonResponse({'status': 'unsupported event'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=405)

def push_event(payload):
    author = payload['pusher']['name']
    to_branch = payload['ref'].split('/')[-1]  # Extract branch name
    timestamp = format_timestamp(payload['head_commit']['timestamp'])

    pushdata=Push_event(author=author, branch=to_branch, datetime=timestamp)
    pushdata.save()

    message = f'"{author}" pushed to "{to_branch}" on {timestamp}'
    print(message)
    
    return JsonResponse({'message': message}, status=200)

def pull_request_event(payload):
    action = payload['action']
    author = payload['pull_request']['user']['login']
    from_branch = payload['pull_request']['head']['ref']
    to_branch = payload['pull_request']['base']['ref']
    
    if action == 'opened':
        timestamp = format_timestamp(payload['pull_request']['created_at'])
        pull_request=Pull_request(author=author,from_branch=from_branch, to_branch=to_branch, datetime=timestamp)
        pull_request.save()
        message = f'"{author}" submitted a pull request from "{from_branch}" to "{to_branch}" on {timestamp}'
    
    elif action == 'closed' and payload['pull_request'].get('merged', False):
        timestamp = format_timestamp(payload['pull_request']['merged_at'])
        pull_request=Merge_event(author=author,from_branch=from_branch, to_branch=to_branch, datetime=timestamp)
        pull_request.save()
        message = f'"{author}" merged branch "{from_branch}" to "{to_branch}" on {timestamp}'
    
    else:
        message = f'Pull request action "{action}" is not handled.'

    print(message)
    return JsonResponse({'message': message}, status=200)


def format_timestamp(timestamp):
    parsed_timestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S%z")
    return parsed_timestamp
