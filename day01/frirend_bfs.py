# 친구 관계 그래프

# A와 B가 친구이면, A의 리스트에 B가, B의 리스트에 A가 모두 있어야 합니다.

fr_info = {
    'Summer': ['John', 'Justin', 'Mike'],   # John, Justin, Mike
    'John':   ['Summer','Justin'],           # Summer, Justin
    'Justin': ['John', 'Summer', 'Mike', 'May'],  # John, Summer, Mike, May
    'Mike':   ['Summer', 'Justin'],           # Summer, Justin
    'May':    ['Justin', 'Kim'],           # Justin, Kim
    'Kim':    ['May'],                   # May
    'Tom':    ['Jerry'],                   # Jerry
    'Jerry':  ['Tom'],                   # Tom

}
# 확인: Summer의 친구 목록 출력
print("Summer의 친구:", fr_info['Summer'])

# 확인: May의 친구 목록 출력
print("May의 친구:", fr_info['May'])