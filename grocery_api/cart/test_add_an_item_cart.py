import json

from playwright.sync_api import APIRequestContext
import pytest

filepath = "C:\\June2026_Synechron_API\\data_global.json"

@pytest.mark.order(5)
@pytest.mark.dependency(scope="session", depends=["create_cart"], name = "add_item")

@pytest.mark.parametrize("pid",[1225,1709,1710,2177])
def test_add_an_item_cart(before_each_test: APIRequestContext,pid):
     
   # read base_uri fro json
     with open(filepath,"r") as file:
         data = json.load(file)
     payload ={
          "productId": pid,
          "quantity": 2
          
     }
     response = before_each_test.post(
         f"/carts/{data['cart_id']}/items", data=payload)
     assert response.status == 201
     response_json = response.json()
     print(json.dumps(response_json, indent=4))
     assert response_json['created'] == True
     data['item_id'] = response_json['itemId']
     with open(filepath, "w") as file:
         json.dump(data, file, indent=4)