import requests


# TODO 1. Create your user account
"""
Call /v1/users API by HTTP POST.
$ curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes", "notMinor":"yes"}'
{"message":"Success.","isSuccess":true}

"""

pixela_end_pt = "https://pixe.la/v1/users"

USER_NAME = "pufter"
TOKEN = "739trr19trr2022pihi"
GRAPH_NAME = "testgraph1"

user_params = {
    "token":USER_NAME, 
    "username":TOKEN, 
    "agreeTermsOfService":"yes", 
    "notMinor":"yes"
    }

        # Sending POST req for an Account creation
# post_respns = requests.post(url=pixela_end_pt , json=user_params)
        # Print the rsponse message
# print(post_respns.text)



# TODO 2. Create a graph definition
"""
Call /v1/users/<username>/graphs by HTTP POST.
$ curl -X POST https://pixe.la/v1/users/a-know/graphs -H 'X-USER-TOKEN:thisissecret' -d '{"id":"test-graph","name":"graph-name","unit":"commit","type":"int","color":"shibafu"}'
{"message":"Success.","isSuccess":true}

"""

# graph endpoint 
graph_endpoint = f"{pixela_end_pt}/{USER_NAME}/graphs"

graph_config = {
    "id" : "testgraph1",
    "name" : "Running in Morning",
    "unit" : "km",
    "type" : "float",
    "color" : "sora"
}

"""
garph_response = requests.post(url = graph_endpoint, json= graph_config)
print(garph_response.text)
"""
# above is not  gonna work becuse we have to provide authentication
# which is done by header (http header), using the "headers= " kewargs
heADErs = {
    "X-USER-TOKEN" : TOKEN
}
# garph_response = requests.post(url = graph_endpoint, json= graph_config, headers= heADErs)
# print(garph_response.text)


# TODO 3. goto the HTML page: https://pixe.la/v1/users/pufter/graphs/testgraph1.html
# Only shows the graph : https://pixe.la/v1/users/pufter/graphs/testgraph1
"""
Get the graph!
Browse https://pixe.la/v1/users/a-know/graphs/test-graph ! This is also /v1/users/<username>/graphs/<graphID> API.

"""

# TODO 4. Post value to the graph: Challenge Add a Pixel to the Habit Tracker using a Post Request
"""
Call /v1/users/<username>/graphs/<graphID> by HTTP POST.
$ curl -X POST https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret' -d '{"date":"20180915","quantity":"5"}'
{"message":"Success.","isSuccess":true}

"""
# Formatted datetime
from datetime import datetime

# y give 12, 13, 20, 22 ets Y gives 2012, 2013, 2020, 2022
tIMe = datetime.now()
now_time = tIMe.strftime("%Y%m%d")
print(now_time)

any_date_time = datetime(year=2022, month=1, day=18).strftime("%Y%m%d")
print(any_date_time)

pix_data = {
    # date: yyyymmdd
    # "date":tIMe.strftime("%Y%m%d"),
    "date":now_time,
    "quantity":"15.0"
}

add_pix__endpoint = f"{graph_endpoint}/testgraph1"

# add_pix_response = requests.post(url = add_pix__endpoint, json= pix_data, headers= heADErs)
# print(add_pix_response.text)



# TODO 5. PUT and DELETE to update and delete pixels

edit_pix_data = {
    "quantity":"1.0"
}

edit_pix_endpoint = f"https://pixe.la/v1/users/{USER_NAME}/graphs/{GRAPH_NAME}/{any_date_time}"

# edit_pix_response = requests.put(url = edit_pix_endpoint, json= edit_pix_data, headers= heADErs)
# print(edit_pix_response.text)



# TODO 6. DELETE  pixels
delete_pix_response = requests.delete(url = edit_pix_endpoint, headers= heADErs)
print(delete_pix_response.text)

# python api_post.py