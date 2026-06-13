import tkinter as tk
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup
import csv


def scrape_products():

    url = url_entry.get().strip()

    if url == "":
        messagebox.showerror(
            "Error",
            "Please enter a website URL."
        )
        return

    try:

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        items = soup.find_all(
            "article",
            class_="product_pod"
        )

        if len(items) == 0:

            messagebox.showwarning(
                "No Products Found",
                "No products found.\nUse https://books.toscrape.com/"
            )

            return

        # Clear old table data
        for row in tree.get_children():
            tree.delete(row)

        products = []

        for item in items:

            name = item.h3.a["title"]

            price = item.find(
                "p",
                class_="price_color"
            ).text

            rating = item.find(
                "p",
                class_="star-rating"
            )["class"][1]

            products.append(
                [name, price, rating]
            )

            tree.insert(
                "",
                tk.END,
                values=(name, price, rating)
            )

        with open(
                "products.csv",
                "w",
                newline="",
                encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow(
                [
                    "Product Name",
                    "Price",
                    "Rating"
                ]
            )

            writer.writerows(products)

        status_label.config(
            text=f"{len(products)} products saved to products.csv",
            fg="green"
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


def clear_table():

    for row in tree.get_children():
        tree.delete(row)

    status_label.config(
        text="Table cleared",
        fg="blue"
    )


# ---------------- GUI ----------------

root = tk.Tk()

root.title(
    "E-Commerce Product Scraper"
)

root.geometry(
    "1000x600"
)

title = tk.Label(
    root,
    text="E-Commerce Product Scraper",
    font=("Arial", 20, "bold")
)

title.pack(
    pady=15
)

url_label = tk.Label(
    root,
    text="Enter Website URL",
    font=("Arial", 14)
)

url_label.pack()

url_entry = tk.Entry(
    root,
    width=60,
    font=("Arial", 12)
)

url_entry.pack(
    pady=10
)

scrape_button = tk.Button(
    root,
    text="Scrape Products",
    bg="lightgreen",
    font=("Arial", 13),
    width=18,
    command=scrape_products
)

scrape_button.pack(
    pady=10
)

clear_button = tk.Button(
    root,
    text="Clear Table",
    bg="lightcoral",
    font=("Arial", 13),
    width=18,
    command=clear_table
)

clear_button.pack()

columns = (
    "Product Name",
    "Price",
    "Rating"
)

tree = ttk.Treeview(
    root,
    columns=columns,
    show="headings"
)

tree.heading(
    "Product Name",
    text="Product Name"
)

tree.heading(
    "Price",
    text="Price"
)

tree.heading(
    "Rating",
    text="Rating"
)

tree.column(
    "Product Name",
    width=650
)

tree.column(
    "Price",
    width=120
)

tree.column(
    "Rating",
    width=100
)

tree.pack(
    fill=tk.BOTH,
    expand=True,
    padx=10,
    pady=15
)

status_label = tk.Label(
    root,
    text="Ready",
    font=("Arial", 12, "bold")
)

status_label.pack()

root.mainloop()