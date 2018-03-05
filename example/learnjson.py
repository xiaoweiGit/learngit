import json
data="{\"Method\":119,\"Data\":\"{\\\"paging\\\":{\\\"PageIndex\\\":1,\\\"PageSize\\\":10,\\\"RecCount\\\":0},\\\"OrderNo\\\":\\\"WAP531466478\\\",\\\"Mobile\\\":\\\"13916109894\\\"}\"}"

text=json.loads(data)
print(text)
