from uagents import Agent, Context, Model
from uagents.query import query
from uagents.setup import fund_agent_if_low
import requests

dummyjson_api_url = "https://dummyjson.com/products"
combined_products = []

class Message(Model):
    value: str

processor_agent = Agent(
    name="processor_agent",
    seed="processor_agent_seed",
    port=8000,
    endpoint=["http://127.0.0.1:8000/submit"],
)

# print(processor_agent.address)

@processor_agent.on_message(model=Message)
async def message_handler(ctx:Context, sender:str, msg:Message):
    ctx.logger.info(f"Received msg: {msg.value}")
    query_message = msg.value
    global combined_products  # Use the combined_products list globally
    
    try:
        # Fetch product data from the DummyJSON API
        dummyjson_response = requests.get(dummyjson_api_url)
        
        if dummyjson_response.status_code == 200:
            dummyjson_data = dummyjson_response.json()
            products = dummyjson_data.get("products", [])  # Get the products list if available
            combined_products.extend(products)  # Add products to the combined list
            ctx.logger.info("Products from DummyJSON API added to the combined dataset.")

        else:
            ctx.logger.error(f"Failed to fetch products from DummyJSON API. Status code: {dummyjson_response.status_code}")

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
    # await ctx.send('agent1qvpd7hf852t0xz5ad0p3pgflnqg4kym8ajncyxv6r56ez85ue8zgumwwjd4', Message(value=query_message))


        
if __name__ == "__main__":
    fund_agent_if_low(processor_agent.wallet.address())
    processor_agent.run()