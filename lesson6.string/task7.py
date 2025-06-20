lines = int(input("Enter lines: "))
sits = int(input("Enter the sits: "))
meters = int(input("Enter meters: "))

for line in range(1, lines):
    print("=" * sits, "*" * meters, "=" * sits)
    