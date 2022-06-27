import requests


def finally_order_count():
    print(f"Finally order count is {WebStore.count_order}")


def present_max_order_from_mail():
    max_key = max(WebStore.address_count_dict, key=WebStore.address_count_dict.get)
    print(f"Most of our orders are from {max_key} mail, and he made  {WebStore.address_count_dict[max_key]} orders")


def present_orders_count():
    for key in WebStore.address_count_dict:

        print(f"from {key} we have {WebStore.address_count_dict[key]} order")


class WebStore:
    count_order = 0
    finally_address_list = []
    address_count_dict = dict()

    def __init__(self, address):
        # self.order = order_name
        self.address = address
        WebStore.count_order += 1
        if WebStore.address_count_dict.get(address):
            WebStore.address_count_dict[address] += 1
        else:
            WebStore.address_count_dict.update({address: 1})
        WebStore.finally_address_list.append(self.address)


order1 = WebStore("yolyanlala@gmail.com")
order2 = WebStore("ayolyanlala@gmail.com")
order3 = WebStore("ayolyanlala@gmail.com")
order4 = WebStore("ayolyanlala@gmail.com")
order5 = WebStore("oooo@gmail.com")
order6 = WebStore("yolyanlala@gmail.com")


finally_order_count()
present_orders_count()
print(WebStore.address_count_dict)
#print(WebStore.finally_address_list)
present_max_order_from_mail()

