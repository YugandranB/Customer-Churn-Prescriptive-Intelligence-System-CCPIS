import google.generativeai as genai

def generate_strategy(api_key, customer_row):

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-flash-latest")

    products = ", ".join(customer_row['Top_Products'])

    prompt = f"""
    You are a senior CRM strategist.

    Segment: {customer_row['Segment']}
    Location: {customer_row['Country']}
    Purchase Rhythm: {customer_row['IPT']} days
    Products: {products}

    Generate retention plan with reasoning.
    """

    response = model.generate_content(prompt)

    return response.text
