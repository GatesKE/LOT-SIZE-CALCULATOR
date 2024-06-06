def calculate_lot_size(risk_amount, commission_per_lot, sl_size):
    # Lot size calculation formula
    lot_size = risk_amount / ((10 * sl_size) + commission_per_lot)
    # Rounding the lot size to 2 decimal places
    lot_size = round(lot_size, 2)
    return lot_size

def main():
    # Get user input
    risk_amount = float(input("Enter your risk amount in dollars: "))
    commission_per_lot = float(input("Enter your broker's commission per lot (in dollars): "))
    sl_size = float(input("Enter your SL size (in pips): "))
    
    # Calculate lot size
    lot_size = calculate_lot_size(risk_amount, commission_per_lot, sl_size)
    
    # Print the result
    print(f"Calculated lot size: {lot_size}")

if __name__ == "__main__":
    main()
