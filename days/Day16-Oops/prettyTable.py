try:
    import importlib
    PrettyTable = importlib.import_module("prettytable").PrettyTable
    
    # 1. Create a table object
    table = PrettyTable()
    
    # 2. Add columns (Column Name, List of values)
    table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
    table.add_column("Type", ["Electric", "Water", "Fire"])
    
    # 3. Change alignment if desired (e.g., left-align)
    table.align = "l"
    
    # 4. Print the table
    print(table)
except ImportError:
    print("Error: prettytable module is not installed. Install it using: pip install prettytable")