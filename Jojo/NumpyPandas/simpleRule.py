customerData=[
    {
        "customerId": "C001",
        "age": 25,
        "location": "New York",
        "gender": "Male",
        "purchaseAmout": 150.0,
        "isLoyal": True
    },
    {
        "customerId": "C002",
        "age": 30,
        "location": "Los Angeles",
        "gender": "Female",
        "purchaseAmout": 200.0,
        "isLoyal": False
    },
    {
        "customerId": "C003",
        "age": 22,
        "location": "Chicago",
        "gender": "Male",
        "purchaseAmout": 150.0,
        "isLoyal": True
    },
    {
        "customerId": "C004",
        "age": 28,
        "location": "Houston",
        "gender": "Female",
        "purchaseAmout": 200.0,
        "isLoyal": True
    }
]

threshold = 180.0
def prediksiLoyalty(purchase): # simple rule model
    if purchase >= threshold:
        return True
    else:
        return False
    
print("=== Simple Rule 'ML' ===")
#conditional adalah rules dalam machine learning
# misalkan kita ingin menentukan apakah customer loyal atau tidak berdasarkan purchase amount
for customer in customerData:
    # customer["isLoyal"]=prediksiLoyalty(customer['purchaseAmout']) #set loyal berdasarkan rules
    actualLoyal=customer['isLoyal']
    predictLoyal=prediksiLoyalty(customer['purchaseAmout'])

    print(f'''Customer ID: {customer["customerId"]},
Amount: ${customer["purchaseAmout"]},
Actual Loyalty: {actualLoyal},
Predicted Loyalty: {predictLoyal} - {'Correct' if actualLoyal == predictLoyal else 'Incorrect'} ''')

newCustAmount = 190.00
newCustAmount2= 80.00

print(f"New Customer Amount: ${newCustAmount:.2f}, Predicted Loyalty: {prediksiLoyalty(newCustAmount)}")
print(f"New Customer Amount: ${newCustAmount2:.2f}, Predicted Loyalty: {prediksiLoyalty(newCustAmount2)}")