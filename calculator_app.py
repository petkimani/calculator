import streamlit as st

def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Invalid operator"

def main():
    st.title("Simple Calculator")

    # Input fields
    num1 = st.number_input("Enter the first number", step=0.1, format="%.2f")
    num2 = st.number_input("Enter the second number", step=0.1, format="%.2f")
    
    # Operator selection
    operator = st.selectbox("Select an operator", ["+", "-", "*", "/"])
    
    # Calculate button and result display
    if st.button("Calculate"):
        result = calculator(num1, num2, operator)
        if isinstance(result, str):  # Check if result is an error message
            st.error(result)
        else:
            st.success(f"The result is: {result:.2f}")

if __name__ == "__main__":
    main()
