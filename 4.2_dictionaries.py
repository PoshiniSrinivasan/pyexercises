"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A dictionary containing five fields about a shipment.
# 2. Process: The program reads the shipment details, changes its status,
# removes one field and checks for a field that does not exist.
# 3. Out: The updated shipment details and a message for the missing field.
# 4. My object is a supply chain shipment. My five fields are
# shipment ID, origin, destination, carrier and status.


# Your code below
# Create a dictionary describing a shipment
shipment = {
    "shipment_id": "SH101",
    "origin": "Chennai",
    "destination": "Paris",
    "carrier": "DHL",
    "status": "In Transit"
}

# Read and display the shipment destination
print("Destination:", shipment["destination"])

# Change the shipment status
shipment["status"] = "Delivered"

# Remove the carrier field
shipment.pop("carrier")

# Check for a field that does not exist
try:
    print(shipment["delivery_date"])
except KeyError:
    print("Delivery date field does not exist.")

# Display every remaining field
print("Updated shipment details:")

for field, value in shipment.items():
    print(field, ":", value)