# E-Commerce Product Scraper GUI

A Python-based GUI application that extracts product information from e-commerce websites and stores the data in a CSV file. The application provides a user-friendly interface for entering URLs, scraping product details, displaying the extracted data in a table, and exporting the results.

## Features

* User-friendly graphical interface built with Tkinter
* Accepts website URL as input
* Extracts product names, prices, and ratings
* Displays scraped data in a table
* Saves extracted information to a CSV file
* Clear table functionality
* Error handling and status messages

## Technologies Used

* Python 3
* Tkinter
* Requests
* BeautifulSoup4
* CSV Module

## Installation

Install the required packages:

```bash
pip install requests beautifulsoup4
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ecommerce-product-scraper-gui-python.git
```

2. Navigate to the project directory:

```bash
cd ecommerce-product-scraper-gui-python
```

3. Run the application:

```bash
python product_scraper_gui.py
```

## Usage

1. Enter the website URL.
2. Click the **Scrape Products** button.
3. View the extracted product information in the table.
4. Product data is automatically saved in `products.csv`.
5. Use the **Clear Table** button to remove displayed data.

## Output

The application creates a CSV file named:

```text
products.csv
```

containing:

* Product Name
* Price
* Rating

## Project Structure

```
ecommerce-product-scraper-gui-python/
│
├── product_scraper_gui.py
├── products.csv
├── requirements.txt
├── README.md
└── screenshots/
    └── output.png
```

## Author

**Aritro Biswas**
