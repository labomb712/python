p = {
    "사과": 1000,
    "바나나": 800,
    "오렌지": 1500,
    "수박": 10000,
    "딸기": 3000
}

cart = {}


def add_item(item_name, quantity):
    if item_name in p:
        cart[item_name] = cart.get(item_name, 0) + quantity
        print(f"'{item_name}' {quantity}개가 카트에 추가되었습니다.")
    else:
        print(f"'{item_name}'은(는) 판매하지 않는 상품입니다.")


def display_cart_and_total():
    print("\n--- 쇼핑 카트 ---")
    if not cart:
        print("카트가 비어 있습니다.")
        return

    total_cost = 0
    for item, quantity in cart.items():
        item_price = p.get(item, 0)
        line_total = item_price * quantity
        total_cost += line_total
        print(f"{item}: {quantity}개 (개당 {item_price}원) = {line_total}원")
    
    print(f"---")
    print(f"총 가격: {total_cost}원")


add_item("사과", 2)
add_item("바나나", 3)
add_item("오렌지", 1)

display_cart_and_total()