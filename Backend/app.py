from flask import Flask, request
from uagents.query import query
from uagents import Model
from flask_cors import CORS

class Message(Model):
    value: str

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['GET', 'POST'])
async def frontend_input():
    if request.method== 'POST':
        data = request.json
        input_string = data.get('search')
        print(input_string)
        await query(destination='agent1qvpd7hf852t0xz5ad0p3pgflnqg4kym8ajncyxv6r56ez85ue8zgumwwjd4',message=Message(value=input_string))  
        processed_result = f"You entered: {input_string}"
        return processed_result
    return processed_result     
        
if __name__ == '__main__':
    app.run(debug=True)
