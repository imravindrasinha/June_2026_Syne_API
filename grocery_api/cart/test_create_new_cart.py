import json

from playwright.sync_api import APIRequestContext
import pytest

filepath = "C:\\June2026_Synechron_API\\data_global.json"
@pytest.mark.order(4)
@pytest.mark.dependency(scope = "session", name="create_cart")
def test_create_new_cart(before_each_test: APIRequestContext):
     request = before_each_test # this will allocate memory for API Request
   # read base_uri fro json
     with open(filepath,"r") as file:
         data = json.load(file)
     response = before_each_test.post(
         "/carts")
     assert response.status == 201
     assert response.json()['created'] == True
     print(json.dumps(response.json(), indent=4))
     cart_id = response.json()['cartId']
     data['cart_id'] = cart_id
     with open(filepath,"w") as file:
         json.dump(data,file,indent = 4)