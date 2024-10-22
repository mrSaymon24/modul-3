calls = 0
def count_calls():
    global calls
    calls += 1
def string_info (string):
    count_calls()
    length = len(string)
    upper = string.upper()
    lower = string.lower()
    return (length, upper, lower)
def is_contains (string, list_to_search):
    count_calls()
    return string.lower() in (item.lower() for item in list_to_search)
result1 = string_info("'Capybara")
result2 = string_info("Armageddon")
result3 = is_contains('Urban', ['ban', 'BaNaN', 'urBAN']) # Urban ~ urBAN
result4 = is_contains('cycle', ['recycling', 'cyclic']) # No matches
print("String info results:", result1)
print("String info results:", result2)
print("Is 'urban' in list?", result3)
print("Is 'openAI' in list?", result4)
print("Total function calls:", calls)
