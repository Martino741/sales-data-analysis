import pandas as pd

# Création des données
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone"],
    "Sales": [50000, 30000, 20000, 45000, 35000]
}

# Transformer en DataFrame
df = pd.DataFrame(data)

# Afficher les données
print("Dataset:")
print(df)

# Calcul du total des ventes
total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

# Analyse des ventes par produit
sales_by_product = df.groupby("Product")["Sales"].sum()

print("\nSales by Product:")
print(sales_by_product)
