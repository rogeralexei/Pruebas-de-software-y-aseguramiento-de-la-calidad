import json
import sys
import time

def load_json_file(file_path):
    """Loads JSON data from a file and handles errors."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file - {file_path}")
    return None

def compute_total_sales(price_catalogue, sales_record):
    """Computes the total sales cost based on the catalogue prices."""
    total_cost = 0.0
    errors = []
    
    for sale in sales_record:
        product = sale.get("product")
        quantity = sale.get("quantity")
        
        if product not in price_catalogue:
            errors.append(f"Warning: Product '{product}' not found in catalogue.")
            continue
        
        if not isinstance(quantity, (int, float)) or quantity < 0:
            errors.append(f"Warning: Invalid quantity '{quantity}' for product '{product}'.")
            continue
        
        total_cost += price_catalogue[product] * quantity
    
    return total_cost, errors

def main():
    """Main function to execute the sales computation program."""
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py priceCatalogue.json salesRecord.json")
        sys.exit(1)
    
    price_file, sales_file = sys.argv[1], sys.argv[2]
    
    price_catalogue = load_json_file(price_file)
    sales_record = load_json_file(sales_file)
    
    if price_catalogue is None or sales_record is None:
        print("Error: Could not load input files. Exiting.")
        sys.exit(1)
    
    start_time = time.time()
    total_cost, errors = compute_total_sales(price_catalogue, sales_record)
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    result_output = [
        "Sales Computation Results:",
        "----------------------------------",
        f"Total Sales Cost: ${total_cost:.2f}",
        f"Execution Time: {elapsed_time:.4f} seconds",
        "----------------------------------"
    ]
    
    if errors:
        result_output.append("Errors and Warnings:")
        result_output.extend(errors)
    
    result_text = "\n".join(result_output)
    print(result_text)
    
    with open("SalesResults.txt", "w", encoding='utf-8') as result_file:
        result_file.write(result_text)
    
if __name__ == "__main__":
    main()
