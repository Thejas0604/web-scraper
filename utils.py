import csv

def save_to_csv(products, filename='amazon_products.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Product Name', 'Price', 'Availability', 'Rating'])
        for product in products:
            writer.writerow([product['name'], product['price'], product['availability'], product['rating']])

def save_to_html(products, filename='amazon_products.html'):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Amazon Product Report</title>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
            }
            th {
                background-color: #f2f2f2;
                text-align: left;
            }
        </style>
    </head>
    <body>
        <h1>Amazon Product Report</h1>
        <table>
            <tr>
                <th>Product Name</th>
                <th>Price</th>
                <th>Availability</th>
                <th>Rating</th>
            </tr>
    """
    for product in products:
        html_content += f"""
            <tr>
                <td>{product['name']}</td>
                <td>{product['price']}</td>
                <td>{product['availability']}</td>
                <td>{product['rating']}</td>
            </tr>
        """
    html_content += """
        </table>
    </body>
    </html>
    """
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)