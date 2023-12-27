from uagents import Agent, Context, Model
from uagents.query import query
from uagents.setup import fund_agent_if_low
import requests
from main import local_agent

dummyjson_api_url = "https://dummyjson.com/products"
fake_store_api_url = "https://fakestoreapi.com/products"

combined_products = []

class Message(Model):
    value: str

agent= Agent(name="agent", endpoint=["http://localhost:8001"], port=8001)



@agent.on_interval(period=60)  # Adjust the interval as needed (in seconds)
async def display_products(ctx: Context):
    global combined_products  # Use the combined_products list globally
    value = "test"
    query_message = await query(local_agent.address, Message(value=value))

    try:
        # Fetch product data from the DummyJSON API
        dummyjson_response = requests.get(dummyjson_api_url)
        fakestore_response = requests.get(fake_store_api_url)

        if dummyjson_response.status_code == 200:
            dummyjson_data = dummyjson_response.json()
            products = dummyjson_data.get("products", [])  # Get the products list if available
            combined_products.extend(products)  # Add products to the combined list
            ctx.logger.info("Products from DummyJSON API added to the combined dataset.")

        else:
            ctx.logger.error(f"Failed to fetch products from DummyJSON API. Status code: {dummyjson_response.status_code}")

        if fakestore_response.status_code == 200:
            fakestore_products = fakestore_response.json()
            combined_products.extend(fakestore_products)  # Add products to the combined list
            ctx.logger.info("Products from Fake Store API added to the combined dataset.")

        else:
            ctx.logger.error(f"Failed to fetch products from Fake Store API. Status code: {fakestore_response.status_code}")

        # Search for products by title within the combined dataset
        search_query = query_message
        found_products = []
        for product in combined_products:
            if product.get("title", "").lower() == search_query.lower():
                found_products.append(product)
        display_products = []
        for product in combined_products:
            for found in found_products:
                if product.get("category", "").lower() == found.get("category", "").lower():
                    display_products.append(product)


        if display_products:
            ctx.logger.info(f"Products found for '{search_query}':")
            for found_product in display_products:
                ctx.logger.info(f"ID: {found_product['id']}, Title: {found_product['title']}, Price: ${found_product['price']}")
                images = found_product.get("images", [])
                if images:
                    ctx.logger.info("Images:")
                    for image_url in images:
                        ctx.logger.info(image_url)
                else:
                    ctx.logger.info("No images available for this product.")
        else:
            ctx.logger.info(f"No products found for '{search_query}'.")

    except requests.RequestException as e:
        ctx.logger.error(f"Request to the API failed: {e}")
        
if __name__ == "__main__":
    fund_agent_if_low(agent.wallet.address())
    agent.run()