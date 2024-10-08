i = 0  # Global variable

def demo():
    global i
    i += 1
    if i == 100:  # Base case to stop recursion
        return  # Exit the function once i reaches 100 if I use break then it 
                # will not work break statement: The break keyword is only used inside loops, but your code doesn't have any loops (it's a recursive function). Instead, I should use return to exit from the recursion once the condition is met.
    print("Rafsan", i)
    demo()  # Recursive call

demo()  # Initial call
