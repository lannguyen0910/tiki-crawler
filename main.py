import argparse
import os
from dotenv import load_dotenv
from pathlib import Path

parser = argparse.ArgumentParser(description="Crawling data from Tiki")
parser.add_argument('--category', type=str,
                    help='Crawl data based on category')
parser.add_argument('--keyword', type=str,
                    help='Crawl data based on user input')
parser.add_argument('--saved_folder', type=str, default="data",
                    help='Output folder to save product data to')
parser.add_argument('--saved_format', type=str, required=True, choices={"csv", "json"},
                    help='Output format to save product data')
parser.add_argument('--num_products', type=int, default=50,
                    help='Number of items to save (min 50 items)')

if __name__ == '__main__':
    category_api_url = "https://api.tiki.vn/integration/v2/categories"
    product_api_url = "https://api.tiki.vn/integration/v2.1/products"
    env_filename = '.env'

    env_path = Path('.') / env_filename
    load_dotenv(dotenv_path=env_path)
    headers = {"user-agent": os.environ['MY_USER_AGENT']}

    args = parser.parse_args()

    assert args.keyword is not None and args.category is not None, "Must input `keyword` argument or `category` argument"
    assert args.keyword is None and args.category is None, "Cannot input both `keyword` argument and `category` argument at the same time"

    if not os.path.exists(args.saved_folder):
        os.makedirs(args.saved_folder)